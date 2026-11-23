---
title: S01 LINE 官方文件：接收訊息（Webhook）
type: source
sources: [S01]
updated: 2026-11-15
---

**一句話**：LINE 平台怎麼把使用者訊息「推」到你的伺服器，以及收到後要注意什麼。

## 重點
- 使用者傳訊息或加好友 → LINE 對你登記的 Webhook URL 發 HTTP POST [S01]
- 先驗證簽章（x-line-signature）再處理，防止假請求 [S01]
- 未回 2xx 才會重送；重送預設關閉、不保證送達 [S01]
- 可能重複、可能亂序 → 用 `webhookEventId` 去重、看 `timestamp` [S01]
- 文字只能從 webhook 當下讀取 → 需要記錄就要自己存 [S01]

## 對應學習目標
目標 2「一則訊息怎麼跑」、目標 4「上線風險」。

## 影響頁面
[Webhook](../concepts/webhook.md)、[Messaging API](../concepts/messaging-api.md)、[安全・隱私・成本](../concepts/security-privacy-cost.md)、[系統架構](../syntheses/architecture.md)
