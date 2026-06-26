---
name: brief
description: วิเคราะห์หุ้นรายตัว — 4 Layer + Bull/Bear + บันทึก showcase และ briefs/
---

# /brief [TICKER] — Company Brief

## Input
```
/brief AAPL
/brief NVDA
```

---

## Pre-flight

```
☐ อ่าน portfolio.md — เช็คว่า TICKER อยู่ใน Holdings หรือ Watchlist
☐ ห้ามแต่งข้อมูล — ถ้าหาไม่ได้เขียน "ไม่พบข้อมูล"
```

---

## ขั้นตอน

### 1. ดึงข้อมูล (WebSearch พร้อมกัน)

```
☐ ราคาปัจจุบัน + % change
☐ Revenue, EPS, FCF margin (2 ปีล่าสุด)
☐ Net Debt/EBITDA + Interest coverage
☐ Morningstar Fair Value หรือ GuruFocus GF Value
☐ ข่าว/catalyst สำคัญ 30 วันล่าสุด
☐ Short interest + insider activity (ถ้ามี)
```

---

### 2. วิเคราะห์ 4 Layer

**Layer 1: Quality Filter** — ถ้าไม่ผ่านข้อใดข้อหนึ่ง หยุดทันที

```
☐ Wide Moat (brand / switching cost / network effect / cost advantage)
☐ Management ดี — capital allocation + ไม่ dilute เกิน
☐ Balance Sheet แข็ง — Net Debt/EBITDA < 3x
☐ FCF margin >10% หรือ trend ขาขึ้น
☐ Interest coverage > 5x
```

**Layer 2: Compounder Filter** (≥4/5 ผ่าน)

```
1. โตได้อีก 5–10 ปีไหม?
2. TAM ใหญ่กว่า market cap ≥5x ไหม?
3. Revenue growth ≥15% YoY หรือ accelerating?
4. Competitive advantage ยั่งยืนอีก 10 ปี?
5. ถ้าย้อนมาจากปี 2036 จะเสียดายที่ไม่ซื้อปี 2026?
```

**Layer 3: Valuation**

```
🟢 Cheap     — ต่ำกว่า fair value ≥20%
🟡 Fair      — ±20% ของ fair value
🔴 Expensive — เกิน fair value >20%
```

**Layer 4: Action**

```
🟢 Buy              — Cheap + ≥4/5 + thesis แข็ง
🔵 Starter Position — Fair + ≥4/5 + catalyst ชัด
🟠 Watch            — ดีแต่ราคา Expensive หรือรอ catalyst
🔴 Avoid            — ไม่ผ่าน Quality หรือ <4/5
```

---

### 3. Bull/Bear Case

**Bull Case** — เหตุผล 3 ข้อที่ทำให้ราคาขึ้น 50–100% ใน 3–5 ปี
**Bear Case** — เหตุผล 3 ข้อที่ทำให้ thesis พังหรือราคาร่วงหนัก

จบด้วย: **"❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1 — 1 ประโยค]"**

---

### 4. Output ใน Chat

```
📋 [TICKER] — [ชื่อบริษัท]  [วันที่]
[sector tag] | [moat type]

💰 ราคา: $XXX [+X%] | Fair Value: $XXX | [🟢 Cheap / 🟡 Fair / 🔴 Expensive]

━━ Layer 1: Quality ━━
Wide Moat    ✅/❌ — [เหตุผล]
Management   ✅/❌ — [เหตุผล]
Balance Sheet✅/❌ — Net Debt/EBITDA [X.Xx]
FCF          ✅/❌ — [margin หรือ trend]
Debt         ✅/❌ — Interest coverage [Xx]
→ ผล: ✅ ผ่าน / ❌ หยุด ([ข้อที่ fail])

━━ Layer 2: Compounder (X/5) ━━
1. โตได้ 5–10 ปี?    ✅/❌ — [เหตุผล]
2. TAM ≥5x mkt cap?  ✅/❌ — [ตัวเลข]
3. Growth ≥15%?      ✅/❌ — [ตัวเลข]
4. Moat ยั่งยืน?     ✅/❌ — [เหตุผล]
5. เสียดายไม่ซื้อ?   ✅/❌ — [เหตุผล]

━━ Layer 3: Valuation ━━
Fair Value: $XXX (แหล่ง: Morningstar/GuruFocus)
ส่วนต่าง: [−X% Cheap / +X% Expensive]

━━ Layer 4: Action ━━
[🟢 Buy / 🔵 Starter / 🟠 Watch / 🔴 Avoid]
[เหตุผล ≤2 บรรทัด]

━━ Bull / Bear ━━
🐂 Bull: [ข้อ 1] / [ข้อ 2] / [ข้อ 3]
🐻 Bear: [ข้อ 1] / [ข้อ 2] / [ข้อ 3]

❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1]
🚨 ขายถ้า: [observable event — 1 ประโยค]
```

---

### 5. Save ไฟล์

**บันทึก** `briefs/[TICKER]-[YYYY-MM-DD].md` — ใช้ output format เดิม

**อัปเดต showcase/index.html:**

หาก `<!-- BRIEF_[TICKER]_START -->` มีอยู่แล้ว → แทนที่ content ระหว่าง markers

หากไม่มี → inject card ใหม่ก่อน `<!-- WATCHLIST -->` โดยใช้ format:

```html
<!-- BRIEF_[TICKER]_START -->
<div class="card" style="border-color:[action-color];">
  <div class="card-header">
    <div>
      <div class="ticker">[TICKER]</div>
      <div class="company-name">[ชื่อบริษัท]</div>
    </div>
    <span class="badge" style="background:[action-color];">[BUY/STARTER/WATCH/AVOID]</span>
  </div>
  <div class="sector-tag">[sector]</div>
  <div class="moat-tag">[moat type]</div>
  <div class="metrics">
    <div class="metric"><div class="metric-label">ราคา</div><div class="metric-value">$[XXX]</div></div>
    <div class="metric"><div class="metric-label">Fair Value</div><div class="metric-value">$[XXX]</div></div>
    <div class="metric"><div class="metric-label">Valuation</div><div class="metric-value">[🟢/🟡/🔴] [Cheap/Fair/Exp]</div></div>
    <div class="metric"><div class="metric-label">Compounder</div><div class="metric-value">[X]/5</div></div>
  </div>
  <div class="action-box action-[enter/wait/hold/avoid]">
    <span class="action-label">[🟢 Buy / 🔵 Starter / 🟠 Watch / 🔴 Avoid]</span>
    <div class="action-detail">[เหตุผล ≤2 บรรทัด]</div>
  </div>
  <div style="font-size:0.8rem;margin-top:8px;">
    <span style="color:#68d391;">🐂 Bull:</span> [ข้อ 1 — สั้น]<br>
    <span style="color:#fc8181;">🐻 Bear:</span> [ข้อ 1 — สั้น]
  </div>
  <div class="wrong-box" style="margin-top:8px;">
    <strong>❓ Thesis ผิดได้ถ้า</strong>[เหตุผลอันดับ 1]
  </div>
  <div class="updated-at">[วันที่]</div>
</div>
<!-- BRIEF_[TICKER]_END -->
```

**action-color mapping:**
- Buy → `#68d391`
- Starter → `#4299e1`  
- Watch → `#f6ad55`
- Avoid → `#fc8181`

**action class mapping:**
- Buy → `action-enter`
- Starter → `action-hold`
- Watch → `action-wait`
- Avoid → `action-avoid`

จากนั้น push:
```bash
git add briefs/ showcase/index.html
git commit -m "brief [TICKER] [DATE]: [action] | [valuation] | [thesis killer สั้น]"
git push origin main
```

---

## กฎ

- ไม่ผ่าน Layer 1 → หยุดทันที แสดงแค่ข้อที่ fail
- Thesis killer ต้องเป็น 1 ข้อเท่านั้น
- Bull/Bear แต่ละข้อต้องเป็น observable fact ไม่ใช่ wish
- Action ต้องชัด 1 คำ — ห้ามกำกวม
