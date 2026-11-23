---
title: Apps Script + Gemini（免伺服器的 AI Bot）
type: concept
sources: [S03, S04]
updated: 2026-11-15
---

**一句話定義**：用 Google Apps Script 當 Bot 的「大腦外殼」，呼叫 Gemini API 理解訊息，不用自己租伺服器。

**比喻**：Apps Script 是幫你接電話的秘書，Gemini 是秘書旁邊那位很會理解話意的顧問，試算表是秘書的記事本。

## 重點
- 四元件：LINE 官方帳號（介面）、Apps Script（執行環境）、Gemini API（語意理解）、Google 試算表（資料庫）[S03]
- 金鑰放 Script Properties，不寫進程式碼 [S03]
- 部署為網頁應用程式：執行身分「我」、存取權「任何人」，`/exec` 網址貼到 LINE Webhook URL [S03]
- **改程式後一定要部署新版本**，否則不會生效 [S03]
- 建議測試順序：先測 AI→試算表，通過再接 LINE [S03]
- Gemini 沒回結果時要有備援訊息 [S03]
- 模型會下架，Bot 突然壞掉先檢查模型名稱【易變】[S03]
- LLM 預設不記得上一句，需要對話歷史 → 見[對話記憶](conversation-memory.md) [S04]

## 相關頁面
- [結構化輸出](structured-output.md)
- [Webhook](webhook.md)
- [系統架構](../syntheses/architecture.md)
