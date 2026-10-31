"""จัดกลุ่ม ticker จาก Finviz Market Scan โดย "อ่านเนื้อหา brief จริง" ไม่ตัดจากชื่อไฟล์อย่างเดียว

ใช้ (รันที่ root ของโปรเจกต์): python .claude/skills/daily-brief/scan_filter.py < scan.txt
  scan.txt = ticker คั่นด้วยช่องว่าง/ขึ้นบรรทัดใหม่ ตามลำดับ market cap

กลุ่มผลลัพธ์:
  HOLDING/WATCHLIST     อยู่ใน portfolio.md แล้ว — ตัดออก
  BRIEFED-ACTIVE        Layer 4 ล่าสุดเป็น Buy/Starter/Watch (ไม่มีคำว่า Avoid) — ตัดออก ไม่ต้องเทียบซ้ำ
  AVOID-TOO-RECENT      Avoid และ brief ล่าสุดอายุ <90 วัน — ไม่เข้า recheck (กฎตายตัว ข้อ 2)
  AVOID-NEEDS-READ      Avoid และอายุ >=90 วัน — **ต้องเปิดไฟล์อ่าน Layer 1 + Layer 4 เอง** เพื่อตัดสินข้อ 1
                        (Avoid เดิมมาจาก growth เพียงอย่างเดียว ไม่มี ❌ ที่ Layer 1) สคริปต์ไม่ตัดสินแทน
                        เพราะตรวจ ❌ อัตโนมัติจับเกินจริง (ข้อความ "ไม่มี ❌" ก็ติด)
  UNCLEAR               อ่าน Action ไม่ออก — ต้องเปิดไฟล์อ่านเอง ห้ามสรุปว่า "ไม่มี"
  MENTIONED-NO-BRIEF    ไม่มีไฟล์ brief แต่มีชื่ออยู่ใน archive/knowledge/portfolio.md — แสดงไฟล์ที่พบ ให้เปิดดูบริบทก่อน
  NEVER-SEEN            ไม่เคยปรากฏเลย = New Candidate จริง
                        (ถ้า mkt cap สูงมากแต่เพิ่งโผล่ ให้ตรวจก่อนว่าทำไมไม่เคยขึ้น — เช่น sales QoQ เพิ่งข้าม 30%)
"""
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # console Windows (cp874) พิมพ์อีโมจิไม่ได้
sys.stdin.reconfigure(encoding="utf-8")

ROOT = Path(".")
tickers = sys.stdin.read().split()

portfolio = (ROOT / "portfolio.md").read_text(encoding="utf-8")
table_tickers = set()
for line in portfolio.splitlines():
    m = re.match(r"\|\s*(?:~~)?\**([A-Z.\-]{1,6})\**(?:~~)?\s*(?:🆕)?\s*\|", line)
    if m:
        table_tickers.add(m.group(1))

briefs = {}
for f in (ROOT / "briefs").glob("*.md"):
    m = re.match(r"^([A-Z.\-]+)-(\d{4}-\d{2}-\d{2})\.md$", f.name)
    if m:
        briefs.setdefault(m.group(1), []).append((m.group(2), f))


def mentioned_in(t):
    r = subprocess.run(
        ["grep", "-rlwE", re.escape(t), "briefs", "archive", "knowledge", "portfolio.md"],
        capture_output=True, text=True, encoding="utf-8",
    )
    return r.stdout.split()[:2]


def layer4_action(text):
    hits = list(re.finditer(r"Layer 4[^\n]*Action[^\n]*\n+(.{0,300})", text, re.S))
    return " ".join(hits[-1].group(1).split())[:160] if hits else ""


for t in tickers:
    if t in table_tickers:
        print(f"{t}\tHOLDING/WATCHLIST")
        continue
    if t in briefs:
        d, f = sorted(briefs[t])[-1]
        act = layer4_action(f.read_text(encoding="utf-8"))
        age = (date.today() - date.fromisoformat(d)).days
        if not act:
            print(f"{t}\tUNCLEAR\t{d}\t(ไม่พบหัวข้อ Layer 4 Action)")
        elif re.search(r"avoid|🔴", act, re.I):
            tag = "AVOID-TOO-RECENT" if age < 90 else "AVOID-NEEDS-READ"
            print(f"{t}\t{tag}\t{d} (age {age}d)\t{act}")
        elif re.search(r"buy|starter|watch|🟢|🔵|🟠", act, re.I):
            print(f"{t}\tBRIEFED-ACTIVE\t{d}\t{act[:80]}")
        else:
            print(f"{t}\tUNCLEAR\t{d}\t{act}")
        continue
    hit = mentioned_in(t)
    print(f"{t}\t{'MENTIONED-NO-BRIEF' if hit else 'NEVER-SEEN'}\t{' '.join(hit)}")
