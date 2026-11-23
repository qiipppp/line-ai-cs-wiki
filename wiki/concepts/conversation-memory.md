---
title: 對話記憶（Conversation History）
type: concept
sources: [S04, S01]
updated: 2026-11-15
---

**一句話定義**：讓 AI「記得剛剛聊過什麼」的機制——把之前的問答一起送給模型。

**比喻**：金魚 vs 筆記本。LLM 本身像金魚每次都忘，對話歷史就是讓它翻閱的筆記本。

## 重點
- 一問一答的 API 每次請求都會忘記前面內容 [S04]
- 早期做法：把過去問答串在新 prompt 前面 [S04]
- Gemini SDK 的 ChatSession 會自動累積 History [S04]
- 訊息文字只能在 webhook 當下讀取，事後拿不回來 [S01]
- 因此若要跨訊息記憶，需要自己把對話存起來（例如存在試算表，以 userId 區分）【推論】

## 相關頁面
- [Apps Script + Gemini](gas-gemini-serverless.md)
- [Webhook](webhook.md)
