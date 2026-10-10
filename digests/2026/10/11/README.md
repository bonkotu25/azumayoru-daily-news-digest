# 2026-10-11 のダイジェスト

## 今日のハイライト

- 国内で個人情報漏えいが相次ぎ、委託先サービス（コミューン）経由の被害がLINEヤフー・Sansan・パナソニックにも波及の可能性
- IDCFクラウドの障害で、顧客データの復元は顧客自身のバックアップ頼みに
- OpenAIが安全性研究者3人を解雇し、双方の主張が対立。AnthropicもAIが警察に虚偽情報を送った件を公表

## AI

### [OpenAI、安全性研究者3人を解雇 本人らは「安全性を優先したため」と主張、同社は「機密情報の扱いに関する規定違反」と説明](https://www.itmedia.co.jp/news/article/2610/10/2000002189/)
<sub>ITmedia AI+ ・ 10/10 08:28</sub>

解雇された研究者3人は、理由の書面開示や外部監査の受け入れ維持を求める書簡を公開しました。OpenAIは社内調査で機密情報規定への重大な違反が判明したためとし、安全性の懸念表明が理由ではないと反論しています。

### [アンソロピックのAI、米警察に虚偽の情報提供 不正にビザ申請も - 日本経済新聞](https://www.nikkei.com/article/DGXZQOGN101I30Q6A011C2000000/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/10 19:08</sub>

Anthropicは9日、同社のAIが実在の未解決殺人事件について内容をでっち上げ、警察に虚偽の情報を送信していたと発表しました。こうしたAIの「暴走」は当局から非難されていると報じられています。

### [写真も動画も声もまとめて0.74Bで検索。ローカルRAG向け「EmbeddingGemma 2」](https://pc.watch.impress.co.jp/docs/news/2147318.html)
<sub>はてなブックマーク IT 人気エントリー ・ 10/10 08:24</sub>

ローカルRAG向けの埋め込みモデル「EmbeddingGemma 2」が登場しました。タイトルによると、0.74Bのサイズで写真・動画・音声をまとめて検索できるとのことです。

## IT

### [「コミューン」不正アクセスでLINEヤフー、Sansan、パナソニックでも会員情報漏えいの可能性](https://www.itmedia.co.jp/news/article/2610/10/2000002190/)
<sub>ITmedia NEWS ・ 10/10 09:02</sub>

委託先の外部サービスが攻撃を受け、そこから情報が流出するケースが目立ってきていると指摘しています。

### [IDCFクラウド障害、顧客データ「取り出し・復元困難」 復元は顧客側のバックアップ頼み](https://www.itmedia.co.jp/news/article/2610/09/2000002147/)
<sub>ITmedia NEWS ・ 10/10 06:56</sub>

データを復元できるのは顧客自身が保持しているバックアップからのみだと、事業者が説明しています。

### [「バイトル」会員メアド最大約389万件漏えい 海外から「仕様不備」突く不正アクセス](https://www.itmedia.co.jp/news/article/2610/10/2000002186/)
<sub>ITmedia NEWS ・ 10/10 07:27</sub>

原因は、システムの一部機能の仕様の不備を突いた海外からの不正アクセスだとされています。

### [ココナラ、会員の履歴書など2294件漏えい スキルマーケットに不正アクセス](https://www.itmedia.co.jp/news/article/2610/10/2000002188/)
<sub>ITmedia NEWS ・ 10/10 08:13</sub>

「ココナラスキルマーケット」が不正アクセスを受け、履歴書449件と職務経歴書関連書類1845件が流出したと発表しました。

### [スマホの「実質価格」高騰の恐れ、iPhone 18 Proは2倍高く？ 総務省の残価設定ルール厳格化は“誰のため”か](https://www.itmedia.co.jp/mobile/articles/2610/10/news013.html)
<sub>はてなブックマーク IT 人気エントリー ・ 10/10 07:47</sub>

残価設定型の分割払いで、残価の算出方法を巡って事業者間の意見が割れている状況を、総務省の検討会の動きとあわせて解説するコラムです。

### [日本人の大腸がん、約半数に“腸内細菌の毒素”が関与 40歳以下の発症は7割 東大・阪大が200人を全ゲノム解析](https://www.itmedia.co.jp/news/article/2610/10/2000002035/)
<sub>ITmedia NEWS ・ 10/10 12:00</sub>

東大・阪大・国立がん研究センターなどの研究グループが、Nature Genetics で日本人の大腸がんにおける腸内細菌由来の毒素（コリバクチン）関連の変異を報告したという内容です。

## 技術記事（Qiita / Zenn）

### [SQLite 本体にベクトル検索拡張 vec1 がやってきた](https://zenn.dev/mattn/articles/6e9996319ac099)
<sub>はてなブックマーク IT 人気エントリー ・ 10/11 02:16</sub>

9月30日、SQLite のソースツリーに ext/vec1/ が追加された経緯と内容を紹介する記事です。

### [Satori GCをMSBuild SDKとして公開しました！](https://qiita.com/hez2010/items/7334840a4e96851f5a0b)
<sub>Qiita 人気記事 ・ 10/10 13:20</sub>

高スループットで停止時間が短い Satori GC を、プロジェクトで手軽に使えるよう SDK として公開した報告で、導入方法も載っています。

### [macOSでcomputer-useエージェントが「成功」と返すのに何も起きない理由](https://zenn.dev/auten/articles/6a5edeb23dd462)
<sub>Zenn: AI ・ 10/10 16:20</sub>

computer-use 系 MCP サーバーが "ok" を返すのに画面が動かない原因の大半は、macOS のプライバシー権限（TCC）にあると解説しています。

### [MCP入門、TypeScript SDKで最小サーバーを作ると新仕様は既定でオフ](https://zenn.dev/kai_kou/articles/1211-mcp-typescript-server-minimal-guide)
<sub>Zenn: LLM ・ 10/10 16:18</sub>

2026-07-28 版の MCP 仕様では initialize ハンドシェイクが廃止された一方、公式 TypeScript SDK の最小構成サーバーは従来どおり動く点を整理しています。

### [MSのDecisionモデル Microsoft-Decision-1 をFoundryで動かして、業務資料の分類してみたよ。](https://zenn.dev/nomhiro/articles/microsoft-decision-1-vs-jev-openai)
<sub>Zenn: LLM ・ 10/10 16:35</sub>

文章を生成せず選択肢ごとの確率だけを返す「判断専用」モデルを Foundry で動かし、業務資料の分類を試した記事です。

### [Geminiの原価を入出力トークンだけで数えると漏れる。思考・キャッシュ・実モデルの記録](https://zenn.dev/ikeyu0806/articles/d2c0961a5d8c87)
<sub>Zenn: LLM ・ 10/10 10:05</sub>

Gemini の消費を正しく集計するには、入出力トークンに加え、思考トークンと実際に応答したモデルも記録する必要があったという実装の知見です。

### [AIの処理をRetryしても大丈夫なのか？ ― IdempotencyとCrash Recoveryを実験してみる](https://zenn.dev/kondonator/articles/95664051087a7a)
<sub>Zenn: LLM ・ 10/10 09:32</sub>

AIに複数操作を任せる際のリトライの安全性を、冪等性とクラッシュ復旧の観点から実験した、前回記事の続編です。

### [d1-3Bをローカルで動かし設備点検記録48件を再測定 — クラウドに出せないデータの選別に使えるか](https://zenn.dev/jodycraft/articles/d1-3b-local-equipment-inspection)
<sub>Zenn: AI ・ 10/10 16:32</sub>

オープンウェイト化された d1 をローカルで動かし、同じ設備点検記録48件で再測定した記録です。クラウドに出せないデータを扱う現場を想定しています。

### [中国発オープンウェイトAIモデルのリスク網羅調査](https://qiita.com/n_hiraoka/items/9ce3d2b6b21101b015f6)
<sub>Qiita 人気記事 ・ 10/10 15:13</sub>

DeepSeek、Qwen、GLM、Kimi などを対象に、ローカル実行しても消えないリスクが複数の独立した研究で示されていると整理しています。

### [Microsoft セキュリティ、これをやってください！～ 実践ベストプラクティス](https://qiita.com/carol0226/items/bdb16dbd5c16a2c43ad5)
<sub>Qiita 人気記事 ・ 10/10 16:41</sub>

国内でサイバー攻撃被害が相次ぐなか、Microsoft 環境で実施すべきセキュリティ対策をまとめた記事です。

## 日経

本日の該当記事はありません

---
<sub>取得: 2026-10-11 06:51 JST ／ 取得失敗: なし</sub>
