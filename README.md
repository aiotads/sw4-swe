# 《Software Engineering at Google》研究閱讀系統

> 把整本《Software Engineering at Google》（602 頁、25 章、5 大部分）逐章轉成
> **中英並陳的研究筆記（Markdown）＋ 精簡靜態 HTML 視覺化**，並用一份總索引串連全書。
> 產出供團隊內 **L4~L6 軟體工程師**精讀。

🔗 **線上閱讀（GitHub Pages）：** `https://<org-or-user>.github.io/<repo>/`
（部署後請把網址換成實際的；入口頁是 [`site/index.html`](site/index.html)）

---

## 這是什麼 / 給誰看

這不是一份讀書心得，而是一套**可長期維護、可逐章接續產出**的研讀系統。團隊任何人都可以：

- 直接到 GitHub Pages 上**讀章節**（深色學術風、右上角一鍵切換中／英）。
- 想吸收原書密集論證又怕只看摘要失真？每章同時有**繁中研讀筆記**與**英文 English-to-English 導讀**，可對照原文語感。
- 把書裡的決策原則回扣到自己手上的技術決策——每章都從「L4~L6 的真實痛點」切入，講清楚 **trade-off**。

全書論點圍繞三條主軸，視覺化用固定配色標記，每章都會回扣：

| 主軸 | 一句話 | 配色 |
|---|---|---|
| **Time / 時間** | 軟體工程是「整合了時間維度的程式設計」，程式碼有預期壽命，必須能因應變化。 | 琥珀 |
| **Scale / 規模** | 組織與程式碼長大時，每件重複做的事都要次線性擴展，否則撐不住。 | 青藍 |
| **Trade-offs / 取捨** | 工程決策是在不完美資訊下權衡成本；要有理由，不能「因為我說了算」。 | 紫紅 |

> 核心金句：**"Software engineering is programming integrated over time."**

---

## 系統架構

整個專案分成三層：**原始資料 → 研究筆記 → 視覺化網站**，外加一套規範「怎麼做」的 SKILL。

```
原始書 PDF
   │  _extract.py / _slice.py / _figs.py（擷取、切章、盤點圖）
   ▼
chapters/raw/chNN.txt   ← 切好的單章原文（唯一資料來源）
   │  套用 swe-research SKILL 的五階段研究流程
   ▼
chapters/chNN.md        ← 繁中研究筆記（七段結構）
chapters/chNN.en.md     ← 英文研究筆記（English-to-English 導讀）
   │  視覺化重繪
   ▼
site/chNN.html          ← 各章雙語視覺化（自包含、無 JS、無 CDN）
site/index.html         ← 總索引：依 5 大 Part 分組，串連全部章節
```

### 目錄結構

```
d:\ah\swe\
├── README.md                              ← 本檔
├── CLAUDE.md                              ← 全書「事實與規格」：主軸、章節清單、檔案結構、HTML 主題
├── PROGRESS.md                            ← 進度單一事實來源（跨 session 記憶，續做先讀它）
├── .claude/skills/swe-research/SKILL.md   ← 研究「方法」：五階段流程 + 圖政策 + 雙語規範
├── swe_at_google.2.pdf                    ← 原始書
├── _extract.py / _slice.py / _figs.py     ← 擷取、切章、盤點圖的工具腳本
├── chapters/
│   ├── raw/chNN.txt                       ← 切好的原文（資料來源）
│   ├── chNN.md                            ← 成品：繁中研究筆記
│   └── chNN.en.md                         ← 成品：英文研究筆記
└── site/                                  ← ★ GitHub Pages 發佈根目錄
    ├── index.html                         ← 總索引（網站入口）
    ├── chNN.html                          ← 各章視覺化
    └── assets/                            ← 共用主題資源
```

### 三份治理文件，各司其職

職責切得很乾淨，這是本系統能長期穩定接續的關鍵：

- **`CLAUDE.md` — 規範「事實與規格」**：全書三大主軸、25 章清單與 PDF 頁碼、檔案結構、HTML 主題（深色配色、CSS 變數、版面、頁尾導航）。
- **`.claude/skills/swe-research/SKILL.md` — 規範「方法」**：怎麼把一章原文變成成品（見下節）。
- **`PROGRESS.md` — 進度的單一事實來源**：跨 session 的進度帳本。**新一輪接續工作前先讀它的「▶ 下一步」**，完成一章後立即回寫。

### 網站設計原則（全書一致）

- **精簡靜態**：每個 `chNN.html` 自包含、內嵌 `<style>`、**無 JavaScript、無外部 CDN**——適合直接丟 GitHub Pages，離線也能開。
- **深色學術風**：統一的 CSS 變數與版面，最大內容寬度約 860px、置中、行高舒適。
- **中英一鍵切換**：用**純 CSS（zero JS）** 的 radio + label 機制切換語言，所有語言相依內容包進 `.zh / .en`。
- **圖一律重繪**：概念圖／流程圖用 **inline SVG** 在深色主題重繪（套三主軸配色）；產品 UI 截圖才抽原圖 base64 內嵌於可收合區。
- **每章頁尾固定導航**：`← 上一章 ｜ 總索引 ｜ 下一章 →`。

---

## SKILL：`swe-research` 專注什麼

`swe-research` 是本系統的核心方法論——它確保每一章都用**同一套研究流程與品質守則**產出，而不是隨手寫摘要。它專注三件事：

### 1. 五階段研究閱讀流程（每章跑完整一輪）

| 階段 | 做什麼 | 產出 |
|---|---|---|
| **① 廣讀 Skim** | 通讀原文建章節地圖：這章在回答什麼問題？ | 心智圖骨架 |
| **② 精讀 Deep** | 逐節抓核心主張、Google 真實案例、數字、年份——**所有數字與案例回原文查核** | 細節重點 + 待引金句 |
| **③ 思考 Reflect** | 把論點轉成「對 L4~L6 的工程決策意味著什麼」，回扣三大主軸 | 痛點切入 + 取捨分析 |
| **④ 提問 Question** | 生成 3~5 題驅動實作反思的蘇格拉底式問題 | 延伸提問清單 |
| **⑤ 重複閱讀 Review** | 跨章連結、中英一致性校驗、防過度簡化／誤譯 | 跨章連結 + 全文校對 |

### 2. 受眾與語言守則（硬性）

- **對象**：L4~L6 工程師。碩士級敘事，**避免兩個極端**——不淪為名詞解釋（太淺）、也不堆學術黑話（太深）；每個概念都落到「現場會怎麼用」。
- **繁中輸出**，技術名詞／制度名（Hyrum's Law、Beyoncé Rule、SemVer、monorepo…）保留英文並附首見中譯。
- **譯「神」不譯「字」**：英文諺語／比喻（boiled frog、bus factor、shifting left）譯出神髓，必要時加文化註解，原文核心主張不得失真。

### 3. 雙語成品規格

- **每章固定七段結構**：摘要 → 為什麼要讀 → 細節重點 → 原文引用（中英並陳）→ 關鍵字補充 → 延伸提問 → 跨章連結。
- 中文版金句＝英文原文＋繁中翻譯＋語境註；英文版採 **English-to-English** 淺白重述，服務想用英文吸收的讀者，**不是把中文機械翻回去**。
- **完成檢查清單**＋**完成一章後四個必更新**（`PROGRESS.md`／`CLAUDE.md`／`index.html`／回報確認），確保隨時可安全中斷、下次無縫接續。

> 動工任一章前，先讀 [`SKILL.md`](.claude/skills/swe-research/SKILL.md) 與 [`CLAUDE.md`](CLAUDE.md)。

---

## 進度

進度以 [`PROGRESS.md`](PROGRESS.md) 為**單一事實來源**（含逐章狀態表與變更日誌）。

- ✅ **Part I — Thesis**：ch01
- ✅ **Part II — Culture**：ch02–ch07（文化篇全數完成）
- 🚧 **Part III — Processes**：ch08 起進行中
- ⬜ **Part IV — Tools**：ch16–ch25
- ⬜ **Part V — Conclusion**：Afterword（併入全書回顧）

> 量產節奏：一次一章，每章產出 `chNN.md` + `chNN.en.md` + 雙語 `chNN.html`，並更新總索引。

---

## 在本機閱讀

所有 HTML 自包含、無外部依賴，直接用瀏覽器開即可：

```bash
# 直接開總索引
start site/index.html      # Windows
# open site/index.html     # macOS

# 或起一個簡單本機伺服器
python -m http.server -d site 8000
# 瀏覽 http://localhost:8000
```

## 部署到 GitHub Pages

網站根目錄是 [`site/`](site/)。在 repo 設定裡把 Pages 來源指到 `site/`（或把 `site/` 內容放到 `gh-pages` 分支 / `docs/`），即可發佈。入口頁為 `site/index.html`。
