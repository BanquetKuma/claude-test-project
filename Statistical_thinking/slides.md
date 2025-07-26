---
theme: seriph
background: /images/statistical_thinking_flowchart.jpeg
title: 統計思考のススメ：日常に潜む数字の真実を見抜く力
info: |
  ## 統計思考のススメ
  一般市民向けの統計学入門プレゼンテーション

  統計の専門家が、日常生活に役立つ統計的な考え方を
  分かりやすく解説します。
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: 'Noto Sans JP'
  serif: 'Noto Serif JP'
---

# 統計思考のススメ

## 日常に潜む数字の真実を見抜く力

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover:bg="white op-10">
    Press Space for next page <span class="i-carbon-arrow-right inline"></span>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub" title="Open in GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <span class="i-carbon-logo-github"></span>
  </a>
</div>

<!--
皆さん、こんにちは。今日は「統計思考のススメ」と題して、
日常生活で出会う様々な数字の裏側に隠された真実を、
一緒に探っていきたいと思います。
-->

---
layout: intro
class: text-center
---

# 自己紹介

<div class="text-center">
  <h2 class="text-5xl font-bold mt-6 mb-4 bg-gradient-to-r from-blue-400 to-purple-600 bg-clip-text text-transparent">熊田 翔</h2>
  <p class="text-2xl opacity-90">統計学には昔から興味があり、仕事でも使ってきました</p>
</div>

<div class="mt-10 grid grid-cols-3 gap-6">
  <div class="bg-gradient-to-br from-blue-500 to-blue-700 bg-opacity-20 rounded-xl p-5 transform hover:scale-105 transition-all">
    <div class="i-carbon-certificate text-5xl mb-3 text-yellow-400"/>
    <h3 class="text-lg font-bold mb-2">🏆 統計関連資格</h3>
    <p class="text-sm">統計検定<br/>1級・準1級・2級</p>
  </div>
  <div class="bg-gradient-to-br from-green-500 to-green-700 bg-opacity-20 rounded-xl p-5 transform hover:scale-105 transition-all">
    <div class="i-carbon-analytics text-5xl mb-3 text-green-400"/>
    <h3 class="text-lg font-bold mb-2">🔬 趣味が高じて</h3>
    <p class="text-sm">統計学は趣味から始めた<br/>探究心の賜物</p>
  </div>
  <div class="bg-gradient-to-br from-purple-500 to-purple-700 bg-opacity-20 rounded-xl p-5 transform hover:scale-105 transition-all">
    <div class="i-carbon-industry text-5xl mb-3 text-purple-400"/>
    <h3 class="text-lg font-bold mb-2">⚙️ 現在の戦場</h3>
    <p class="text-sm">製造業×データサイエンス<br/>現場の数字と格闘中</p>
  </div>
</div>

<div class="text-center mt-8 text-lg opacity-80 animate-bounce">
「数字の向こう側にある、本当の物語を一緒に見つけましょう！」
</div>

<!--
どうも、熊田です！今日はよろしくお願いします。
簡単に自己紹介をさせてください。
-->

---
layout: two-cols
---

# 私のキャリア

<div>

### 🏭 最初の10年：モノづくりの現場

- 大手電機メーカー・半導体スタートアップ
- パワー半導体の生産技術者
- **年間数千万円のコスト削減**を実現
- データ活用の可能性に目覚める

</div>

::right::

<div>

### 📊 その後の4年：データの世界へ

- 34歳でデータサイエンティストに転身
- 化学プラントの故障原因究明
- **AIによる予知保全システム**開発
- 最近は**生成AI**のシステム開発も

</div>

<div>

<div class="mt-8 p-4 bg-blue-500 bg-opacity-20 rounded-lg">
  <p class="text-center font-bold">
    現場のリアル × データ分析 = 課題解決
  </p>
</div>

</div>

<div class="absolute bottom-0 left-0 right-0 h-32 overflow-hidden">
  <img src="./images/Image_fx.jpg" class="w-full h-full object-cover opacity-80" />
</div>

<!--
私のキャリアは少し変わっていて、製造業の現場とデータサイエンスという
2つの世界を経験しているのが強みです。
-->

---
layout: center
class: text-center
---

# その数字、信じて大丈夫？

<div>

<div class="text-2xl mt-8">
  「お客様満足度95%！」
</div>

</div>

<div>

<div class="text-2xl mt-4">
  「視聴率20%超えの大ヒットドラマ」
</div>

</div>

<div>

<div class="text-2xl mt-4">
  「〇〇の成功率80%」
</div>

</div>

<div>

<div class="mt-12 text-3xl font-bold text-orange-400">
  本当にそうでしょうか？🤔
</div>

</div>

<!--
皆さん、こんな数字を見たことありませんか？
でも、これらの数字、本当に信じていいのでしょうか？
-->

---
layout: fact
---

# 今日のゴール

<div class="text-2xl">
  <p>難しい計算は一切しません！</p>
  <p class="mt-4">数字に騙されず、賢く付き合うための</p>
  <p class="mt-4 text-4xl font-bold text-blue-400">「統計思考」</p>
  <p class="mt-4">を一緒に探検しましょう</p>
</div>

<div>

<div class="mt-12 text-xl opacity-80">
  まるで「数字の探偵」になるようなものです！ 🕵️
</div>

</div>

<!--
今日は難しい数学の話はしません。
皆さんが日常生活で数字と賢く付き合うための「考え方のコツ」、
つまり統計思考を身につけていただきます。
-->

---
layout: section
---

# アイスブレイク統計クイズ

## 頭の体操をしてみましょう！

<!--
本題に入る前に、皆さんの直感がどれくらい正しいか試してみましょう。
-->

---

# クイズ1：モンティ・ホール問題

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="p-4 bg-blue-500 bg-opacity-20 rounded-lg">
    <h3 class="text-lg font-bold mb-2">📋 前提条件</h3>
    <ul class="text-sm space-y-1">
      <li>3つのドアのうち1つに車、2つにヤギが隠されています</li>
      <li>司会者はどのドアに何があるかを知っています</li>
      <li>司会者は必ずヤギのドアを開けます</li>
      <li>あなたの目標は車を当てることです</li>
    </ul>
  </div>
  
  <div class="p-4 bg-blue-500 bg-opacity-20 rounded-lg">
    <p class="text-lg">あなたはドア1を選びました。司会者がドア3を開けてヤギを見せました。</p>
    <p class="text-lg mt-2 font-bold">ドアを変えますか？それとも変えませんか？</p>
  </div>
</div>

<div class="grid grid-cols-3 gap-4 mt-8">
  <div class="bg-gray-300 rounded-lg p-6 text-center">
    <div class="text-5xl mb-3">🚪</div>
    <p>ドア 1</p>
    <div class="text-2xl mt-3">🚗 or 🐐</div>
  </div>
  <div class="bg-gray-300 rounded-lg p-6 text-center">
    <div class="text-5xl mb-3">🚪</div>
    <p>ドア 2</p>
    <div class="text-2xl mt-3">🚗 or 🐐</div>
  </div>
  <div class="bg-gray-300 rounded-lg p-6 text-center">
    <div class="text-5xl mb-3">🚪</div>
    <p>ドア 3</p>
    <p class="text-sm">（司会者が開ける）</p>
    <div class="text-4xl mt-3">🐐</div>
  </div>
</div>

<v-click>

<div class="mt-4 text-center">
  <p class="text-2xl font-bold text-green-400">正解：ドアを変えた方が当たる確率が2倍に！</p>
  <p class="mt-2">最初:1/3 → 変更後:2/3</p>
</div>

</v-click>

<!--
有名なモンティ・ホール問題です。
直感に反しますが、ドアを変えると当たる確率が2倍になるんです。
-->

---

# モンティ・ホール問題の解説

<div class="grid grid-cols-2 gap-8 mt-8">
  <div>
    <h3 class="text-xl mb-4">🎥 詳しい解説動画</h3>
    <iframe 
      width="100%" 
      height="315" 
      src="https://www.youtube.com/embed/1MuwwFipX9o" 
      title="モンティ・ホール問題の詳しい解説" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  </div>
  
  <div class="flex items-center">
    <div class="p-4 bg-blue-500 bg-opacity-20 rounded-lg">
      <h3 class="text-lg font-bold mb-3">なぜ確率が2倍に？</h3>
      <p class="text-base mb-3">この動画で、なぜドアを変えると確率が2倍になるのかを分かりやすく解説しています！</p>
      <div class="mt-3 p-2 bg-yellow-400 bg-opacity-30 rounded">
        <p class="font-bold text-sm">💡 ポイント</p>
        <p class="text-sm font-bold">直感に反する結果の理由を視覚的に理解できます</p>
      </div>
    </div>
  </div>
</div>

<!--
モンティ・ホール問題の詳しい解説動画です。
直感に反する結果の理由を詳しく説明しています。
-->

---

# クイズ2：グラフのトリック

<div class="grid grid-cols-2 gap-8 mt-8">
  <div>
    <h3 class="text-xl mb-4">このグラフを見ると...</h3>
    <div class="bg-gray-200 rounded-lg p-4">
      <img src="./images/misleading_graph_quiz2.png" alt="誤解を招くグラフの例" class="w-full h-auto"/>
    </div>
    <p class="mt-4">売上が2倍以上に急成長！？</p>
  </div>
  
  <div>
    <h3 class="text-xl mb-4">でも実際は...</h3>
    <v-click>
    <div class="bg-red-500 bg-opacity-20 rounded-lg p-6 mt-8">
      <p class="text-2xl font-bold">伸び率はたったの10%</p>
      <p class="mt-4">縦軸が0から始まっていないため、</p>
      <p>変化が誇張されて見えるのです</p>
    </div>
    </v-click>
  </div>
</div>

<!--
グラフの見せ方一つで、同じデータでも全く違う印象を与えることができます。
これが統計リテラシーが必要な理由の一つです。
-->

---

# クイズ3：秘書問題【最適停止問題】

<div class="grid grid-cols-2 gap-8 mt-6">
  <div>
    <h3 class="text-lg font-bold mb-3">📋 問題設定</h3>
    <div class="bg-blue-500 bg-opacity-20 rounded-lg p-4">
      <ul class="text-sm space-y-2">
        <li>100人の候補者から1人の秘書を採用したい</li>
        <li>候補者は1人ずつ順番に面接する</li>
        <li>その場で採用/不採用を決めなければならない</li>
        <li>一度不採用にした人は二度と呼び戻せない</li>
        <li>最優秀の人を採用したい</li>
      </ul>
    </div>
    <div class="mt-4 bg-yellow-400 bg-opacity-20 rounded-lg p-4">
      <p class="font-bold mb-2">🤔 どうすれば最適な人を選べる？</p>
      <p class="text-sm">何人目で決断すべきでしょうか？</p>
    </div>
  </div>
  <div>
    <h3 class="text-lg font-bold mb-3">✨ 統計学的な最適解</h3>
    <v-click>
    <div class="bg-green-500 bg-opacity-20 rounded-lg p-4">
      <p class="text-2xl font-bold text-center mb-4">37%ルール</p>
      <ul class="text-sm space-y-2">
        <li>1. 最初の37人（100人の37%）は見送る</li>
        <li>2. その中で最も優秀だった人を基準とする</li>
        <li>3. 38人目以降で基準を超えたら即採用！</li>
      </ul>
    </div>
    <div class="mt-4 p-3 bg-blue-500 bg-opacity-20 rounded">
      <p class="text-sm font-bold">📊 この戦略の成功確率：約37%</p>
      <p class="text-xs mt-1">数学的に証明された最適戦略です（1/e ≈ 0.368）</p>
    </div>
    <div class="mt-6 text-center">
      <p class="text-base font-bold text-gray-700">💡 日常生活でも応用可能：家探し、転職、パートナー選びなど</p>
    </div>
    </v-click>
  </div>
</div>

---

# 秘書問題の解説

<div class="grid grid-cols-2 gap-8 mt-8">
  <div>
    <h3 class="text-xl mb-4">🎥 詳しい解説動画</h3>
    <iframe 
      width="100%" 
      height="315" 
      src="https://www.youtube.com/embed/hUEtN6-kVqk" 
      title="秘書問題（最適停止問題）の詳しい解説" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  </div>
  
  <div class="flex items-center">
    <div class="p-4 bg-blue-500 bg-opacity-20 rounded-lg">
      <h3 class="text-lg font-bold mb-3">なぜ37%なのか？</h3>
      <p class="text-base mb-3">この動画で、最適停止問題の数学的な背景と、なぜ37%（1/e）が最適解になるのかを分かりやすく解説しています！</p>
      <div class="mt-3 p-2 bg-yellow-400 bg-opacity-30 rounded">
        <p class="font-bold text-sm">💡 ポイント</p>
        <p class="text-sm font-bold">日常生活での応用例も紹介されています</p>
      </div>
    </div>
  </div>
</div>

<!--
秘書問題（最適停止問題）の詳しい解説動画です。
数学的な証明と実生活での応用例を説明しています。
-->

---
layout: center
---

# 統計思考とは？

<div>

<div class="text-3xl mt-8 text-center">
  1つの数字や出来事だけでなく<br/>
  <span class="text-blue-400 font-bold">全体像</span>と<span class="text-green-400 font-bold">つながり</span>を見て<br/>
  物事の本質を探る考え方
</div>

</div>

<div>

<div class="mt-12 grid grid-cols-3 gap-4">
  <div class="bg-white bg-opacity-10 rounded-lg p-6 text-center">
    <div class="text-4xl mb-2">📊</div>
    <p class="font-bold">全体像で見る</p>
    <p class="text-sm mt-2">平均とばらつき</p>
  </div>
  <div class="bg-white bg-opacity-10 rounded-lg p-6 text-center">
    <div class="text-4xl mb-2">🔗</div>
    <p class="font-bold">つながりを見抜く</p>
    <p class="text-sm mt-2">相関と因果</p>
  </div>
  <div class="bg-white bg-opacity-10 rounded-lg p-6 text-center">
    <div class="text-4xl mb-2">🎲</div>
    <p class="font-bold">不確かさを乗りこなす</p>
    <p class="text-sm mt-2">確率と期待値</p>
  </div>
</div>

</div>

<!--
統計思考とは、単に数字を見るだけでなく、
その背景にある全体像やつながりを理解する考え方です。
-->

---
layout: section
---

# 神が仕組んだ4つのパターン

## 数字の『カタチ』を知る

<!--
一見、混沌として見えるこの世界。
しかし、その背後には驚くべき秩序が隠されています。
-->

---
layout: two-cols
---

# 1. 自然界の秩序：正規分布

![正規分布グラフ](./images/normal_distribution.png)

### 📐 確率密度関数

<style>
.katex .frac-line {
  border-bottom-width: 0.02em !important;
}
</style>

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

- <span style="font-size: 0.85em;">μ：平均値（分布の中心）　　σ：標準偏差（分布の広がり）</span>

::right::

### ✅ どんなカタチ？
平均値を中心にした、左右対称の美しい釣鐘型（ベルカーブ）

### ✅ 身近な利用例
身長や体重、製品の誤差など

### ✅ 作られた歴史
天体の位置を観測する際の「誤差」の研究から体系化されました。まるで、**この宇宙に存在するあらゆる『誤差』や『ズレ』でさえも、創造主が定めた美しい法則に従っている**かのような発見でした。偏差値の考え方もここから生まれています。

> 宇宙に存在するあらゆる『誤差』や『ズレ』でさえも、創造主が定めた美しい法則に従っている

<!--
正規分布は、自然界で最も頻繁に現れる分布です。
平均値を中心に左右対称な美しい形をしています。
-->

---
layout: two-cols
---

# 2. 運命の選択：二項分布

![二項分布グラフ](./images/binomial_distribution.png)

### 📐 確率質量関数

<style>
.katex .frac-line {
  border-bottom-width: 0.02em !important;
}
</style>

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

- n：試行回数　　p：成功確率　　k：成功回数

::right::

### ✅ どんなカタチ？
「成功か失敗か」の2択を繰り返したときの結果の分布

### ✅ 身近な利用例
コイン投げ、シュートの成功回数、品質管理

### ✅ 作られた歴史
サイコロ賭博の勝敗確率の研究から生まれました。

> 偶然の象徴であるコイン投げの中に、ベルヌーイは神の定めたゲームのルールを垣間見た

<!--
二項分布は、「成功か失敗か」という2択を繰り返したときの結果を表します。
-->

---
layout: two-cols
---

# 3. 摂理のささやき：ポアソン分布

![ポアソン分布グラフ](./images/poisson_distribution.png)

### 📐 確率質量関数

<style>
.katex .frac-line {
  border-bottom-width: 0.02em !important;
}
</style>

<div style="display: flex; align-items: center; justify-content: space-between; gap: 2rem;">
<div>

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$

</div>
<div style="font-size: 0.85em;">
λ：平均発生回数　　e：自然対数の底（≈2.718）　　k：実際の発生回数
</div>
</div>

::right::

### ✅ どんなカタチ？
一定期間に「珍しいこと」が起こる回数の分布

### ✅ 身近な利用例
1日の交通事故の件数、1時間の電話の着信数、お客様の来店数

### ✅ 作られた歴史
当初は「裁判における誤審の数」を推定するために使われました。

> 気まぐれに起こる人の世の出来事にも、実は天の定めた脈拍（リズム）がある

<!--
ポアソン分布は、一定期間に珍しいことが起こる回数を表します。
地震の確率計算にも使われる重要な分布です。
-->


---
layout: two-cols
---

# 4. 富の宿命：対数正規分布

![対数正規分布グラフ](./images/lognormal_distribution.png)

### 📐 確率密度関数

<style>
.katex .frac-line {
  border-bottom-width: 0.02em !important;
}
</style>

$$f(x) = \frac{1}{x\sqrt{2\pi\sigma^2}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}$$

- μ：対数の平均　　σ：対数の標準偏差

::right::

### ✅ どんなカタチ？
大多数が低い値に、一部だけが極端に高い値を持つ、長い裾を引いた形

### ✅ 身近な利用例
個人の所得分布、SNSのフォロワー数、株価

### ✅ 作られた歴史
「成長率は、その時点での大きさに比例する」という法則から導かれます。**富や成功といった人の世の理（ことわり）までもが、あらかじめ定められた普遍的な法則の上に成り立っている**ことを、この分布は静かに物語っています。

### ✅ グラフの2つの曲線
- 🟠 σ = 0.5（あまり歪まない形）
- 🔴 σ = 1.0（より歪む形）
- σが大きいほど『少数が極値を持つ』現象が顕著に

**🔴 赤い曲線（σ = 1.0）の方が格差が大きい**  
より多くの人が低い値に集中し、少数がより極端に高い値を持つ

<!--
対数正規分布は、大多数が低い値に集中し、
一部だけが極端に高い値を持つ分布です。
これが「平均年収」が実感とズレる理由です。
-->

---
layout: section
---

# 実践！日常にひそむ統計思考

## 学んだ知識を使って謎を解き明かそう

<!--
では、学んだ知識を使って、私たちの身の回りにある数字の謎を解き明かしていきましょう！
-->

---
layout: two-cols
---

# ケース1：選挙速報の謎

### 🤔 疑問：なぜ開票0%で「当選確実」？

### 🗳️ 出口調査
投票所での聞き取り調査

### 📊 統計思考の答え：標本調査
- 出口調査で「縮図」を作る
- 偏りのないサンプル選び
- 少数から全体を高精度で推定

> 💡 全員に聞かなくても、上手にサンプルを選べば全体が分かる！

::right::

![母集団と標本の関係](./images/population_sample_venn.png)

<!--
選挙速報で開票率0%なのに当選確実が出る理由は、
統計学の標本調査という技術のおかげです。
ベン図で母集団（全有権者）と標本（出口調査対象者）の関係を視覚的に説明しています。
-->

---
layout: two-cols
---

# 選挙速報の統計データ

![サンプル数と誤差の関係](./images/election_sample_error.png)

::right::

![出口調査 vs 実際の結果](./images/election_poll_vs_actual.png)

<!--
選挙速報で使われる統計データの可視化です。
左：サンプル数と誤差の関係、右：出口調査と実際の結果の比較を示しています。
-->

---

# ケース2：地震確率の真実

### 「南海トラフ地震、30年以内に約26%」の意味

## 計算の仕組み（ポアソン分布）

1. 平均100年に1回発生と仮定
2. 30年間「起きない確率」を計算
3. 約74%（だから起きる確率26%）

## ⚠️ 本当の意味

- 「30年後が危ない」ではなく
- **「今この瞬間から危険」**

## 📝 統計モデルの限界

- 実際の地震には周期性がある
- 統計的思考理解のための簡易例

<div style="position: absolute; right: 100px; top: 200px; text-align: center;">
  <div style="font-size: 120px;">🏚️</div>
  <div style="font-size: 20px; font-weight: bold;">備えあれば憂いなし</div>
  <div style="font-size: 14px;">統計は警告<br/>行動は今すぐ</div>
</div>

<!--
地震の確率は、ポアソン分布を使って計算されています。
-->

---


# ポアソン分布による地震確率の計算

![地震確率計算の仕組み](./images/poisson_calculation_mechanism.png)

### 📊 計算の仕組み

**1 - P(地震なし) = P(地震あり)**

- 左グラフ：ポアソン分布による各発生回数の確率
- 右グラフ：補集合を利用した地震発生確率の計算

<!--
ポアソン分布を使った地震確率計算の仕組みを視覚的に説明。
「起きない確率」から「起きる確率」を求める補集合の関係を図示。
-->

---

# ケース3：生成AIの謎

### ChatGPTはどうやって文章を作る？

## 生成AIの正体
**超巨大な「次の単語予測マシン」**

## Temperature（温度）設定

| 🧊 低い | 🔥 高い |
|---------|---------|
| 確率の高い無難な単語 | 創造的だが不正確も |

<div style="position: absolute; right: 50px; top: 150px; text-align: center; background-color: #f3f4f6; padding: 20px; border-radius: 10px;">
  <div style="margin-bottom: 10px;">「今日の天気は...」</div>
  <div style="margin-bottom: 10px;">
    <span style="background-color: #dbeafe; padding: 5px 10px; margin: 0 5px; border-radius: 5px;">晴れ 45%</span><br/>
    <span style="background-color: #e5e7eb; padding: 5px 10px; margin: 0 5px; border-radius: 5px;">曇り 30%</span><br/>
    <span style="background-color: #e5e7eb; padding: 5px 10px; margin: 0 5px; border-radius: 5px;">雨 25%</span>
  </div>
  <div style="font-size: 48px;">🤖</div>
  <div>次の単語を確率で選択</div>
</div>

<!--
生成AIは、実は統計モデルそのものです。
-->

---

<div class="mt-2">

# Temperature設定による創造性の制御

</div>

<div class="mt-8">

![Temperature設定の仕組み](./images/temperature_creativity_mechanism.png)

</div>

---

# ケース3：生成AIと統計の関係

<div class="mt-12 p-8 bg-yellow-500 bg-opacity-20 rounded-lg">
  <p class="text-2xl font-bold text-center">
    生成AIは統計と確率の塊！
  </p>
  <p class="text-xl mt-4 text-center">
    「もっともらしい」≠「正しい」
  </p>
</div>

<div class="mt-8 text-center">
  <p class="text-lg">生成AIは膨大なデータから</p>
  <p class="text-lg">「次に来そうな単語」を確率的に予測</p>
  <p class="text-xl mt-4 font-bold">だから時々ウソをつく！</p>
</div>

<!--
膨大なデータから「次に来そうな単語」を確率的に予測しているだけなんです。
-->

---

# ケース4：期待値の謎

### 「平均的に得をする」という魔法の数字

## 🎯 期待値が考え出された背景

- **17世紀のギャンブル問題**から誕生
- パスカルとフェルマーが「公平な分配」を数学的に解決
- 「運」を「数学」で予測する革命的アイデア

## 🎲 期待値の目的

- **未来の結果を予測**：完全ではないが「傾向」がわかる
- **リスクと利益のバランス**：投資や保険の基本概念
- **公平性の判断基準**：ゲームやクジが「フェア」かどうか

---
layout: two-cols
---

# 期待値の実際の利用シーン

## 💼 ビジネス・投資
- **株式投資**：将来のリターン予測
- **保険**：保険料の計算基準
- **マーケティング**：キャンペーンの効果予測

## 🎮 日常生活
- **宝くじ**：「期待値マイナス」だから胴元が儲かる
- **ガチャ**：スマホゲームの排出率
- **スポーツくじ**：「投資」か「娯楽」かの判断

## 🏥 医療・科学
- **治療効果**：新薬の効果予測
- **リスク評価**：副作用の発生確率

::right::

<div class="flex items-center justify-center h-full">
  <img src="./images/Expected_value.jpg" alt="期待値の実践的応用分野" class="w-full max-w-lg object-contain" />
</div>

---

# 期待値の計算方法

## 🧮 基本の公式

**期待値 = Σ(各結果の値 × その確率)**

## 📊 具体例：コイン投げゲーム

<div class="grid grid-cols-2 gap-8 mt-6">
  <div>
    <h3 class="text-lg font-bold mb-4">ゲームのルール</h3>
    <ul class="text-sm space-y-2">
      <li>• 参加費：100円</li>
      <li>• 表が出たら：200円もらえる</li>
      <li>• 裏が出たら：0円</li>
      <li>• 各面の確率：50%</li>
    </ul>
  </div>
  
  <div>
    <h3 class="text-lg font-bold mb-4">期待値の計算</h3>
    <div class="text-sm space-y-2">
      <p>期待収入 = 200円×0.5 + 0円×0.5 = 100円</p>
      <p>期待利益 = 100円 - 100円 = <span class="font-bold text-green-600">0円</span></p>
      <p class="mt-4 font-bold">→ フェアなゲーム！</p>
    </div>
  </div>
</div>

## ⚠️ 期待値の落とし穴

- **「平均的に」は「必ず」ではない**
- **短期では大きくブレる可能性**
- **感情的な判断を数字で補強**

---

# 日本のギャンブル期待値ランキング

### 🎰 統計思考で見る「お得度」比較

<div class="mb-6 text-center">
  <a href="https://docs.google.com/document/d/1jfXmAFdNSUs96jsvNL3PZhwN0Bnn3yqz2mG-Ekam3es/edit?usp=sharing" target="_blank" class="text-blue-600 hover:text-blue-800 underline text-lg font-bold">
    📊 日本のギャンブルにおける期待値の分析レポート：洗練されたプレイヤーのための包括的ガイド
  </a>
</div>

<div class="mt-8">

| 順位 | ギャンブル種別 | 期待値 | 特徴 | 💡 ポイント |
|:---:|:---|:---:|:---|:---|
| 🥇 | **パチンコ・パチスロ** | <span class="text-green-600 font-bold">85～115%</span> | 設定次第で100%超も可能 | スキル＋情報戦 |
| 🥈 | **競馬** | <span class="text-yellow-600 font-bold">70～80%</span> | 券種により変動 | 知識が活かせる |
| 🥉 | **競輪・競艇** | <span class="text-yellow-600 font-bold">約75%</span> | 一律の還元率 | 予測スキルが重要 |
| 4位 | **オートレース** | <span class="text-orange-600 font-bold">約70%</span> | キャンペーンで改善 | プロモーション狙い |
| 5位 | **スポーツくじ** | <span class="text-red-600 font-bold">約50%</span> | 純粋な運勝負 | 娯楽として割り切り |
| 6位 | **宝くじ** | <span class="text-red-600 font-bold">約46%</span> | 最も低い還元率 | 「夢代」として考える |

</div>

<!--
各ギャンブルの期待値を比較することで、統計的に「お得」な選択が見えてきます。
参考資料：https://docs.google.com/document/d/1jfXmAFdNSUs96jsvNL3PZhwN0Bnn3yqz2mG-Ekam3es/edit?usp=sharing
-->

---

# ギャンブル期待値の統計思考

### 🔍 統計思考のポイント

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="bg-green-500 bg-opacity-20 rounded-lg p-4">
    <h4 class="font-bold mb-2">✅ プラス期待値の可能性</h4>
    <p class="text-sm">パチンコ・パチスロのみ100%超が理論上可能</p>
    <p class="text-xs mt-1">※高設定台の見極めとスキルが必要</p>
  </div>
  
  <div class="bg-yellow-500 bg-opacity-20 rounded-lg p-4">
    <h4 class="font-bold mb-2">⚖️ スキルの影響度</h4>
    <p class="text-sm">公営競技：知識と分析力で差がつく</p>
    <p class="text-xs mt-1">宝くじ：スキル無関係の純粋な運</p>
  </div>
</div>

### 💭 期待値から見た選択指針

<div class="mt-8 space-y-4">
  <div class="bg-blue-500 bg-opacity-20 rounded-lg p-4">
    <h4 class="font-bold mb-2">💰 投資思考</h4>
    <p class="text-sm">パチスロ（情報収集＋技術習得が前提）</p>
    <p class="text-xs mt-1">理論上プラス期待値だが、高度なスキルと時間投資が必要</p>
  </div>
  
  <div class="bg-purple-500 bg-opacity-20 rounded-lg p-4">
    <h4 class="font-bold mb-2">🏇 趣味・娯楽</h4>
    <p class="text-sm">競馬・競輪（スポーツ知識を活かす）</p>
    <p class="text-xs mt-1">知識と分析力で楽しみながら期待値改善の可能性</p>
  </div>
  
  <div class="bg-orange-500 bg-opacity-20 rounded-lg p-4">
    <h4 class="font-bold mb-2">✨ 夢購入</h4>
    <p class="text-sm">宝くじ（エンターテインメント料54%を承知の上で）</p>
    <p class="text-xs mt-1">統計的には不利だが、夢を買う娯楽として割り切る</p>
  </div>
</div>

### 🎯 統計思考の結論

<div class="mt-8 p-6 bg-gray-500 bg-opacity-20 rounded-lg border-2 border-gray-400">
  <p class="text-lg font-bold text-center mb-2">期待値は選択の指針であり、絶対的な答えではない</p>
  <p class="text-center">目的と価値観に合った「賢い選択」を統計思考で支援する</p>
</div>

<!--
期待値の比較を通じて、統計思考による意思決定の重要性を理解できます。
数字だけでなく、個人の目的や価値観も考慮した総合的な判断が大切です。
-->

---
layout: section
---

# 演習：統計の罠を見抜こう！

## 実際のニュースやグラフから問題点を探す

<!--
それでは、実際のニュースやグラフを見て、
統計的な問題点を見つける練習をしてみましょう。
-->

---

# 演習1：誤解を招くグラフ

### このグラフの問題点は？

<div class="grid grid-cols-2 gap-8">
  <div>
    <img src="./images/misleading_graph_exercise1_clean.png" alt="誤解を招く企業比較グラフ" style="width: 100%; height: auto;"/>
  </div>
  
  <div>
    
### 見つけるべきポイント
- 縦軸は0から始まっている？
- 目盛りの間隔は一定？
- 比較対象は公平？

### 正しい表示方法
必ず0から始め、一定の目盛りで表示する
    
  </div>
</div>


<!--
グラフを見るときは、まず軸の設定を確認しましょう。
これだけで多くのトリックを見抜けます。
-->

---

# 演習2：相関と因果の混同

### ニュース記事の例
「アイスクリームの売上が増えると、溺死事故が増加」

![相関と因果の関係を示すグラフ](./images/correlation_causation_graph.png)

<!--
相関関係があっても因果関係があるとは限りません。
-->

---

# 演習2：相関と因果の解釈

<div class="mt-12 p-8 bg-orange-500 bg-opacity-20 rounded-lg">
  <h3 class="text-2xl font-bold text-center mb-4">真の原因：夏（気温）🌞</h3>
  <p class="text-xl text-center">両方に影響を与える第3の要因を探そう！</p>
</div>

<div class="mt-8 text-center">
  <p class="text-lg">アイスクリーム売上 ← 気温 → 水遊び機会増加</p>
  <p class="text-lg mt-4 font-bold">直接の因果関係はない！</p>
</div>

<!--
第3の要因が両方に影響していることがよくあります。
-->

---

# 演習3：サンプルバイアス

### アンケート結果の例
「インターネット調査：スマホ利用率95%」

![サンプルバイアスの比較グラフ](./images/sample_bias_graph.png)

<!--
調査方法によって結果が大きく変わることがあります。
-->

---

# 演習3：バイアスの原因

### 🔍 問題点の分析

<div class="mt-8 space-y-4">
  <div class="bg-red-500 bg-opacity-20 rounded-lg p-4">
    <p class="text-lg font-bold">📱 ネット調査 → ネット利用者のみ</p>
    <p class="text-sm mt-2">調査手段が対象を限定してしまう</p>
  </div>
  
  <div class="bg-orange-500 bg-opacity-20 rounded-lg p-4">
    <p class="text-lg font-bold">👴 高齢者の意見が反映されない</p>
    <p class="text-sm mt-2">重要な層が調査から除外される</p>
  </div>
  
  <div class="bg-yellow-500 bg-opacity-20 rounded-lg p-4">
    <p class="text-lg font-bold">💻 デジタルデバイドの無視</p>
    <p class="text-sm mt-2">技術格差が結果を歪める</p>
  </div>
</div>

---

# 🚨 サンプルバイアスを撃退せよ！

<div class="mt-6 p-8 bg-red-500 bg-opacity-20 rounded-lg border-2 border-red-400">
  <h3 class="text-2xl font-bold text-center mb-6">⚡ バイアス・バスター作戦 ⚡</h3>
  <div class="grid grid-cols-3 gap-4">
    <div class="bg-white bg-opacity-50 rounded-lg p-4 text-center">
      <div class="text-3xl mb-2">🎯</div>
      <p class="font-bold text-sm">多角的攻撃</p>
      <p class="text-xs">複数の調査方法を併用</p>
    </div>
    <div class="bg-white bg-opacity-50 rounded-lg p-4 text-center">
      <div class="text-3xl mb-2">⚖️</div>
      <p class="font-bold text-sm">バランス調整</p>
      <p class="text-xs">年齢層別の重み付け</p>
    </div>
    <div class="bg-white bg-opacity-50 rounded-lg p-4 text-center">
      <div class="text-3xl mb-2">📋</div>
      <p class="font-bold text-sm">透明性確保</p>
      <p class="text-xs">調査方法の明記</p>
    </div>
  </div>
</div>

<div class="mt-4 p-6 bg-yellow-400 bg-opacity-30 rounded-lg">
  <p class="text-lg font-bold text-center">🔍 探偵の基本ルール 🔍</p>
  <p class="text-base text-center mt-2">「誰に、どうやって聞いたか」を必ずチェック！</p>
  <p class="text-center mt-2 font-bold text-red-600 text-xl">これがバイアス発見の鍵 🗝️</p>
</div>

<!--
誰に、どうやって聞いたかを必ず確認しましょう。
-->

---
layout: center
---

# 📚 おすすめ書籍

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="text-center">
    <div class="mb-4">
      <a href="https://www.amazon.co.jp/%E7%B5%B1%E8%A8%88%E5%AD%A6%E3%81%8C%E6%9C%80%E5%BC%B7%E3%81%AE%E5%AD%A6%E5%95%8F%E3%81%A7%E3%81%82%E3%82%8B-%E8%A5%BF%E5%86%85-%E5%95%93/dp/4478022216" target="_blank">
        <img src="./images/71YpaI60-+L._SL1500_.jpg" alt="統計学が最強の学問である" class="w-48 h-64 mx-auto object-cover rounded shadow-lg hover:shadow-xl transition-shadow cursor-pointer">
      </a>
    </div>
    <p class="text-sm">統計学の実践的な活用法を<br/>分かりやすく解説した名著</p>
  </div>
  
  <div class="text-center">
    <div class="mb-4">
      <a href="https://www.amazon.co.jp/%E7%B5%B1%E8%A8%88%E5%AD%A6%E3%82%92%E6%8B%93%E3%81%84%E3%81%9F%E7%95%B0%E6%89%8D%E3%81%9F%E3%81%A1-%E6%97%A5%E7%B5%8C%E3%83%93%E3%82%B8%E3%83%8D%E3%82%B9%E4%BA%BA%E6%96%87%E5%BA%AB-%E3%83%87%E3%82%A4%E3%83%B4%E3%82%A3%E3%83%83%E3%83%89%E3%83%BB%E3%82%B5%E3%83%AB%E3%83%84%E3%83%96%E3%83%AB%E3%82%B0/dp/453219539X" target="_blank">
        <img src="./images/41CZJVfVY0L.jpg" alt="統計学を拓いた異才たち" class="w-48 h-64 mx-auto object-cover rounded shadow-lg hover:shadow-xl transition-shadow cursor-pointer">
      </a>
    </div>
    <p class="text-sm">統計学の歴史と変人たちの<br/>エピソードを楽しく学べる</p>
  </div>
</div>

<div class="mt-8 text-center">
  <p class="text-lg">📖 統計の世界への扉を開こう</p>
</div>

---
layout: center
---

# まとめ：統計思考を「一生モノの武器」に

<div class="text-xl mt-6 space-y-3">
  <p>✅ 数字を見たら「それって、ほんま？」と疑う</p>
  <p>✅ 数字の裏にある「カタチ」や「見せ方」に注意</p>
  <p>✅ 「一部」から「全体」を推測する技術を理解</p>
  <p>✅ 生成AIも統計と確率の産物と認識</p>
</div>

<!--
統計思考は、皆さんの日常生活を豊かにする道具です。
-->

---
layout: center
---

# 統計思考は数字の探偵術

<div class="mt-8 p-8 bg-blue-500 bg-opacity-20 rounded-lg">
  <p class="text-2xl text-center font-bold">
    難しい数学ではありません
  </p>
  <p class="text-xl text-center mt-4">
    世界をより「解像度高く」見るための<br/>
    面白くて役に立つ視点です
  </p>
</div>

<div class="mt-8 text-center">
  <p class="text-lg">今日学んだことを、ぜひ明日から実践してみてください</p>
</div>

<!--
今日学んだことを、ぜひ明日から実践してみてください。
-->

---
layout: end
class: text-center
---

# 🎉 ミッション・コンプリート！

<div class="mt-2 grid grid-cols-3 gap-4">
  <div class="bg-red-500 bg-opacity-20 rounded-lg p-4 text-center">
    <div class="text-4xl mb-2">🕵️</div>
    <p class="font-bold">数字の探偵</p>
    <p class="text-sm">レベルアップ！</p>
  </div>
  <div class="bg-green-500 bg-opacity-20 rounded-lg p-4 text-center">
    <div class="text-4xl mb-2">🛡️</div>
    <p class="font-bold">統計の盾</p>
    <p class="text-sm">装備完了！</p>
  </div>
  <div class="bg-blue-500 bg-opacity-20 rounded-lg p-4 text-center">
    <div class="text-4xl mb-2">⚔️</div>
    <p class="font-bold">疑問の剣</p>
    <p class="text-sm">習得済み！</p>
  </div>
</div>

<div class="mt-8 p-6 bg-gradient-to-r from-purple-500 to-pink-500 bg-opacity-20 rounded-lg">
  <p class="text-2xl font-bold text-center">🌟 今日から君も統計マスター！ 🌟</p>
  <p class="text-lg text-center mt-2">世界をより鋭く見抜く力を手に入れました</p>
</div>

<div class="mt-6 p-4 bg-yellow-400 bg-opacity-30 rounded-lg animate-pulse">
  <p class="text-xl font-bold text-center">🎤 質疑応答タイム 🎤</p>
  <p class="text-center mt-1">何でも聞いちゃってください！</p>
</div>

<!--
ご清聴ありがとうございました。
何か質問がございましたら、お気軽にどうぞ。
-->