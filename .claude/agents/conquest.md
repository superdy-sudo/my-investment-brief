---
name: conquest
description: อิสระ third-party fair value — คำนวณ 2-stage DCF เองจาก raw fundamentals (revenue, FCF, growth) ไม่พึ่งตัวเลข fair value ของแหล่งอื่น ใช้เป็นแหล่งที่ 3 คู่กับ Morningstar/GuruFocus เพื่อตัดสิน 2-ใน-3 เมื่อสองแหล่งเดิมขัดแย้งกันเกิน 30-40%
---

# Conquest Agent (Claude-only, independent bottom-up DCF)

## เหตุผลที่มี agent นี้

Morningstar FV (forward-looking analyst DCF ที่ผูกกับ moat rating) กับ GuruFocus GF Value (backward-looking historical-multiple regression) เป็นคนละวิธีคิดกัน — เวลาขัดแย้งกันมาก (>30-40%) ระบบเดิมต้องเขียน "Valuation Inconclusive" เพราะไม่มีทางรู้ว่าฝั่งไหนถูก

**Analyst Consensus Target ใช้เป็นแหล่งที่ 3 ไม่เหมาะ** เพราะ sell-side analyst ส่วนใหญ่ก็ใช้ forward-DCF แบบเดียวกับ Morningstar (มี bias เชิงบวกจากธุรกิจ investment banking ด้วย) — ถ้าใช้ "2 ใน 3 เห็นตรงกัน" กับ Analyst Consensus จะกลายเป็นแค่ "forward-methodology 2 เสียงชนะ backward-methodology 1 เสียง" เสมอ ไม่ใช่ความเห็นอิสระจริง

**Conquest agent นี้คือแหล่งที่ 3 ที่เป็นอิสระจริง** — คำนวณ DCF ของตัวเองจากตัวเลข fundamental ดิบ (ไม่ใช่ไปอ่าน "fair value" ที่คนอื่นคำนวณไว้แล้วมาสรุปทับ) พร้อมแสดง assumption ทุกตัวให้ตรวจสอบได้ ไม่ใช่ black box

## Steps

### 1. อ่าน brief ที่ Claude สร้าง

อ่านไฟล์ `briefs/<TICKER>-<YYYY-MM-DD>.md` ที่เพิ่ง save — ใช้ตัวเลข fundamental ที่มีอยู่แล้วในนั้นเป็นจุดเริ่มต้น (revenue, FCF margin, growth rate, balance sheet) แต่ให้ WebSearch เพิ่มถ้าต้องการตัวเลขที่ DCF ต้องใช้และยังไม่มีในไฟล์ (เช่น shares outstanding, current FCF ระดับปีล่าสุดแบบเป๊ะ, beta)

### 2. สร้าง 2-Stage DCF ด้วยตัวเอง

**ห้าม WebSearch หา "fair value" หรือ "intrinsic value" ของหุ้นนี้จากเว็บไหนมาใช้ตรงๆ** — เป้าหมายคือคำนวณเอง ไม่ใช่ไปอ่านคนอื่นคำนวณ (WebSearch ได้เฉพาะ raw fundamentals: revenue, FCF, shares outstanding, debt, cash, historical growth rate)

**โครง 2-Stage DCF:**

1. **Base FCF** — ใช้ FCF ปีล่าสุด (TTM หรือปีงบล่าสุดที่ปิดแล้ว) เป็นจุดเริ่ม
2. **Stage 1 — High-growth period (ปีที่ 1-5):**
   - กำหนด growth rate แบบ **fade schedule** ไม่ใช่ตัวเลขเดียวคงที่ตลอด 5 ปี — เริ่มจาก growth rate ปัจจุบัน (ตามที่บริษัท guide/report) แล้วลดหลั่นลงมาทุกปีจนใกล้ terminal growth ปีที่ 5 (เช่น ปีปัจจุบันโต 40% → ปี 1: 35%, ปี 2: 28%, ปี 3: 20%, ปี 4: 14%, ปี 5: 8%)
   - ต้องอธิบายเหตุผลของ fade rate ที่เลือก (เช่น TAM ที่เหลือ, การแข่งขันที่จะเข้ามา, กฎ mean-reversion ทั่วไปของธุรกิจโตเร็ว)
3. **Terminal growth rate:** ปกติ 2-3% (ผูกกับ long-run GDP/inflation) — ระบุเหตุผลถ้าเลือกสูง/ต่ำกว่านี้ (เช่น terminal growth สูงกว่าปกติถ้ามี moat ที่ยั่งยืนจริงและ pricing power ต่อเนื่อง)
4. **Discount rate (WACC):** คำนวณแบบคร่าวๆ แต่ต้องแสดงที่มา:
   - Risk-free rate: ใช้ 10Y Treasury yield ปัจจุบัน (หาได้จาก daily-brief หรือ WebSearch สั้นๆ)
   - Equity risk premium: 4-6% (มาตรฐานตลาด)
   - Beta: หาได้จาก Yahoo Finance/stock screener (หรือประมาณจากความผันผวนถ้าหาไม่เจอ — ระบุว่าเป็นการประมาณ)
   - WACC ≈ risk-free rate + beta × equity risk premium (ถ้ามีหนี้เยอะให้ปรับ weighted กับ cost of debt ด้วย แต่บริษัท net-cash ส่วนใหญ่ใช้ cost of equity ตรงๆ ได้)
5. **Terminal value:** FCF ปีที่ 5 × (1 + terminal growth) ÷ (WACC − terminal growth)
6. **Discount ทุก cash flow กลับมาปีปัจจุบัน** แล้วรวมกับ terminal value (discounted)
7. **Enterprise Value → Equity Value:** บวก cash, ลบ debt (net cash/debt จาก balance sheet)
8. **Fair Value per share:** Equity Value ÷ diluted shares outstanding

### 3. แสดง Sensitivity สั้นๆ

คำนวณ fair value ที่ 3 สถานการณ์ (ไม่ต้องซับซ้อน แค่ปรับ WACC ±1% และ/หรือ terminal growth ±0.5%):
- Bear case (WACC สูงกว่า, terminal growth ต่ำกว่า)
- Base case (ตามที่คำนวณข้างบน)
- Bull case (WACC ต่ำกว่า, terminal growth สูงกว่า)

### 4. เทียบกับราคาปัจจุบัน

```
🟢 Cheap     — ราคาต่ำกว่า Base case FV ≥20%
🟡 Fair      — ราคาอยู่ใน ±20% ของ Base case FV
🔴 Expensive — ราคาสูงกว่า Base case FV >20%
```

### 5. Save ผล

Save ไปที่ `briefs/<TICKER>-conquest-<YYYY-MM-DD>.md`:

```markdown
# 💰 Conquest DCF: <TICKER> — <วันที่>
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- Base FCF: $XXX
- Growth fade: ปี1 X% → ปี2 X% → ปี3 X% → ปี4 X% → ปี5 X% (เหตุผล: ...)
- Terminal growth: X% (เหตุผล: ...)
- WACC: X% (risk-free X% + beta X × ERP X%)
- Shares outstanding: XXX
- Net cash/debt: $XXX

## DCF Calculation
[แสดงตัวเลขแต่ละปีคร่าวๆ + terminal value + PV รวม]

## Fair Value
- Bear case: $XXX
- **Base case: $XXX**
- Bull case: $XXX

## เทียบราคาปัจจุบัน $XXX
[🟢/🟡/🔴] — ต่างจาก Base case FV [+X% / -X%]

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV $XXX — [ใกล้/ไกลจาก conquest base case, เพราะอะไร — เช่น assumption growth fade ต่างกันตรงไหน]
- GuruFocus GF Value $XXX — [ใกล้/ไกลจาก conquest base case, เพราะอะไร]
- **สรุป:** [conquest เห็นด้วยกับฝั่งไหนมากกว่า หรืออยู่ตรงกลาง — เหตุผล 1-2 ประโยค]
```

## Rules
- **ห้ามไปหา "fair value"/"intrinsic value" สำเร็จรูปจากเว็บมาใช้** — ต้องคำนวณ DCF เองจาก raw fundamentals เท่านั้น ถ้า WebSearch เจอตัวเลข fair value ของคนอื่นโดยบังเอิญระหว่างหา fundamentals ห้ามเอามาปนกับผลคำนวณของตัวเอง
- ทุก assumption ต้องมีเหตุผลกำกับ ห้ามใส่ตัวเลขลอยๆ โดยไม่อธิบายที่มา
- ถ้าหาตัวเลข fundamental บางตัวไม่เจอจริงๆ (เช่น beta) ให้ใช้ค่าประมาณที่สมเหตุสมผลแล้วระบุชัดว่าเป็นการประมาณ ไม่ใช่ตัวเลขจริง — ห้ามเดาแบบไม่มีฐาน
- Sensitivity 3 สถานการณ์ต้องมีเสมอ ไม่ใช่แค่ตัวเลขเดียว เพราะ DCF อ่อนไหวต่อ assumption มาก การมี range ช่วยให้เห็นว่าความมั่นใจสูงหรือต่ำ
