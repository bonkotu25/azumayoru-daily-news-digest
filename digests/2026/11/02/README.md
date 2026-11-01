# 2026-11-02 のダイジェスト

## 今日のハイライト

- OpenAI・Google・Microsoft が、AI 学習への利用可否を robots.txt で一括指定する共通仕様に対応を表明
- GMO インターネットグループへの不正アクセスで、北朝鮮系ハッカー集団の関与の可能性が浮上
- GitHub が「Copilot Fusion」を正式リリース。タスクに応じて AI モデルを自動選択

## AI

### [AI学習への利用拒否をrobots.txtで一括指定へ OpenAIやGoogleなどが対応表明](https://www.itmedia.co.jp/news/article/2611/01/2000002776/)
<sub>ITmedia AI+ ・ 11/01 08:31</sub>

OpenAI・Google・Microsoft が、サイト運営者が AI 学習への利用意向をまとめて指定できる共通の仕組みに対応すると発表しました。robots.txt に共通トークンを書くだけで各社のクローラーを一元管理できる見込みで、Anthropic の担当者も個人名義で実装を表明しています。

### [GitHub、「Copilot Fusion」正式リリース。タスクに応じて最適なAIモデル選択で高性能かつ低コストに。GitHub Universe 2026](https://www.publickey1.jp/blog/26/githubcopilot_fusionaigithub_universe_2026.html)
<sub>Publickey ・ 11/02 23:36</sub>

GitHub Universe 2026 で、新機能「GitHub Copilot Fusion」の正式リリースが発表されました。タスクごとに最適な AI モデルを選ぶことで、性能とコストの両立をうたっています。

### [Wikipediaの編集者はどのようにしてAI生成テキストを見つけて除外しているのか？](https://gigazine.net/news/20261101-wikipedia-ai-content/)
<sub>はてなブックマーク IT ・ 11/01 19:19</sub>

Wikipedia には AI による記事本文の生成・書き換えを原則禁じるガイドラインがあり、違反内容の発見と削除を担うボランティア活動「WikiProject AI Cleanup」の創設メンバーの話が紹介されています。

### [GitHub - vercel-labs/agent-desktop: Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it sees any app's real UI structure through OS accessibility trees and operates…](https://github.com/vercel-labs/agent-desktop)
<sub>はてなブックマーク IT ・ 11/01 11:51</sub>

OS のアクセシビリティツリー経由でデスクトップアプリを読み取り・操作する、AI エージェント向けの computer use ツールです。macOS・Windows・Linux 向けの CLI と C ライブラリとして提供されています。

## IT

### [【独自】GMO攻撃、北朝鮮ハッカーか 複数の痕跡、政府に報告](https://www.47news.jp/15170379.html)
<sub>はてなブックマーク IT ・ 11/01 23:23</sub>

GMO インターネットグループは、一連の不正アクセスの攻撃側に北朝鮮系のハッカー集団がいる可能性が高いと分析しており、マルウェアの特徴などの痕跡から判断したとみられます。政府側にも報告したもようで、真相解明が今後の焦点です。

### [楽天証券、顧客情報流出の可能性 NTTデータ委託先不正アクセスで](https://japan.cnet.com/article/35254251/)
<sub>はてなブックマーク IT ・ 11/01 08:27</sub>

NTTデータの委託先が提供する「デジタル証券プラットフォーム」が不正アクセスを受け、楽天証券は情報が外部に持ち出された可能性の報告を受けました。発生日時は 10 月 30 日とされています。

### [いまのダークウェブでは二段階認証も無力化する「ブラウザのクローンデータ」が売買されており、その対策にはブラウザを使い分けることが有効らしい](https://togetter.com/li/2765521)
<sub>はてなブックマーク IT ・ 11/01 21:12</sub>

ID とパスワードの一覧より、ログイン状態や端末の特徴ごと抜き取った「ブラウザのクローンデータ」が闇市場の主力商品になっているという投稿のまとめです。対策としてブラウザの使い分けが挙げられています。

### [HonoがPRを閉じた理由](https://slides.yusu.ke/foss4g-2026)
<sub>はてなブックマーク IT ・ 11/01 20:35</sub>

Hono の作者による FOSS4G 分科会シンポジウム 2026「AI 時代の FOSS4G」の発表スライドで、OSS 開発における PR の扱いを AI 時代の視点から語る内容です。

### [GitHub - nishikawaakira/waf-dojo: Hands-on AWS WAF training game](https://github.com/nishikawaakira/waf-dojo)
<sub>はてなブックマーク IT ・ 11/01 18:00</sub>

実際の攻撃を防ぎながら AWS WAF を学べる、ハンズオン形式のトレーニングゲームです。環境構築から参加者への配布、運用、後片付けまでの手順も用意されています。

## 技術記事（Qiita / Zenn）

### [AIに証明を書かせてセキュアに開発する言語 Tauto をリリースしました！](https://qiita.com/ryo33/items/3a1a9d1ba2b289b23244)
<sub>Qiita ・ 11/01 17:06</sub>

AI が書いたコードの差分を全部読む負担に対し、AI に証明を書かせることで安全性を担保する言語 Tauto の公開報告です。

### [compact の使い方、間違えるとトークン代 2.75 倍？ Claude Code で測ってわかった 5 つの結論【2026年版】](https://qiita.com/songchong/items/ac9779bb8e8838b546b9)
<sub>Qiita ・ 11/02 04:05</sub>

プロンプトキャッシュの仕組みを踏まえ、Claude Code で compact の使い方によるトークン代の差を計測した記事です。使い方次第でコストが大きく変わるという結果が示されています。

### [ローカル LLM の監視強化（前編）：Qwen の「外への送信」報道を受けて、AI エージェントを OS とネットワークで止める](https://qiita.com/nabe2030/items/0b89543adbf2ba60bf25)
<sub>Qiita ・ 11/01 08:07</sub>

LLM 単体は勝手に外部アクセスできないという前提を整理したうえで、AI エージェントを OS とネットワークの層で制限する対策を扱う前編です。

### [Claude Code に本番のリポジトリを直させ、マージまで任せる範囲の決め方（型とスクリプト付き）](https://zenn.dev/tasukina/books/claude-code-merge-line)
<sub>Zenn ・ 11/02 02:11</sub>

Claude Code に開発を任せた 17 回の運用記録をもとに、人のレビューなしでマージさせてよい範囲の決め方をまとめた本です。

### [Kiro CLIとKiro Crewを改めて入門してAWSで動かすまで](https://zenn.dev/upgradetech/articles/2026-11-kiro-crew-api-key-intro)
<sub>Zenn ・ 11/01 23:43</sub>

Kiro が IDE 以外に CLI・Web・Mobile・Crew の入口を持つようになったことを整理し、API キーによるヘッドレス実行を実機で試した入門記事です。

### [ダウンロードもロードもできるのに0問しか解けない。Ollama公式タグの量子化崖を自分のデータ再集計で確かめた](https://zenn.dev/matsushima_a/articles/day-033-quantized-llm-cliff)
<sub>Zenn ・ 11/01 23:16</sub>

Ollama 公式の一部の低ビット量子化タグが、ロードはできても HumanEval+ をほぼ解けないとする論文を、自身のデータで再集計して確かめた記事です。

### [ベクトル検索だけでは足りない ― ハイブリッド検索とCrossEncoder再ランキングの実装手順](https://zenn.dev/johnny1024/articles/3ecdf0573f5d73)
<sub>Zenn ・ 11/01 23:00</sub>

ベクトル検索とキーワード検索の候補を RRF などで統合し、CrossEncoder で再ランキングする 3 段構成の実装手順を解説しています。

### [Bedrockのプロンプトキャッシュは何を再利用するのか、図で整理した](https://zenn.dev/hknote/articles/bedrock-claude-prompt-caching)
<sub>Zenn ・ 11/01 13:00</sub>

Amazon Bedrock 上の Claude で、プロンプトキャッシュに何が保存され次回どう再利用されるかを、料金の変化も含めて図で整理した記事です。

### [失敗したコード履歴を残すとAIがまた同じミスをする！「失敗履歴の累積」vs「失敗ターンの剪定（Pruning）」実機検証](https://zenn.dev/tappers/articles/ai-labo-e19-error-trace-pruning)
<sub>Zenn ・ 11/01 10:24</sub>

コーディングエージェントの設計パターンを、同一モデル・同一課題のオフライン環境で定量的に A/B 比較した検証シリーズの一編です。

### [脆弱性情報を開発チームで見逃さないようにSlackにRSSフィードを設定してみた](https://qiita.com/yukmaru/items/a3f358cc3e58e435df61)
<sub>Qiita ・ 11/01 03:52</sub>

脆弱性情報にいち早く気づくため、無料で手軽な RSS フィードを Slack に流す仕組みを作った事例です。

## 日経

### [サイバー保険のジレンマ 油断が生む防衛の死角、加入企業が狙われるケースも (サイバー・クライシス)](https://business.nikkei.com/atcl/gen/19/00954/102900001/)
<sub>日経ビジネス電子版 ・ 11/02 05:00</sub>

不正アクセスが相次ぐなかサイバー保険への注目が高まる一方、保険が新たなリスクを生みかねない落とし穴があると指摘しています。経営層には保険と防衛投資のバランスを見極める責任が問われるとしています。

### [GMO・PHPの陰で悪用確認リストKEV入り重大脆弱性が3件、至急点検が必要](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12141/)
<sub>日経クロステック ・ 11/02 05:00</sub>

CISA が 10 月 27〜28 日に、Brotli、Linux カーネル、Adobe Commerce / Magento の脆弱性計 3 件を悪用確認済みリスト KEV に追加しました。企業が点検すべき点と対策を解説しています。

### [三菱電機、廃エアコンからレアアース回収 再資源化で新規調達35％削減 (「ごみ」が日本を救う)](https://business.nikkei.com/atcl/gen/19/00947/102900002/)
<sub>日経ビジネス電子版 ・ 11/02 05:00</sub>

調達環境が厳しさを増すなか、三菱電機が廃エアコンからレアアースを回収する取り組みを進めています。「都市鉱山」を資源安全保障の戦略資産とみる動きを紹介しています。

### [2ナノ半導体で医療AI ラピダス参画のLSTC、富士フイルムや北大と](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12108/)
<sub>日経クロステック ・ 11/02 05:00</sub>

ラピダスなどが参画する LSTC が、富士フイルムや北海道大学と、先端半導体を使った医療画像処理システムを開発します。

### [インテルCTO、量子や脳型演算など5分野に注力 「過去の失敗繰り返さない」](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12106/)
<sub>日経クロステック ・ 11/02 05:00</sub>

インテル CTO が、量子コンピューターや脳型演算、光電融合など 5 分野に投資し、CPU に続く収益源に育てたい考えを示しました。

### [日立製作所、GPUの冷却電力3割減 新構造コールドプレートで](https://xtech.nikkei.com/atcl/nxt/column/18/03322/102300015/)
<sub>日経クロステック ・ 11/02 05:00</sub>

日立が AI サーバー向けに新構造のコールドプレートを開発し、冷却に要する電力を約 3 割減らせる見込みとしています。

### [あえて文章を生成しない判断特化型AI、選択肢や確率を回答 再利用に強み](https://xtech.nikkei.com/atcl/nxt/keyword/18/00002/102100330/)
<sub>日経クロステック ・ 11/02 05:00</sub>

出力を事前定義の選択肢や確率に限る判断特化型 AI の解説です。結果を他のプログラムで再利用しやすく、非定型データ処理の自動化での活用が期待されています。

### [スターバックスが学んだ「AI導入後」の教訓、米企業もROI創出に苦戦](https://xtech.nikkei.com/atcl/nxt/column/18/03807/102700001/)
<sub>日経クロステック ・ 11/02 05:00</sub>

北米の AI カンファレンス「Ai4」で大企業が明かした AI 導入の実態を、コンサルタントが整理した記事です。

---
<sub>取得: 2026-11-02 06:51 JST ／ 取得失敗: なし</sub>
