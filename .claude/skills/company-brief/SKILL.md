---
name: company-brief
description: Research a public company and produce a structured investment brief. Trigger when the user asks for a brief, research, or analysis on a stock ticker or company name.
---

# Company Brief — Future Compounder System

## เป้าหมาย
หาบริษัทที่มีโอกาสเป็น 3–10x ใน 5–10 ปี ไม่ใช่แค่หุ้นที่ดีวันนี้

---

## Layer 1: Quality Filter (ผ่านก่อน — ไม่ผ่านจบเลย)

ตรวจ 5 ข้อ จาก WebSearch + keen agent:

```
☐ Wide Moat — มีกำแพงป้องกันชัดเจน (brand / switching cost / network effect / cost advantage)
☐ Management ดี — track record + capital allocation + ไม่ dilute shareholders เกิน
☐ Balance Sheet แข็ง — Net Debt/EBITDA < 3x หรือมีเหตุผลชัดเจน
☐ Free Cash Flow ดี — FCF margin >10% หรือ FCF trend ขาขึ้น
☐ Debt ไม่สูงเกิน — interest coverage > 5x
```

**ถ้าไม่ผ่านข้อใดข้อหนึ่ง → จบ ไม่วิเคราะห์ต่อ**

ตอบว่า: "[TICKER] ไม่ผ่าน Quality Filter เพราะ [ข้อที่ fail] — ไม่แนะนำวิเคราะห์ต่อ"

---

## Layer 2: Compounder Filter (ตอบ 5 ข้อ)

```
1. บริษัทยังโตได้อีก 5–10 ปีไหม?
   → ตลาดยังไม่อิ่มตัว / ยังขยาย geography / product ใหม่ที่ชัดเจน

2. TAM ใหญ่พอไหม?
   → ตลาดปลายทางใหญ่กว่า market cap ปัจจุบัน ≥ 5x

3. Revenue/Growth ยังเร่งอยู่ไหม?
   → Revenue growth ≥ 15% YoY หรือ accelerating

4. มี Competitive Advantage ที่ยั่งยืนไหม?
   → อีก 10 ปี position แข็งแกร่งขึ้นหรืออย่างน้อยเท่าเดิม

5. ถ้าย้อนกลับมาจากปี 2036 จะเสียดายไหมที่ไม่ซื้อปี 2026?
   → ถามตรงๆ แล้วตอบให้สั้น ซื่อสัตย์
```

**ผ่าน ≥ 4/5 → ไปต่อ Layer 3**
**ผ่าน < 4/5 → Watchlist เฉย ๆ หรือ Avoid**

---

## Layer 3: Valuation

สรุปแค่ 3 ระดับ โดยใช้ Morningstar FV / GuruFocus / EV/FCF:

```
🟢 Cheap   — trading ต่ำกว่า fair value ≥ 20%
🟡 Fair    — ใกล้ fair value (±20%)
🔴 Expensive — เกิน fair value >20%
```

ถ้า Expensive → "รอ — อย่าไล่ราคา"

---

## Layer 4: Action

**ตอบแค่ข้อเดียว พร้อมเหตุผลไม่เกิน 3 บรรทัด:**

```
🟢 Buy              — Cheap + ผ่าน ≥ 4/5 + thesis แข็ง
🔵 Starter Position — Fair + ผ่าน ≥ 4/5 + มี catalyst ชัด
🟠 Watch            — ดีแต่ราคายัง Expensive หรือรอ catalyst
🔴 Avoid            — ไม่ผ่าน Quality หรือ Compounder < 4/5
```

---

## คำถามบังคับ (ทุก recommendation)

> **"อะไรคือเหตุผลอันดับ 1 ที่ทำให้ Thesis นี้ผิด?"**

ตอบ 1 ประโยค — ห้ามใส่หลายข้อ เลือก worst enemy จริงๆ

ตัวอย่าง:
- AVGO → "AI CapEx ชะลอจนลูกค้าลดการลงทุน hyperscaler"
- PLTR → "Commercial growth ต่ำกว่าที่ตลาดคาดต่อเนื่อง 2+ ไตรมาส"

---

## Output Format

บันทึก `briefs/[TICKER]-[YYYY-MM-DD].md`:

```markdown
# [TICKER] — [ชื่อบริษัท]
วันที่: [YYYY-MM-DD]

## บริษัทนี้ทำอะไร?
[2-3 ประโยค ภาษาคน — ทำอะไร เงินมาจากไหน ทำไมเปลี่ยนยาก]

## Layer 1: Quality Filter
- Wide Moat: ✅/❌ [เหตุผล]
- Management: ✅/❌ [เหตุผล]
- Balance Sheet: ✅/❌ [Net Debt/EBITDA]
- FCF: ✅/❌ [FCF margin หรือ trend]
- Debt: ✅/❌ [interest coverage]

ผลรวม: ✅ ผ่าน / ❌ ไม่ผ่าน (fail ที่ [ข้อ])

## Layer 2: Compounder Filter
1. โตได้อีก 5-10 ปี? ✅/❌ — [เหตุผล]
2. TAM ใหญ่พอ? ✅/❌ — [ตัวเลข TAM]
3. Growth ≥15%? ✅/❌ — [ตัวเลข]
4. Competitive Advantage ยั่งยืน? ✅/❌ — [เหตุผล]
5. เสียดายไม่ซื้อปี 2026? ✅/❌ — [เหตุผล]

ผลรวม: X/5 → [ผ่าน/ไม่ผ่าน]

## Layer 3: Valuation
Fair Value: $XXX (แหล่ง: [Morningstar/GuruFocus/ประมาณการ])
ราคาปัจจุบัน: $XXX
ส่วนต่าง: [+X% Expensive / -X% Cheap]
สรุป: 🟢 Cheap / 🟡 Fair / 🔴 Expensive

## Layer 4: Action
**[🟢 Buy / 🔵 Starter / 🟠 Watch / 🔴 Avoid]**
[เหตุผล ≤ 3 บรรทัด]

## ❓ Thesis ผิดได้ถ้า
[เหตุผลอันดับ 1 — 1 ประโยค]

## Kill Condition
ขายถ้า: [observable event ที่ทำให้ขาย — 1 ประโยค]
```

---

## กฎ

- ห้ามแต่งข้อมูล — ถ้าหาไม่ได้เขียน "ไม่พบข้อมูล"
- Thesis killer ต้องเป็น 1 ข้อ — ห้ามใส่หลายข้อ
- ถ้าไม่ผ่าน Layer 1 → หยุดทันที ไม่ต้องทำ Layer ต่อไป
- Action ต้องเป็น 1 คำ — ห้ามตอบกำกวม
