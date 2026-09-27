#!/usr/bin/env python3
"""ダイジェストの公開結果を Discord の Webhook に通知する。

Webhook URL は環境変数 DISCORD_WEBHOOK_URL から読む（リポジトリには書かない）。
未設定の場合は何もせずに正常終了するので、フォークした環境でもそのまま動く。

使い方:
    python3 scripts/notify_discord.py success --date 2026-09-28
    python3 scripts/notify_discord.py failure --date 2026-09-28 --message "全フィードの取得に失敗"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JST = timezone(timedelta(hours=9))
FIELD_VALUE_MAX = 1024
COLOR_SUCCESS = 0x2EA043  # 緑
COLOR_FAILURE = 0xE5484D  # 赤
USER_AGENT = "DiscordBot (https://github.com/bonkotu25/azumayoru-daily-news-digest, 1.0)"


def repo_web_url() -> str:
    """git の origin から https://github.com/<owner>/<repo> を組み立てる。"""
    try:
        remote = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "remote", "get-url", "origin"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return ""
    m = re.search(r"([^/:]+)/([^/]+?)(?:\.git)?/?$", remote)
    return f"https://github.com/{m.group(1)}/{m.group(2)}" if m else ""


def digest_path(day: date) -> Path:
    return REPO_ROOT / "digests" / f"{day:%Y}" / f"{day:%m}" / f"{day:%d}" / "README.md"


def parse_digest(text: str) -> tuple[list[str], list[tuple[str, int]], datetime | None]:
    """ダイジェストから、ハイライトの行、カテゴリごとの掲載件数、取得日時を取り出す。"""
    highlights: list[str] = []
    categories: list[tuple[str, int]] = []
    body, _, footer = text.partition("\n---\n")
    for section in re.split(r"^## ", body, flags=re.MULTILINE)[1:]:
        heading, _, content = section.partition("\n")
        heading = heading.strip()
        if heading == "今日のハイライト":
            highlights = [line[2:].strip() for line in content.splitlines() if line.startswith("- ")]
        else:
            categories.append((heading, len(re.findall(r"^### \[", content, flags=re.MULTILINE))))

    fetched_at = None
    m = re.search(r"取得: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) JST", footer)
    if m:
        fetched_at = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=JST)
    return highlights, categories, fetched_at


def short_name(heading: str) -> str:
    """「技術記事（Qiita / Zenn）」→「技術記事」のように、括弧書きを除く。"""
    return re.sub(r"[（(].*?[）)]", "", heading).strip()


def truncate(text: str, limit: int) -> str:
    return text if len(text) <= limit else text[: limit - 1] + "…"


def count_fields(categories: list[tuple[str, int]]) -> list[dict]:
    """カテゴリ別の件数を 2 列で並べる。

    Discord は横並びの項目を 1 行に最大 3 つ置くので、2 つごとに空の項目を挟んで 2 列にそろえる。
    """
    spacer = {"name": "\u200b", "value": "\u200b", "inline": True}
    fields: list[dict] = []
    for i, (name, n) in enumerate(categories):
        fields.append({"name": short_name(name), "value": f"{n}件", "inline": True})
        if i % 2 == 1:
            fields.append(spacer)
    return fields


def success_payload(day: date) -> dict:
    highlights, categories, fetched_at = parse_digest(digest_path(day).read_text(encoding="utf-8"))
    total = sum(n for _, n in categories)
    fields = count_fields(categories)
    if highlights:
        value = "\n".join(f"{i}. {h}" for i, h in enumerate(highlights, 1))
        fields.append({"name": "今日のハイライト", "value": truncate(value, FIELD_VALUE_MAX), "inline": False})

    embed = {
        "title": f"[{day:%Y-%m-%d}] ニュースダイジェスト（{total}件）",
        "color": COLOR_SUCCESS,
        "fields": fields,
        "footer": {"text": f"データ取得日: {day:%Y-%m-%d}"},
    }
    if fetched_at:
        embed["timestamp"] = fetched_at.isoformat()  # Discord が閲覧者の時刻表示に合わせて表示する
    url = repo_web_url()
    if url:
        embed["url"] = f"{url}/tree/main/digests/{day:%Y}/{day:%m}/{day:%d}"
    return {"embeds": [embed]}


def failure_payload(day: date, reason: str) -> dict:
    embed = {
        "title": f"[{day:%Y-%m-%d}] ダイジェストを公開できませんでした",
        "color": COLOR_FAILURE,
        "fields": [{"name": "理由", "value": truncate(reason, FIELD_VALUE_MAX), "inline": False}],
        "timestamp": datetime.now(JST).isoformat(),
    }
    return {"embeds": [embed]}


def send(webhook_url: str, payload: dict) -> None:
    payload["allowed_mentions"] = {"parse": []}  # 本文中の @everyone などでメンションを飛ばさない
    req = urllib.request.Request(
        webhook_url + ("&" if "?" in webhook_url else "?") + "wait=true",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": USER_AGENT},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        resp.read()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("status", choices=["success", "failure"])
    parser.add_argument("--date", type=date.fromisoformat, required=True, help="ダイジェストの日付（YYYY-MM-DD）")
    parser.add_argument("--message", default="", help="failure のときの理由")
    args = parser.parse_args()

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("DISCORD_WEBHOOK_URL が未設定のため、通知をスキップしました。")
        return 0

    if args.status == "success":
        payload = success_payload(args.date)
    else:
        payload = failure_payload(args.date, args.message or "不明")

    try:
        send(webhook_url, payload)
    except Exception as e:  # URL を含むエラーメッセージを出さないよう、種類だけ表示する
        print(f"Discord への通知に失敗しました: {type(e).__name__} {getattr(e, 'code', '')}", file=sys.stderr)
        return 1

    print("Discord に通知しました。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
