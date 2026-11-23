---
title: 安全・隱私・成本
type: concept
sources: [S01, S02, S03]
updated: 2026-11-15
---

**一句話定義**：上線前一定要想的三件事——假請求、客人資料、帳單。

## 安全
- 驗證 `x-line-signature`，其他來源可能送惡意請求 [S01]
- Apps Script 讀不到簽章 → `/exec` 網址保密、加 userId 白名單 [S03]
- 金鑰放 Script Properties，不放程式碼 [S03]

## 隱私
- 免費層 Gemini 請求可能被用於改善 Google 產品，避免傳送敏感資料 [S03]
- 使用者收回訊息時，也要從你的紀錄中移除 [S01]

## 成本【易變】
- 推播額度以收件人數計算 [S02]
- Reply 不計入推播額度；免費推播當時每月 200 則 [S03]
- Gemini 免費層有用量上限，多人使用可能用完 [S03]

## 相關頁面
- [Webhook](webhook.md)
- [Reply vs Push](reply-vs-push.md)
- [上線檢查清單](../syntheses/launch-checklist.md)
