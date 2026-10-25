# 2026-10-26 のダイジェスト

## 今日のハイライト

- GMOインターネットグループのクラウドサービスへの不正アクセスで、攻撃者が身代金の期限を示して利用者PCの乗っ取りを予告
- 認証局 eMudhra の中間CAが侵害され、Apple が該当証明書を自動でブロック
- 「DuckDB 2.0 LTS」が正式リリース、Quackプロトコルによるクライアント/サーバ機能などを搭載

## AI

### [AIによる脆弱性発見が加速、専門家「混乱期の始まり」](https://www.afpbb.com/articles/-/3659236)
<sub>はてなブックマーク IT 人気エントリー（AFP） ・ 10/25 13:22</sub>

PHPで見つかった二つの重大な脆弱性への対応に企業や政府機関が追われた週を受け、AIによる脆弱性発見の加速を専門家が「混乱期の始まり」と評している。

### [「AIを虐待すると復讐されるかも」マスク氏も警告…アンソロピックが“AIいじめ”対策でポリシー改定 識者が危惧するAIへの暴言のリスク（ABEMA TIMES） - Yahoo!ニュース](https://news.yahoo.co.jp/articles/2997423a08fc213f62fb5f6e7d3b3091570bfcdc)
<sub>はてなブックマーク IT 人気エントリー（Yahoo!ニュース） ・ 10/25 12:52</sub>

Anthropicが利用規約を改定し、AIへの残酷な言動の繰り返しなど悪質な「虐待的行為」を禁止する方針を示した。これに対する識者の見方を紹介する記事。

### [AI ネイティブの SDLC プレイブック](https://claude.com/ja/resources/articles/the-ai-native-sdlc-playbook)
<sub>はてなブックマーク IT 人気エントリー（claude.com） ・ 10/25 10:29</sub>

「コードはもはやボトルネックではない」という前提で、6つの段階ごとの進め方と実例をまとめたプレイブック。ダウンロード版も用意されている。

## IT

### [GMOへの攻撃者、利用者PCの乗っ取りを画策 会社は注意喚起 - 日本経済新聞](https://www.nikkei.com/article/DGXZQOUC250PP0V21C26A0000000/)
<sub>はてなブックマーク IT 人気エントリー（日本経済新聞） ・ 10/25 19:33</sub>

GMOインターネットグループのクラウドサービスへの不正アクセスで、攻撃者を名乗る人物が27日正午までの身代金支払いを要求し、応じなければ利用者のPCを乗っ取ると予告している。

### [政府に緊急要請のGMO 被害拡大防げるか 利用者に呼びかけ強化 | NHKニュース](https://news.web.nhk/newsweb/na/nd-20261024de64946)
<sub>はてなブックマーク IT 人気エントリー（NHK） ・ 10/25 07:13</sub>

投資家向けクラウドサービスで身に覚えのない取引が確認された問題で、GMOは被害拡大防止のため「能動的サイバー防御」を政府に緊急要請し、利用者への呼びかけを強めている。

### [About the compromised eMudhra intermediate CAs - Apple Support](https://support.apple.com/en-us/149555)
<sub>はてなブックマーク IT 人気エントリー（Apple Support） ・ 10/25 13:52</sub>

侵害された eMudhra の中間CA証明書を Apple が自動的にブロックしていることを案内するサポート文書。Mac管理者がコマンドラインツール向けに取れる任意の対応にも触れている。

### [「DuckDB 2.0 LTS」正式リリース。Quackプロトコルによるクライアント/サーバ機能や非同期処理による高速化など](https://www.publickey1.jp/blog/26/duckdb_20_ltsquack.html)
<sub>Publickey ・ 10/26 00:44</sub>

DuckDB Foundationが、OLAP型データベース「DuckDB 2.0 LTS」（コード名 Cinnamon Teal）の正式リリースを発表した。Quackプロトコルによるクライアント/サーバ機能や、非同期処理による高速化が特徴。

### [電子漫画「ピッコマ」 顧客のメールアドレス約100万件流出 | NHKニュース](https://news.web.nhk/newsweb/na/nd-20261025de65227)
<sub>はてなブックマーク IT 人気エントリー（NHK） ・ 10/25 18:19</sub>

メール配信に使っている委託先企業が不正アクセスを受け、ピッコマの顧客メールアドレス約100万件が流出したと運営会社が発表した。

### [ソフトウェアの脆弱性情報をいち早く入手する - CVE・CISA KEV・JPCERT/CC・OSV｜npaka](https://note.com/npaka/n/na5ad6472d68c)
<sub>はてなブックマーク IT 人気エントリー（note） ・ 10/25 21:07</sub>

CVE・CISA KEV・JPCERT/CC・OSVという4つの代表的な脆弱性情報源と、その活用方法を紹介する解説記事。

### [eMudhra のインシデントは Web にとって何を意味するのか | blog.jxck.io](https://blog.jxck.io/entries/2026-10-25/emudhra.html)
<sub>はてなブックマーク IT 人気エントリー（blog.jxck.io） ・ 10/25 05:22</sub>

PHP2Shellよりも eMudhra の件のほうが Web の信頼を揺るがす深刻な問題だとする筆者が、認証局の仕組みのおさらいから論じている。

## 技術記事（Qiita / Zenn）

### [eMudhra事件でWebアプリ開発者が点検すべきこと](https://qiita.com/autotaker1984/items/ef99b5791fe799a4ca66)
<sub>Qiita 人気記事 ・ 10/25 01:45</sub>

中間CAの秘密鍵が公開情報から復元でき、他人のドメインの証明書を偽造され得る事件について、Webアプリ開発者が確認すべき点を整理している。

### [トークン代 9 割減？プロンプトキャッシュの仕組みと効果の実測 — 保持時間が過ぎるとコスト 11 倍に](https://qiita.com/songchong/items/7144594b0ad9529a168b)
<sub>Qiita 人気記事 ・ 10/26 04:00</sub>

「キャッシュで入力が9割安くなる」という通説を実測で検証し、保持時間を過ぎるとコストが11倍になる点を取り上げている。

### [Claude Code の「ブロック済み」を1か月信じていた。フックは何も止めていなかった](https://qiita.com/devoctane/items/eb3ac408041b2f04c780)
<sub>Qiita 人気記事 ・ 10/25 15:45</sub>

PreToolUse Hookで危険なコマンドをブロック済みだと思っていたところ、実際には機能していなかったと気づいた経緯の記録。

### [Claude Codeのskillが「選ばれるのに読まれない」理由：発火を2段階に分けて測った](https://zenn.dev/lilpacy/articles/claude-code-skill-two-stage-activation)
<sub>Zenn: AI ・ 10/25 20:48</sub>

skillの発火を「候補に選ばれる段階」と「実際に読まれる段階」に分けて測定し、前者では9/9で選ばれたskillが実作業では一度も読まれなかった例を示している。

### [NVIDIA OpenShellのdefault-denyネットワークポリシーを実機で検証した](https://zenn.dev/matsushima_a/articles/day-026-openshell-default-deny-network-policy)
<sub>Zenn: AI ・ 10/25 23:10</sub>

AIエージェントをサンドボックスで隔離するNVIDIA製ランタイムを実際に動かし、ポリシーがなければ外向き通信が全拒否され、読み取り専用ルールの追加でGETだけが通ることをログで確認している。

### [Cloudflare の security-audit-skill を、個人開発アプリで試してみた](https://zenn.dev/suna/articles/e0e3af015d7bed)
<sub>Zenn: AI ・ 10/25 21:54</sub>

AIが問題を探し、別のAIが検証するCloudflare公開のセキュリティ監査Skillを、OWASP ASVSで点検済みの個人開発アプリに適用して試した記録。

### [本番DBは9秒で消えた――AIエージェントの安全は「指示」だけに任せられない](https://zenn.dev/kotakotahiro/articles/111c2f74a72d16)
<sub>Zenn: LLM ・ 10/26 00:49</sub>

ルールがあったにもかかわらずステージング環境のDBが9秒で消えた事例から、指示の工夫だけでは届かない層での安全対策を考える。

## 日経

### [安川電機がフィジカルAIを食品工場などへ拡大、ロボットへの指示を生成AIで](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12110/)
<sub>日経クロステック ・ 10/26 05:00</sub>

AWSと連携し、クラウド上の生成AIが人間の要望をロボットの処理できる作業内容へ変換するシステムを構築したという。

### [BroadcomがVMware上位版を訴求、企業は残るか移るか 旧版サポート残り1年](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12123/)
<sub>日経クロステック ・ 10/26 05:00</sub>

vSphere 8.0の一般サポート終了まで1年を切り、BroadcomがVCF 9.1への移行を促している。値上げに直面してきた利用企業は移行か他社製品かの判断を迫られる。

### [国税庁のシステム「KSK2」で手続き遅延が1カ月継続、国税労組は解決を要求](https://xtech.nikkei.com/atcl/nxt/column/18/00001/12111/)
<sub>日経クロステック ・ 10/26 05:00</sub>

9月24日の稼働開始から1カ月が経っても、納税証明書の交付に通常より時間がかかる状況が続いている。

### [川崎重工のフィジカルAIロボ、戦略を2軸分析 ファナック・トヨタと違い](https://xtech.nikkei.com/atcl/nxt/column/18/03688/101300018/)
<sub>日経クロステック ・ 10/26 05:00</sub>

造船所や介護の現場で鍛えたフィジカルAIロボットを外部に売り出す川崎重工について、他のロボット関連企業との比較から独自性を分析している。

### [通信競争激化のNTTドコモ、金融を第2の柱に 1億会員を収益源へ (テーマ別まとめ記事)](https://business.nikkei.com/atcl/gen/19/00081/090200976/)
<sub>日経ビジネス電子版 ・ 10/26 05:00</sub>

住信SBIネット銀行の買収で銀行業に参入し、証券・決済と組み合わせた金融事業を成長の柱に据えるドコモの取り組みをまとめている。

### [テスラ「サイバーキャブ」の衝撃 車の稼働率10倍へ、収益構造が激変](https://xtech.nikkei.com/atcl/nxt/column/18/03800/101900003/)
<sub>日経クロステック ・ 10/26 05:00</sub>

ハンドルやペダルのないロボタクシーが自動車産業の収益構造に与え得る変化と、周辺産業への影響を読み解く。

---
<sub>取得: 2026-10-26 06:51 JST ／ 取得失敗: なし</sub>
