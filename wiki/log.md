---
title: 執行紀錄 log
type: overview
sources: [S01, S02, S03, S04, S05, S06, S07]
updated: 2026-11-15
---

# log.md（只能 append，格式：`## [日期 時間] 動作 | 說明`）

> 查最近紀錄：`grep "^## \[" wiki/log.md | tail -5`
> 使用模型：Claude Opus 5.5（claude-opus-5-5），於 Claude App 對話中執行；工具：WebSearch、WebFetch、檔案讀寫、Python、無頭 Chrome。

## [2026-11-15 22:56] discuss | 決定主題
與 AI 討論 4 個候選主題，選「LINE Bot × AI 客服自動化」。理由見 `docs/discussion.md`。

## [2026-11-15 23:00] discuss | 設定讀者與學習目標
讀者＝不熟程式的店家／同學；訂 4 個學習目標（為什麼、怎麼跑、怎麼接 AI、怎麼不亂講）。每篇來源都要對應至少 1 個目標。

## [2026-11-15 23:02] fetch-fail | Karpathy gist、Farzaa gist
兩個方法參考網址不在擷取允許清單內 → 改用 WebSearch 找到二手整理（agentpedia）取得三層架構與 ingest/query/lint 說明。只作為方法參考，不算主題來源。

## [2026-11-15 23:05] ingest | S01 LINE：接收訊息（Webhook）
新增 raw/S01、sources/s01；更新 concepts：webhook、messaging-api、security-privacy-cost。

## [2026-11-15 23:06] ingest | S02 LINE：發送訊息
新增 raw/S02、sources/s02；新增 concepts：reply-vs-push。
CHECK：搜尋片段提到 reply token「一分鐘內、只能用一次」，但 S02 全文未寫明 → 不寫入 Wiki。

## [2026-11-15 23:08] ingest | S03 數位時代：GAS × Gemini
新增 raw/S03、sources/s03；新增 concepts：gas-gemini-serverless、structured-output、line-official-account；更新 webhook、security-privacy-cost。
CHECK：「每月 200 則」屬文章當時方案 → 標【易變】。

## [2026-11-15 23:10] ingest | S04 LY Corp：Gemini ChatSession
新增 raw/S04、sources/s04；新增 concepts：conversation-memory。
CHECK：擷取摘要中「歷史需要外部儲存」為擷取模型的推論，原文無 → 在 Wiki 標【推論】。

## [2026-11-15 23:12] ingest | S05 Thoughtworks：三個陷阱
新增 raw/S05、sources/s05；新增 concepts：grounding-knowledge-base。

## [2026-11-15 23:13] ingest | S06 Hyperleap：轉真人
新增 raw/S06、sources/s06；新增 concepts：human-handoff。
CONFLICT：搜尋 snippet 寫「15–25% 升級率是健康範圍」，全文擷取顯示文章沒有通用健康值 → 以全文為準，數字不收錄。

## [2026-11-15 23:15] fetch-fail | S07 UPTOGO 全文擷取失敗（client_error）
改用搜尋引擎段落，raw 標「完整度：部分」，只引用取得的 3 點。

## [2026-11-15 23:16] ingest | S07 UPTOGO：罐頭訊息
新增 raw/S07、sources/s07；新增 concepts：keyword-auto-reply。

## [2026-11-15 23:20] query | 為什麼不用關鍵字自動回應就好？
製作簡報大綱時提出，答案回寫為 syntheses/why-ai-not-keyword.md。

## [2026-11-15 23:21] query | 一則訊息怎麼跑？
整合 S01–S04 寫成 syntheses/architecture.md；加入知識庫與交棒兩站（標【推論】）。

## [2026-11-15 23:22] query | 上線前要檢查什麼？
整合 S01、S03、S05、S06 寫成 syntheses/launch-checklist.md。

## [2026-11-15 23:25] lint | 第 1 次：1 個問題
index.md 宣告 22 頁，實際 23 頁 → 修正。第 2 次通過。

## [2026-11-15 23:30] generate | 依 outline.md 產生 index.html（19 張）

## [2026-11-15 23:31] lint | 第 3 次：1 個問題
HTML 註解中的範例 section 被誤判為投影片 → 修 lint 腳本先去除註解。第 4 次通過（24 頁／7 來源／19 張）。

## [2026-11-15 23:35] render-check | 3 輪
第 1 輪：內容擠上半部、封面頁碼看不見；第 2 輪：旅程圖來源標籤被撐開、手機按鈕折行；第 3 輪全部通過。

## [2026-11-15 23:40] workflow | 修改為 v2
內容錯誤集中在取資料階段且 Lint 抓不到 → 寫入前新增「③ 來源核對」節點，CLAUDE.md 加入 snippet／推論／易變規則。
