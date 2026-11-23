---
title: LINE 官方帳號（LINE Official Account）
type: concept
sources: [S03, S07]
updated: 2026-11-15
---

**一句話定義**：店家在 LINE 上的「門市櫃檯」，客人加好友後就能在聊天室跟店家對話。

**比喻**：官方帳號是店面；Messaging API 是店面後方通往辦公室的「內線」，讓程式（Bot）能代替店員接話。

## 重點
- 先在 LINE Official Account Manager 建立官方帳號，再啟用 Messaging API，才會在 LINE Developers Console 產生 channel，接著發行 channel access token [S03]
- 原生功能就有「自動回應訊息」可做罐頭回覆 [S07]
- 接上自己的 Bot 後，要關閉原生自動回應，否則兩邊會一起回話互相干擾 [S03]

## 相關頁面
- [Messaging API](messaging-api.md)
- [關鍵字自動回應](keyword-auto-reply.md)
- [系統架構](../syntheses/architecture.md)
