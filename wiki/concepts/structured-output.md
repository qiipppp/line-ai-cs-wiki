---
title: 結構化輸出（讓 AI 只回 JSON）
type: concept
sources: [S03]
updated: 2026-11-15
---

**一句話定義**：要求 AI 用固定欄位格式回答，程式才能穩定讀取、寫入資料表。

**比喻**：請客人填「表單」而不是寫「作文」——欄位固定，店員才好處理。

## 重點
- S03 的 prompt 要求 Gemini **只回 JSON**，四個欄位：summary、category、date、time [S03]
- category 限定三選一（繳費／會議／其他），避免 AI 自創分類 [S03]
- 日期統一 YYYY-MM-DD，「明天」等相對日期要換算 [S03]
- **缺的欄位留空字串，不准編造** [S03]

## 範例（依 S03 的欄位設計，改寫為客服情境）【推論】

```json
{ "intent": "預約", "date": "2026-11-20", "time": "14:00", "need_human": false }
```

## 相關頁面
- [Apps Script + Gemini](gas-gemini-serverless.md)
- [知識庫與防亂講](grounding-knowledge-base.md)
