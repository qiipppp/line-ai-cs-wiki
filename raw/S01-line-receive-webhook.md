---
id: S01
title: Receive messages (webhook) — LINE Developers 官方文件
url: https://developers.line.biz/en/docs/messaging-api/receiving-messages/
type: 官方文件
fetched: 2026-11-15
完整度: 全文擷取（WebFetch）
---

## 擷取筆記（以中文改寫，非原文轉載）

- 使用者加好友或傳訊息給 LINE 官方帳號時，LINE 平台會對你在 LINE Developers Console 登記的 Webhook URL（Bot 伺服器）送出 HTTP POST，內容是 webhook event 物件。
- 伺服器若長時間收不到 webhook，平台可能暫停 webhook。
- 事件種類：Message、Edit、Unsend、Follow、Unfollow、Join、Leave、Member join/leave、Postback、Video viewing complete；另有 Beacon、Account link。
- 可用性依聊天類型不同：Follow / Unfollow 只在一對一聊天。
- 處理事件前要驗證 request header 的簽章（x-line-signature），確認請求真的來自 LINE 且未被竄改；文件提醒其他來源可能送惡意 POST。
- 建議以非同步方式處理事件。
- 伺服器未回 2xx 時才會觸發重送（redelivery）；重送預設關閉，需在 Messaging API 分頁開啟「Use webhook」與「Webhook redelivery」。
- 重送次數與間隔不公開，不保證送達；重送事件保留相同 event ID 與 reply token，`deliveryContext.isRedelivery` 為 true。
- 可能重複收到，用 `webhookEventId` 去重；事件可能亂序，需看 `timestamp`。
- 使用者收回（unsend）訊息時，應從管理畫面與儲存中移除。
- 圖片、影片、音訊、檔案可用 message ID 取得內容，一段時間後自動刪除；文字只能從 webhook 本身讀取。
- 可用 webhook 中的 user ID 呼叫 profile 端點取得顯示名稱、頭像等。
