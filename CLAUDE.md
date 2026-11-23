# CLAUDE.md — LINE Bot × AI 客服自動化 LLM Wiki 規則書（Schema）

> 這份檔案是給 AI 代理（Claude / Codex / Gemini CLI 都可）讀的「工作規則」。
> 任何人把這個 repo 交給 AI，並說「依 CLAUDE.md 新增一篇資料」或「依 CLAUDE.md 做一份新簡報」，
> AI 都應該照下面同一套方式產出，讓 Wiki 與簡報可以持續、一致地擴充。
> 參考：Karpathy〈LLM Wiki〉idea file 的三層架構（raw / wiki / schema）與三種操作（ingest / query / lint）。

---

## 1. 需求摘要

| 項目 | 內容 |
|---|---|
| 主題 | LINE Bot × AI 客服自動化：小店家如何用 LINE 官方帳號 + LLM 做出「會回答、不亂講、會交棒給真人」的客服 |
| 讀者 | 不熟悉程式的店家、非資訊科系同學 |
| 產出 1 | `wiki/`：可持續累積的 Markdown 知識庫 |
| 產出 2 | `index.html`：可在 GitHub Pages 瀏覽的教學型 HTML 簡報 |
| 語言 | 繁體中文；技術名詞第一次出現時附英文（例：Webhook） |
| 品質底線 | 簡報上的每一個重點，都必須能追溯到 Wiki 頁面，Wiki 頁面再追溯到 `raw/` 來源 |

---

## 2. 目錄結構

```
raw/                 # 第 1 層：來源擷取筆記（只新增、不修改）S01, S02, ...
wiki/                # 第 2 層：AI 維護的知識頁
  index.md           #   全部頁面目錄（每次 ingest 都要更新）
  log.md             #   時間序紀錄（只能 append）
  overview.md        #   主題總覽
  sources/           #   每篇來源一頁摘要 sNN-*.md
  concepts/          #   概念頁（一個概念一頁）
  syntheses/         #   跨來源整合、Query 回答回寫
CLAUDE.md            # 第 3 層：本規則書
index.html           # 教學簡報（GitHub Pages 首頁）
workflow/            # loop / graph 說明、流程圖、執行與檢查紀錄
scripts/lint_wiki.py # 自動檢查腳本
```

---

## 3. 頁面格式規則

每個 `wiki/` 頁面開頭必須有 frontmatter：

```yaml
---
title: Webhook
type: concept          # concept | source | synthesis | overview
sources: [S01, S03]    # 至少 1 個；synthesis 至少 2 個
updated: 2026-11-15
---
```

內文規則：

1. **一句話定義**放最前面（給完全不懂的人）。
2. **比喻**一個（教學用）。
3. **重點**用條列，每條結尾標來源 `[S01]`。
4. **AI 自己的推論**一律標 `【推論】`，不得偽裝成來源事實。
5. **會變動的數字**（價格、額度、模型名稱）標 `【易變】`並寫「依來源文章當時」。
6. 頁尾 `## 相關頁面` 用**相對路徑連結**（例：`[Reply vs Push](reply-vs-push.md)`），至少 1 個連結，避免孤兒頁。
7. 搜尋結果的摘要片段（snippet）**不得直接寫進 Wiki**，必須以全文擷取為準；全文取不到時，在 source 頁標 `完整度：部分`。

---

## 4. 操作流程

### 4.1 Ingest（新增一篇資料）—— 先討論、後生成

1. 人提供或 AI 搜尋到來源 → 先在對話中**討論**：這篇要回答哪個學習目標？可信度？
2. 取得全文 → 在 `raw/` 新增 `SNN-短名.md`（網址、擷取日、完整度、擷取筆記）。
3. **來源核對**：把要寫進 Wiki 的每個事實回頭對照 raw；與 snippet 或其他來源矛盾的，記到 log 的 `CONFLICT`。
4. 寫 `wiki/sources/sNN-*.md` 摘要。
5. 更新或新增相關 `concepts/` 頁（一篇來源通常影響 3–6 頁）。
6. 更新 `index.md`，在 `log.md` append：`## [日期] ingest | SNN 標題`。

### 4.2 Query（用 Wiki 回答問題 / 做簡報）

1. 先讀 `index.md` 找相關頁，再讀頁面；**不准**用 Wiki 以外的記憶補內容。
2. Wiki 不足 → 回到 Ingest 補資料，而不是硬寫。
3. 好的回答回寫到 `syntheses/`，log 記 `query`。

### 4.3 Lint（健康檢查）

執行 `python3 scripts/lint_wiki.py`，必須全部通過：
- frontmatter 完整、sources 都存在於 `raw/`
- 相對連結沒有斷鏈、沒有孤兒頁、index 收錄所有頁面
- 簡報每張 `<section>` 都有 `data-wiki`，且指向存在的 Wiki 頁面

---

## 5. 簡報產生規則（之後做新簡報也照這套）

1. **大綱先行**：先從 Wiki 產出大綱 `workflow/outline.md`，每一點標出 Wiki 頁面；人確認後才寫 HTML。
2. **教學結構**固定為：情境問題 → 名詞地圖 → 運作原理 → 實作要點 → 風險與對策 → 檢查清單 → 小測驗 → 總結與延伸閱讀。
3. 每張投影片 `<section class="slide" data-wiki="concepts/webhook.md" data-src="S01">`。
4. 一張投影片只講一個概念；文字不超過 6 行；至少一半投影片要有圖、表或範例。
5. 單一 HTML 檔、不依賴外部 CDN；支援鍵盤 ← → 、點擊、觸控換頁；手機可讀。
6. 頁尾顯示「📚 Wiki 出處」，可用 `W` 鍵切換顯示（方便老師檢查對應）。
7. 產生後必須做**渲染檢查**：用無頭瀏覽器逐頁截圖，看有無溢版、空白頁，再跑 lint。

---

## 6. 新增內容的快速指令範例

- 「依 CLAUDE.md ingest 這篇：<網址>」
- 「依 CLAUDE.md lint 一次，把問題修掉並記 log」
- 「依 CLAUDE.md 第 5 節，用 Wiki 做一份『Rich Menu 是什麼？』的 10 頁簡報」
