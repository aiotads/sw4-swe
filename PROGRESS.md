# PROGRESS — SWE@Google 研讀進度帳本（單一事實來源）

> 本檔是跨 session 的進度記憶。**每個新 session 開工前先讀本檔**，找到「下一章」續做；
> **每完成一章，立即更新本檔 + `CLAUDE.md` 進度 + `site/index.html` 卡片狀態與進度條**。
> 產出規格見 `.claude/skills/swe-research/SKILL.md`（五階段 + 圖政策 + 中英雙語）。

## ▶ 下一步（NEXT UP）
- **Ch9 — Code Review（程式碼審查）**，PDF p.193–212
- 本章原書圖況待 `_figs.py` 確認；多為流程/概念，無 UI 截圖（Critique 的 UI 截圖在 ch19）→ 概念圖用 inline SVG（建議：CL 審查流程／LGTM·Approval·readability 三道關卡）。
- 動作：產 `chapters/ch09.md` + `chapters/ch09.en.md` + 雙語 `site/ch09.html` → 更新本檔、CLAUDE.md、index.html → 等使用者確認再進 Ch10。

## 狀態圖例
- ✅ 完成　🚧 進行中　⬜ 未開始
- 欄位：MD（繁中筆記）｜EN（英文筆記）｜HTML（雙語視覺化）｜IDX（index 卡片已標完成）

## 進度總表（8 / 25 章完成）

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
| 09 | Code Review | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | **NEXT** |
| 10 | Documentation | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | |
| 11 | Testing Overview | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | Fig11-1~4 | 測試金字塔 |
| 12 | Unit Testing | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | DAMP vs DRY |
| 13 | Test Doubles | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | fake/stub/mock |
| 14 | Larger Testing | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | Fig14-1~6 | |
| 15 | Deprecation | III Processes | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | |
| 16 | Version Control and Branch Management | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig16-1 | monorepo |
| 17 | Code Search | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig17-1~4（含UI截圖） | UI 圖抽原圖 base64 |
| 18 | Build Systems and Build Philosophy | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig18-1~5 | |
| 19 | Critique: Google's Code Review Tool | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig19-1~8（UI截圖） | 多為產品截圖→base64 |
| 20 | Static Analysis | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig20-1,20-2 | Tricorder |
| 21 | Dependency Management | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig21-1 | 鑽石依賴/SemVer |
| 22 | Large-Scale Changes | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | LSC |
| 23 | Continuous Integration | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | Fig23-1~5 | |
| 24 | Continuous Delivery | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | |
| 25 | Compute as a Service | IV Tools | ⬜ | ⬜ | ⬜ | ⬜ | 自製 | CaaS |
| — | Afterword | V Conclusion | ⬜ | ⬜ | ⬜ | ⬜ | — | 併入全書回顧，不單獨成章 |

## 變更日誌（最新在上）
- 2026-06-17：完成 ch08 Style Guides and Rules 雙語（md+en.md+雙語 html）；**進入 Part III 流程篇**；自製兩張概念 SVG（一致性的階層：檔案⊂團隊⊂專案⊂程式碼庫＋外部社群；執行光譜：社會性→技術性）。index 進度 8/25、進度條 32%。
- 2026-06-16：完成 ch07 Measuring Engineering Productivity 雙語（md+en.md+雙語 html）；自製兩張概念 SVG（GSM 三層框架：目標→訊號→指標，含由上而下/由下而上箭頭；QUANTS 五面向卡片）；收束 ch03 readability 線。**Part II 文化篇 ch02–07 全數完成**。index 進度 7/25、進度條 28%。
- 2026-06-16：完成 ch06 Leading at Scale 雙語（md+en.md+雙語 html）；inline SVG 重繪 Fig 6-1（Good/Fast/Cheap＝品質/延遲/容量取捨三角）與 Fig 6-2（成功的螺旋：分析→掙扎→牽引→獎賞→壓縮）；themes 首次納入 Time 標籤；index 進度 6/25、進度條 24%。
- 2026-06-16：完成 ch05 How to Lead a Team 雙語（md+en.md+雙語 html）；本章原書無正式 Figure，自製「激勵×方向 2×2 矩陣」概念 SVG（分心→給方向／低潮→給激勵／漂流→兩者都給／茁壯→別給過量）＋反模式↔正向模式雙欄；index 進度 5/25、進度條 20%。
- 2026-06-16：完成 ch04 Engineering for Equity 雙語（md+en.md+雙語 html），自製「偏見惡性循環」概念 SVG（非代表性團隊→偏誤入資料→傷害弱勢→信任流失，順時針循環＋打破點）；index 進度 4/25、進度條 16%。
- 2026-06-16：完成 ch03 Knowledge Sharing 雙語（md+en.md+雙語 html），自製「知識分享擴展光譜」概念 SVG（1對1→社群→組織級，地基為心理安全感）；index 進度 3/25、進度條 12%。
- 2026-06-16：建立進度帳本機制；完成 ch01、ch02 雙語（中/英切換）+ 圖；index 雙語骨架。
