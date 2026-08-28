# 💰 Conquest DCF: LLY — 2026-08-28
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base (2026) revenue:** $86B (FY2026 guidance midpoint $85-87B)
- **Base FCF margin (2026):** ~13% (TTM FCF $10.37B / TTM revenue ~$80B) — depressed by $18B+ manufacturing capex program (2024-2028)
- **Revenue growth fade (เหตุผล: Q2'26 growth +48% YoY และ guidance implied +30-33% เป็นจุดเริ่มที่สูงเกินจะยั่งยืน — ต้อง fade ลงเมื่อ base ใหญ่ขึ้นเรื่อยๆ, oral-GLP1 competition จาก Novo เข้มขึ้น, และ GLP-1 category growth ปกติแล้วต้อง normalize):**
  - ปี1 (2027): +30% → revenue $111.8B
  - ปี2 (2028): +24% → revenue $138.6B
  - ปี3 (2029): +18% → revenue $163.5B
  - ปี4 (2030): +13% → revenue $184.8B
  - ปี5 (2031): +9% → revenue $201.4B
- **FCF margin expansion (เหตุผล: manufacturing capex program เสร็จปี 2028 → operating leverage เข้า, mature big-pharma FCF margin ทั่วไปอยู่ที่ 25-30%):**
  - ปี1: 15% → ปี2: 18% → ปี3: 21% → ปี4: 23% → ปี5: 25%
- **Terminal growth: 3.0%** (เหตุผล: สูงกว่า GDP เล็กน้อย เพราะ Wide Moat + pipeline refresh ต่อเนื่อง (retatrutide, immunology/oncology/neurology) แต่ไม่สูงกว่านี้เพราะมี patent-cliff risk ระยะยาวสำหรับ tirzepatide franchise)
- **WACC ≈ 7.0%:**
  - Risk-free rate: 4.68% (10Y Treasury, ประมาณ Aug 27, 2026)
  - Beta: 0.48 (Yahoo Finance 5Y monthly)
  - Equity risk premium: 5.0%
  - Cost of equity = 4.68% + 0.48×5.0% = 7.08%
  - Debt weight เล็กมาก (~3-4% ของ capital structure ที่ market cap ~$1.05T vs total debt ประมาณ $40B) → WACC ≈ cost of equity เกือบเต็มที่ ≈ **7.0%**
- **Shares outstanding: 895M diluted** (10-Q Q1 2026 / GuruFocus)
- **Net debt (ประมาณ):** ~$31B (cash $9.0B, total debt ประมาณ $40B จาก net debt/EBITDA 1.57x × TTM EBITDA ประมาณ $20B — เป็นการประมาณ ไม่ใช่ตัวเลขจริงจาก filing เพราะไม่มี total debt breakdown ตรงในข้อมูลที่มี)

## DCF Calculation (Base case)

| ปี | Revenue | FCF margin | FCF | Discount factor @7% | PV |
|----|---------|-----------|-----|---------------------|-----|
| 1 (2027) | $111.8B | 15% | $16.8B | 0.9346 | $15.70B |
| 2 (2028) | $138.6B | 18% | $24.9B | 0.8734 | $21.75B |
| 3 (2029) | $163.5B | 21% | $34.3B | 0.8163 | $28.00B |
| 4 (2030) | $184.8B | 23% | $42.5B | 0.7629 | $32.42B |
| 5 (2031) | $201.4B | 25% | $50.3B | 0.7130 | $35.87B |

Sum PV (Stage 1) = **$133.7B**

Terminal Value = FCF5 × (1+g) / (WACC−g) = $50.3B × 1.03 / (0.07−0.03) = **$1,295.3B**
PV of Terminal Value = $1,295.3B × 0.7130 = **$923.5B**

Enterprise Value = $133.7B + $923.5B = **$1,057.2B**
Equity Value = EV + cash − net debt ≈ $1,057.2B − $31B = **$1,026.2B**

**Fair Value per share = $1,026.2B / 895M shares = $1,147**

## Sensitivity (3 scenarios)

| Scenario | WACC | Terminal g | Fair Value/share |
|----------|------|-----------|-------------------|
| Bear | 8.0% | 2.5% | **$823** |
| **Base** | **7.0%** | **3.0%** | **$1,147** |
| Bull | 6.0% | 3.5% | **$1,858** |

(Range กว้างมาก — สะท้อนว่า DCF ของ LLY อ่อนไหวสูงต่อ WACC/terminal growth เพราะ cash flow ส่วนใหญ่มาจาก terminal value ที่ discount ไกลออกไป 5+ ปี และ growth ยังเร่งสูงอยู่)

## เทียบราคาปัจจุบัน $1,176.10

Base case FV $1,147 vs ราคา $1,176.10 → ส่วนต่าง = (1,147−1,176.10)/1,176.10 = **−2.5%**

🟡 **Fair** — ราคาปัจจุบันอยู่ในช่วง ±20% ของ Base case FV (เกือบเท่ากันเป๊ะ)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $980** — Conquest base ($1,147) สูงกว่า Morningstar ~17%; ใกล้กันในเชิงทิศทางมากกว่าฝั่ง GuruFocus เพราะ Morningstar และ Conquest ทั้งคู่เป็น forward-DCF ที่ discount cash flow ระยะยาวและใช้ terminal growth ระดับ GDP — Morningstar อาจใช้ WACC สูงกว่า (Morningstar ปกติปรับ WACC ตาม moat/uncertainty rating ซึ่งจะสูงกว่า cost-of-equity แบบ CAPM ตรงๆ ที่ conquest ใช้) หรือ margin-expansion assumption ระมัดระวังกว่า
- **GuruFocus GF Value $1,520** — Conquest base ต่ำกว่า GuruFocus ~24.5%; ห่างกันมากกว่า เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ไม่ได้ fade growth ลงแรงเท่า DCF แบบ forward-looking ของ conquest — cost-saving study ล่าสุดของ Zepbound ที่ดัน GF Value ขึ้นอาจสะท้อนใน multiple expansion มากกว่าจะสะท้อนใน cash flow จริงที่ conquest ใช้
- **สรุป:** Conquest ($1,147, Fair) อยู่ตรงกลางระหว่าง Morningstar ($980, Expensive) กับ GuruFocus ($1,520, Cheap) แต่ตัวเลขจริงเอนไปทาง Morningstar มากกว่า (ห่างกันแค่ 17% เทียบกับ 24.5% จาก GuruFocus) — บ่งชี้ว่า GuruFocus อาจ optimistic เกินไปกับ margin/multiple ระยะสั้น ขณะที่ Morningstar's conservative WACC ใกล้เคียงกับมุมมองอิสระของ conquest มากกว่า ถึงแม้ bucket สุดท้ายของ conquest เองคือ "Fair" ไม่ใช่ "Expensive" เต็มตัว — ผลลัพธ์นี้ไม่ได้ resolve ข้อขัดแย้งแบบ 2-ต่อ-1 ชัดเจน แต่ให้น้ำหนักเพิ่มกับฝั่ง Morningstar/valuation-neutral มากกว่าฝั่ง cheap ของ GuruFocus (Note: บันทึกไว้ก่อนหน้าใน memory ว่า conquest มี bias เข้มงวดตามธรรมชาติจาก WACC/terminal-growth ที่ conservative — ควรอ่านผลนี้เป็น "มุมมองเข้มที่สุดในสาม" ไม่ใช่คำตัดสินสุดท้าย)
