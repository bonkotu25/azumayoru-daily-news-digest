# 2026-11-13 のダイジェスト

## 今日のハイライト

- NVIDIA のジェンスン・フアン CEO が即日辞任し、クレス CFO が暫定 CEO に就任（IT）
- GitHub Actions のワークフローに悪性コードを注入する広域サプライチェーン攻撃が発生、CI のシークレットが狙われる（IT）
- AWS がローカルで AWS API を再現する「AWS Emulator」を無償公開、コードはすべて AI エージェントが記述（AI）

## AI

### [Amazon、AWSのAPIを手元で再現する「AWS Emulator」を無償公開 コードはすべてAIエージェントが記述](https://www.itmedia.co.jp/news/article/2611/12/2000003126/)
<sub>ITmedia AI+ ・ 11/12 09:56</sub>

AWS アカウントなしで AWS API をローカルに再現し、開発や CI の統合テストに使えるツールが無料で公開された。コードは自律型 AI エージェントが人のレビューなしで書いたという。

### [Google Antigravity、クラウド上でAIエージェントが働く「リモートエージェント」機能を搭載。就業時間外でもAIエージェントは働き続ける](https://www.publickey1.jp/blog/26/google_antigravityaiai.html)
<sub>Publickey ・ 11/13 00:13</sub>

Google の AI エージェント開発環境 Antigravity に、エージェントをクラウド上で動かし続けられる「リモートエージェント」機能が加わった。

### [Google、選択肢から答えを選ぶことに特化した「Gemini Decisions API」発表 回答を生成せず確率で返す](https://www.itmedia.co.jp/aiplus/article/2611/12/2000003123/)
<sub>ITmedia AI+ ・ 11/12 07:03</sub>

ツール選択や条件判定のように選択肢から答えを選ぶ用途向けの API で、マルチモーダル入力を1回の推論で評価して確率と信頼度を返す。通常のモデルより高速・低コストだという。

### [OpenAI APIで国内推論可能に GPT-6 Lunaのみ](https://www.itmedia.co.jp/aiplus/article/2611/12/2000003129/)
<sub>ITmedia AI+ ・ 11/12 11:25</sub>

OpenAI の API で、GPT-6 Luna に限って日本国内での推論を選べるようになった。

### [Claude Enterpriseがセキュリティと管理機能を強化 DLP・EDR連携など新機能の全容は](https://kn.itmedia.co.jp/kn/article/2611/12/2000003082/)
<sub>ITmedia AI+ ・ 11/12 07:00</sub>

Anthropic が Claude Enterprise に設定状況の一覧化、DLP 連携、個人アカウントの遮断などを追加し、企業の AI 統制とシャドー IT 対策を強化した。

### [Claude Fable 5.2、フェルマーの最終定理を約30時間で形式化―1000エージェントの協調実験 | 財経新聞](https://www.zaikei.co.jp/article/20261111/877067.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/12 19:22</sub>

Anthropic は、1000 体の Claude Fable 5.2 エージェントがフェルマーの最終定理の証明を約 28.7 時間で形式化したと発表した。

### [Google DeepMind、「AlphaGenome 2」発表 細胞の種類ごとにDNA変異の影響を予測するAI](https://www.itmedia.co.jp/news/article/2611/12/2000003132/)
<sub>ITmedia AI+ ・ 11/12 11:29</sub>

1億を超える細胞データで学習し、細胞の種類や状態を指定して DNA 変異の影響を予測できるモデル。非営利目的なら API で利用できる。

### [ユナイテッド航空、外部のAIアシスタントによる航空券の予約などを禁止へ 「チェックインには人間の確認が必要」](https://www.itmedia.co.jp/news/article/2611/12/2000003127/)
<sub>ITmedia AI+ ・ 11/12 10:49</sub>

情報漏えいや意図しないアカウント操作の恐れを理由に、サードパーティ製 AI エージェントによる自社サービスの利用を禁止する。米国では外部 AI を制限する企業が相次いでいる。

## IT

### [NVIDIA、“革ジャンCEO”ことフアン氏が辞任 クレスCFOが暫定CEOに](https://www.itmedia.co.jp/news/article/2611/12/2000003160/)
<sub>ITmedia NEWS ・ 11/12 23:53</sub>

1993 年の共同創業から NVIDIA を率いてきたジェンスン・フアン氏が CEO と取締役を即日辞任した。暫定 CEO は CFO のコレット・クレス氏が務め、正式な後任を社内外から選ぶ。

### [GitHub Actions を狙った広域サプライチェーン攻撃（11/10~11/12）に関する注意喚起 - GMO Flatt Security Blog](https://blog.flatt.tech/entry/github_actions_widespread_supply_chain_attack)
<sub>はてなブックマーク IT 人気エントリー ・ 11/12 22:19</sub>

多数のリポジトリで悪性コミットにより GitHub Actions のワークフローへ不正コードが注入され、実行時に CI 環境のシークレットが外部へ送られる事例が発生している。

### [マイクロソフト、「365」世界で大規模障害 メール送れずビジネスに影響 - 日本経済新聞](https://www.nikkei.com/article/DGXZQOGN12CY20S6A111C2000000/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/13 05:58</sub>

日本時間 13 日未明から Microsoft 365 で大規模障害が起き、世界各地でメールに接続できない状態になった。日本も影響を受けているとみられる。

### [「Apache HTTP Server 2.4.71」が公開 ～深刻度「Critical」を含む3件の脆弱性を修正／「mod_http2」にリモートコード実行の欠陥、v2.4.55以降が影響](https://forest.watch.impress.co.jp/docs/news/2155719.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/12 14:25</sub>

Apache HTTP Server 2.4.71 で、mod_http2 のリモートコード実行を含む 3 件の脆弱性が修正された。2.4.55 以降が影響を受ける。

### [無印良品「21年までクレカ番号で顧客を識別していた」 “全ケタ保有＆漏えい“巡り謝罪 削除漏れなぜ発生](https://www.itmedia.co.jp/news/article/2611/12/2000003144/)
<sub>ITmedia NEWS ・ 11/12 17:00</sub>

良品計画が不正アクセスについて会見し、2021 年までカード番号で顧客を識別していたこと、システム変更後も一部のカード情報を削除せずに残していたことを認めた。

### [宝くじ公式サイト、会員の当落情報まで第三者が閲覧の可能性 リスト型攻撃か](https://www.itmedia.co.jp/news/article/2611/12/2000003158/)
<sub>ITmedia NEWS ・ 11/12 18:54</sub>

宝くじ公式サイトに第三者が不正ログインし、一部会員の当落情報や氏名・住所などを閲覧した可能性がある。不正購入などは確認されていない。

### [ドコモ「5G SA」また障害、原因は5日と同じ「交換機の輻輳」 約9時間で復旧](https://www.itmedia.co.jp/news/article/2611/12/2000003125/)
<sub>ITmedia NEWS ・ 11/12 09:53</sub>

ドコモの 5G SA で再び障害が起き、約 9 時間で復旧した。原因は前回と同じ交換機の輻輳で、サイバー攻撃の形跡はないという。

### [そのヤバいDockerイメージをいつまで使うのか - keroxpのScrapbox](https://scrapbox.io/keroxp/%E3%81%9D%E3%81%AE%E3%83%A4%E3%83%90%E3%81%84Docker%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%82%92%E3%81%84%E3%81%A4%E3%81%BE%E3%81%A7%E4%BD%BF%E3%81%86%E3%81%AE%E3%81%8B)
<sub>はてなブックマーク IT 人気エントリー ・ 11/12 19:43</sub>

「コンテナだから安全」という思い込みに警鐘を鳴らし、古い Docker イメージを使い続けるリスクを論じた記事。

## 技術記事（Qiita / Zenn）

### [CLAUDE.md に「このコードはあなたのもの」と書くと、重複したコードをまとめてくれるのか。Claude Code・Codex・Gemini CLI で132回試したら、まとめたのは Claude だけだった](https://qiita.com/suwa_nobu/items/1dd9df248ee6f4c9dfd4)
<sub>Qiita 人気記事 ・ 11/12 09:12</sub>

AI が既存コードを複製しがちな問題に対し、指示ファイルの一文で重複をまとめるかを 3 つのコーディングエージェントで計 132 回検証した。まとめたのは Claude Code だけだった。

### [ISUCONから学ぶAIとの付き合い方](https://zenn.dev/ojey/articles/isucon2026-kansousen)
<sub>Zenn: AI ・ 11/12 22:24</sub>

ISUCON2026 の感想戦で、同じ Claude Code に続きを任せたところ約 6 万点から 61 万点まで伸びた。AI に何かを足すのではなく、人が渡していた指示を減らしたことが効いたという。

### [中国・10年物PHPのEC基幹を4人×2週間でJavaへ——AIを「865行のルール」と「差分比較コマンド」で縛った移行手順](https://zenn.dev/soliperse/articles/8f3e21e9d26f92)
<sub>Zenn: AI ・ 11/12 22:42</sub>

約 54 万行の PHP 製 EC 基幹を 2 週間で Java に移した中国の事例について、AI を縛ったルールと差分比較による検証手順を整理している。

### [Skills を持つ単一エージェントは、サブエージェント構成より品質で上回ることが多い — Anthropic が示す移行の手順](https://zenn.dev/happy_elements/articles/201519107f93de)
<sub>Zenn: LLM ・ 11/12 12:38</sub>

サブエージェントに分けた構成をメインループへ統合し、Skills とツールを持たせる方法を説いた Anthropic のブログ記事を解説している。

### [AIエージェントが決定を勝手に変えてしまった5つのパターンと工夫](https://zenn.dev/dress_code/articles/568fd547315abe)
<sub>Zenn トレンド ・ 11/12 12:00</sub>

ADR や仕様書を読ませて Claude Code や Codex に作業させても、決めた内容がいつのまにか変わってしまう 5 つのパターンと、その対策をまとめている。

### [Claude Code に忘れさせたら、トークン使用量が4割減った](https://zenn.dev/sae_eng/articles/0e9ed7205ebc41)
<sub>Zenn トレンド ・ 11/12 08:00</sub>

compact の設定と離席中に compact させる仕組みを調整したところ、使い勝手を変えずに送信トークンが約 4 割減ったという実践記録。

### [Node.js 22 / 24 / 26 の脆弱性、自分のアプリが影響を受けるか確認する方法【2026年11月】](https://zenn.dev/rakko_inc/articles/nodejs-security-nov-2026-proxy)
<sub>Zenn トレンド ・ 11/12 11:31</sub>

11 月 11 日公表の Node.js セキュリティリリースについて、自分のアプリが対象かを判断する方法を解説。深刻度 High の 7 件はロードバランサーや nginx の背後の構成には届かないとしている。

### [PLaMo 3 Translate 8B GGUFをVRAM 12GBで実測：短文は10/10、長文は訳し切れず](https://zenn.dev/localai_lab/articles/38ec01cf9cc16a)
<sub>Zenn: LLM ・ 11/12 14:44</sub>

翻訳特化 LLM の公式 GGUF 3 種を VRAM 12GB の GPU で llama.cpp により動かし、翻訳品質と速度を測定した。短文は全問正解だったが長文は訳し切れなかった。

### [VS Code の Local harness は2027年2月に削除：Copilot harness へ移行する手順とつまずきポイント](https://qiita.com/shahin0809/items/ccb8a8ddf11d6cb4113d)
<sub>Qiita 人気記事 ・ 11/12 16:50</sub>

2027 年 2 月に削除される VS Code の Local harness から Copilot harness へ移行する手順と、つまずきやすい点を紹介している。

### [VSCodeのCompare Modelsが面白そうなので試してみた](https://qiita.com/shivvvvvv/items/c1feef6d2ad5ff7f8f73)
<sub>Qiita 人気記事 ・ 11/12 20:59</sub>

11 月 11 日に安定版が出た VS Code 1.146 の新機能 Compare Models を解説し、実際に試している。

## 日経

### [中国DeepSeek、6月に続き150億ドルの巨額調達 テンセント・CATLが参加](https://xtech.nikkei.com/atcl/nxt/column/18/03065/111100023/)
<sub>日経クロステック ・ 11/13 05:00</sub>

DeepSeek がテンセントや CATL などから約 150 億ドルを調達したと報じられた。6 月に続く大型調達となる。

### [PHPの重大脆弱性発見の経緯公表 財団が「構造的な失敗」と認める](https://xtech.nikkei.com/atcl/nxt/mag/nc/18/020800017/110501523/)
<sub>日経クロステック ・ 11/12 07:04</sub>

PHP 財団が重大な脆弱性 2 件の経緯を公表し、2024 年に兆候をつかみながら修正が滞ったことを「構造的な失敗」と認めた。

### [VMware旧版のサポート残り1年 上位版へ移行促すブロードコム](https://xtech.nikkei.com/atcl/nxt/mag/nc/18/020800017/110501524/)
<sub>日経クロステック ・ 11/12 07:01</sub>

VMware vSphere 8.0 の一般サポート終了まで 1 年を切り、Broadcom は VMware Cloud Foundation 9.1 への移行を促している。

### [家庭機器が犯罪の出口に、レジデンシャルプロキシーが横行 警告で防げず](https://xtech.nikkei.com/atcl/nxt/column/18/00989/102100222/)
<sub>日経クロステック ・ 11/13 05:00</sub>

家庭の機器やアプリが知らないうちに通信の中継点にされ、攻撃元の追跡や不正アクセスの検知を難しくしている。出荷時から中継機能を組み込んだ機器もあるという。

### [パナソニックが入力画面変化を予測する世界モデル、現場作業へ応用期待](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12162/)
<sub>日経クロステック ・ 11/13 05:00</sub>

入力操作で端末の画面がどう変わるかを予測する世界モデルを開発した。製造現場での実績入力作業を AI で自動化する用途を想定している。

### [旭化成、材料開発プロセス全体を自律化へ 半導体向け絶縁材に適用](https://xtech.nikkei.com/atcl/nxt/news/24/03462/)
<sub>日経クロステック ・ 11/13 05:00</sub>

AI と自動化で材料開発を自律的に進める施設を 2027 年 1 月に稼働させ、半導体向け感光性絶縁材料の開発に使う。

### [東急電鉄、AIで閉扉判断を支援 ワンマン運転士の負担軽減へ](https://xtech.nikkei.com/atcl/nxt/mag/nc/18/020800017/110501526/)
<sub>日経クロステック ・ 11/12 07:00</sub>

ホームのカメラ映像を AI が解析して車椅子利用者などを認識し、運転台に表示するシステムを東横線の各駅へ順次導入する。

### [共和党敗北も「米国のAIデータセンターは止まらない」 エネルギー政策不変 (トランプ2.0の世界)](https://business.nikkei.com/atcl/gen/19/00685/111100086/)
<sub>日経ビジネス電子版 ・ 11/13 05:00</sub>

共和党の敗北が米国のエネルギー政策や原油価格に与える影響について、専門家に聞いたインタビュー。

---
<sub>取得: 2026-11-13 06:51 JST ／ 取得失敗: なし</sub>
