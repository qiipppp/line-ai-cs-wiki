---
title: 主題總覽：LINE Bot × AI 客服自動化
type: overview
sources: [S01, S02, S03, S04, S05, S06, S07]
updated: 2026-11-15
---

## 這個 Wiki 在回答什麼？
小店家（例如寵物美容店）想讓 LINE 官方帳號 24 小時回答客人，又不想讓 AI 亂講話。這個 Wiki 整理了做到這件事需要懂的概念。

## 四個學習目標
1. **為什麼**需要 AI 客服？→ [關鍵字自動回應](concepts/keyword-auto-reply.md)、[為什麼不用關鍵字就好？](syntheses/why-ai-not-keyword.md)
2. 一則訊息**怎麼跑**？→ [Messaging API](concepts/messaging-api.md)、[Webhook](concepts/webhook.md)、[Reply vs Push](concepts/reply-vs-push.md)、[系統架構](syntheses/architecture.md)
3. 怎麼把 **AI 接上去**？→ [Apps Script + Gemini](concepts/gas-gemini-serverless.md)、[結構化輸出](concepts/structured-output.md)、[對話記憶](concepts/conversation-memory.md)
4. 怎麼讓 AI **不亂講、會交棒**？→ [知識庫與防亂講](concepts/grounding-knowledge-base.md)、[真人交棒](concepts/human-handoff.md)、[安全・隱私・成本](concepts/security-privacy-cost.md)、[上線檢查清單](syntheses/launch-checklist.md)

## 來源分布
官方文件 2 篇（S01、S02）、中文實作教學 2 篇（S03、S07）、LINE 母公司技術部落格 1 篇（S04）、產業觀點 2 篇（S05、S06）。

## 已知缺口（下次 ingest 方向）
- 圖文選單（Rich Menu）、Flex Message
- LINE 官方帳號目前的實際收費方案（易變，需查官方）
- 使用 RAG 檢索店家 FAQ 的具體做法
