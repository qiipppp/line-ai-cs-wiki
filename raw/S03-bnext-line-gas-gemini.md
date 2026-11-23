---
id: S03
title: 把LINE變成待辦小幫手！4步驟教你用Google Apps Script串接Gemini — 數位時代
url: https://www.bnext.com.tw/article/91909/line-ai-todo-gas-gemini
type: 中文教學文章
fetched: 2026-11-15
完整度: 全文擷取（WebFetch）
---

## 擷取筆記（以中文改寫）

- 架構：LINE 訊息經 webhook 進入 Apps Script 網頁應用程式 → Gemini 解讀文字或圖片 → 結果寫入 Google 試算表 → 有日期時間就建立日曆事件 → 用 LINE Reply API 回覆。不用租伺服器。
- 四個元件：Google 試算表（資料庫）、Google Apps Script（執行環境）、Gemini API（語意理解）、LINE 官方帳號（前端介面）。
- API 金鑰放在 Script Properties（指令碼屬性），不寫進程式碼。
- 先在 LINE Official Account Manager 建立官方帳號，再啟用 Messaging API，才會在 Developers Console 產生 channel，接著發行 channel access token。
- Prompt 要求 Gemini **只回 JSON**：summary、category（固定三選一：繳費／會議／其他）、date（YYYY-MM-DD，相對日期要換算）、time（HH:mm，沒有就留空）。缺的欄位留空字串，不准編造。
- Gemini 沒有回傳結果時，送出備援訊息請使用者重傳。
- 部署：Deploy → New deployment → Web app；執行身分「我」、存取權「任何人」；複製 `/exec` 網址貼到 LINE Webhook URL，開啟 Use webhook 並按 Verify。
- 每次改程式都要「編輯部署 → 新版本」，否則不會生效；網址不變。
- 測試建議：先測「Gemini → 試算表」，通過後再接 LINE。
- 要關閉 LINE 官方帳號的自動回應，否則預設回應會干擾。
- Verify 出現 302 Found 屬於 Apps Script 正常轉址，可直接傳訊息測試。
- 模型會下架：機器人突然失效時檢查是否有新模型名稱。
- Apps Script 讀不到 LINE 簽章 header，知道 `/exec` 網址的人可以送假請求；對策是網址保密或加 userId 白名單。
- 免費層的 Gemini 請求可能被用於改善 Google 產品，避免放敏感資料。
- 回覆（reply）免費、不計入每月推播額度（文章寫 200 則，屬當時方案）；分享給多人仍可能用完推播額度或 Gemini 免費額度。
