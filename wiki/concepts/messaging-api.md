---
title: Messaging API
type: concept
sources: [S01, S02, S03]
updated: 2026-11-15
---

**一句話定義**：LINE 提供給程式的「收訊息＋發訊息」介面，讓你的伺服器能和 LINE 使用者雙向溝通。

**比喻**：像店面的「內線電話系統」——客人說話時 LINE 打給你（Webhook），你要回話時打回 LINE（Reply / Push API）。

## 重點
- **收**：使用者的動作透過 Webhook 以 HTTP POST 送到你的伺服器 [S01]
- **發**：用 Reply（回應使用者）或 Push / Multicast / Narrowcast / Broadcast（主動發）[S02]
- 每次請求最多 5 個訊息物件 [S02]
- 需要 channel access token 才能呼叫發送 API [S03]

## 相關頁面
- [Webhook](webhook.md)
- [Reply vs Push](reply-vs-push.md)
- [LINE 官方帳號](line-official-account.md)
