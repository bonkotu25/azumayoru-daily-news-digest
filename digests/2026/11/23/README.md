# 2026-11-23 のダイジェスト

## 今日のハイライト

- Anthropic の数学者が Claude と共同で「リーマン予想」を証明したと主張、Lean コミュニティが「正しい」と認定
- メルカリが利用する「Notion AI」のチャット記録が外部流出の可能性、AI 委託先で 2 種類の攻撃を確認
- プレイド「KARTE」の不正アクセスで影響企業が拡大、タワーレコードでも約 1100 万件の個人情報が流出

## AI

### [メルカリの情報流出、AI委託先で何が起きた？ 確認された2つの攻撃](https://kn.itmedia.co.jp/kn/article/2611/23/2000003393/)
<sub>ITmedia AI+ ・ 11/23 06:00</sub>

メルカリグループが業務で使う「Notion AI」のチャット記録の一部が流出した可能性が公表されました。AI 処理の委託先では、クラウド事業者への侵害や認証情報の窃取など 2 種類の攻撃が確認されています。

### [Anthropicの数学者、「Claude」と共同で「リーマン予想」を証明したと主張 Leanコミュニティが「正しい」と認定](https://www.itmedia.co.jp/news/article/2611/22/2000003388/)
<sub>ITmedia AI+ ・ 11/22 08:21</sub>

Anthropic の数学者が Claude と共同で証明を発見したと発表し、Lean で書かれた 1700 万行の形式証明を公開しました。Lean コミュニティは検証のうえ「正しい」とする共同声明を出しています。

## IT

### [「委託したとこ全部漏洩してんじゃんよ💢」プレイド『KARTE』の不正アクセスで、ZOZOTOWNや三菱UFJ銀行など影響を受けた企業が次々判明…不安や警戒の声が広がる](https://togetter.com/li/2773732)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 23:51</sub>

プレイドの「KARTE」への不正アクセスで、影響を受けた企業が相次いで判明していると、ネット上の反応とともにまとめられています。委託先経由の漏洩への警戒が広がっています。

### [タワーレコード 不正アクセスで約1100万件の個人情報流出 | NHKニュース](https://news.web.nhk/newsweb/na/nd-20261122de79936)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 19:00</sub>

タワーレコードの通販サイトが不正アクセスを受け、顧客のメールアドレスや氏名など約 1100 万件の個人情報が流出したと発表されました。

### [六花亭に不正アクセス クレカ情報不正利用とみられる被害確認 | NHKニュース](https://news.web.nhk/newsweb/na/nd-20261122de79904)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 14:57</sub>

六花亭のオンラインショップで約 8000 件のクレジットカード情報が流出した可能性があり、不正利用とみられる被害も確認されたと報じられています。

### [Upload2Shell](https://pwn.ai/upload2shell)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 08:53</sub>

Ghostscript の Type 1 フォントローダーにある use-after-free を突き、細工した文書で -dSAFER サンドボックスを越えて任意コマンドを実行できるという脆弱性の解説です。

### [MetaのAIエージェント「Muse」は何ができる？ ChatGPTやGeminiとの違い、注意点を解説](https://www.itmedia.co.jp/mobile/articles/2611/22/news005.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 11:46</sub>

Meta のパーソナル AI エージェント「Muse」が 10 月 23 日に日本で提供開始されたことを受け、できることや他の AI との違い、注意点をまとめた解説記事です。

### [AndroidスマホがWindows PCのサブ画面に？マイクロソフトが新機能 - すまほん!!](https://smhn.info/202611-microsoft-link-to-windows-extend-display-android-second-screen)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 21:29</sub>

Microsoft が、Android スマホを Windows PC の拡張ディスプレイとして使える新機能「Extend display」を準備していると紹介しています。

### [GitHub - awslabs/codekb](https://github.com/awslabs/codekb)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 03:25</sub>

既存システム（ブラウンフィールド）の開発で AI を使う際の、複数リポジトリをまたぐ作業の課題に取り組む awslabs 公開のリポジトリです。

### [回収対象のAnker製モバイルバッテリーで火災発生か 型番「A1257」の一部に使用中止を呼びかけ](https://japan.cnet.com/article/35255262/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/22 07:17</sub>

消費者庁は、回収中の Anker 製モバイルバッテリー（10000mAh）で 10 月に東京都で火災が起きたと発表しました。原因は調査中で、回収理由の不具合との関連は不明です。

## 技術記事（Qiita / Zenn）

### [Claude Code を安全に「自走」させるなら、もう Docker Sandboxes 一択でよくない？と思った話。](https://qiita.com/yamac_tech/items/2f1d598288990c381f2d)
<sub>Qiita 人気記事 ・ 11/22 08:38</sub>

AI コーディングエージェントを確認なしで動かすための隔離環境として、Docker Sandboxes を推す体験談です。

### [Claude Codeの--fallback-modelで無人ジョブを止めない：混雑・利用上限・終了コードの3つの落とし穴と実装](https://qiita.com/joinclass/items/080927f3b092b9de46e6)
<sub>Qiita 人気記事 ・ 11/22 08:30</sub>

launchd から claude -p で 30 以上のジョブを無人実行する中で、まとめて失敗した経験をもとに、--fallback-model 利用時の落とし穴と実装を紹介しています。

### [AIがルールを読み飛ばすので、「検査」に変えた：書き込み時に拒否するフックを作った記録](https://zenn.dev/uzunaru/articles/f67ac6f4d8a540)
<sub>Zenn: AI ・ 11/22 18:56</sub>

AGENTS.md に書いたルールが守られない問題に対し、Claude Code のフックで書き込み時に機械的に検査し、違反なら保存を拒否する仕組みを作った記録です。

### [AI が書いて AI がレビューしたコードでも、3 回に 1 回はバグが残っていた](https://zenn.dev/beyond/articles/92657b461ebcb4)
<sub>Zenn: AI ・ 11/22 17:38</sub>

実装もレビューも AI エージェントに任せる個人開発で、複数観点のレビューを通してもバグが残った割合を振り返っています。

### [Qt CreatorでAIにビルドを頼む：ACPとMCPを実行記録から理解する](https://zenn.dev/sugitakenji/articles/a5a18551387392)
<sub>Zenn: AI ・ 11/22 16:50</sub>

AI の「ビルドしました」という回答が実際のビルド記録と合っているかを、意図的に入れた誤りと実行記録で確かめながら ACP と MCP の動きを理解する記事です。

### [その「繰り返し率」、測っている対象が違うかもしれない — ローカルLLMの思考と本文を分けて測る話](https://zenn.dev/shinkaspool/articles/83e7b524e25a93)
<sub>Zenn: LLM ・ 11/22 10:25</sub>

ローカル LLM の繰り返し率が 76% から 6% に下がったものの、計測していたのが「答え」ではなく主に「思考」だったと気づいた話です。出力が混ざることによる測定の歪みを扱っています。

### [NixOSでStrataを動かそう](https://zenn.dev/mekhr/articles/87b57fbdad4b9e)
<sub>Zenn: LLM ・ 11/22 17:16</sub>

9 月末に登場した推論エンジン Strata を NixOS で動かす手順の紹介です。比較的強い一般 PC で大きなモデルを動かせる点が話題になったと書かれています。

### [ZONOS3-MiniをVRAM 6GBで実測：llama-ttsで日本語読み上げ12回（VRAM・RTF）](https://zenn.dev/localai_lab/articles/0f842a9f6372e8)
<sub>Zenn: LLM ・ 11/22 15:03</sub>

音声合成モデル ZONOS3-Mini を VRAM 6GB の GPU 上で llama.cpp の llama-tts で動かし、日本語の読み上げを条件ごとに実測した記録です。

### [tiny-voca入門 ― 18MBの英語TTSをCPUで動かす。70倍速の看板を実測する](https://zenn.dev/ikesita/articles/zenn-08-tiny-voca)
<sub>Zenn: AI ・ 11/22 15:40</sub>

4.5M パラメータ・18MB の英語 TTS「tiny-voca」を CPU で動かし、公式が掲げる 70 倍速の値を実測値と比べて検証しています。

## 日経

本日の該当記事はありません

---
<sub>取得: 2026-11-23 06:51 JST ／ 取得失敗: なし</sub>
