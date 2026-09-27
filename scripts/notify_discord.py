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
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DISCORD_MAX_CHARS = 2000
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


def success_message(day: date) -> str:
    text = digest_path(day).read_text(encoding="utf-8")
    count = len(re.findall(r"^### \[", text, flags=re.MULTILINE))

    highlights: list[str] = []
    section = re.search(r"^## 今日のハイライト\n(.*?)(?=^## )", text, flags=re.MULTILINE | re.DOTALL)
    if section:
        highlights = [line[2:].strip() for line in section.group(1).splitlines() if line.startswith("- ")]

    lines = [f"📰 **{day:%Y-%m-%d} のダイジェスト**を公開しました（{count}件）"]
    lines += [f"・{h}" for h in highlights]
    url = repo_web_url()
    if url:
        lines.append(f"{url}/tree/main/digests/{day:%Y}/{day:%m}/{day:%d}")
    return "\n".join(lines)


def failure_message(day: date, reason: str) -> str:
    return f"⚠️ **{day:%Y-%m-%d} のダイジェスト**を公開できませんでした\n理由: {reason}"


def send(webhook_url: str, content: str) -> None:
    if len(content) > DISCORD_MAX_CHARS:
        content = content[: DISCORD_MAX_CHARS - 1] + "…"
    payload = {
        "content": content,
        "allowed_mentions": {"parse": []},  # 本文中の @everyone などでメンションを飛ばさない
    }
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
        content = success_message(args.date)
    else:
        content = failure_message(args.date, args.message or "不明")

    try:
        send(webhook_url, content)
    except Exception as e:  # URL を含むエラーメッセージを出さないよう、種類だけ表示する
        print(f"Discord への通知に失敗しました: {type(e).__name__} {getattr(e, 'code', '')}", file=sys.stderr)
        return 1

    print("Discord に通知しました。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
