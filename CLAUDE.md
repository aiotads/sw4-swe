# 專案：《Software Engineering at Google》研究閱讀系統

把整本《Software Engineering at Google》（602 頁、25 章、5 大部分）逐章轉成
**中英並陳的研究筆記（Markdown）＋ 精簡靜態 HTML 視覺化**，最後用一份
`docs/index.html` 串連全部。產出供 **L4~L6 軟體工程師**精讀。

## 工作流程
**續做進度看 `PROGRESS.md`**（單一事實來源，跨 session 記憶）——新 session 開工先讀它的
「▶ 下一步」，完成一章後依 SKILL 規定更新它 + 本檔 + `docs/index.html`。

所有章節的產出與修訂都走 **`swe-research` SKILL**（見
`.claude/skills/swe-research/SKILL.md`）。該 SKILL 規範「方法」（五階段流程、
七段結構、品質守則）；本檔規範「事實與規格」（全書主軸、章節清單、檔案結構、
HTML 主題）。動工任一章前先讀 SKILL。

## 全書三大主軸（每章都要回扣）
這本書的論點全部圍繞三條主軸，視覺化用固定配色標記：

| 主軸 | 一句話 | 配色變數 |
|---|---|---|
| **Time / 時間** | 軟體工程是「整合了時間維度的程式設計」，程式碼有預期壽命，必須能因應變化。 | `--theme-time`（琥珀） |
| **Scale / 規模** | 組織與程式碼長大時，每件重複做的事都要次線性擴展，否則撐不住。 | `--theme-scale`（青藍） |
| **Trade-offs / 取捨** | 工程決策是在不完美資訊下權衡成本；要有理由，不能「因為我說了算」。 | `--theme-trade`（紫紅） |

書的核心金句：**"Software engineering is programming integrated over time."**

## 章節清單（PDF 頁碼）
原文已切到 `chapters/raw/chNN.txt`。

**Part I — Thesis**
- ch01 What Is Software Engineering?（什麼是軟體工程）p31–52

**Part II — Culture / 文化**
- ch02 How to Work Well on Teams（如何在團隊裡好好合作）p55–70
- ch03 Knowledge Sharing（知識分享）p71–96
- ch04 Engineering for Equity（為公平而工程）p97–108
- ch05 How to Lead a Team（如何領導團隊）p109–134
- ch06 Leading at Scale（規模化的領導）p135–150
- ch07 Measuring Engineering Productivity（衡量工程生產力）p151–166

**Part III — Processes / 流程**
- ch08 Style Guides and Rules（風格規範與規則）p169–192
- ch09 Code Review（程式碼審查）p193–212
- ch10 Documentation（文件）p213–234
- ch11 Testing Overview（測試總覽）p235–258
- ch12 Unit Testing（單元測試）p259–284
- ch13 Test Doubles（測試替身）p285–308
- ch14 Larger Testing（大型測試）p309–338
- ch15 Deprecation（棄用）p339–352

**Part IV — Tools / 工具**
- ch16 Version Control and Branch Management（版本控制與分支管理）p355–378
- ch17 Code Search（程式碼搜尋）p379–398
- ch18 Build Systems and Build Philosophy（建置系統與建置哲學）p399–426
- ch19 Critique: Google's Code Review Tool（Critique：Google 的審查工具）p427–444
- ch20 Static Analysis（靜態分析）p445–456
- ch21 Dependency Management（依賴管理）p457–486
- ch22 Large-Scale Changes（大規模變更）p487–506
- ch23 Continuous Integration（持續整合）p507–532
- ch24 Continuous Delivery（持續交付）p533–544
- ch25 Compute as a Service（運算即服務）p545–574

**Part V — Conclusion** — Afterword（後記，不單獨成章）

## 檔案結構
```
d:\ah\swe\
├── CLAUDE.md                              ← 本檔
├── .claude/skills/swe-research/SKILL.md   ← 研究流程技能
├── swe_at_google.2.pdf                    ← 原始書
├── chapters/
│   ├── raw/chNN.txt                       ← 切好的原文（資料來源）
│   ├── chNN.md                            ← 成品：繁中研究筆記
│   └── chNN.en.md                         ← 成品：英文研究筆記（English-to-English）
└── docs/                                  ← GitHub Pages 發佈來源（Pages source = /docs）
    ├── index.html                         ← 總索引（依 5 大 Part 分組）
    ├── chNN.html                          ← 成品：各章視覺化
    └── assets/style.css                   ← 共用主題（HTML 內嵌或外連皆可）
```

## HTML 主題規格（全書一致）
- **精簡靜態**：每個 `chNN.html` 自包含、內嵌 `<style>`、**無 JavaScript、無外部 CDN**。
- 深色學術風。共用 CSS 變數（以 ch01.html 為基準模板，後續章節沿用）：
  - 背景 `--bg:#0f1117`、卡片 `--card:#171a23`、文字 `--fg:#e6e9f0`、次要 `--muted:#9aa3b2`
  - 強調 `--accent:#5b9dd9`、邊框 `--border:#262b38`
  - 三主軸：`--theme-time:#e0a23b`、`--theme-scale:#3bb8c4`、`--theme-trade:#c45b9d`
- 字體：系統無襯線 + 等寬字用於程式碼/英文金句。最大內容寬度約 860px、置中、行高 1.75。
- 每章頁尾固定導航：`← 上一章 ｜ 總索引 ｜ 下一章 →`（首末章對應端點留空或回索引）。
- **導航之後固定 colophon**（`<footer class="colophon">`，全書一致、恆顯示）：①原書出處＋
  授權（改寫自《Software Engineering at Google》，© Google, LLC，`CC BY-NC-ND 4.0`，連 abseil 官方版）；
  ②製作署名 `© 2026 Allen Huang`＋「僅供學習研究、非商業、非官方產物」。沿用 ch01 的 `.colophon` CSS。
  `index.html` 頁尾比照（中英兩版皆含出處＋授權＋署名）。詳見 SKILL。
- 中英並陳金句用 `blockquote`：英文在上（等寬、次要色），繁中在下（正文色、較大）。
- **圖**：概念圖/流程圖一律 inline SVG 在深色主題重繪（用三主軸配色），包進
  `<figure>`＋`<figcaption>`（標 `Figure X-Y` 與繁中圖說）；產品 UI 截圖抽原圖
  base64 內嵌於 `<details>` 收合區。詳見 SKILL「圖的處理」。先跑 `_figs.py` 盤點該章圖。

## 排版與語言守則（摘要，詳見 SKILL）
- 繁體中文輸出；技術名詞/制度名保留英文，首次附中譯。
- 諺語與比喻譯「神」不譯「字」，必要時加文化註解；原文核心主張不得失真。
- 碩士級敘事，避免太淺（名詞解釋）與太深（學術黑話）。
- 檔案路徑引用一律相對於專案根目錄。

## 進度
- [x] 環境：PyMuPDF 已裝；`_extract.py`/`_slice.py`/`_figs.py` 可重跑擷取、切章、盤點圖。
- [x] SKILL 與 CLAUDE.md 建立（含圖政策、中／英雙語切換政策）。
- [x] ch01 完成（雙語 md+html，含 Fig 1-1／1-2 inline SVG）。
- [x] ch02 完成（雙語 md+html，含 HRT 三支柱 SVG）。
- [x] ch03 完成（雙語 md+html，含自製「知識分享擴展光譜」概念 SVG）。
- [x] ch04 完成（雙語 md+html，含自製「偏見惡性循環」概念 SVG）。
- [x] ch05 完成（雙語 md+html，含自製「激勵×方向 2×2」概念 SVG）。
- [x] ch06 完成（雙語 md+html，inline SVG 重繪 Fig 6-1 取捨三角、Fig 6-2 成功螺旋）。
- [x] ch07 完成（雙語 md+html，含自製 GSM 三層／QUANTS 五面向 SVG）；**Part II 文化篇 ch02–07 完成**。
- [x] ch08 完成（雙語 md+html，含自製「一致性階層／執行光譜」SVG）；**進入 Part III 流程篇**。
- [x] ch09 完成（雙語 md+html，含自製「六步審查流程／三個批准位元」SVG）；正確性非首要效益、程式碼是負債。
- [x] ch10 完成（雙語 md+html，含自製「文件像程式碼／完整-準確-清晰三角」SVG）；為讀者最佳化、GooWiki 崩壞。
- [x] ch11 完成（雙語 md+html，inline SVG 重繪 Fig 11-2 巢狀 size／11-3·11-4 金字塔+反模式）；測試支撐改變、size vs scope、Beyoncé Rule。
- [x] ch12 完成（雙語 md+html，含自製「四種變更矩陣／行為非方法」SVG）；unchanging tests、public API、state not interactions、DAMP not DRY。
- [x] ch13 完成（雙語 md+html，含自製「seam/DI／偏好序」SVG）；classical vs mockist、prefer realism、fake+contract test、@DoNotMock。
- [x] ch14 完成（雙語 md+html，含 Fig 14-1 保真度光譜／自製大型測試結構 SVG）；fidelity 首要、SUT 形態、config 故障頭號、A/B diff、十種大型測試。
- [x] ch15 完成（雙語 md+html，含自製「advisory↔compulsory／三類工具」SVG）；程式碼是負債、hope is not a strategy、為除役而設計。**Part III 流程篇 ch08–15 完成**。
- [x] ch16 完成（雙語 md+html，含自製「trunk vs dev branch／One-Version」SVG）；**進入 Part IV 工具篇**；Source of Truth、trunk-based、Piper/monorepo、VMR。
- [x] ch17 完成（雙語 md+html，含自製「五意圖／雙索引」SVG；UI 截圖依 CC BY-NC-ND 改 details 文字描述、不重製）；集中式索引、延遲換算工程時間、sparse n-gram。
- [x] ch18 完成（雙語 md+html，含自製「task vs artifact／分散式建置」SVG）；Fast&Correct、限制彈性提升生產力、Bazel、ObjFS/Forge、One-Version。
- [x] ch19 完成（雙語 md+html，含自製「六階段流程／三件式評分」SVG；UI 截圖依 CC BY-NC-ND 改 details 描述）；Simplicity、信任的地基、attention set、GwsQ。
- [x] ch20 完成（雙語 md+html，含自製「三教訓／工作流整合點」SVG）；effective false positive、開發者幸福、Tricorder、per-project 客製、不發 compiler warning。
- [x] ch21 完成（雙語 md+html，含 Fig 21-1 鑽石依賴／自製四模型 SVG）；寧可版本控制問題、SemVer over/under-constrain、MVS、Live at Head、匯出依賴。
- [x] ch22 完成（雙語 md+html，含自製「原子上限縮小→Rosie 分片／TAP train 五步」SVG）；最大原子變更反而縮小、No Haunted Graveyards＝測試、unfunded mandate、cattle vs pets、四階段流程＋全域核准者、scoped_ptr→unique_ptr／RoseHub。
- [x] ch23 完成（雙語 md+html，含重繪 Fig23-1/2「變更一生/shift left」／自製「TAP 持續測試管線＋Build Cop 回退」SVG）；CI v2、快速回饋迴圈、CB true/green head、CD/RC（設定一起測）、presubmit vs post-submit、mid-air collision、CI is alerting、hermetic/record-replay、TAP/Build Cop/culprit finding、Takeout 四幕、「成本左移」。
- [x] ch24 完成（雙語 md+html，含自製「faster is safer 小/大批次」／「旗標守護＋發布列車」SVG）；CD/Agile「小批次→高品質」、velocity 是團隊運動、別放慢而要投資架構、flag-guarding 解耦、release train、沒有完美 binary、ship only what's used、A/B 部署、Always Be Deploying、保護產品不受開發者傷害。
- [x] ch25 完成（雙語 md+html，含自製「管理運算光譜：寵物→VM→容器牛→serverless」／「Borg batch 填 serving slack」SVG）；CaaS、cattle vs pets、雜務自動化→自動排程→容器化→rightsizing、為失敗而設計、batch vs serving、管理狀態、service discovery/idempotency、容器作為抽象、Hyrum's Law（PID 32,000）、One Service to Rule Them All、serverless 取捨、lock-in。
- [x] **🎉 全書 25 章雙語化全部完成（25/25、進度條 100%）；五大 Part 皆涵蓋。** index.html 標記全書完成。
- [ ]（選用收尾）Afterword 全書回顧文字、全書一致性校對、GitHub Pages 發佈確認。
