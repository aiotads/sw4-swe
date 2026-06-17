# PROGRESS — SWE@Google 研讀進度帳本（單一事實來源）

> 本檔是跨 session 的進度記憶。**每個新 session 開工前先讀本檔**，找到「下一章」續做；
> **每完成一章，立即更新本檔 + `CLAUDE.md` 進度 + `docs/index.html` 卡片狀態與進度條**。
> 產出規格見 `.claude/skills/swe-research/SKILL.md`（五階段 + 圖政策 + 中英雙語）。

## ▶ 下一步（NEXT UP）
- **🎉🎉 專案完成。全書 25 章雙語化 + Afterword 全書回顧皆已交付。**
- 已完成的收尾：① **Afterword（Part V）全書回顧**——index.html 中英兩版皆以 `.afterword` 區塊呈現：回到核心命題、三主軸（Time/Scale/Trade-offs）對應章節、五大 Part 即一個論證的五段、Hyrum's Law 暗線、收束於「能力是練出來的習慣」（取代原本 inert placeholder）。② **全書一致性校對通過**：`ch-card todo` = 0、所有 chNN.html 內部跨章連結皆可解析（無 MISSING）、25 章 colophon 齊全。
- 唯一仍待人工確認者：**GitHub Pages 發佈**（Pages source = /docs；需在 repo 設定啟用、非本機可驗證）。
- 若需再加值：可考慮各章 md 內 `[[chNN]]` 心智連結轉成 html 實連結、或加全書術語表頁，但非必要。

## 狀態圖例
- ✅ 完成　🚧 進行中　⬜ 未開始
- 欄位：MD（繁中筆記）｜EN（英文筆記）｜HTML（雙語視覺化）｜IDX（index 卡片已標完成）

## 進度總表（25 / 25 章完成 ✓ 全書完成）

| Ch | 章名 | Part | MD | EN | HTML | IDX | 圖 | 備註 |
|----|------|------|----|----|------|-----|----|------|
| 01 | What Is Software Engineering? | I Thesis | ✅ | ✅ | ✅ | ✅ | Fig1-1,1-2 SVG | 試點，全書模板基準 |
| 02 | How to Work Well on Teams | II Culture | ✅ | ✅ | ✅ | ✅ | HRT 三支柱 SVG | 無原書圖，自製概念圖 |
| 03 | Knowledge Sharing | II Culture | ✅ | ✅ | ✅ | ✅ | 自製：知識分享擴展光譜 SVG | 心理安全感 + readability |
| 04 | Engineering for Equity | II Culture | ✅ | ✅ | ✅ | ✅ | 自製：偏見惡性循環 SVG | bias is the default |
| 05 | How to Lead a Team | II Culture | ✅ | ✅ | ✅ | ✅ | 自製：激勵×方向 2×2 SVG | servant leadership／無正式圖 |
| 06 | Leading at Scale | II Culture | ✅ | ✅ | ✅ | ✅ | Fig6-1 三角／6-2 螺旋 SVG | 三個 Always |
| 07 | Measuring Engineering Productivity | II Culture | ✅ | ✅ | ✅ | ✅ | 自製：GSM 三層／QUANTS 五面向 SVG | 收束 readability 線 |
| 08 | Style Guides and Rules | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：一致性階層／執行光譜 SVG | Part III 起點 |
| 09 | Code Review | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：六步審查流程／三個批准位元 SVG | 無原書圖 |
| 10 | Documentation | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：文件像程式碼／完整-準確-清晰三角 SVG | 無原書圖 |
| 11 | Testing Overview | III Processes | ✅ | ✅ | ✅ | ✅ | Fig11-2 巢狀 size／11-3·11-4 金字塔+反模式 SVG | 測試金字塔 |
| 12 | Unit Testing | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：四種變更矩陣／行為非方法 SVG | DAMP vs DRY |
| 13 | Test Doubles | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：seam/DI／偏好序 SVG | fake/stub/mock |
| 14 | Larger Testing | III Processes | ✅ | ✅ | ✅ | ✅ | Fig14-1 保真度光譜／自製大型測試結構 SVG | SUT/fidelity |
| 15 | Deprecation | III Processes | ✅ | ✅ | ✅ | ✅ | 自製：advisory↔compulsory／三類工具 SVG | Part III 完成 |
| 16 | Version Control and Branch Management | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：trunk vs dev branch／One-Version SVG | monorepo |
| 17 | Code Search | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：五意圖／雙索引 SVG＋UI 圖 details 描述 | UI 圖不重製、改自製 |
| 18 | Build Systems and Build Philosophy | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：task vs artifact／分散式建置 SVG | Bazel |
| 19 | Critique: Google's Code Review Tool | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：六階段流程／三件式評分 SVG＋UI 圖 details | UI 圖不重製、改自製 |
| 20 | Static Analysis | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：三教訓／工作流整合點 SVG | Tricorder |
| 21 | Dependency Management | IV Tools | ✅ | ✅ | ✅ | ✅ | Fig21-1 鑽石依賴／四模型 SVG | 鑽石依賴/SemVer |
| 22 | Large-Scale Changes | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：原子上限縮小→Rosie 分片／TAP train 五步 SVG | LSC/cattle vs pets |
| 23 | Continuous Integration | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：變更一生/shift left（重繪 Fig23-1/2）／TAP 持續測試管線 SVG | TAP/Build Cop/hermetic |
| 24 | Continuous Delivery | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：faster is safer 小/大批次／旗標守護＋發布列車 SVG | CD/flag guard |
| 25 | Compute as a Service | IV Tools | ✅ | ✅ | ✅ | ✅ | 自製：管理運算光譜（寵物→VM→容器牛→serverless）／Borg batch 填 serving slack SVG | CaaS｜**全書完成** |
| — | Afterword | V Conclusion | ⬜ | ⬜ | ⬜ | ⬜ | — | 併入全書回顧，不單獨成章 |

## 變更日誌（最新在上）
- 2026-06-17：🎉 **完成 ch25 Compute as a Service 雙語（md+en.md+雙語 html）——全書 25 章全部完成（25/25、進度條 100%）。** 自製兩張概念 SVG（管理運算的光譜：bare-metal 寵物→VM→容器當牛→serverless，抽象漸增/管理 overhead 漸減/控制權漸失；一統天下：Borg 把 batch 填進 serving over-provision 的 70% 閒置容量、serving 一需要就回收、batch 幾乎免費跑）；強調 CaaS 定義、cattle vs pets、雜務自動化→自動排程→容器化多租戶→rightsizing、為失敗而設計、batch vs serving、管理狀態（state replication/快取按延遲配置）、service discovery/idempotency、容器作為抽象、Hyrum's Law（PID 32,000 修八年）、One Service to Rule Them All、serverless 取捨（要真正無狀態、比較對象是持久容器）、公有/多雲/混合雲 lock-in。index 進度 25/25、進度條 100%、標記全書完成。
- 2026-06-17：完成 ch24 Continuous Delivery 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（faster is safer：小批次頻繁 vs 大批次稀疏的風險/除錯對比；旗標守護解耦「功能命運 vs binary 發布」＋規律發布列車＋沒有完美 binary）；強調 CD/Agile 信條「小批次→高品質」、六 idioms、velocity 是團隊運動（在共享 head 開發、YouTube 50h 人工回歸反例）、別放慢而要降成本/提紀律/增量化風險＋投資微服務/重寫、flag-guarding（動態 config、發布前一刻開旗標）、release train（Search 每兩天、菲律賓小島 bug、錯過等下一班）、ship only what's used（bloat/動態部署/A/B）、shift left/把現實當基準（多樣性是事實、A/B 部署、change-neutral）、Always Be Deploying、保護產品不受開發者傷害、「光建好結構就產生大部分價值」。index 進度 24/25、進度條 96%。
- 2026-06-17：完成 ch23 Continuous Integration 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（重繪 Fig 23-1/23-2「一段程式變更的一生」＋bug 成本曲線＋shift left；TAP 持續測試管線 presubmit→post-submit→RC→production probers＋Build Cop 回退迴圈）；強調 CI v2 定義（整個生態系的持續組裝測試）、快速回饋迴圈/可取得可行動、CB（true/green head）、CD/RC（設定要一起測）、presubmit vs post-submit、mid-air collision、version skew、「CI is alerting」、hermetic testing/record-replay、TAP（>50,000 變更·>40 億測試/日·11 分鐘）、culprit finding、Build Cop、Takeout 四幕（沙箱 presubmit 擋 95%/夜間減半、可點連結 −35%、對 prod 跑同套隔離失敗、bug tag 停用＋自動清理 MTTCU）、「我負擔不起 CI＝把成本左移」。index 進度 23/25、進度條 92%。
- 2026-06-17：完成 ch22 Large-Scale Changes 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（左：repo/人數越大原子變更上限越低→右：Rosie 把全域變更切成可獨立提交/回退的碎片；TAP train 五步：抽樣 1000→併車→跑受影響測試聯集→逐一定位元兇→產出可安全提交證據）；強調「最大原子變更反而縮小」「No Haunted Graveyards＝靠測試」「unfunded mandate＝基礎設施團隊負責」「cattle vs pets」「次線性人力/>500 編輯就學工具」「四階段流程＋全域核准者」；案例 scoped_ptr→unique_ptr（>50 萬引用、高峰每天 >700 變更/15,000 檔）、填坑、Operation RoseHub（>50 人手發 >2,600 patch 修 Mad Gadget）。index 進度 22/25、進度條 88%。
- 2026-06-17：完成 ch21 Dependency Management 雙語（md+en.md+雙語 html）；inline SVG 重繪 Fig 21-1（鑽石依賴）＋自製四種模型 SVG（Nothing Changes/SemVer/Bundled/Live at Head）；強調「寧可版本控制問題」、Hyrum's Law、SemVer over/under-constrain、MVS、以測試取代估計、匯出依賴（gflags/AppEngine）。index 進度 21/25、進度條 84%。
- 2026-06-17：完成 ch20 Static Analysis 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（三條關鍵教訓；工作流整合點 IDE→code review→presubmit→compiler，愈左愈早愈右愈強制）；UI 截圖（Fig 20-1/2）依 CC BY-NC-ND 文字描述。強調 effective false positive、開發者幸福、Tricorder 四準則、per-project 客製、從不發 compiler warning。index 進度 20/25、進度條 80%。
- 2026-06-17：完成 ch19 Critique 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（六階段審查流程；三件式評分 LGTM＋Approval＋unresolved）；UI 截圖（Fig 19-1~8）依 CC BY-NC-ND 改 `<details>` 文字描述、不重製。強調 Simplicity（放棄 Code Central）、信任的地基、attention set、GwsQ、緊密整合偏好連結。index 進度 19/25、進度條 76%。
- 2026-06-17：完成 ch18 Build Systems and Build Philosophy 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（task-based vs artifact-based 建置；分散式建置：build master→worker pool→共享遠端快取）；強調 Fast & Correct、限制彈性提升生產力、宣告式 manifest、sandboxing、ObjFS/Forge、1:1:1、strict transitive deps、One-Version、手動釘版本。index 進度 18/25、進度條 72%。
- 2026-06-17：完成 ch17 Code Search 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（五類搜尋意圖 How/What/Where/Why/Who-When 佔比；即時搜尋索引 vs 每日 cross-reference 索引）；UI 截圖（Fig 17-1~4）依 CC BY-NC-ND 改以 `<details>` 文字描述、不重製。強調集中式索引 vs 二次方 IDE 索引、延遲換算工程時間、sparse n-gram、completeness 取捨。index 進度 17/25、進度條 68%。
- 2026-06-17：完成 ch16 Version Control and Branch Management 雙語（md+en.md+雙語 html）；**進入 Part IV 工具篇**；自製兩張概念 SVG（trunk-based vs 長壽 dev branch；One-Version Rule 的 fork 鑽石依賴 vs 唯一版本）；強調 VCS＝管理原始碼×時間、Source of Truth、trunk-based、One-Version、Piper/monorepo、VMR、版本號是時間戳。index 進度 16/25、進度條 64%。
- 2026-06-17：完成 ch15 Deprecation 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（advisory↔compulsory 棄用光譜；棄用工具三類 discovery→migration→backsliding prevention）；強調「程式碼是負債」「老≠過時」「hope is not a strategy」「為除役而設計」「in-place 比替換便宜」「alert fatigue」。**Part III 流程篇 ch08–15 全數完成**。index 進度 15/25、進度條 60%。
- 2026-06-17：完成 ch14 Larger Testing 雙語（md+en.md+雙語 html）；inline SVG 重繪 Fig 14-1（保真度/封閉性光譜：unit→production，兩者直接衝突）＋自製大型測試結構 SVG（取得 SUT→植入資料→執行動作→驗證；驗證三法）；強調 fidelity 首要、單元測試五缺口（config 是重大故障頭號原因/2013 全球當機）、SUT 形態、A/B diff 最常見、Dapper/OWNERS、十種大型測試。index 進度 14/25、進度條 56%。
- 2026-06-17：完成 ch13 Test Doubles 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（seam/依賴注入：production 傳真實、test 傳替身經同一建構子；偏好序：真實＞fake＞stub/interaction＋三準則執行時間/確定性/依賴建構＋@DoNotMock）；強調 classical vs mockist、prefer realism over isolation、fake 由 owner 維護+contract test、stubbing/interaction 過度使用→change-detector。index 進度 13/25、進度條 52%。
- 2026-06-17：完成 ch12 Unit Testing 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（四種程式變更矩陣：純重構/新功能/修 bug 不改測試、行為變更才改；測行為而非方法：method↔behavior 多對多＋given/when/then）；強調 maintainability、unchanging tests、test via public API、state not interactions、DAMP not DRY。index 進度 12/25、進度條 48%。
- 2026-06-17：完成 ch11 Testing Overview 雙語（md+en.md+雙語 html）；inline SVG 重繪 Fig 11-2（測試規模巢狀邊界：小=單行程⊂中=單機⊂大=多機）與 Fig 11-3／11-4（測試金字塔 80/15/5＋冰淇淋甜筒/沙漏反模式）；強調「測試支撐改變」「size vs scope 正交」「Beyoncé Rule」「flaky 接近 1% 即失去價值」「coverage 非金標準」「GWS >80% 推送需回滾→政策後減半」。index 進度 11/25、進度條 44%。
- 2026-06-17：完成 ch10 Documentation 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（「把文件當程式碼對待」：owner/版控/review/bug 追蹤/測試 並列對照；好文件三參數取捨三角：completeness／accuracy／clarity）；強調「寫一次讀千次的攤提」「為讀者最佳化」「GooWiki 崩壞→搬進版本控制」「seekers vs stumblers」「文件還不是一等公民」。index 進度 10/25、進度條 40%。
- 2026-06-17：完成 ch09 Code Review 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（提交前審查的六步流程：上傳快照→自審寄出→留言↔修改循環→LGTM→提交；三個批准位元：LGTM／owner approval／readability 組合放行）；強調「正確性非首要效益」「程式碼是負債」「最重要的是第一個 LGTM」。index 進度 9/25、進度條 36%。
- 2026-06-17：完成 ch08 Style Guides and Rules 雙語（md+en.md+雙語 html）；**進入 Part III 流程篇**；自製兩張概念 SVG（一致性的階層：檔案⊂團隊⊂專案⊂程式碼庫＋外部社群；執行光譜：社會性→技術性）。index 進度 8/25、進度條 32%。
- 2026-06-16：完成 ch07 Measuring Engineering Productivity 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（GSM 三層框架：目標→訊號→指標，含由上而下/由下而上箭頭；QUANTS 五面向卡片）；收束 ch03 readability 線。**Part II 文化篇 ch02–07 全數完成**。index 進度 7/25、進度條 28%。
- 2026-06-16：完成 ch06 Leading at Scale 雙語（md+en.md+雙語 html）；inline SVG 重繪 Fig 6-1（Good/Fast/Cheap＝品質/延遲/容量取捨三角）與 Fig 6-2（成功的螺旋：分析→掙扎→牽引→獎賞→壓縮）；themes 首次納入 Time 標籤；index 進度 6/25、進度條 24%。
- 2026-06-16：完成 ch05 How to Lead a Team 雙語（md+en.md+雙語 html）；本章原書無正式 Figure，自製「激勵×方向 2×2 矩陣」概念 SVG（分心→給方向／低潮→給激勵／漂流→兩者都給／茁壯→別給過量）＋反模式↔正向模式雙欄；index 進度 5/25、進度條 20%。
- 2026-06-16：完成 ch04 Engineering for Equity 雙語（md+en.md+雙語 html），自製「偏見惡性循環」概念 SVG（非代表性團隊→偏誤入資料→傷害弱勢→信任流失，順時針循環＋打破點）；index 進度 4/25、進度條 16%。
- 2026-06-16：完成 ch03 Knowledge Sharing 雙語（md+en.md+雙語 html），自製「知識分享擴展光譜」概念 SVG（1對1→社群→組織級，地基為心理安全感）；index 進度 3/25、進度條 12%。
- 2026-06-16：建立進度帳本機制；完成 ch01、ch02 雙語（中/英切換）+ 圖；index 雙語骨架。
