#!/usr/bin/env python3
"""sources.toml に書かれた RSS / Atom フィードを取得し、新着記事を JSON で出力する。

標準ライブラリだけで動く。出力は Claude がダイジェストを書くための下ごしらえで、
記事本文は取得しない（フィードに含まれるタイトル・リンク・概要文のみ）。

使い方:
    python3 scripts/fetch_feeds.py > /tmp/feeds.json
    python3 scripts/fetch_feeds.py --since-hours 72

取得範囲は「前回のダイジェストの日付の 0 時（JST）以降」。実行が失敗した日があっても、
次の実行でその期間の記事を拾える。ダイジェストがまだない場合は直近 30 時間。
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import tomllib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JST = timezone(timedelta(hours=9))
USER_AGENT = "azumayoru-daily-news-digest/1.0 (+https://github.com/bonkotu25/azumayoru-daily-news-digest)"
SUMMARY_MAX_CHARS = 200

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "rss1": "http://purl.org/rss/1.0/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}


def fetch(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def clean_text(raw: str | None) -> str:
    """HTML タグを除去し、空白を詰めて SUMMARY_MAX_CHARS 文字に切り詰める。"""
    if not raw:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > SUMMARY_MAX_CHARS:
        text = text[:SUMMARY_MAX_CHARS].rstrip() + "…"
    return text


def normalize_link(url: str) -> str:
    """トラッキング用のクエリ（utm_* など）を取り除く。"""
    parts = urllib.parse.urlsplit(url.strip())
    query = [(k, v) for k, v in urllib.parse.parse_qsl(parts.query, keep_blank_values=True)
             if not k.startswith("utm_")]
    return urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(query)))


def parse_date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        dt = parsedate_to_datetime(raw)  # RSS 2.0 (RFC 822)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))  # Atom / RDF (ISO 8601)
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=JST)
    return dt


def text_of(elem: ET.Element, path: str) -> str | None:
    found = elem.find(path, NS)
    return found.text if found is not None else None


def parse_feed(data: bytes) -> list[dict]:
    """RSS 2.0 / RSS 1.0 (RDF) / Atom を判別して記事のリストを返す。"""
    root = ET.fromstring(data)
    items: list[dict] = []

    if root.tag == "rss":
        for it in root.iterfind("./channel/item"):
            items.append({
                "title": text_of(it, "title"),
                "link": text_of(it, "link"),
                "summary": text_of(it, "description"),
                "published": text_of(it, "pubDate") or text_of(it, "dc:date"),
            })
    elif root.tag == f"{{{NS['rdf']}}}RDF":
        for it in root.iterfind("rss1:item", NS):
            items.append({
                "title": text_of(it, "rss1:title"),
                "link": text_of(it, "rss1:link"),
                "summary": text_of(it, "rss1:description"),
                "published": text_of(it, "dc:date"),
            })
    elif root.tag == f"{{{NS['atom']}}}feed":
        for it in root.iterfind("atom:entry", NS):
            link = None
            for ln in it.iterfind("atom:link", NS):
                if ln.get("rel", "alternate") == "alternate":
                    link = ln.get("href")
                    break
            items.append({
                "title": text_of(it, "atom:title"),
                "link": link,
                "summary": text_of(it, "atom:summary") or text_of(it, "atom:content"),
                "published": text_of(it, "atom:published") or text_of(it, "atom:updated"),
            })
    else:
        raise ValueError(f"未対応のフィード形式です: {root.tag}")

    return items


def list_digests() -> list[tuple[date, Path]]:
    """既存のダイジェスト（digests/YYYY/MM/DD/README.md）を日付つきで返す。"""
    digests = []
    for path in (REPO_ROOT / "digests").glob("*/*/*/README.md"):
        year, month, day = path.parts[-4:-1]
        try:
            digests.append((date(int(year), int(month), int(day)), path))
        except ValueError:
            continue
    return digests


def recent_digest_links(digests: list[tuple[date, Path]], exclude_days: int, today: date) -> set[str]:
    """直近 exclude_days 日分のダイジェストに掲載済みのリンクを集める（重複掲載の防止用）。"""
    links: set[str] = set()
    for digest_date, path in digests:
        if 0 <= (today - digest_date).days <= exclude_days:
            links.update(re.findall(r"\]\((https?://[^)\s]+)\)", path.read_text(encoding="utf-8")))
    return links


def default_since(digests: list[tuple[date, Path]], now: datetime, max_days: int) -> datetime:
    """前回のダイジェストの日付の 0 時（JST）。ダイジェストがなければ直近 30 時間。最大 max_days 日前まで。"""
    past = [d for d, _ in digests if d < now.date()]
    if not past:
        return now - timedelta(hours=30)
    since = datetime.combine(max(past), datetime.min.time(), tzinfo=JST)
    return max(since, now - timedelta(days=max_days))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--since-hours", type=int, help="この時間内に公開された記事だけを残す（既定: 前回のダイジェスト以降）")
    parser.add_argument("--exclude-days", type=int, default=7, help="直近この日数のダイジェストに載った記事を除外（既定: 7）")
    parser.add_argument("--sources", type=Path, default=REPO_ROOT / "sources.toml")
    args = parser.parse_args()

    now = datetime.now(JST)
    digests = list_digests()
    if args.since_hours is not None:
        since = now - timedelta(hours=args.since_hours)
    else:
        since = default_since(digests, now, args.exclude_days)
    seen = recent_digest_links(digests, args.exclude_days, now.date())

    with args.sources.open("rb") as f:
        config = tomllib.load(f)

    result: dict = {
        "generated_at": now.isoformat(timespec="seconds"),
        "since": since.isoformat(timespec="seconds"),
        "categories": [],
        "errors": [],
    }

    for cat in config["categories"]:
        cat_items: list[dict] = []
        for feed in cat["feeds"]:
            try:
                entries = parse_feed(fetch(feed["url"]))
            except Exception as e:  # 1つのフィードの失敗で全体を止めない
                result["errors"].append({"feed": feed["name"], "url": feed["url"], "error": f"{type(e).__name__}: {e}"})
                continue

            for entry in entries:
                link = normalize_link(entry["link"] or "")
                title = clean_text(entry["title"])
                if not link or not title or link in seen:
                    continue
                published = parse_date(entry["published"])
                if published is not None and published < since:
                    continue
                seen.add(link)  # 複数フィードに同じ記事がある場合は最初の1件だけ残す
                cat_items.append({
                    "source": feed["name"],
                    "title": title,
                    "link": link,
                    "summary": clean_text(entry["summary"]),
                    "published": published.astimezone(JST).isoformat(timespec="minutes") if published else None,
                })

        result["categories"].append({
            "id": cat["id"],
            "title": cat["title"],
            "max_items": cat.get("max_items", 8),
            "items": cat_items,
        })

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
