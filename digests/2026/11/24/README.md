# 2026-11-24 のダイジェスト

## 今日のハイライト

- OpenAI のチーフサイエンティストが、パープレキシティを指標とした AI 開発の業界共通の「上限」を提案
- NVIDIA のジェンスン・フアン氏が 11 日間の不在を経て社長兼 CEO に復帰
- PostgreSQL 19 の正式版がリリース、Omarchy 4.5 も公開

## AI

### [OpenAIのチーフサイエンティスト、AI開発に業界共通の「上限」を提案 指標は「パープレキシティ」](https://www.itmedia.co.jp/news/article/2611/23/2000003394/)
<sub>ITmedia AI+ ・ 11/23 07:49</sub>

OpenAI のチーフサイエンティストが、AI の予測精度を示すパープレキシティを共通指標に、開発の上限を業界で設けるよう提案する論考を公開しました。社内モデルの推移も開示し、早ければ 2027 年にも事前学習が急加速する恐れがあるとしています。

## IT

### [「Microsoft To Do」、2027年6月にアプリ提供終了 法人向けは「Planner」へ移行、個人向けは代替なし](https://www.itmedia.co.jp/news/article/2611/23/2000003395/)
<sub>ITmedia NEWS ・ 11/23 12:12</sub>

Microsoft が、タスク管理アプリ「Microsoft To Do」の全プラットフォーム向けアプリを 2027 年 6 月 30 日に終了すると発表しました。職場・学校向けは Planner が後継で、個人向けは利用できず、データは自動移行されません。

### [DHH氏が開発する「Omarchy 4.5」リリース。一般的なマルチウィンドウをサポート。最速7秒で導入、Appleシリコン対応、Webアプリ版MS Office用ランチャーなど新機能](https://www.publickey1.jp/blog/26/dhhomarchy_457applewebms_office.html)
<sub>Publickey ・ 11/24 00:49</sub>

DHH 氏が主導するデスクトップ向け Linux OS「Omarchy」の最新版 4.5 の正式版がリリースされました。

### [PostgreSQL 19正式リリース。ノンブロッキングなREPACKやI/Oワーカーのオートスケールなど新機能](https://www.publickey1.jp/blog/26/postgresql_19repackio.html)
<sub>Publickey ・ 11/24 00:45</sub>

オープンソースのリレーショナルデータベース PostgreSQL の最新版 19 の正式版がリリースされました。見出しではノンブロッキングな REPACK や I/O ワーカーのオートスケールなどが挙げられています。

### [著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話](https://zenn.dev/koukyosyumei/articles/31c8fcf4da45b7)
<sub>はてなブックマーク IT 人気エントリー ・ 11/23 19:14</sub>

コロンビア大学の研究者が、Rust 製の有名 OSS を Lean 4 で形式検証するベンチマークを作る過程で、実際のセキュリティ脆弱性を複数見つけたという報告です。

### [ジェンスン・フアン氏、11日間の不在の後、NVIDIAのCEOに返り咲き | テクノエッジ TechnoEdge](https://www.techno-edge.net/article/2026/11/23/5793.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/24 00:05</sub>

NVIDIA の創業者ジェンスン・フアン氏が、取締役会の全会一致の決定により、社長兼 CEO として 11 日間の不在を経て復帰しました。

### [ChatGPT の速さを支える OpenAI の Performance Factory](https://openai.com/ja-JP/index/how-openai-performance-factory-keeps-chatgpt-fast/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/23 17:01</sub>

OpenAI が、Codex と自社モデルを活用して性能劣化を素早く発見・修正する自律型システム「Performance Factory」を紹介しています。エージェント開発の速度に従来の手法が追いつかなくなったことが背景です。

### [無料でMacのアプリのウィンドウをiPhoneやiPadからリアルタイムに操作できる「Sill」、オープンソースで中継サーバー不要](https://gigazine.net/news/20261123-sill/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/23 12:11</sub>

Mac のアプリウィンドウをリアルタイム転送し、iPhone や iPad のタッチやキーボードで操作できる、サーバー不要の無料オープンソースアプリ「Sill」の紹介です。

### [NVIDIAグラボの「SSD無限酷使」現象、修正パッチを適用しても直らないとの報告。ちょっと改善するも、まだ書き込みまくる - AUTOMATON](https://automaton-media.com/articles/newsjp/20261123-480470/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/23 15:49</sub>

NVIDIA 製 GPU のドライバで起きる SSD への大量書き込み問題が、ホットフィックス 621.35 の適用後も続いているとの報告です。多少改善はするものの、書き込みは止まっていないとされています。

## 技術記事（Qiita / Zenn）

### [Claude Codeのhooksで：危険な命令は止められる？](https://qiita.com/blogjiraiya377/items/c320bb728b6733f153dd)
<sub>Qiita 人気記事 ・ 11/23 08:57</sub>

プログラミングができない筆者が、Claude Code の hooks で危険な命令を止める見張り役を AI に作らせた記録です。つまずいた点と、別の AI で点検して見つかった内容がまとめられています。

### [Claude Codeのセッションを分岐して並行作業する：/fork と --fork-session の手順・落とし穴・検証方法](https://qiita.com/joinclass/items/8b30d5453db55388966a)
<sub>Qiita 人気記事 ・ 11/23 08:30</sub>

Claude Code のセッションを /fork や --fork-session で分岐し、並行作業する手順と注意点を、日常運用の経験からまとめた記事です。

### [マルチテナントRAGの越境漏えいをpytestのカナリア文書で検知する](https://qiita.com/takumi_engineer/items/aeef0c55f1583fd57492)
<sub>Qiita 人気記事 ・ 11/23 09:00</sub>

マルチテナント RAG で他社文書が回答に混ざる越境漏えいを、テナントごとのカナリア文書と pytest で機械的に検知する方法を示しています。回答品質とは切り離し、権限境界だけをテストする考え方です。

### [Googleが実践するSTAMP/STPAとは何か？ 私たちのSREにも使えるのか](https://zenn.dev/maruloop/articles/7ff108e29741b5)
<sub>Zenn トレンド ・ 11/23 15:56</sub>

Google の SRE 本第 2 版に追加された STAMP/STPA による安全工学の章を取り上げ、システム安全工学の手法が SRE にも使えるのかを考察しています。

### [同じ重みを2回通すSenseNova-Loop-9B、ループを1回にすると掛け算の正解が20問中19問から1問に落ちた](https://zenn.dev/matsushima_a/articles/day-055-sensenova-loop-count-compare)
<sub>Zenn: AI ・ 11/23 23:37</sub>

同じ重みを 2 回通す SenseNova-Loop-9B を手元の GPU で動かし、ループ回数を変えて出力を比べた検証です。タイトルによると、1 回にすると掛け算の正解が 20 問中 19 問から 1 問に落ちたとのことです。

### [agy（Antigravity CLI）のモデル7通りに同じ3課題を解かせた](https://zenn.dev/hiroxasobiba/articles/agy-seven-models-same-three-tasks)
<sub>Zenn: LLM ・ 11/23 20:06</sub>

Google Antigravity の CLI「agy」で選べる 7 つのモデルに、同じ 3 つの課題を解かせて普段使いを決めようとした比較記録です。

### [Microsoft Aion 1.0 InstructをColabで試した：2.3Bで日本語要約・ツールコール・32K長文チェック](https://zenn.dev/shibatamago_dev/articles/aion-1-0-instruct-hands-on)
<sub>Zenn: LLM ・ 11/23 14:22</sub>

Microsoft が MIT ライセンスで重みを公開した 2.3B パラメータのオンデバイス向け小規模言語モデル「Aion 1.0 Instruct」を Colab で試し、日本語要約やツールコールなどを確かめています。

### [思考予算を上げても点数が動かなかった — SciCode 5問での effort 振り](https://zenn.dev/jinno_ai/articles/effort-null-scicode-reasoning-effort)
<sub>Zenn: LLM ・ 11/23 13:29</sub>

OpenAI API の reasoning_effort を上げても、SciCode の 5 問ではテストの合格数が単調には増えなかったという小規模な検証です。推論トークンは大きく増えています。

### [Claude Code のサブエージェントは何体に分けるか——作る前に当てる4つの問い](https://zenn.dev/tottoko_hamu/articles/2026-11-21-214855)
<sub>Zenn: LLM ・ 11/23 16:20</sub>

Claude Code のサブエージェントの数は先に決めず、「繰り返し起きるか」など 4 つの問いを作業ごとに当てて決めることを提案しています。4 つすべてが Yes の作業だけを新しい役にする考え方です。

### [重み編集で Qwen3.5-0.8B をコーディングエージェント安全判定器に改造してみた](https://zenn.dev/chitako/articles/b509c472f2e2d5)
<sub>Zenn: LLM ・ 11/23 15:42</sub>

勾配降下を使わず重みを直接編集する手法で、Qwen3.5-0.8B をコーディングエージェントの安全判定器に改造した技術解説です。

## 日経

### [データセンター、半導体開発…AI企業「垂直統合」の動き 巨大化にリスクも (世界鳥瞰)](https://business.nikkei.com/atcl/NBD/19/world/00839/)
<sub>日経ビジネス電子版 ・ 11/24 05:00</sub>

AI 関連企業が電力からデータセンター、AI 製品までを保有する垂直統合へ向かう動きを解説しています。巨大化には規制圧力などのリスクもあると指摘しています。

### [アンソロピック、公益を守る異色の統治モデル 創業者7人で全議決権の50.1％ (アンソロピックの正体)](https://business.nikkei.com/atcl/gen/19/00950/112000003/)
<sub>日経ビジネス電子版 ・ 11/24 05:00</sub>

上場を果たした Anthropic が、公益性と市場原理の両立を目指す異色のガバナンスを進めていることを取り上げた記事です。

### [世界のIT大手19社、売上高の伸び36.4％に拡大 2026年7～9月決算](https://xtech.nikkei.com/atcl/nxt/column/18/00848/00200/)
<sub>日経クロステック ・ 11/24 05:00</sub>

世界の IT 大手 19 社の 2026 年 7〜9 月期の売上高が前年同期比 36.4％増の 3367 億ドルに達し、伸び率が期を追うごとに拡大していると報じています。

### [AIは「ハーネスを飲み込む」か、マスク氏も反応した10月のAI注目論文](https://xtech.nikkei.com/atcl/nxt/column/18/02801/111900041/)
<sub>日経クロステック ・ 11/24 05:00</sub>

AI エージェントの性能を左右する「ハーネス」の改良そのものを AI に実行させる手法を示した、カーネギーメロン大学とジョンズ・ホプキンス大学の論文を紹介しています。

### [10年目のTransformerが迎える限界、中核技術「アテンション」で進む3大改革](https://xtech.nikkei.com/atcl/nxt/column/18/03794/111700002/)
<sub>日経クロステック ・ 11/24 05:00</sub>

Transformer 登場から 10 年がたち、LLM の課題から生まれつつあるポスト・トランスフォーマーの技術動向を、アテンションの改革を中心に解説しています。

### [AI企業が求める高報酬エンジニア「FDE」、コードを書きつつ経営課題に踏み込む](https://xtech.nikkei.com/atcl/nxt/column/18/03820/111000001/)
<sub>日経クロステック ・ 11/24 05:00</sub>

顧客の現場で課題を解き、得た知見を自社基盤に取り込む「フォワード・デプロイド・エンジニア（FDE）」とはどんな職種かを解説しています。

### [相次ぐサイバー攻撃、漏洩メアドが次の標的に 努力不足の企業に罰則強化論](https://xtech.nikkei.com/atcl/nxt/column/18/03671/111600013/)
<sub>日経クロステック ・ 11/24 05:00</sub>

日本で相次ぐサイバー攻撃を受け、個人情報の収集に対する企業の認識を改めるべきだとする専門家の見方と、罰則強化論を紹介しています。

### [ユミルリンクの「Cuenote」で延べ4786万件流出、2種類の攻撃手法を確認](https://xtech.nikkei.com/atcl/nxt/column/18/00598/011300391/)
<sub>日経クロステック ・ 11/24 05:00</sub>

今週のシステムトラブルとして、メール配信サービス「Cuenote」からの情報漏洩などをセキュリティ研究者が取り上げています。

---
<sub>取得: 2026-11-24 06:51 JST ／ 取得失敗: なし</sub>
