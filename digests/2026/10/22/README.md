# 2026-10-22 のダイジェスト

## 今日のハイライト

- PHP に「緊急」レベルの脆弱性 2 件、修正版が公開され国内サービスで緊急メンテナンスが相次ぐ
- OpenAI が COBOL など学習データの少ない言語でのコーディング・移行能力の向上を発表
- Cloudflare が TypeScript を Rust に移植した「tsrs」を発表

## AI

### [OpenAI、「COBOL」など学習リソースの少ない言語でのコーディング能力が大幅向上 COBOL移行の正解率は最大97.9％に](https://www.itmedia.co.jp/news/article/2610/21/2000002447/)
<sub>ITmedia AI+ ・ 10/21 10:35</sub>

学習データの少ない COBOL や Fortran などでも、最新モデル「GPT-6 Astra」の開発・移行能力が大きく伸びたという発表です。COBOL から現代言語への移行テストでも高い正解率を示したとされています。

### [OpenAIの常時稼働エージェント「dots」、日本のユーザー数は「世界2位」 「仕事の在り方を大きく変える可能性」と長?社長](https://www.itmedia.co.jp/aiplus/article/2610/21/2000002457/)
<sub>ITmedia AI+ ・ 10/21 15:43</sub>

OpenAI の新しいエージェント機能「dots」について、OpenAI Japan 社長が日本のユーザー数は世界 2 位だと説明しました。

### [AIに200万円渡してネットショップを1年運営させてみた──Alibabaの研究者らがシミュレーション 資産14倍の例も](https://www.itmedia.co.jp/news/article/2610/21/2000002421/)
<sub>ITmedia AI+ ・ 10/21 12:00</sub>

Alibaba の Qwen チームらが、LLM エージェントに 1 年間のネットショップ運営を任せて長期のビジネス運用能力を測る論文を発表しました。資産が 14 倍になった例もあるそうです。

### [「政府機関向けGemini」登場 米国政府・自治体と共同開発 データをプライベートクラウドに保持](https://www.itmedia.co.jp/aiplus/article/2610/21/2000002470/)
<sub>ITmedia AI+ ・ 10/21 16:41</sub>

Google Cloud が米政府機関向けの Gemini をプレビュー公開しました。データは各機関の私設環境に置き、許可なく学習には使わないとしています。

### [PFNとTenstorrentがタッグ、生成AI特化プロセッサ開発へ 超高メモリ帯域幅、光電融合技術を実装](https://www.itmedia.co.jp/aiplus/article/2610/21/2000002438/)
<sub>ITmedia AI+ ・ 10/21 07:00</sub>

PFN と Tenstorrent が生成 AI 向けプロセッサを含むシステムの共同開発を開始。CPU は Tenstorrent、AI プロセッサは PFN が担当し、NVIDIA GPU 中心の市場に挑みます。

### [AI利用のペネトレーションテストツール「ARTEX」を使用した攻撃、日本企業20社を標的に 同一グループが複数犯行か 対策のポイントは GMO系列調査](https://www.itmedia.co.jp/aiplus/article/2610/21/2000002452/)
<sub>ITmedia AI+ ・ 10/21 12:08</sub>

GMO サイバーセキュリティ byイエラエの調査で、自律型ペネトレーションテストツール「ARTEX」を使った不正アクセスが、約 20 の日本企業を標的にしていたことが分かりました。

### [三菱電機、ヒューマノイドと工作機械が連携して加工 JIMTOF20226でデモ](https://monoist.itmedia.co.jp/mn/articles/2610/21/news073.html)
<sub>ITmedia AI+ ・ 10/22 06:15</sub>

フィジカル AI を介して、ヒューマノイドロボットと CNC 工作機械が連携する加工システムを開発。自然言語の指示から加工タスクを自動生成します。

### [デジタル庁、「神Excel」対策ツールを公開 AIと組み合わせたデータ整備方法も紹介](https://www.itmedia.co.jp/aiplus/article/2610/21/2000002475/)
<sub>ITmedia AI+ ・ 10/21 18:42</sub>

Excel ファイルが機械にとって読みやすいかを判定するツール「Harunobu」をデジタル庁が公開しました。セル結合の多い「神Excel」の対策にも使えるとのことです。

## IT

### [PHPの「緊急」レベルの脆弱性、開発元が修正バージョン公開 「直ちにアップデートを」](https://www.itmedia.co.jp/news/article/2610/22/2000002480/)
<sub>ITmedia NEWS ・ 10/22 00:53</sub>

リモートコード実行につながる緊急の脆弱性 2 件を修正した PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35 が公開され、公式は全ユーザーに即時の更新を推奨しています。

### [Cloudflare、TypeScriptをRustに移植した「tsrs」を発表。TypeScript 7より最大で70％少ないメモリで8倍速。今後、LSPなどTypeScriptの全機能をサポート予定](https://www.publickey1.jp/blog/26/cloudflaretypescriptrusttsrstypescript_7708lsptypescript.html)
<sub>Publickey ・ 10/22 00:42</sub>

Cloudflare が TypeScript の Rust 移植版「tsrs」を発表しました。開発には同社が買収した VoidZero も関わっています。

### [認証局eMudhraの中間証明書、秘密鍵が「数ミリ秒」で復元可能な脆弱性 大手各社が緊急遮断](https://www.itmedia.co.jp/news/article/2610/21/2000002444/)
<sub>ITmedia NEWS ・ 10/21 09:17</sub>

インドの認証局 eMudhra の中間証明書 8 件で秘密鍵を第三者が復元できる状態でした。主要ブラウザは遮断済みで、Go の開発チームなどが非ブラウザ環境向けの修正を配布しています。

### [Google Cloud障害で英国が混乱「ATMで引き出せない」「裁判延期」……ロンドン拠点の電源不具合、約8時間にわたり](https://www.itmedia.co.jp/news/article/2610/21/2000002445/)
<sub>ITmedia NEWS ・ 10/21 09:32</sub>

ロンドン拠点の電源不具合による障害で、英国の複数の大手銀行で送金やカード決済が止まり、裁判所の遠隔審理も延期されました。

### [LiteLLMパッケージ 再侵害の概要と対策指針 - GMO Flatt Security Blog](https://blog.flatt.tech/entry/litellm_2nd_compromise)
<sub>はてなブックマーク IT 人気エントリー ・ 10/21 21:37</sub>

PyPI の litellm に 10 月 21 日、情報窃取機能を持つ悪性コードが再び注入されました。3 月の事案とは別の再侵害で、国内向けに概要と対策がまとめられています。

### [GitHub CLI: Opt in to expiring, auto-refreshing OAuth tokens - GitHub Changelog](https://github.blog/changelog/2026-10-21-github-cli-opt-in-to-expiring-auto-refreshing-oauth-tokens/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/22 02:00</sub>

GitHub CLI で、有効期限があり自動更新される OAuth 認証情報をパブリックプレビューとして選択的に使えるようになりました。

### [「お名前.com デスクトップクラウド」不正プログラム設置で全プラン停止 FX用VPS、2万6739サーバに影響か](https://www.itmedia.co.jp/news/article/2610/21/2000002442/)
<sub>ITmedia NEWS ・ 10/21 07:55</sub>

FX 自動売買向け VPS で第三者による不正アクセスがあり、一部の環境に不正プログラムが設置されたため、全プランのサーバを停止しています。

### [わずか2週間でGitHubスター30万超 AIでリバースエンジニアリングする「REA」が話題](https://ascii.jp/elem/000/004/444/4444350/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/21 13:48</sub>

AI エージェント向けのリバースエンジニアリング支援ツール「REA」が、10 月 2 日の 41 スターから 21 日には約 34.8 万スターへ急増して話題です。

## 技術記事（Qiita / Zenn）

### [AI の「直しました」に証拠を付けさせろ！ pstack を Claude Code に入れてみた](https://qiita.com/kobayashi-fuuki/items/a7fbba06bb158dae0e11)
<sub>Qiita 人気記事 ・ 10/21 09:45</sub>

Cursor の公式プラグインを Claude Code 環境に導入し、AI の修正報告に証拠を付けさせる運用を試した記事です。

### [Claude Code の長い会話は、閉じずに席を外したほうが安かった。1時間後に戻った費用は閉じた場合の1割](https://qiita.com/suwa_nobu/items/bc2e80a8c1d61b0b2cfe)
<sub>Qiita 人気記事 ・ 10/21 16:01</sub>

Claude Code 2.1.299 のアイドル時コンパクション追加を受けて、長い会話を閉じる場合と離席する場合の費用を比べています。

### [Claude Codeの新コマンド「/advisor fable」で、難所だけFableへ自動で相談するAI活用](https://qiita.com/inoyu-qiita/items/2bf7c23b9586ccafb9fd)
<sub>Qiita 人気記事 ・ 10/21 08:46</sub>

計画は Opus、難所は Fable に相談、実装は Sonnet と、作業に応じてモデルを自動で使い分ける構成を試しています。

### [ARC-AGI-3 の 99.9% を中心に GPT-6 Astra のベンチマークを理解したい](https://qiita.com/masa-asa/items/9d62bfeb91140c7a88a7)
<sub>Qiita 人気記事 ・ 10/21 15:45</sub>

GPT-6 Astra の ARC-AGI-3 での高スコアを軸に、発表されたベンチマークの数字を読み解こうとする記事です。

### [cronのclaude -pが"ok"だけで4万トークン——--safe-modeと--tools ""で98%削減](https://zenn.dev/yosiki/articles/claude-p-cron-token-diet)
<sub>Zenn トレンド ・ 10/21 18:22</sub>

定期実行の `claude -p "ok"` が毎回大量のコンテキストを読み込んでいた問題を、オプション指定で大幅に減らした事例です。

### [Laravel の token guard 認証バイパス、表に無い 11 以下はどうなの？全タグのソースを確認してみた](https://zenn.dev/nix/articles/236ceb8194a9c5)
<sub>Zenn トレンド ・ 10/21 09:52</sub>

10 月 19 日の Laravel アドバイザリ（MySQL / MariaDB で token guard 利用時）について、公表対象外の旧バージョンを全タグのソースで確認した記事です。

### [Claude Sonnet 5.5へ載せ替えると400になる4つの書き方：smokeテストで先に潰す](https://zenn.dev/yunisuta/articles/claude-sonnet-400-smoke-anthropic-tnzgdo)
<sub>Zenn: LLM ・ 10/21 15:45</sub>

モデル ID の置き換えだけで 400 エラーになるリクエストの形を、最小のスモークテストで再現し、新しい書き方へ直す手順を紹介しています。

### [MCPが「ステートレス」になった日 — 2026-07-28仕様を、金融系フルスタックエンジニアの視点で読み解く](https://zenn.dev/ojineko/articles/5369ceca94cd17)
<sub>Zenn: AI ・ 10/21 19:01</sub>

MCP の新仕様 2026-07-28 でセッションを前提としない設計に変わった点を、単なる最適化ではない設計思想の転換として読み解きます。

### [MiniCPM5-2BをVRAM 6GBで動かす：約115 tok/s、思考の切り方・min_p・Ollamaテンプレートの注意](https://zenn.dev/localai_lab/articles/3ff120145cb92d)
<sub>Zenn: LLM ・ 10/21 11:38</sub>

VRAM 6GB の GPU で公式 GGUF の Q4_K_M が約 115 tok/s、Q8_0 で約 81 tok/s という実測と、設定上の注意点をまとめています。

### [VRAM 8GB・12GB でローカルLLMはどれだけ遅くなる？ 同じモデルで実測した](https://zenn.dev/shacikku3/articles/vram-8gb-12gb-local-llm-speed)
<sub>Zenn: LLM ・ 10/21 15:08</sub>

同じモデル（gemma4:12b-it-q8_0）を RTX 4080 など複数の条件で動かし、生成速度を比較した実測記事です。

## 日経

### [アクティビストに狙われたダイキン 失敗を許容する文化を残せるか (ダイキン 5兆円企業の盆踊り)](https://business.nikkei.com/atcl/gen/19/00944/101300004/)
<sub>日経ビジネス電子版 ・ 10/22 05:00</sub>

アクティビストの標的となったダイキンが、経営指標を「額」から「率」へ移す転換を打ち出し、社員の自主性を支えてきた文化との両立が課題になっています。

### [ニデック歴代5社長に責任認定 276億円損害の根底に永守氏の影 (ガバナンスの今・未来)](https://business.nikkei.com/atcl/gen/19/00304/102100273/)
<sub>日経ビジネス電子版 ・ 10/21 17:00</sub>

会計不正に関する役員責任調査委員会の報告書が、損害に創業者の永守氏が大きく関わっていたことを改めて示したと伝えています。

### [26年の半導体売上高、8月までの累計で1兆米ドルを突破](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12092/)
<sub>日経クロステック ・ 10/22 05:00</sub>

米 SIA の発表で、2026 年の世界半導体売上高が 8 月までの累計で早くも 1 兆米ドルを超えました。

### [半導体メモリーの27年、市場拡大続き競争激化 中国2社が台風の目](https://xtech.nikkei.com/atcl/nxt/column/18/03740/100800014/)
<sub>日経クロステック ・ 10/22 05:00</sub>

AI サーバー向けの需要拡大と価格上昇を背景に、2027 年もメモリー市場の拡大と競争の激化が続くという見通しです。

### [Anthropic「物理AI版MCP」を米量子QuEraが実証、エラーの復旧成功率99％](https://xtech.nikkei.com/atcl/nxt/column/18/00138/101502126/)
<sub>日経クロステック ・ 10/22 05:00</sub>

Anthropic が公開した「MHS（Model Hardware Standard）」を米 QuEra が実証した、という内容です。

### [Microsoftが数百のAIモデルをオンプレミスで実行可能に、ソブリンAI向け](https://xtech.nikkei.com/atcl/nxt/news/24/03432/)
<sub>日経クロステック ・ 10/21 05:00</sub>

Microsoft が 10 月 20 日、オンプレミス環境で数百の AI モデルを実行できるようにすると発表しました。ソブリン AI 関連機能の拡充の一環です。

### [NECの委託先にサイバー攻撃、複数顧客でシステム障害と情報漏洩](https://xtech.nikkei.com/atcl/nxt/news/24/03431/)
<sub>日経クロステック ・ 10/21 09:25</sub>

NEC は、委託先が 9 月下旬に受けた攻撃で、窃取された正規アカウントの認証情報が顧客環境への不正アクセスに使われたと発表しました。

### [TDKと太陽誘電の提携、専門家「背景に中国台頭」 再編へ発展も](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12075/)
<sub>日経クロステック ・ 10/21 05:00</sub>

TDK と太陽誘電が AI 向け電子部品の共同開発などの提携を検討へ。将来の資本提携も協議する方針です。

---
<sub>取得: 2026-10-22 06:50 JST ／ 取得失敗: なし</sub>
