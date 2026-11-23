# LINE Bot × AI 客服自動化 — LLM Wiki ＋ 教學 HTML 簡報

TAICA 生成式 AI：文字與圖像生成的原理與實務｜作業：用 LLM Wiki 做一份教學 HTML 簡報

- 🎞️ **教學簡報**：https://qiipppp.github.io/line-ai-cs-wiki/
- 📚 **LLM Wiki 目錄**：[wiki/index.md](wiki/index.md)
- 🧭 **規則書（CLAUDE.md）**：[CLAUDE.md](CLAUDE.md)
- 🔁 **Loop / Graph 說明**：[workflow/workflow.md](workflow/workflow.md)
- 🧪 **實際執行與檢查紀錄**：[workflow/run-log.md](workflow/run-log.md)
- 💭 **反思**：[workflow/reflection.md](workflow/reflection.md)
- 💬 **先討論、後生成紀錄**：[docs/discussion.md](docs/discussion.md)

## 主題與簡介
小店家（例如寵物美容店）想讓 LINE 官方帳號 24 小時回答客人，又怕 AI 亂講話。這個 Wiki 從 7 篇資料（LINE 官方文件、中文實作教學、產業案例）整理出 11 個概念與 3 篇整合頁，再用它產生 19 張教學投影片，讓不懂程式的人理解：為什麼需要 AI 客服、一則訊息怎麼跑、怎麼接上 AI、怎麼避免出事。

## 專案結構（Karpathy LLM Wiki 三層架構）
```
raw/        第 1 層：7 篇來源擷取筆記（S01–S07）
wiki/       第 2 層：AI 維護的知識頁（index、log、overview、concepts、syntheses、sources）
CLAUDE.md   第 3 層：規則書（頁面格式、ingest/query/lint 流程、簡報產生規則）
index.html  教學簡報（GitHub Pages 首頁）
workflow/   流程圖、大綱、執行紀錄、lint 與渲染檢查輸出、反思
scripts/    lint_wiki.py 自動檢查
```

## Wiki ↔ 簡報對應
每張投影片 `<section>` 都有 `data-wiki`（對應 Wiki 頁）與 `data-src`（對應來源），頁尾自動顯示「📚 Wiki 出處」（按 **W** 切換）。對應關係由 `scripts/lint_wiki.py` 的 S1/S2 檢查自動驗證：

```bash
python3 scripts/lint_wiki.py
# Wiki 頁面 24｜raw 來源 7｜投影片 19
# ✅ 全部檢查通過
```

## 如何用同一套規則繼續擴充
把 repo 交給任一 AI 代理（Claude Code / Codex / Gemini CLI），下指令：
- 「依 CLAUDE.md ingest 這篇：<網址>」
- 「依 CLAUDE.md lint 一次並修正」
- 「依 CLAUDE.md 第 5 節，用 Wiki 做一份『Rich Menu 是什麼？』的簡報」

## 使用的 AI
Claude Opus 5.5（claude-opus-5-5），於 Claude App 中執行。
