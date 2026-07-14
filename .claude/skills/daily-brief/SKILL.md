---
name: daily-brief
description: อัปเดตพอร์ต + Top Pick + Watchlist ประจำวัน
---

# Daily Brief — Minimal System

## หลักการ
> "ข่าวที่ไม่เปลี่ยน Thesis ไม่ต้องใส่"

เป้าหมายคือ **ช่วยตัดสินใจ** ไม่ใช่รวบรวมข่าว

---

## Pre-flight (ทำก่อนเสมอ — < 30 วินาที)

```
☐ อ่าน portfolio.md — ห้ามใช้ memory
☐ อ่าน knowledge/INDEX.md (สรุป 1 บรรทัด/ticker) — เปิด knowledge/[TICKER].md เต็มเฉพาะตัวที่จำเป็น (ราคาเปลี่ยนแรง/มี earnings ใกล้/user ถามเจาะจง) ประหยัด token
☐ เช็ควันที่ — weekend แจ้ง "ตลาดปิด ราคา T-1"
☐ เช็ค .env มี OPENAI_API_KEY ไหม
```

## ⚠️ กฎราคาหุ้น — curl (Bash) เท่านั้น ห้าม WebFetch tool

**ห้ามใช้ WebSearch สำหรับราคา** — AI summary ของ WebSearch มักคืนราคาเก่าหรือผิดพลาด

**ห้ามใช้ WebFetch tool ดึงราคาจาก Yahoo Finance** — พบว่า WebFetch tool (ที่ผ่าน AI summarization) โดน Yahoo block/fail บ่อยมาก (2026-07-13/14) แต่ยิง `curl` ตรงจาก Bash กลับใช้ได้ปกติ 100% — สาเหตุคือ WebFetch tool proxy โดน rate-limit/block ไม่ใช่ API ตายจริง

ใช้ **Bash curl** ตรง Yahoo Finance API (ต้องใส่ User-Agent ไม่งั้นบาง endpoint อาจ reject):
```bash
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://query1.finance.yahoo.com/v8/finance/chart/[TICKER]?interval=1d&range=1d"
```
Parse ค่า `meta.regularMarketPrice` จาก JSON output = ราคา real-time — fetch หลาย ticker พร้อมกันได้ด้วย loop เดียว:
```bash
for t in GWRE PLTR AVGO V SPGI; do
  echo "=== $t ==="
  curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://query1.finance.yahoo.com/v8/finance/chart/$t?interval=1d&range=1d" | grep -o '"regularMarketPrice":[0-9.]*'
done
```

**⚠️ ห้ามใช้วันที่จาก JSON/timestamp มาแปลงเอง** — Unix timestamp แปลงผิดบ่อย (เจอเคสจริง: ราคาถูกต้อง แต่บอกวันที่เป็น "May 2024" ทั้งที่จริงคือ Jul 2026)
→ **ใช้วันที่ปัจจุบันของระบบเสมอ** (วันที่รัน brief) ไม่ใช่วันที่จาก JSON/timestamp — ราคาที่ได้คือราคา ณ ตอนรันอยู่แล้ว ไม่ต้องพึ่งวันที่จาก API

**Fallback ถ้า curl โดน block ด้วย** (rare): ลอง `query2.finance.yahoo.com` แทน `query1` ก่อน ถ้ายัง fail ทั้งคู่ค่อย fallback ไป WebSearch ตามกฎเดิม (ราคาอาจ lag)

WebSearch ใช้ได้เฉพาะ: ค้นข่าว/catalyst เท่านั้น ห้ามใช้ดึงราคา

---

## Mode Detection

| Argument | Mode |
|----------|------|
| (ไม่มี) | Full Brief |
| `close` | Close Brief — สรุปปลายวัน |
| `topup [จำนวน]` | Top-up — แนะนำซื้อตัวไหน |
| `TICKER,...` | Spot Brief — วิเคราะห์ตัวที่ระบุ |

---

## Full Brief

### 1. ดึงข้อมูล (ทำพร้อมกัน)

**Holdings — fetch ราคาเฉพาะตัวที่เข้าเงื่อนไข:**
- มี earnings วันนี้ → WebSearch ข่าวเต็ม
- ราคาเปลี่ยน >3% → WebSearch หาสาเหตุ
- ที่เหลือ → fetch ราคาอย่างเดียว ไม่ search news

**Market (WebSearch 1 ครั้ง):**
- S&P, NASDAQ, VIX, 10Y Yield

**Top Pick:**
- fetch ราคา + เช็ค entry zone เทียบ portfolio.md

### 2. ตอบ 4 คำถามต่อ Holding ทุกตัว

```
[TICKER] $XXX [+X%]
├─ Thesis เปลี่ยนไหม?     ✅ No change / ⚠️ [อะไรเปลี่ยน]
├─ Valuation เปลี่ยนไหม?  ✅ Fair / ⚠️ Expensive / 🟢 Cheap
├─ Entry/Exit Zone?        ✅ ถืออยู่ (buffer X%) / 🚨 Kill ใกล้ / 🎯 TP1 ใกล้
└─ Action วันนี้           Hold / Watch / ⚠️ Review
```

### 3. Top Pick

```
🏆 Top Pick: [TICKER]
   ราคา: $XXX | Zone: $X–$X [✅ อยู่ใน zone / ⚠️ เกิน zone]
   เหตุผล: [1 ประโยค]
   ❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1]
   Action: Buy / Starter Position / Watch
```

ถ้าราคาเกิน entry zone → เปลี่ยน Top Pick ไปตัวถัดไปใน Watchlist

### 4. สรุปใน Chat

```
📊 [วันที่] — Daily Brief

🌍 ตลาด: S&P [+X%] | NASDAQ [+X%] | VIX [XX]

📌 Holdings:
   TICKER  $XXX [+X%] | ✅/⚠️/🚨 | [เหตุผล ถ้าเปลี่ยน]
   ...
   (ตัวที่ไม่เปลี่ยน Thesis → แสดงแค่ราคาและ ✅)

🏆 Top Pick: TICKER $XXX
   Action: [Buy/Starter/Watch] — [เหตุผล 1 ประโยค]
   ❓ ผิดได้ถ้า: [เหตุผลอันดับ 1]

📅 Earnings ใน 7 วัน: [ถ้ามี]
⚠️ ต้องทำวันนี้: [action เดียว หรือ "ไม่มี"]

🔮 Predictions for Today:
   1. [สิ่งที่คาดว่าจะเกิด — พร้อม trigger ที่จะ confirm/deny]
   2. [ถ้ามี]
   3. [ถ้ามี]
```

**หมายเหตุ:** Predictions section บังคับทุกครั้ง — Close Brief จะใช้ grade accuracy

### 5. Save + Push

```bash
git add portfolio.md showcase/index.html
git commit -m "brief [วันที่]: [Top Pick] | [market 1 ประโยค]"
git push origin main
```

อัปเดต showcase/index.html ด้วย comment markers เดิม (แทนที่เฉพาะ content ระหว่าง markers)

---

## Close Brief (`/daily-brief close`)

**เป้าหมาย:** ตรวจ prediction + เรียนรู้จากสิ่งที่ผิด + เตรียมพรุ่งนี้
**ไม่ใช่:** สรุปข่าวซ้ำ / เขียน Holdings ใหม่ทุกตัว / เขียน TP/Kill ซ้ำ

Search เฉพาะตัวที่เปลี่ยน >1% หรือมี after-hours news — ที่เหลือไม่ต้อง search

```
📊 Close — [วันที่]   🌍 ปิด: S&P [+X%] | NASDAQ [+X%] | VIX [XX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔮 1. Prediction Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[copy Predictions จาก Morning Brief มา grade]

   Predicted → Reality → ✅/❌
   [prediction 1]  → [เกิดจริง?]  → ✅/❌
   [prediction 2]  → [เกิดจริง?]  → ✅/❌

   Accuracy: X/X ([%])
   ผิดเพราะ: [ถ้าผิด — 1 ประโยค อย่า justify แค่อธิบาย]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 2. What's Changed (vs Morning Brief)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[เขียนเฉพาะตัวที่เปลี่ยน >1% หรือมีข่าวใหม่]
   TICKER [+X%] — [เหตุผล 1 ประโยค]
   ...
   (ถ้าไม่มีอะไรเปลี่ยน → "No material changes")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧭 3. Thesis Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[เฉพาะตัวที่เปลี่ยน — ตัวที่ No Change ไม่ต้องเขียน]
   TICKER → Improved / No Change / Weakened — [เหตุผล ≤1 บรรทัด]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 4. Lessons Learned (≤3 ข้อ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   • [สิ่งที่ตลาดสอนวันนี้ — ไม่ใช่แค่ fact แต่คือ pattern]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 5. Tomorrow Watch (≤3 ข้อ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   • [สิ่งที่ต้องดูพรุ่งนี้ — เฉพาะที่ actionable]
```

**Token target:** 700–900 tokens | อ่านจบ 3 นาที

---

## Top-up Mode (`/daily-brief topup [จำนวน]`)

```
1. อ่าน portfolio.md (ไม่ต้อง search)
2. Fetch ราคา Holdings + Top Pick ทั้งหมด
3. คัดกรอง:
   - Size Up: Holdings ลง ≥8% + thesis ✅ + kill buffer >10%
   - เข้าใหม่: Watchlist ที่ราคาอยู่ใน entry zone
4. **Concentration Risk Check** (เฉพาะ Size Up ของ ticker ที่ถืออยู่แล้ว) — คำนวณ % ของพอร์ตรวมที่ ticker นั้นจะกลายเป็นหลัง top-up นี้ ถ้าเกิน 40% ให้เติม "⚠️ Concentration สูง — จะเป็น ~X% ของพอร์ต" ต่อท้ายคำแนะนำ (ไม่ใช่ Avoid อัตโนมัติ แค่เตือน เพราะ style นี้ยอมรับ concentration สูง)
5. ตอบ:
```

```
💰 Top-up แนะนำ — $[จำนวน]

[TICKER]  $XXX | [เหตุผล 1 ประโยค] | Action: [%] [⚠️ Concentration สูง ถ้าเข้าเงื่อนไข]
[TICKER]  $XXX | [เหตุผล 1 ประโยค] | Action: [%]

❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1 ของตัวที่แนะนำ]
```

ไม่ save ไฟล์ — ตอบใน chat อย่างเดียว

---

## Spot Brief (`/daily-brief TICKER`)

```
1. Fetch ราคา + WebSearch news 48 ชม.
2. ตรวจ 4 Layer (ถ้าตัวใหม่ — ดู company-brief SKILL)
3. ตอบ:
```

```
[TICKER] — [ชื่อบริษัท]
ราคา: $XXX | Moat: Wide/Narrow/None
Thesis: [2 ประโยค]
Action: 🟢 Buy / 🟡 Starter / 🟠 Watch / 🔴 Avoid
❓ ผิดได้ถ้า: [เหตุผลอันดับ 1]
```

---

## กฎ

- ข่าวที่ไม่เปลี่ยน Thesis → ไม่ใส่
- Search เฉพาะ: earnings วันนี้ หรือ ราคาเปลี่ยน >3%
- ตัวที่เงียบ → แสดงแค่ราคา + ✅
- ทุก recommendation ต้องมี "❓ Thesis ผิดได้ถ้า"
- ห้ามแต่งข้อมูล — ถ้าหาไม่ได้บอกตรงๆ
