---
id: S02
title: Send messages — LINE Developers 官方文件
url: https://developers.line.biz/en/docs/messaging-api/sending-messages
type: 官方文件
fetched: 2026-11-15
完整度: 全文擷取（WebFetch）
---

## 擷取筆記（以中文改寫）

- 兩大類發送方式：回覆使用者（reply）與主動發送。
- Reply message：回應使用者加好友或傳訊息的事件，帶上 webhook 事件中的 `replyToken`。
- Push message：任何時候發給單一使用者、群組或多人聊天。
- Multicast：發給指定的多個 user ID。
- Narrowcast：依屬性（年齡、性別、OS、地區）或受眾發送，不能發給群組。
- Broadcast：發給官方帳號的所有好友。
- 每個請求最多 5 個訊息物件（reply、push、multicast、broadcast、narrowcast 皆同）。
- 計費額度以「收件人數」計算，不是訊息物件數：4 個物件發給 5 人算 5 則。封鎖或不存在的使用者不計。
- Narrowcast 有月上限，接近上限時其他發送可能失敗。
- 回覆需要時間準備時，可顯示 loading 動畫提示使用者稍候。
- 本頁未寫明 reply token 的時效與是否只能用一次（見 log 中的 CHECK 紀錄）。
