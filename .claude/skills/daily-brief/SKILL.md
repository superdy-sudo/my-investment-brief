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
☐ เช็ควันที่ — weekend แจ้ง "ตลาดปิด ราคา T-1"
☐ เช็ค .env มี OPENAI_API_KEY ไหม
```

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
```

### 5. Save + Push

```bash
git add portfolio.md showcase/index.html
git commit -m "brief [วันที่]: [Top Pick] | [market 1 ประโยค]"
git push origin main
```

อัปเดต showcase/index.html ด้วย comment markers เดิม (แทนที่เฉพาะ content ระหว่าง markers)

---

## Close Brief (`/daily-brief close`)

```
📊 Close — [วันที่]

🌍 ปิด: S&P [+X%] | NASDAQ [+X%] | VIX [XX]

📌 Holdings (เฉพาะที่เปลี่ยน >1%):
   TICKER $XXX [+X%] | Thesis ✅/⚠️ | [เหตุผล]

❓ พรุ่งนี้ดูอะไร: [1-2 ข้อ]
```

Search เฉพาะตัวที่เปลี่ยน >1% หรือมี after-hours news — ที่เหลือไม่ต้อง search

---

## Top-up Mode (`/daily-brief topup [จำนวน]`)

```
1. อ่าน portfolio.md (ไม่ต้อง search)
2. Fetch ราคา Holdings + Top Pick ทั้งหมด
3. คัดกรอง:
   - Size Up: Holdings ลง ≥8% + thesis ✅ + kill buffer >10%
   - เข้าใหม่: Watchlist ที่ราคาอยู่ใน entry zone
4. ตอบ:
```

```
💰 Top-up แนะนำ — $[จำนวน]

[TICKER]  $XXX | [เหตุผล 1 ประโยค] | Action: [%]
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
