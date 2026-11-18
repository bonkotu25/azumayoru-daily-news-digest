# 2026-11-19 のダイジェスト

## 今日のハイライト

- OpenAIが「GPT-6.2 Astra / Sol」を発表。前世代を超える性能をコスト3分の1以下で実現したとしている
- 楽天証券で最大約1572万口座分が漏えいした可能性。本番データをマスキングせずテスト環境に置いていたことが判明
- NGINXのHTTP/2に認証なしでリモートコード実行が可能になりうる重大な脆弱性2件（CVE-2026-123633 / CVE-2026-123007）

## AI

### [「GPT-6.2 Astra／Sol」登場 前世代超える性能を「コスト1/3で実現」 Ultrafast提供も拡大](https://www.itmedia.co.jp/aiplus/article/2611/18/2000003282/)
<sub>ITmedia AI+ ・ 11/18 10:32</sub>

OpenAIが「GPT-6.2 Astra」「GPT-6.2 Sol」を発表。Astraは一部の評価で前世代を上回るスコアを3分の1以下のコストで実現したとしており、第三者機関の総合指標ではClaude Fable 5.2に次ぐ2位とされる。

### [孫正義氏が明かす、アンソロピック出資見送りの舞台裏 「僕の失敗」「あん時入れときゃよかった」](https://www.itmedia.co.jp/business/articles/2611/18/news086.html)
<sub>ITmedia AI+ ・ 11/18 22:03</sub>

孫正義氏が日経主催イベントの対談で、Anthropicへの出資見送りを「僕の失敗の例の一つ」と振り返った。OpenAIへの集中投資や「群戦略」でのパートナー選びが背景にあったという。

### [NotionのAIチャット流出おそれ、幹部が日本での対応状況明かす 「心よりおわび」](https://www.itmedia.co.jp/aiplus/article/2611/18/2000003299/)
<sub>ITmedia AI+ ・ 11/18 16:56</sub>

Notion AIのチャット記録が漏えいした可能性がある件で、Notion LabsのCISOが日本での対応状況を取材に答えた。

### [わが社はChatGPTでどう紹介されている？ OpenAIが企業向けの確認機能を提供開始](https://www.itmedia.co.jp/enterprise/articles/2611/18/news022.html)
<sub>ITmedia AI+ ・ 11/18 10:40</sub>

OpenAIが、ChatGPTが自社をどう紹介しているかを確認できる企業向け機能をβ版で公開した。米国の対象企業は、自社のAIエージェントをChatGPT広告のリンク先に設定することもできる。

### [「オントロジー」とは結局何なのか Palantir、Databricks、Snowflake、NVIDIAで中身が違う理由](https://atmarkit.itmedia.co.jp/ait/articles/2611/19/news008.html)
<sub>ITmedia AI+ ・ 11/19 05:00</sub>

Palantir、Databricks、Snowflake、NVIDIAなど各社の製品を比べ、「オントロジー」が何を定義しどこまで実行するのかを開発者の視点で整理した解説記事。

### [GAS×Geminiが一般提供開始 IT管理者が確認すべき権限設定は？](https://kn.itmedia.co.jp/kn/article/2611/18/2000003256/)
<sub>ITmedia AI+ ・ 11/18 07:00</sub>

Google Apps ScriptとGeminiの連携が一般提供になり、自然言語の指示でスクリプトの作成・編集・エラー修正ができる。IT管理者が確認すべき権限設定にも触れている。

### [Googleドライブの最新ファイルをGeminiが常時参照 「スキル」に新機能追加](https://kn.itmedia.co.jp/kn/article/2611/18/2000003259/)
<sub>ITmedia AI+ ・ 11/18 07:00</sub>

Geminiの「スキル」機能が拡張され、作成したスキルを他ユーザーと共有したり、Googleドライブのファイルを追加して常に最新データを参照させたりできるようになった。

## IT

### [楽天証券の大規模漏えい、なぜテスト環境に顧客情報が？ 「本番データでの確認が必要だった」](https://www.itmedia.co.jp/news/article/2611/18/2000003302/)
<sub>ITmedia NEWS ・ 11/18 20:16</sub>

楽天証券が本番の顧客データをマスキングせずテスト環境に保存していたことが判明した。最大約1572万口座分が漏えいした可能性がある。

### [NewsPicks漏えい、Metabase脆弱性が原因 パッチ適用前日にデータ窃取、JPCERT/CC公表「不審IPアドレス」で攻撃発覚](https://www.itmedia.co.jp/news/article/2611/18/2000003300/)
<sub>ITmedia NEWS ・ 11/18 16:59</sub>

NewsPicksの情報漏えいはMetabaseの脆弱性が原因で、修正版への更新(8月12日)より前に攻撃者が侵入しデータを窃取していたという。

### [「JINS」最大約1829万件漏えいの可能性 RIZAPやしまむらも……「KARTE」不正アクセスの影響広がる](https://www.itmedia.co.jp/news/article/2611/18/2000003287/)
<sub>ITmedia NEWS ・ 11/18 11:52</sub>

マーケティングサービス「KARTE」への不正アクセスの影響が広がり、JINSでは最大約1829万件が漏えいした可能性がある。RIZAPやしまむらにも影響が及んでいる。

### [NVIDIA、フアン氏退任後初の決算 取締役会「正式なCEOは急がず適任者を選ぶ」](https://www.itmedia.co.jp/news/article/2611/18/2000003280/)
<sub>ITmedia NEWS ・ 11/18 09:38</sub>

NVIDIAがフアン前CEO退任後初の第3四半期決算を発表し、売上高は前年同期比103％増。会長は前CEOを復帰させる意向はないと述べ、後任は慎重に選ぶとした。

### [マイクロソフト、AIによるサイバー攻撃にAIエージェントで対抗する新サービス「Microsoft Perception」提供開始](https://www.publickey1.jp/blog/26/aiaimicrosoft_perception.html)
<sub>Publickey ・ 11/19 01:00</sub>

Microsoft Ignite 2026で、AIによるサイバー攻撃にAIエージェントで対抗する新サービス「Microsoft Perception」の提供開始が発表された。

### [マイクロソフト、AIが生成したアプリを企業内で安全に実行するランタイム「Copilot Managed Runtime」正式リリース](https://www.publickey1.jp/blog/26/aicopilot_managed_runtime.html)
<sub>Publickey ・ 11/19 00:58</sub>

Microsoft Ignite 2026で、AIが生成したアプリを企業内で安全に実行するための基盤「Copilot Managed Runtime」が正式リリースされた。

### [［速報］マイクロソフト、コーディング用AIモデルとして高性能かつ低価格「MAI Code 2」「MAI Code 2 Flash」発表](https://www.publickey1.jp/blog/26/aimai_code_2mai_code_2_flash.html)
<sub>Publickey ・ 11/18 06:48</sub>

Microsoftが、高性能かつ低価格をうたうコーディング用AIモデル「MAI Code 2」と、さらに安価な「MAI Code 2 Flash」を発表した。

### [Unauthenticated Remote Code Execution in NGINX: CVE-2026-123633 and CVE-2026-123007 | Wiz Blog](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
<sub>はてなブックマーク IT 人気エントリー ・ 11/19 00:27</sub>

NGINXのHTTP/2に関する2件の重大な脆弱性(CVE-2026-123633、CVE-2026-123007)により、認証なしでリモートコード実行が可能になりうるとWizが報告している。

## 技術記事（Qiita / Zenn）

### [AI も「一晩寝かせる」と考えがまとまる🥱 寝ている間に記憶を整理する Dreaming の仕組み](https://qiita.com/KYoshiyama/items/623e13ced9c119b614aa)
<sub>Qiita 人気記事 ・ 11/18 11:13</sub>

Anthropicが5月に発表した「Dreaming」について、同社自身の研究結果が出たことを受け、仕組みを図解で紹介する記事。

### [【AWS Emulator】消し忘れの恐怖から卒業！公式エミュレータでS3とLambdaを動かしてみた](https://qiita.com/N-Kyo/items/a111d174a751506790e2)
<sub>Qiita 人気記事 ・ 11/18 13:12</sub>

11月11日に一般提供となったAWS Emulatorで、接続先を環境変数で切り替えるだけでデプロイなしにS3とLambdaを動かしてみた記録。

### [RAGの「分からない」と参照元を自動検証するPython評価スクリプトの作り方](https://qiita.com/takumi_engineer/items/8287c5fb775d834086a4)
<sub>Qiita 人気記事 ・ 11/18 09:00</sub>

RAGの「参照元を出す」「根拠がなければ答えない」動作と検索ヒット率を、標準ライブラリだけで自動チェックする評価スクリプトの作り方。

### [【AWS】AgentCore Memoryのセッション全体要約とチャンクの違いを検証【AgentCore】](https://qiita.com/Nana_777/items/13df4ab402129246becd)
<sub>Qiita 人気記事 ・ 11/18 08:30</sub>

Amazon Bedrock AgentCore Memoryのsummary strategyで、セッション全体の要約と従来のチャンク単位の要約がどう違うかを検証している。

### [tsrs を導入したら oxlint の type-aware linting と typecheck が爆速になった話](https://zenn.dev/dress_code/articles/6c179ae5129131)
<sub>Zenn トレンド ・ 11/18 16:00</sub>

oxlintのtype-aware lintingとtypecheckがCI上で重いステップだった問題に、tsrsを導入して高速化した事例。

### [Claude Codeに危ないコマンドを打たせないフック — AIが作った安全装置は何も止めていなかった](https://zenn.dev/miokuri_ai/articles/c8f93358846ac3)
<sub>Zenn: AI ・ 11/18 17:30</sub>

rm -rfやgit reset --hardなどをClaude Codeに実行させないフックを、動くコード付きで解説。AIが作った安全装置が実際には何も止めていなかった、という経験も扱う。

### [Opus 5 に替えた途端、AI が手順を飛ばし始めた ― 原因はルールの書き方ではなかった](https://zenn.dev/nyabicode/articles/opus5-broke-my-rules)
<sub>Zenn: AI ・ 11/18 16:36</sub>

Opus 5に替えてから指示の手順を飛ばすようになった原因を、ルールの書き方ではなくその下の土台にあったとして考察した記事。

### [llama.cpp v1 を内蔵 GPU で試したら、長い入力の読み込みは約 2 倍、MoE キャッシュは遅くなった](https://zenn.dev/maruhana/articles/llamacpp-v1-igpu-prompt-2x-moe-cache)
<sub>Zenn: LLM ・ 11/18 19:22</sub>

llama.cppのv1.0.0を内蔵GPUのPCで試し、長い入力の読み込みは約2倍になった一方、MoEキャッシュは遅くなったという実測結果。

### [新機能、SageMaker AI の KV cache-aware routing を他のルーティング手法と比較](https://zenn.dev/aws_japan/articles/sagemaker-kv-aware-routing-bench)
<sub>Zenn: LLM ・ 11/18 09:34</sub>

SageMaker AIに追加されたKV cache-aware routingを、先行のprefix-aware routingなど他のルーティング手法と比較したベンチマーク。

## 日経

### [米、先端半導体「抜け道」監視網 NVIDIA騒動で米中覇権争いが第三国に拡大 (AIデータセンター・エフェクト)](https://business.nikkei.com/atcl/gen/19/00887/111700014/)
<sub>日経ビジネス電子版 ・ 11/19 05:00</sub>

米商務省が16日、AI向け先端半導体の輸出規制強化を発表した。シンガポールなど5カ国への輸出や、中国企業が遠隔利用する第三国のデータセンターへの輸出に許可取得を求める方針。

### [米国に「悪魔の選択」迫るAI競争 減速なら中国優位、加速でも人類滅亡危機](https://xtech.nikkei.com/atcl/nxt/column/18/03671/111300008/)
<sub>日経クロステック ・ 11/19 05:00</sub>

米中の技術覇権競争が激化するなか、各国が安全性への懸念を抱えつつ開発競争から降りられないジレンマを、経済安全保障の専門家が読み解く。

### [VMware継続は3割弱、「脱VM進める」「新規投資を抑制」の声も 独自調査](https://xtech.nikkei.com/atcl/nxt/column/18/03833/111600001/)
<sub>日経クロステック ・ 11/19 05:00</sub>

日経クロステックがVMware利用企業・自治体を調査し、26社・団体から50システム分の回答を得た。ライセンス変更に伴う値上げの影響や移行方針を聞いている。

### [直販とFDEで「Devin」を伸ばす、Cognition日本法人の正井社長が語る普及策](https://xtech.nikkei.com/atcl/nxt/column/18/02893/111700018/)
<sub>日経クロステック ・ 11/19 05:00</sub>

米Cognitionの日本法人社長が、ソフトウエア開発向け自律型AIエージェント「Devin」の直販やFDE相当チームによる展開策を語った。

### [オムロン、フィジカルAI想定の「大脳」確保 約1000億円で産業用PC企業を買収](https://xtech.nikkei.com/atcl/nxt/mag/ne/18/00001/00703/)
<sub>日経クロステック ・ 11/19 05:00</sub>

オムロンが米IPCメーカーOnLogicを約1046億円で買収する。PLCと産業用PCの連携を強め、フィジカルAIをFAに導入する基盤作りを進める。

### [川崎重工業、フィジカルAIロボを外販 溶接向け4脚型や見守り向け犬型を28年度に](https://xtech.nikkei.com/atcl/nxt/mag/ne/18/00007/00350/)
<sub>日経クロステック ・ 11/19 05:00</sub>

川崎重工業が、溶接用の4脚ロボットと高齢者見守り用の犬型ロボットを2028年度に外販する。いずれも開発開始から約半年で試作機を完成させた。

### [日本が半導体で対米投資、3兆円で2工場 グローバルファウンドリーズ運営](https://xtech.nikkei.com/atcl/nxt/mag/ne/18/00001/00700/)
<sub>日経クロステック ・ 11/19 05:00</sub>

GlobalFoundriesが米ニューヨーク州マルタに最大210億ドルで製造棟2つを建設すると発表した。日本による対米投融資の一環。

### [NTTが光チップレットを31年量産、東芝系や新光電気と連合](https://xtech.nikkei.com/atcl/nxt/mag/ne/18/00001/00704/)
<sub>日経クロステック ・ 11/19 05:00</sub>

NTTなど4社が、GPUの近くまで光配線を引き込む「光チップレット」を2031年までに国内で量産する体制を整える。

---
<sub>取得: 2026-11-19 06:51 JST ／ 取得失敗: なし</sub>
