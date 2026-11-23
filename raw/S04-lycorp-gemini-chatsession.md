---
id: S04
title: 使用 Google Gemini Pro 打造有記憶的 LINE Bot（ChatSession）— LY Corporation Tech Blog
url: https://techblog.lycorp.co.jp/zh-hant/build-llm-linebot-google-gemini-pro-chat-session
type: 技術部落格（LINE 母公司）
fetched: 2026-11-15
完整度: 全文擷取（WebFetch）
---

## 擷取筆記（以中文改寫）

- 作者想做「記得前面對話」的 LINE Bot。
- 文章指出舊式 Completion API 是「一問一答」，每次請求之間會忘記；過去要把之前的問答串接在新 prompt 前面才有記憶。
- Gemini 的 SDK 提供 ChatSession（`model.StartChat()`），每次送出的提問與回覆會自動存進 History。
- 文章以 Go 示範，但沒有完整寫出 webhook 與 session 如何串接。
- 成本（文章寫於 2024/01/03，屬當時）：Gemini Pro 每分鐘 60 次以內免費，超過依字元與圖片計價。
- 文章**沒有**討論：webhook 是否無狀態、歷史要存哪裡、上下文長度限制、隱私。

> CHECK 註記：擷取工具摘要中出現「歷史需要外部儲存」的說法，經核對屬擷取模型的推論，原文未寫；Wiki 中以【推論】標示。
