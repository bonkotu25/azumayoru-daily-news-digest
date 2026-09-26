# azumayoru-daily-news-digest

AI・IT・技術記事・日経のニュースを RSS から集め、Claude が毎朝要約して蓄積するリポジトリです。

📰 ダイジェストは [`digests/`](digests/) に `年/月/日/README.md` の形で置かれます（例: `digests/2026/09/27/`）。

## カテゴリと情報源

| カテゴリ | 情報源 |
|---|---|
| AI | ITmedia AI+ |
| IT | ITmedia NEWS、Publickey、はてなブックマーク IT 人気エントリー |
| 技術記事 | Qiita 人気記事、Zenn トレンド、Zenn（AI / LLM トピック） |
| 日経 | 日経ビジネス電子版、日経クロステック |

情報源の定義は [`sources.toml`](sources.toml) にあります。

## 仕組み

```
Claude Code の Routine（毎朝 6:50 JST）
  └─ CLAUDE.md の手順に従って実行
       1. scripts/fetch_feeds.py で RSS を取得（直近30時間・掲載済みを除外）
       2. Claude が記事を選び、要約を書く
       3. digests/YYYY/MM/DD/README.md を作成
       4. PR を作成してマージ（main への直接 push は禁止）
```

- 実行には、リポジトリ所有者の Claude の利用枠を使います。実行スケジュールは Claude 側の設定で、このリポジトリには含まれていません。
- 自分の環境で同じことをしたい場合は、このリポジトリをフォークし、ご自身の Claude Code で Routine を設定してください。

## 掲載方針

- 掲載するのは、記事の **タイトル・リンク・短い要約** だけです。記事本文は取得も転載もしません。
- 要約は、RSS フィードに含まれる情報をもとに Claude が作成したものです。正確な内容は、必ずリンク先の元記事で確認してください。
- 各記事の著作権は、それぞれの配信元に帰属します。

## 運用メモ

### ネットワーク許可ドメイン

Claude Code on the web の環境で実行する場合、次のドメインへのアクセスを許可する必要があります。

```
rss.itmedia.co.jp
www.publickey1.jp
b.hatena.ne.jp
qiita.com
zenn.dev
business.nikkei.com
xtech.nikkei.com
```

### 手動で実行する

```bash
python3 scripts/fetch_feeds.py              # 直近30時間の記事を JSON で出力
python3 scripts/fetch_feeds.py --help       # オプション一覧
```

Python 3.11 以上が必要です。外部パッケージは使いません。
