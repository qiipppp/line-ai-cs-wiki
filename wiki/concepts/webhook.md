---
title: Webhook
type: concept
sources: [S01, S03]
updated: 2026-11-15
---

**一句話定義**：「有事就通知你」的網址——客人一傳訊息，LINE 就主動把內容送到這個網址。

**比喻**：門鈴。你不用一直開門看有沒有客人（輪詢），客人按鈴（事件）你才去應門。

## 重點
- 觸發時機：加好友、傳訊息、收回訊息等事件 [S01]
- 必須先驗證 `x-line-signature` 簽章，確定是 LINE 送的、沒被竄改 [S01]
- 只有伺服器沒回 2xx 才會重送，而且重送預設關閉、不保證成功 [S01]
- 可能收到重複或亂序事件：用 `webhookEventId` 去重、看 `timestamp` 排序 [S01]
- 在 Apps Script 中，部署成「網頁應用程式」後的 `/exec` 網址就是 Webhook URL [S03]
- Apps Script 讀不到簽章 header → 網址要保密或加 userId 白名單 [S03]

## 相關頁面
- [Messaging API](messaging-api.md)
- [Apps Script + Gemini](gas-gemini-serverless.md)
- [安全・隱私・成本](security-privacy-cost.md)
