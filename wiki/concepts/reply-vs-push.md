---
title: Reply vs Push（回覆與主動推播）
type: concept
sources: [S02, S03]
updated: 2026-11-15
---

**一句話定義**：Reply 是「客人先開口、你回應」；Push 是「你主動找客人」。

**比喻**：Reply 像櫃檯回答客人問題；Push 像店家主動打電話通知「您的毛孩美容好了」。

## 比較

| | Reply | Push 系列（Push / Multicast / Narrowcast / Broadcast） |
|---|---|---|
| 誰先開始 | 使用者先傳訊息 | 店家主動 |
| 需要什麼 | webhook 給的 `replyToken` [S02] | 使用者 ID 或受眾 [S02] |
| 額度 | 依 S03，回覆不計入每月推播額度 | 計入額度，以收件人數計算 [S02] |
| 每次最多 | 5 個訊息物件 [S02] | 5 個訊息物件 [S02] |

## 重點
- 額度以「人數」計：4 個物件發給 5 人算 5 則 [S02]
- 每月免費推播額度依方案而定（S03 當時寫 200 則）【易變】[S03]
- 客服問答以 Reply 為主最省額度；主動通知才用 Push【推論】

## 相關頁面
- [Messaging API](messaging-api.md)
- [安全・隱私・成本](security-privacy-cost.md)
