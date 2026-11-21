# 2026-11-22 のダイジェスト

## 今日のハイライト

- Anthropicの数学者がClaudeとの共同でリーマン予想の証明を発見したと発表
- 米国で銀行・空港などのシステム障害が相次ぎ、AIによる脆弱性修正の急増が背景との指摘
- 米国株が急落し、AnthropicのIPOでもAI関連株への懸念を払拭できず

## AI

### [AIに必要なのは知識か、企業独自の判断基準か？ 管理職調査で見えたAI活用の盲点](https://kn.itmedia.co.jp/kn/article/2611/22/2000003384/)
<sub>ITmedia AI+ ・ 11/22 06:00</sub>

管理職を対象にした調査で、半数以上が利用されなくなったAIツールや用途があると回答した。背景には企業独自の判断基準に関わる課題があるようだ。

### [超難問「リーマン予想」AIと証明か 米アンソロピックの数学者発表：朝日新聞](https://www.asahi.com/articles/ASVCP10Z2VCPUHBI00GM.html)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 13:12</sub>

Anthropicの数学者が、同社のAIモデルClaudeと共同でリーマン予想の証明を発見したと個人サイトで発表した。

### [企業はAIをどう選ぶようになった？ ChatGPT、Copilot、Geminiの勢力図](https://kn.itmedia.co.jp/kn/article/2611/21/2000003385/)
<sub>ITmedia AI+ ・ 11/21 14:22</sub>

企業が業務で使うAIの顔ぶれが変わりつつあり、既存の業務環境に組み込まれたAIを使う動きも広がっているという。

### [AIで成果を出す企業ほど「人を増やす」？ “通説”を否定する調査結果をIDCが発表](https://www.itmedia.co.jp/enterprise/articles/2611/21/news003.html)
<sub>ITmedia AI+ ・ 11/21 09:00</sub>

IDCの調査では、AI投資で高いROIを得ている組織ほど今後の増員を見込む割合が高く、「AIで人員は減る」という通説と食い違う結果になった。

## IT

### [「パッチ地獄」が米IT障害誘発、AIがせかす脆弱性修正 銀行や空港停止 - 日本経済新聞](https://www.nikkei.com/article/DGXZQOGN18CYM0Y6A111C2000000/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 09:21</sub>

米国の銀行や空港でシステム障害が相次いでおり、AIが大量の脆弱性を見つけパッチ適用を急がざるを得ないことが背景にあると報じている。

### [相次ぐシステム障害、AIはどこまで関係しているのか--「12月はさらに深刻に」と専門家](https://japan.cnet.com/article/35255244/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 08:39</sub>

MicrosoftのOutlookや航空管制、Chase銀行などで障害が続く状況を取り上げ、AIとの関係を専門家の見方とともに検討している。

### [Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 08:08</sub>

手元のノートPCで動かせる小型モデル「Inkling 2 Mini」の公開。中間層を3回繰り返すループ型のトランスフォーマーだという。

### [形式検証を活用した脆弱性診断LLMのプロトタイプをEthereum Foundationに納品｜Nyx Foundation](https://note.com/nyxfoundation/n/n782d4fb32344)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 16:28</sub>

Nyx FoundationがEthereum Foundationの助成で、LLMを使った脆弱性診断ツールSPECAのプロトタイプを納品した。仕様書から確認項目を作り、実装が満たすかを調べる仕組み。

### [GitHub - mitaku/andon: A one-person software factory: AI coding agents take tasks from a ledger through review to merge, and call the human only for decisions only they can make.](https://github.com/mitaku/andon)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 19:52</sub>

AIコーディングエージェントがissueを受け取り、実装・レビュー・マージまで進める「一人用ソフトウェア工場」のリポジトリ。人は人にしか決められない判断のときだけ呼ばれる。

### [寝てる間に自動で動くAIエージェントを誰でも作れる：10分でわかる pstack 実践ガイド](https://zenn.dev/canly/articles/ca6875cd79539f)
<sub>はてなブックマーク IT 人気エントリー ・ 11/21 07:35</sub>

AI Engineer CODE 2026の基調講演で語られた、寝ている間にエージェントがPRを進める手法（pstack）の実践ガイド。MITライセンスで公開されているという。

## 技術記事（Qiita / Zenn）

### [【pre:Inventまとめ】AWSのAIエージェント認証がいろいろ進化！MCPサーバー構築を例に一挙解説](https://qiita.com/minorun365/items/bd6091f2599a0f37326b)
<sub>Qiita 人気記事 ・ 11/21 13:03</sub>

re:Invent直前の「pre:Invent」で発表された、AWSのAIエージェント認証まわりの機能強化を、MCPサーバー構築を例にまとめている。

### [pgvectorのHNSWでテナント絞り込みすると検索が0件になる問題と対策](https://qiita.com/takumi_engineer/items/142ca7088f13f006da82)
<sub>Qiita 人気記事 ・ 11/21 18:51</sub>

マルチテナントRAGで、pgvectorのHNSWにtenant_idの絞り込みを付けると件数が足りなくなる問題について、仕組みと再現・対策・検知をコードで示している。

### [AIエージェントに堅牢なテストを書かせるには？](https://zenn.dev/yasuakiomokawa/articles/3ac970c3a3a1c7)
<sub>Zenn トレンド ・ 11/21 18:09</sub>

AIエージェントに、実装変更で壊れにくいテストを書かせる手順を4つにまとめた記事。筆者が自分のプロダクトで15日間試した結果を反映している。

### [【TLA+】AIにテストケースを書かせるな。ルールを書け](https://zenn.dev/karamage/articles/73027ee36796dc)
<sub>Zenn トレンド ・ 11/21 11:12</sub>

AIにテストケースを書かせず、TLA+でルールを書くという考え方を紹介している。実装もレビューもテストも同じAIという状況への違和感が出発点。

### [AlphaGoの探索をClaude Codeに載せてみた](https://zenn.dev/natsu529/articles/7b246228d11b82)
<sub>Zenn: LLM ・ 11/21 18:59</sub>

Claude Codeなどが一回で外した修正を、複数の方法で試して最良の答えを選ぶ自作ツール「agent-mcts」をMITライセンスで公開した記事。

### [Claude Code の費用は、書かせた量ではなく読み直しで決まっていた](https://zenn.dev/kumukumu/articles/claude-code-cost-is-rereading)
<sub>Zenn: LLM ・ 11/21 14:00</sub>

Claude Codeの利用ログ128日分を集計し、費用は書かせた量（出力）より会話の読み直しが大きく占めていたと報告している。

### [バイブコーディング・isdd・AI-DLCに同じ依頼を出して、できあがりと手間を比べた](https://qiita.com/notfolder/items/c4480072ef594e591dc8)
<sub>Qiita 人気記事 ・ 11/21 08:49</sub>

バイブコーディング、isdd、AI-DLCに同じ依頼を出し、できあがりと手間を比べた検証記事。

## 日経

### [米国市場ナスダック5％安、アンソロピックは支えられず S&P・ダウ調整局面 (Views)](https://business.nikkei.com/atcl/seminar/19/00030/112100826/)
<sub>日経ビジネス電子版 ・ 11/21 09:51</sub>

米国株が急落し、AnthropicのIPOも市場を支えられず、AI関連銘柄への懸念が強まったと伝えている。

---
<sub>取得: 2026-11-22 06:50 JST ／ 取得失敗: なし</sub>
