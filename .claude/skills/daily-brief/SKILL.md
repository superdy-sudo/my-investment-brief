---
name: daily-brief
description: อัปเดตพอร์ต + Top Pick + Watchlist ประจำวัน
---

# Daily Brief Skill

## Trigger
/daily-brief

---

## Step 0: อ่าน config
- อ่าน `CLAUDE.md` → investment style
- อ่าน `portfolio.md` → Holdings, Top Pick ปัจจุบัน, Watchlist

---

## Step 1: Update Holdings (ทำก่อนเสมอ)

dispatch augustus พร้อมกันทุกตัวใน Holdings (run_in_background: true)

หาข้อมูลแต่ละตัว:
- ราคาปัจจุบัน → P&L %
- news 24-48 ชม.
- analyst rating เปลี่ยนไหม
- thesis ยังใช้ได้ไหม → ✅ / ⚠️ / ❌

save `briefs/<TICKER>-update-<YYYY-MM-DD>.md`
อัปเดต showcase Holdings section

---

## Step 2: Top Pick — brief ซ้ำหรือเปลี่ยน

### อ่าน Top Pick ปัจจุบันจาก portfolio.md

**ถ้ายังไม่มี Top Pick เลย → หาครั้งแรก (ดู Step 2B)**

**ถ้ามี Top Pick อยู่แล้ว → เช็ค 3 ข้อนี้ก่อน:**

| เงื่อนไข | ทำอะไร |
|----------|--------|
| thesis ยังดี + ไม่มีตัวใหม่ดีกว่าชัดเจน | brief ซ้ำตัวเดิม อัปเดตราคา/news ล่าสุด |
| thesis ⚠️ เฝ้าระวัง | brief ซ้ำ แต่เพิ่ม warning ชัดขึ้น |
| thesis ❌ พัง หรือ ซื้อไปแล้ว | หา Top Pick ใหม่ (ดู Step 2B) |

> **หลักการ:** ไม่ต้องหาใหม่ทุกวัน ถ้าตัวเดิมยังดีอยู่ brief ซ้ำได้เลย

---

### Step 2B: หา Top Pick ใหม่ (เฉพาะเมื่อต้องเปลี่ยน)

dispatch augustus ใช้ **Mode A — Stock Selection**

**ลำดับที่ต้องทำ (ห้ามข้าม):**

1. **Morningstar Wide Moat list ก่อน**
   - หุ้นที่ผ่าน moat screening จาก analyst มืออาชีพแล้ว
   - ไม่ต้องเดาว่ามี moat ไหม — Morningstar ตรวจให้แล้ว

2. **Cross-check กับ Quality Fund 13F**
   - Fundsmith / Polen / Akre / Ensemble ถืออะไรอยู่
   - หุ้นที่ติดทั้ง Morningstar + Quality Fund = candidate แข็งแกร่งที่สุด

3. **Hard Filter (ตัดออกถ้าไม่ผ่าน):**
   - ❌ ไม่ใช่ US stock (NYSE/NASDAQ)
   - ❌ Market cap < $2B
   - ❌ Revenue ลด YoY (ดูจาก StockAnalysis.com)
   - ❌ D/E > 3x โดยไม่มีเหตุผล

4. **Valuation check ด้วย GuruFocus**
   - เลือกตัวที่ trading ใกล้หรือต่ำกว่า fair value

5. **เลือก 1 ตัวที่ดีที่สุด** — quality > novelty

ดูรายละเอียดวิธีค้นทั้งหมดใน `augustus.md` → Mode A

dispatch keen + North + augustus วิเคราะห์ตัวนั้น
save `briefs/<TICKER>-<YYYY-MM-DD>.md`

อัปเดต `portfolio.md` → บันทึก Top Pick ใหม่

---

## Step 3: Update Watchlist

อ่าน Watchlist จาก `portfolio.md`

**สำหรับแต่ละตัวใน Watchlist:**
- ถ้ามีการขยับ ±3%+ หรือ news สำคัญ → augustus อัปเดตสั้นๆ
- ถ้าเงียบ → ข้ามไป ไม่ต้อง brief

**Auto-drop rule:**
- ถ้าตัวไหนเงียบมา 14 วันติด (ไม่มี news สำคัญ + ราคาไม่ขยับ) → ลบออกจาก Watchlist อัตโนมัติ
- แจ้งใน summary ว่า "ลบ TICKER ออก — เงียบ 14 วัน"

**Watchlist max 10 ตัว**
- Top Pick เก่าที่เปลี่ยนแล้ว → ย้ายเข้า Watchlist อัตโนมัติ (ถ้ายังไม่ถึง 10)
- ถ้า list เต็ม → ไม่เพิ่มใหม่จนกว่าจะมีตัวออก

---

## Step 4: Bull vs Bear Debate (Gemini)

หลัง brief Top Pick เสร็จ → dispatch bear agent (run_in_background: true)
- bear อ่าน brief → เรียก Gemini API → หา bear case
- save `briefs/<TICKER>-bear-<YYYY-MM-DD>.md`
- save `briefs/<TICKER>-debate-<YYYY-MM-DD>.md`

ถ้า Top Pick ซ้ำตัวเดิม → ข้ามขั้นตอนนี้ได้ (debate เดิมยังใช้ได้)

---

## Step 5: อัปเดต showcase/index.html

Layout:
1. **🏆 Tier List** — ทุกตัวที่เคย brief (S/A/B/C)
2. **📌 Holdings** — SPGI, CME, MA + P&L
3. **🏆 Top Pick วันนี้** — 1 card เด่น พร้อม debate verdict
4. **👁 Watchlist** — เฉพาะตัวที่มีความเคลื่อนไหว
5. **📅 Scout Calendar** — brief เต็มเรียงตามวัน

**Card ทุกใบต้องมี ACTION VERDICT ที่บนสุดเสมอ — นี่คือสิ่งสำคัญที่สุด:**

```
🟢 เข้าได้เลย
   เหตุผล: [1-2 ประโยค ระบุว่าทำไมตอนนี้ถึงเหมาะ]
   เงื่อนไข: [ซื้อที่ราคาไหน หรือจำนวนเท่าไหร่]

🟡 รอก่อน
   รออะไร: [ระบุ catalyst หรือเงื่อนไขที่ต้องรอ เช่น "รอ earnings Q2", "รอราคาลงถึง $X"]
   ดูอีกครั้ง: [วันที่หรือ event ที่จะ re-evaluate]

🔴 หลีกเลี่ยง
   เหตุผล: [ระบุชัดว่าทำไม — valuation แพง / thesis พัง / leverage สูง]
```

Holdings ใช้:
```
✅ ถือต่อ — [เหตุผล 1 ประโยค]
⚠️ ระวัง — [สิ่งที่ต้องติดตาม]
🚨 พิจารณาขาย — [เหตุผล + kill condition ที่ถูก trigger]
```

**Card ทุกใบต้องมี section "🏢 บริษัทนี้ทำอะไร?" เสมอ:**
- เขียนเป็น "ภาษาคน" — อธิบายเหมือนคุยกับเพื่อนที่ไม่รู้เรื่องหุ้น
- ต้องตอบ 3 ข้อ: (1) ทำธุรกิจอะไร (2) เงินมาจากไหน (3) ทำไมคนเปลี่ยนไปใช้เจ้าอื่นได้ยาก
- ห้ามใช้ศัพท์เทคนิคโดยไม่อธิบาย
- ความยาว 3-4 บรรทัด อ่านจบใน 20 วินาที

**Tier List อัปเดต:**
- S = Bull ชนะ + moat แข็ง + valuation fair
- A = ดีแต่รอ หรือ valuation stretched
- B = มีข้อกังวล หรือ bear ชนะ
- C = ไม่ตรง style

---

## Step 6: สรุปใน chat

```
📌 Holdings:
   SPGI [+X%] ✅ | CME [+X%] ✅ | MA [+X%] ✅

🏆 Top Pick: TICKER (ซ้ำ / ใหม่)
   thesis: ยังดีอยู่ — [เหตุผล 1 ประโยค]
   debate: Bull ชนะ / Bear ชนะ / Tie

👁 Watchlist: X ตัว (Y ตัวมีการขยับ, Z ตัวถูก drop)

🌐 Showcase: อัปเดตแล้ว
```

---

## Rules

- ห้ามแต่งข้อมูล ถ้าไม่พบให้บอกตรงๆ
- augustus ห้ามทำนายตลาด รายงานเฉพาะ observable signals
- brief ซ้ำได้ถ้าตัวเดิมยังดี ไม่ต้องหาใหม่เพื่อความแปลกใหม่
- save ทุกอย่างลงไฟล์เสมอ ไม่ทิ้งไว้แค่ใน chat
