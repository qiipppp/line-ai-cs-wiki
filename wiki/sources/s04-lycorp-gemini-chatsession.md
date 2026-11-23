---
title: S04 LY Corp 技術部落格：有記憶的 Gemini LINE Bot
type: source
sources: [S04]
updated: 2026-11-15
---

**一句話**：LLM 預設「一問一答」不記得上一句，要靠對話歷史（History）才有記憶。

## 重點
- 舊式 API 每次請求互不相關；要把過去問答一起送才有記憶 [S04]
- Gemini SDK 的 ChatSession 會自動把問答存進 History [S04]
- 文章未說明 webhook 與 session 的串接方式，也未討論歷史存放位置 [S04]

## 對應學習目標
目標 3「怎麼把 AI 接上去」。

## 影響頁面
[對話記憶](../concepts/conversation-memory.md)、[Apps Script + Gemini](../concepts/gas-gemini-serverless.md)
