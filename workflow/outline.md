# 簡報大綱（由 Wiki Query 產生，CLAUDE.md 第 5.1 節）

> 產生方式：AI 先讀 `wiki/index.md` → 依四個學習目標挑頁面 → 每張投影片只用該頁內容。
> 「目標」欄對應 overview.md 的四個學習目標；「Wiki 頁面」欄會寫進 HTML 的 `data-wiki`。

| # | 投影片 | 教學結構段落 | 目標 | Wiki 頁面 | 來源 |
|---|---|---|---|---|---|
| 1 | 封面：讓 LINE 官方帳號變成不會亂講的 AI 客服 | — | — | overview.md | — |
| 2 | 今天學完你會知道 4 件事 | — | 1–4 | overview.md | — |
| 3 | 情境：店員一直回答一樣的問題 | 情境問題 | 1 | concepts/keyword-auto-reply.md | S07 |
| 4 | 關鍵字自動回應的限制（互動：試打一句話） | 情境問題 | 1 | concepts/keyword-auto-reply.md | S07 |
| 5 | 關鍵字 vs AI 客服 | 情境問題 | 1 | syntheses/why-ai-not-keyword.md | S07, S03, S05 |
| 6 | 名詞地圖：官方帳號、Messaging API、Webhook、Bot、LLM | 名詞地圖 | 2 | concepts/line-official-account.md, concepts/messaging-api.md | S03, S01, S02 |
| 7 | 一則訊息的旅程（逐步動畫） | 運作原理 | 2 | syntheses/architecture.md | S01, S02, S03 |
| 8 | Webhook＝門鈴：簽章、重送、去重 | 運作原理 | 2 | concepts/webhook.md | S01, S03 |
| 9 | Reply vs Push 與訊息額度 | 運作原理 | 2 | concepts/reply-vs-push.md | S02, S03 |
| 10 | 免伺服器：Apps Script + Gemini 四元件 | 實作要點 | 3 | concepts/gas-gemini-serverless.md | S03 |
| 11 | 讓 AI 只回 JSON | 實作要點 | 3 | concepts/structured-output.md | S03 |
| 12 | AI 是金魚：對話記憶 | 實作要點 | 3 | concepts/conversation-memory.md | S04, S01 |
| 13 | 三個真實翻車案例 | 風險與對策 | 4 | concepts/grounding-knowledge-base.md | S05 |
| 14 | 防亂講四招 | 風險與對策 | 4 | concepts/grounding-knowledge-base.md | S05, S06, S03 |
| 15 | 什麼時候交棒給真人 | 風險與對策 | 4 | concepts/human-handoff.md | S06 |
| 16 | 安全・隱私・成本 | 風險與對策 | 4 | concepts/security-privacy-cost.md | S01, S02, S03 |
| 17 | 上線前檢查清單（可勾選） | 檢查清單 | 2–4 | syntheses/launch-checklist.md | S01, S03, S05, S06 |
| 18 | 小測驗 3 題 | 小測驗 | 1–4 | concepts/keyword-auto-reply.md, concepts/reply-vs-push.md, concepts/human-handoff.md | S07, S02, S06 |
| 19 | 總結＋延伸閱讀 | 總結 | 1–4 | overview.md | S01, S02, S03, S04, S05, S06, S07 |

## 大綱檢查（outline check）
- [x] 四個學習目標都至少有 3 張投影片（目標1：3–5；目標2：6–9；目標3：10–12；目標4：13–16）
- [x] 每張都有 Wiki 頁面
- [x] 教學結構 8 段都出現
- [x] 沒有用到 Wiki 以外的內容；S06 的「15–25%」衝突數字未使用
- [x] 決策：第 11 張不放完整 Apps Script 程式碼——Wiki 中沒有程式碼頁，放了就等於用 Wiki 以外的記憶補內容；只放依 S03 欄位設計改寫的 JSON 範例（Wiki 已標【推論】）
