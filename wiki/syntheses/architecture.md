---
title: 系統架構：一則訊息的旅程
type: synthesis
sources: [S01, S02, S03, S04]
updated: 2026-11-15
---

**一句話**：客人傳一句話，到收到 AI 回覆，中間經過 6 站。

```
客人（LINE App）
  │ ① 傳訊息「這週六下午可以預約洗澡嗎？」
  ▼
LINE 平台 ──② Webhook POST──► Apps Script /exec（Bot 伺服器）
                                │ ③ 驗證來源（白名單）、去重
                                │ ④ 讀知識庫＋對話歷史 → 呼叫 Gemini（要求 JSON）
                                │ ⑤ 寫入試算表；需要真人就通知店員
LINE 平台 ◄──⑥ Reply API(replyToken)──┘
  │
  ▼
客人收到回覆
```

| 站 | 做什麼 | 依據 |
|---|---|---|
| ② | LINE 把事件以 HTTP POST 送到 Webhook URL | [S01] |
| ③ | 驗證簽章；Apps Script 無法驗簽時改用網址保密／白名單；用 webhookEventId 去重 | [S01][S03] |
| ④ | Gemini 理解語意，只回固定欄位 JSON | [S03] |
| ④ | 帶入對話歷史才有記憶 | [S04] |
| ⑤ | 試算表當資料庫 | [S03] |
| ⑥ | 用 replyToken 回覆，每次最多 5 個訊息物件 | [S02] |

> 「讀知識庫」與「通知店員」兩步是依 S05、S06 的建議加入的設計【推論：S03 原始案例沒有這兩步】。

## 相關頁面
- [Webhook](../concepts/webhook.md)
- [Apps Script + Gemini](../concepts/gas-gemini-serverless.md)
- [真人交棒](../concepts/human-handoff.md)
