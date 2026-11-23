---
title: S02 LINE 官方文件：發送訊息
type: source
sources: [S02]
updated: 2026-11-15
---

**一句話**：Bot 回話的五種方式，以及「訊息額度」怎麼算。

## 重點
- Reply 用 webhook 給的 `replyToken` 回應使用者 [S02]
- Push / Multicast / Narrowcast / Broadcast 是主動發送 [S02]
- 每次請求最多 5 個訊息物件 [S02]
- 額度以「收件人數」計算，不是物件數 [S02]
- 回覆較慢時可顯示 loading 動畫 [S02]

## 對應學習目標
目標 2「一則訊息怎麼跑」、目標 4「成本」。

## 影響頁面
[Reply vs Push](../concepts/reply-vs-push.md)、[Messaging API](../concepts/messaging-api.md)、[安全・隱私・成本](../concepts/security-privacy-cost.md)
