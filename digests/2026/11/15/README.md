# 2026-11-15 のダイジェスト

## 今日のハイライト

- Microsoft 365 の障害で、ChatGPT と Claude の Microsoft 365 コネクタも動作不良に（AI）
- AI を悪用したサイバー攻撃の拠点と疑われるサーバーが、世界で約千台見つかった（IT）
- Cursor が、Claude Code 拡張機能の不正コピーが出回ったセキュリティインシデントの続報を公開（IT）

## AI

### [【追記あり】M365障害、ChatGPT／Claudeのコネクタにも影響 「ほとんどのリクエストで動作しない」](https://www.itmedia.co.jp/aiplus/article/2611/13/2000003164/)
<sub>ITmedia AI+ ・ 11/14 20:35</sub>

Microsoft 365 の複数サービスで起きた障害により、ChatGPT と Claude の Microsoft 365 コネクタも正常に動かない状態になり、両社が報告した。

### [NVIDIAをつくった男、ジェンスン・フアン “デニーズの皿洗い“から“AI時代の主役“へ、激動の半生](https://www.itmedia.co.jp/business/articles/2611/14/news008.html)
<sub>ITmedia AI+ ・ 11/14 07:30</sub>

NVIDIA を創業したジェンスン・フアン氏の、皿洗いのアルバイトから億万長者になるまでの半生を振り返る読み物。

## IT

### [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 09:52</sub>

長期間動き続け、いつ・どう動くかを自分で判断するエージェントについて、基本となる要素とその組み合わせ方を解説したガイド。

### [AI悪用の攻撃拠点、千台発見 サイトの弱点探索、不正侵入疑い](https://www.47news.jp/15231027.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 23:55</sub>

AI を使ってウェブサイトの弱点を探す攻撃の拠点と疑われるサーバーが、10月以降、世界で千台前後あることが、日本の専門機関と海外企業の国際調査で分かった。

### [Cognitoの自己サインアップが有効だと、誰でもAWSの一時認証情報を取得できる：AI攻撃ツールARTEXの事例と確認したい設定3点 | DevelopersIO](https://dev.classmethod.jp/articles/cognito-self-signup-agentic-attack/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 21:48</sub>

S3 と Cognito を組み合わせた SPA 構成が攻撃用 AI エージェントに悪用された事例を紹介し、確認したい設定を3点挙げている。

### [マーケ支援のプレイド、不正アクセスでサービス停止 - 日本経済新聞](https://www.nikkei.com/article/DGXZQOUC13B0E0T11C26A1000000/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 09:47</sub>

プレイドが主力サービス「KARTE」への不正アクセスを発表した。情報流出の有無は調査中で、緊急メンテナンスを行っている。

### [【速報】マネックス証券、マイナカード画像漏えいか](https://www.47news.jp/15227159.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 00:36</sub>

委託先が管理する口座開設システムへの不正アクセスで、本人確認書類の画像1592件と最大113万件のメールアドレスが漏えいした恐れがあるという。

### [An update on our recent security incident · Cursor](https://cursor.com/blog/security-incident-update)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 11:05</sub>

10月29日に調査中と伝えていた、Cursor の拡張機能マーケットプレイスに Claude Code 拡張の不正なコピーが出た件の続報。

### [[アップデート] Amazon Route 53 で、レコードセットの変更/削除を保護できるようになりました | DevelopersIO](https://dev.classmethod.jp/articles/route53-recordset-protections/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 07:48</sub>

Amazon Route 53 のレコードセットを、変更や削除から保護できるようになったアップデートの紹介記事。

### [Gemini、Google Walletと連携して家計を分析--サブスクの値上げも検出](https://japan.cnet.com/article/35254868/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/14 07:02</sub>

Gemini が Google Wallet の情報を使って支出の分析や予算づくりを支援する機能を、米国で提供開始。日本ではまだ使えない。

## 技術記事（Qiita / Zenn）

### [ちょっと見ない間にClaude APIが進化してた！](https://qiita.com/moritalous/items/9e7c02b749037238b2bc)
<sub>Qiita 人気記事 ・ 11/14 15:32</sub>

Python と公式 SDK を使い、進化した Claude API の機能を試していく記事。

### [Claude Codeを並列で回すとsettings.jsonが壊れる問題を、mkdirロックとアトミック書き込みで止める](https://qiita.com/joinclass/items/8c40b05a48487aa588c0)
<sub>Qiita 人気記事 ・ 11/14 08:30</sub>

Claude Code を 17 本以上のジョブで並列に動かす運用で起きる settings.json の破損を、mkdir によるロックとアトミック書き込みで防ぐ方法。

### [AWS Emulatorが一般提供されたので、ローカルでS3バケットを作成してみた](https://qiita.com/moyomoyomoyo/items/522ba880ff37971aa969)
<sub>Qiita 人気記事 ・ 11/14 16:41</sub>

11月11日に発表された、AWS をローカルで動かせる「AWS Emulator」で、S3 バケットを作成してみた記録。

### [【2026/11/13時点】Claude Duet を Team プランで触ってみた（組織で使うときの注意点つき）](https://zenn.dev/canly/articles/e2bd67c9a4c18b)
<sub>Zenn トレンド ・ 11/14 08:45</sub>

Team プランの管理画面に現れた Claude Duet（ベータ）を組織で有効にして試し、できることと組織利用時の注意点をまとめている。

### [サンドボックスが消えたらエージェントを起動しない：bubblewrap を起動直前に検証・復旧する fail-closed ガード](https://zenn.dev/coastlinedb/articles/a8111256ac5469)
<sub>Zenn: AI ・ 11/15 00:09</sub>

VM の入れ替わりで bwrap が消える障害が続いたため、エージェント起動の直前に毎回検証し、壊れていれば退避コピーで復旧する仕組みを作った。

### [AI に Excel を読ませるなら、Python より3〜13倍速く、メモリ使用量は最大92%減](https://zenn.dev/itoken_lab/articles/excel-read-fast-light)
<sub>Zenn: AI ・ 11/14 21:30</sub>

Skill に同梱した実行ファイルで Excel を CSV や JSON に変換し、Python より高速かつ省メモリで AI に渡す方法を紹介している。

### [AIが作ったPRは、1本ずつレビューしても足りない](https://zenn.dev/veripsa/articles/hybrid-llm-merge-risk-design)
<sub>Zenn: LLM ・ 11/14 21:30</sub>

Git ではきれいにマージできても、2つの変更を合わせると壊れるケースを検証し、並行する AI 実装のレビューで見落としやすい点を論じる。

### [スリーパーエージェントを自作して、差分からバックドアを探してみた](https://zenn.dev/50s_zerotohero/articles/d065a3fef832ee)
<sub>Zenn: LLM ・ 11/14 20:03</sub>

特定の合言葉で豹変するバックドア入りモデルを自作し、差分から仕込みを見つけられるかを試した。

### [SAST の外側を探す AI：SonarQube Hunter Agent の仕組みと導入条件](https://zenn.dev/r_goto/articles/sonarqube-hunter-agent)
<sub>Zenn: AI ・ 11/14 21:31</sub>

SAST では見つけにくいロジック上の脆弱性を AI が探す SonarQube Hunter Agent の仕組みと導入条件をまとめた、他社ブログの要約記事。

### [AI駆動開発で実装が速くなったら、CI待ちが一番長くなった——品質を落とさずCIを軽くする](https://qiita.com/ktdatascience/items/b129d5eee1bc9077f085)
<sub>Qiita 人気記事 ・ 11/14 10:15</sub>

AI で実装が速くなった結果ボトルネックになった CI の待ち時間を、品質を落とさずに短くする方法を扱う。

## 日経

本日の該当記事はありません

---
<sub>取得: 2026-11-15 06:50 JST ／ 取得失敗: なし</sub>
