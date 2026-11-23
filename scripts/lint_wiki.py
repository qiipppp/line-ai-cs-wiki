#!/usr/bin/env python3
"""
lint_wiki.py — LLM Wiki 健康檢查（CLAUDE.md 第 4.3 節的自動化版本）

用法：
    python3 scripts/lint_wiki.py          # 在 repo 根目錄執行

檢查項目（每一項對應 workflow 圖中的一個「檢查節點」）：
  L1 frontmatter：每頁要有 title / type / sources / updated
  L2 sources 存在：frontmatter 的 S01… 必須在 raw/ 找得到
  L3 內文引用：內文出現的 [Sxx] 必須存在於 raw/，且列在該頁 frontmatter
  L4 斷鏈：相對路徑 .md 連結要指到真的檔案
  L5 孤兒頁：除了 index.md，每頁至少被另一頁連到
  L6 index 完整：index.md 要收錄所有頁面，頁數宣告要正確
  L7 synthesis 至少引用 2 個來源
  S1 簡報對應：index.html 每張 slide 都要有 data-wiki，且指向存在的 Wiki 頁
  S2 簡報來源：slide 的 data-src 必須是該 Wiki 頁 sources 的子集合

教學註解：
  - 用 re（正規表達式）抓 frontmatter 與連結，不需要安裝任何套件。
  - 每個檢查都把錯誤放進 errors 清單，最後一次列出，方便 AI 一次修完再重跑（lint loop）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
SLIDES = ROOT / "index.html"

errors: list[str] = []
warnings: list[str] = []


def parse_frontmatter(text: str) -> dict:
    """抓出 --- 包住的 YAML 區塊，只解析本專案用到的簡單 key: value 格式。"""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def parse_list(value: str) -> list[str]:
    """把 '[S01, S03]' 轉成 ['S01', 'S03']。"""
    return [x.strip() for x in value.strip("[]").split(",") if x.strip()]


# ---- 讀取 raw/ 裡有哪些來源 ID ----
raw_ids = set()
for p in RAW.glob("S*.md"):
    fm = parse_frontmatter(p.read_text(encoding="utf-8"))
    if fm.get("id"):
        raw_ids.add(fm["id"])

pages = sorted(WIKI.rglob("*.md"))
rel = lambda p: p.relative_to(WIKI).as_posix()
page_sources: dict[str, set] = {}
inbound: dict[str, int] = {rel(p): 0 for p in pages}

for p in pages:
    text = p.read_text(encoding="utf-8")
    name = rel(p)
    fm = parse_frontmatter(text)

    # L1
    for key in ("title", "type", "sources", "updated"):
        if key not in fm:
            errors.append(f"L1 {name}: frontmatter 缺少 {key}")
    srcs = set(parse_list(fm.get("sources", "")))
    page_sources[name] = srcs

    # L2
    for s in srcs - raw_ids:
        errors.append(f"L2 {name}: frontmatter 來源 {s} 在 raw/ 不存在")

    # L3（去掉 frontmatter 後再找 [Sxx]）
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    for s in set(re.findall(r"\[(S\d\d)\]", body)):
        if s not in raw_ids:
            errors.append(f"L3 {name}: 內文引用 [{s}] 在 raw/ 不存在")
        elif s not in srcs:
            errors.append(f"L3 {name}: 內文引用 [{s}] 沒列在 frontmatter sources")

    # L4 + 計算被連結次數
    for target in re.findall(r"\]\(([^)#]+\.md)\)", body):
        dest = (p.parent / target).resolve()
        if not dest.exists():
            errors.append(f"L4 {name}: 斷鏈 → {target}")
        elif WIKI in dest.parents and dest != p.resolve():
            inbound[dest.relative_to(WIKI).as_posix()] += 1

    # L7
    if fm.get("type") == "synthesis" and len(srcs) < 2:
        errors.append(f"L7 {name}: synthesis 只引用 {len(srcs)} 個來源（至少 2）")

# L5
for name, n in inbound.items():
    if name != "index.md" and n == 0:
        errors.append(f"L5 {name}: 孤兒頁（沒有任何頁面連到它）")

# L6
index_text = (WIKI / "index.md").read_text(encoding="utf-8")
listed = set(re.findall(r"\]\(([^)]+\.md)\)", index_text))
for name in inbound:
    if name != "index.md" and name not in listed:
        errors.append(f"L6 index.md 沒有收錄 {name}")
m = re.search(r"共 (\d+) 頁", index_text)
real = len(pages) - 1
if m and int(m.group(1)) != real:
    errors.append(f"L6 index.md 宣告共 {m.group(1)} 頁，實際 {real} 頁")

# S1 / S2 簡報對應檢查
slide_count = 0
if SLIDES.exists():
    html = SLIDES.read_text(encoding="utf-8")
    # 先移除 HTML 註解：第 3 次 lint 時，<head> 註解裡的範例 <section class="slide"> 被誤判成第 1 張投影片
    html = re.sub(r"<!--.*?-->", "", html, flags=re.S)
    for i, tag in enumerate(re.findall(r"<section[^>]*class=\"slide[^\"]*\"[^>]*>", html), 1):
        slide_count += 1
        wiki_attr = re.search(r'data-wiki="([^"]*)"', tag)
        src_attr = re.search(r'data-src="([^"]*)"', tag)
        if not wiki_attr:
            errors.append(f"S1 slide {i}: 沒有 data-wiki")
            continue
        wiki_pages = [w.strip() for w in wiki_attr.group(1).split(",") if w.strip()]
        allowed = set()
        for w in wiki_pages:
            if w not in page_sources:
                errors.append(f"S1 slide {i}: data-wiki 指向不存在的頁面 {w}")
            else:
                allowed |= page_sources[w]
        if src_attr:
            for s in [x.strip() for x in src_attr.group(1).split(",") if x.strip()]:
                if s not in allowed:
                    errors.append(f"S2 slide {i}: data-src {s} 不在對應 Wiki 頁的 sources 裡")
else:
    warnings.append("找不到 index.html，略過簡報檢查")

# ---- 輸出 ----
print(f"Wiki 頁面 {len(pages)}｜raw 來源 {len(raw_ids)}｜投影片 {slide_count}")
for w in warnings:
    print("WARN ", w)
if errors:
    for e in errors:
        print("FAIL ", e)
    print(f"\n❌ {len(errors)} 個問題，請修正後重跑（lint loop）")
    sys.exit(1)
print("✅ 全部檢查通過")
