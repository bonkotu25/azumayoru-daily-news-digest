# 2026-10-12 のダイジェスト

## 今日のハイライト

- Anthropic が、自社の AI モデル Claude が評価や社内利用の中で実在のウェブサイトやシステムに意図しない送信を行っていたと公表（AI）
- ロシア IT 大手 Yandex のクラウドで電源障害が発生し、サービスが利用できない状態に（IT）
- Hono Conference 2026 が開催され、Hono の採用事例と現状に関する登壇資料が公開（IT）

## AI

### [AnthropicのAIモデルが米国政府サイトへ意図しない送信を行っていた事案についてまとめてみた - piyolog](https://piyolog.hatenadiary.jp/entry/2026/10/11/012014)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 06:06</sub>

2026年10月9日に Anthropic が公表した、Claude が評価や社内利用の中で実在のサイトやシステムに意図しない通信を行っていた事案を時系列で整理した記事です。

### [「AIに指示するだけでひとりでそこそこのゲームが作れてしまいます」ゲームクリエイター・堀井雄二氏がAIを使い30分ほどでゲームを作成し、様々な反応が寄せられる](https://togetter.com/li/2756939)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 21:39</sub>

堀井雄二氏が、AI への指示だけで 30 分ほどでゲームを作れたと投稿し、その発言に寄せられた反応をまとめています。

### [CPUのみで動作するリアルタイム多言語音声認識「早耳」、GPUもクラウドAPIも使わずメモリ2GB未満でライブ字幕表示からブラウザ表示・話者ラベル付け・翻訳字幕まで可能](https://gigazine.net/news/20261011-hayamimi/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 13:33</sub>

GPU もクラウド API も使わず CPU だけで動く音声認識ツール「Hayamimi（早耳）」の紹介です。ライブ字幕や話者ラベル、翻訳字幕にも対応しているとのことです。

## IT

### [Yandexのデータセンター障害についてまとめてみた - piyolog](https://piyolog.hatenadiary.jp/entry/2026/10/11/011521)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 06:06</sub>

10月8日に Yandex Cloud の ru-central1-b で電源が途絶し、サービスが使えなくなった障害の経緯をまとめた記事です。

### [月間100万人のサービス刷新で、 技術選定をHonoに振り切った話](https://speakerdeck.com/yutobara/gekkan-100-mannin-no-sabisu-sasshin-de-gijutsu-sentei-o-hono-ni-furikita-hanashi-e49c651f-8130-48bb-b6ef-eac3cc9f358a)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 17:34</sub>

Hono Conference 2026 の登壇資料です。月間 100 万人のサービスを 6 人と AI で作り直した際の開発基盤づくりと、Hono が効いた理由を紹介しています。

### [GitHub Actions上で証明書を付与するサプライチェーン構築 | おそらくはそれさえも平凡な日々](https://songmu.jp/riji/entry/2026-10-11-github-actions-artifact-attestations.html)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 18:26</sub>

サプライチェーンインシデントが相次ぐ中、OSS の配布側として GitHub Actions 上で成果物に証明書（attestation）を付与する仕組みを構築した記録です。

### [pixiv閲覧中にMcAfeeを装ったAndroidの盗聴警告画面が突然表示…カメラ・マイク動作中や「誰かがあなたの銀行情報と連絡先にアクセスしようとしています」という警告文も](https://togetter.com/li/2756877)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 17:26</sub>

pixiv 閲覧中に McAfee を装った偽の警告画面が Android に表示されたという報告のまとめです。

### [オートパイロットは外せる人間を前提にしている — AI時代のエンジニア技能維持を航空業界に学ぶ](https://zenn.dev/shimitaro/articles/eb45d8d63c7bd1)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 10:59</sub>

AI にコードを書かせる時代にエンジニアが残すべき技能について、航空業界の制度を一次資料にたどって考察した記事です。

## 技術記事（Qiita / Zenn）

### [Claude Code の deny に `../` を書いたら、隣のフォルダへの書き込みが止まらなかった（2.1.296で実測）](https://zenn.dev/emilk1225/articles/73356c9b0e156d)
<sub>Zenn: AI ・ 10/11 19:16</sub>

Claude Code 2.1.296 の deny 設定に `../` を書いた場合の挙動を、筆者の Windows 10 環境で実測した検証記事です。

### [プロンプトキャッシュは、変数の位置ひとつで 72% から 0% になる。LLM の費用を決めていたのは呼ぶ回数だった](https://zenn.dev/maruhana/articles/llm-call-count-prompt-cache-variable-position)
<sub>Zenn: LLM ・ 10/11 19:11</sub>

プロンプト中の変数の位置によってキャッシュ率が 72% から 0% に変わる事例を通じ、LLM の費用を左右する要因を整理しています。

### [Uzuの「llama.cpp比4倍」を整理する — 投機的デコードを外すと27 tok/s](https://zenn.dev/amu_lab/articles/uzu-speculative-decoding-16gb-mac-benchmark)
<sub>Zenn: LLM ・ 10/11 11:50</sub>

Apple Silicon 向け推論エンジン Uzu の「llama.cpp 比 4 倍」という報告を、投機的デコードの有無で切り分けて検討した記事です。

### [AIが書いたRailsを全部は読まない - 契約による設計とミューテーションテストでレビューの場所を絞る](https://zenn.dev/okamyuji/articles/rails-invariants-evilution-crap)
<sub>Zenn: AI ・ 10/11 13:15</sub>

AI が出す数百行の差分を全部は読み切れない前提で、契約による設計とミューテーションテストでレビューすべき箇所を絞る方法を紹介しています。

### [Claude Code プラグインはスキル化しても軽くならなかった。必要なスキルだけ symlink で配って無人タスクの常時コストを削った](https://zenn.dev/serotoninmax/articles/claude-code-plugin-skill-links)
<sub>Zenn: LLM ・ 10/11 10:09</sub>

プラグインをスキル化しても軽くならなかったため、必要なスキルだけを symlink で配って無人タスクの常時コストを減らした工夫を紹介しています。

### [Firestore エミュレーターが重すぎたので、Java なしで動く互換エミュレーターを Rust で作った](https://qiita.com/nomunomu0504/items/f764426407431c183016)
<sub>Qiita 人気記事 ・ 10/11 15:35</sub>

公式エミュレーターが重いという課題から、Java を使わずに動く互換エミュレーター「hidane（火種）」を Rust で作った紹介記事です。

### [自分用のDesklyにRemote MCPとOAuthを付けた。Claude Codeからの読み書きと、スマホでつまずいたこと](https://qiita.com/ishizakahiroshi/items/7eb94a303a1aab6e0f98)
<sub>Qiita 人気記事 ・ 10/11 12:58</sub>

Cloudflare Workers 上の入口に Remote MCP と OAuth を付け、Claude Code から読み書きできるようにした過程と、スマホで同意ボタン周りでつまずいた点をまとめています。

### [【AWS】GitHub ActionsとAgentCore Evaluationsでエージェントの評価をCI/CDに組み込んでみた](https://qiita.com/yakumo_09/items/6f3936d9f7255a4259d9)
<sub>Qiita 人気記事 ・ 10/11 21:51</sub>

AWS のブログを参考に、GitHub Actions から AgentCore Evaluations を呼んでエージェントの品質ゲートを CI/CD に組み込んだ記事です。

### [Claude Codeに任せる範囲と止める仕組みの設計 〜計画モード・SessionStartフック・/loop・課金前確認の使い分け〜](https://qiita.com/charge0315/items/fcec85cc5250e39bab97)
<sub>Qiita 人気記事 ・ 10/11 08:33</sub>

「全部任せる」と「全部確認する」の間で、計画モードやフックなどを使い分けて任せる範囲と止める仕組みを設計する考え方を紹介しています。

## 日経

本日の該当記事はありません

---
<sub>取得: 2026-10-12 06:50 JST ／ 取得失敗: なし</sub>
