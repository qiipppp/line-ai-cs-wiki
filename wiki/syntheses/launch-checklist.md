---
title: AI 客服上線前檢查清單
type: synthesis
sources: [S01, S03, S05, S06]
updated: 2026-11-15
---

**一句話**：上線前逐項打勾，避免「會回答但會闖禍」。

## 連線
- [ ] Webhook URL 已設定且 Use webhook 開啟 [S03]
- [ ] 已關閉 LINE 原生自動回應 [S03]
- [ ] 改完程式已部署新版本 [S03]

## 安全
- [ ] 驗證來源（簽章，或 Apps Script 的網址保密＋白名單）[S01][S03]
- [ ] 金鑰放 Script Properties [S03]
- [ ] 重複事件用 webhookEventId 去重 [S01]

## 回答品質
- [ ] AI 只依店家知識庫回答，不知道就說不知道 [S05][S06]
- [ ] 上線前用真實問句離線測試 [S05]
- [ ] 知識庫有人負責更新 [S05]

## 交棒
- [ ] 四種觸發條件都有設計 [S06]
- [ ] 交棒時帶完整對話紀錄 [S06]
- [ ] 營業時間外的回覆時段寫清楚 [S06]

## 相關頁面
- [真人交棒](../concepts/human-handoff.md)
- [安全・隱私・成本](../concepts/security-privacy-cost.md)
