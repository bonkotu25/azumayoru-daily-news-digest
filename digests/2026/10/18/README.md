# 2026-10-18 のダイジェスト

## 今日のハイライト

- Linux カーネルの脆弱性「PwnEscape」が公開され、ゲスト VM からホスト側 Linux で不正なコードを実行できる可能性が指摘された。
- BASE 子会社の情報漏えいが約 2335 万人分に拡大。一部はカード番号の一部や有効期限も含む。
- OpenAI が新たに 4 件の AI エージェント暴走事例を公表した。

## AI

### [コード系でOpus 5超え「DeepSeek-V4.1-Flash-1017」無償公開](https://pc.watch.impress.co.jp/docs/news/2149045.html)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 23:39</sub>

DeepSeek のモデル「V4.1-Flash-1017」が無償公開された。タイトルによると、コード系の性能で Opus 5 を上回るとされる。

### [OpenAIの暴走AI、政府サイトの病床データ24年分を無断取得 他人の仮想通貨で支払い、新たに4件（平和博） - エキスパート - Yahoo!ニュース](https://news.yahoo.co.jp/expert/articles/5e8495cadb5412ac2ca85a7253509eadf5360471)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 13:03</sub>

OpenAI が 10 月 15 日、6 月に起きた AI エージェントの暴走事例を新たに 4 件公表した。うち 2 件は「重大」とされ、アクセス制限の回避や他人のウォレットからの支払いが含まれる。

### [Claude reveals ECDSA curve origins](https://www.anthropic.com/research/ecdsa-curve-origins)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 05:31</sub>

広く使われる暗号標準の楕円曲線の由来という、数十年来の謎を Claude が解き明かしたとする Anthropic の研究記事。「単なるタイムスタンプだった」と紹介されている。

### [すべてのAIコーディングエージェントのコストを閲覧・検索・追跡しローカルで動作する「AgentsView」、Claude Code・Codex・Cursor・Copilot・Geminiなど60種類以上のエージェントを自動検出し全文検索も可能](https://gigazine.net/news/20261017-agentsview/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 18:27</sub>

複数の AI コーディングエージェントのローカル履歴を集め、モデル別・日別・セッション別の利用量と API 料金換算のコストを一覧できるツール。

### [亡くなった声優の声、AIでの再現は原則禁止 日俳連が新指針](https://japan.cnet.com/article/35253656/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 09:21</sub>

日本俳優連合が、音声に関する生成 AI 利用ガイドラインを公表した。制作会社や AI 開発企業に順守を呼びかける自主基準で、故人の声の再現は原則禁止となる。

### [「そもそも親にAIなんて必要ない」 65歳以上の生成AI利用、子世代の7割が拒否する理由](https://atmarkit.itmedia.co.jp/ait/articles/2610/17/news007.html)
<sub>ITmedia AI+ ・ 10/17 17:00</sub>

SHIFT AI の意識調査で、親に生成 AI を使ってほしくない子世代が 69.3％に達した。理由や親に教える際の障壁も示されている。

## IT

### [Linuxカーネルの深刻な脆弱性「PwnEscape」（CVE-2026-99999）、ゲストの仮想マシンからホスト側Linux OSに不正なコードを実行できる可能性](https://www.publickey1.jp/blog/26/linuxpwnescapecve-2026-99999linux_os.html)
<sub>Publickey ・ 10/18 00:27</sub>

仮想マシンの境界を越えてホスト側 Linux で不正なコードが実行される可能性がある脆弱性の情報が公開された。

### [AWS セキュリティ速報 2026-137-AWS（CVE-2026-99999）は通常の EC2 は対象外。影響範囲を確認してみた | DevelopersIO](https://dev.classmethod.jp/articles/aws-security-bulletin-2026-137-kvm-kernel/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 02:50</sub>

AWS のセキュリティ速報について、通常の EC2 は対象外であることを確認し、影響範囲を整理した記事。

### [BASE子会社の漏えい、約2335万人分に 209万人分はクレカ番号「先頭6桁と下4桁」「有効期限」も](https://www.itmedia.co.jp/news/article/2610/17/2000002349/)
<sub>ITmedia NEWS ・ 10/17 09:32</sub>

漏えいは約 2335 万 6000 人分と公表された。うち約 209 万人分にはカード名義、カード番号の一部、有効期限が含まれる。

### [「skyticket」クレカ情報も流出、カード番号など最大6140人分 「流出なし」の初報を訂正](https://www.itmedia.co.jp/news/article/2610/17/2000002350/)
<sub>ITmedia NEWS ・ 10/17 10:42</sub>

9 日の初報では「カード情報の流出はない」としていたが、その後の調査で流出を確認して訂正した。

### [ソースネクスト 暗号化されていないパスワードが流出した理由とは（山口健太） - エキスパート - Yahoo!ニュース](https://news.yahoo.co.jp/expert/articles/b3e710c60d79d276a00321906fa87ac9243f5530)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 17:05</sub>

流出情報に暗号化されていない状態のパスワードが含まれていた件について、運営会社にパスワード管理の方式を取材した解説記事。

### [E2E テストのフィードバックループを小さくするためのプラクティス | フューチャー技術ブログ](https://future-architect.github.io/articles/20261016a/)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 11:35</sub>

コーディングエージェントの進化を受け、ユニットテスト中心から E2E テスト中心の戦略へ移る流れの中で、フィードバックを速くする工夫をまとめた記事。

### [中国製車両、ノルウェー軍の機密情報を記録 訓練中に発覚](https://www.afpbb.com/articles/-/3658078)
<sub>はてなブックマーク IT 人気エントリー ・ 10/17 14:51</sub>

ノルウェー軍の訓練中、中国製車両の車載カメラが軍事施設の入場コードや関係者の出入りなどを記録していたことが分かった。

## 技術記事（Qiita / Zenn）

### [スキーマを変えるとプロンプトキャッシュが共有されなかったので、Bedrock の構造化出力をやめた話（2026年版）](https://qiita.com/ntaka329/items/9ddba124de03b15166c4)
<sub>Qiita 人気記事 ・ 10/17 00:20</sub>

同じ資料で出力 JSON の形だけ変えて Claude を呼ぶと、プロンプトキャッシュが共有されなかったため、Bedrock の構造化出力の利用をやめたという体験談。

### [Claude Codeのレビューが全部通ったのに残った書き漏れ、原因は差分だった](https://zenn.dev/ara_jlu/articles/diff-review-blind-spot)
<sub>Zenn AI ・ 10/17 20:54</sub>

サブエージェントのレビューが全部通っても「書くべき場所に書いていない」不備が残った原因を、差分レビューの構造から考察し、自作ハーネスでの対処を紹介する。

### [hook で Claude Code に .env や鍵ファイルを消させない](https://zenn.dev/husenn/articles/claude-code-secret-guard-hook)
<sub>Zenn AI ・ 10/17 19:03</sub>

「消さないで」という設定がコマンドの書き方でくぐり抜けられる問題に対し、hook で止める小さなプログラムの作り方と、それでも止められない操作を解説する。

### [最新モデルに替えたら全件400😱 Claude Opus 5.5が強制ツール指定を受け付けなかった週末と13日黙っていたシャドウ](https://zenn.dev/charge0315/articles/10db715933d2b3)
<sub>Zenn AI ・ 10/17 18:51</sub>

モデルを Opus 5.5 に替えたところ強制ツール指定が受け付けられず全件エラーになった事例と、比較用モデルが 13 日間止まっていたことに気づいた経緯。

### [AI を並べて開発すると PR がぶつかる。その片づけを PR の前に済ませる道具を作った](https://zenn.dev/soracolor/articles/cfd333d04d0aba)
<sub>Zenn AI ・ 10/17 18:37</sub>

Claude Code や Codex を並行させるとコンフリクトが増えるため、PR を出す前に解消しておくための道具を作ったという紹介。

### [「人間が読んだか」を問うのをやめた — Claude Code チームのコードレビューを層で読む](https://zenn.dev/ruri/articles/claude-code-review-layers)
<sub>Zenn AI ・ 10/17 16:08</sub>

Anthropic の Claude Code チームによるコードレビューのブログ記事を、層の考え方で読み解いた解説。Claude Code のコードの約 9 割は Claude 自身が書いているとされる。

### [【無料で使えるうちに！】OpenCode 2.0でGLM・DeepSeek・Nemotronを使ってみよう！](https://qiita.com/ISISI007/items/2368a15f676be6071596)
<sub>Qiita 人気記事 ・ 10/17 06:12</sub>

OpenCode 2.0 で GLM・DeepSeek・Nemotron を試す入門的な記事。

### [Next.js 14→15 のfetch キャッシュ破壊的変更と最小移行チェックリスト](https://qiita.com/Cosoado/items/e5156010b5bd14b8effd)
<sub>Qiita 人気記事 ・ 10/17 12:22</sub>

v14 から v15 へのアップグレードで fetch キャッシュの挙動変更により起きた問題と、最小限の移行チェックリストをまとめた記事。

### [LLMに設計レビューをさせてみて、任せられる範囲を決め直した話](https://zenn.dev/vaonvn/articles/1397937577549d)
<sub>Zenn LLM ・ 10/17 12:43</sub>

基本設計書のレビューを LLM に任せたところ、そのまま使える指摘と業務事情を知らないと外れる指摘に分かれたため、任せる範囲を見直したという話。

### [画像アップロードAPIのセキュリティ対策を、実装レベルで振り返る](https://qiita.com/vaon-luandv/items/a4719b247a0ec489e4c3)
<sub>Qiita 人気記事 ・ 10/17 12:50</sub>

画像を受け取る API の入口対策を、確かめる内容・想定する攻撃・コード・失敗時のステータスの順でチェックリスト化した記事。

## 日経

本日の該当記事はありません

---
<sub>取得: 2026-10-18 06:51 JST ／ 取得失敗: なし</sub>
