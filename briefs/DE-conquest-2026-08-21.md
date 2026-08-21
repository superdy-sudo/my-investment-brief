# 💰 Conquest DCF: DE (Deere & Company) — 2026-08-21
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (Y0):** $5.25B — midpoint ของ FY2026 Equipment Operations cash flow guidance ($5.0B–$5.5B) ที่บริษัทเพิ่งปรับขึ้น เทียบเท่า FCF margin ~11% บน TTM revenue $47.4B ใช้ *Equipment Operations* cash flow เท่านั้น ไม่รวม Financial Services segment (ดูเหตุผลเรื่อง net debt ด้านล่าง — จับคู่ FCF ฝั่ง industrial กับ debt ฝั่ง industrial ให้สอดคล้องกัน)
- **Growth fade (Stage 1, ปี 1–5):** ปี1 7% → ปี2 6% → ปี3 5% → ปี4 4% → ปี5 3%
  - เหตุผล: TTM growth ปัจจุบันอยู่ที่ +4% และไตรมาสล่าสุดเร่งเป็น +5-6% แต่ส่วนหนึ่งมาจาก tariff refund ($382M คิดเป็น one-time/timing) และ AI-data-center construction boom ซึ่งเป็น cyclical tailwind ไม่ใช่ secular growth ใหม่ (Deere เพิ่งออกจาก 2 ปีติดลบหนัก -15.6%/-11.7% — นี่คือการ bounce off trough) — ผมให้ momentum การฟื้นตัวสูงกว่า run-rate ปัจจุบันเล็กน้อยในปี 1-2 (สะท้อน construction/AI capex demand ที่ยังไปต่อ) แล้ว fade ลงเร็วสู่ระดับ GDP+cyclical-average ~3% ภายในปี 5 เพราะ ag/construction equipment เป็นธุรกิจ mature cyclical ที่ mean-revert เร็วเมื่อ replacement cycle และ tariff refund หมดฤทธิ์
- **Terminal growth:** 2.5% — ใกล้ long-run GDP+inflation ไม่ให้ premium เพิ่มเพราะแม้ Deere มี switching-cost moat (precision ag ecosystem, dealer network) แต่ธุรกิจหลักยังเป็น cyclical hardware ที่ไม่มี pricing power แบบ secular growth compounder
- **WACC:** 9.3% = risk-free 4.47% (10Y UST, ส.ค. 2026) + beta 0.96 (5Y monthly, จาก stockanalysis.com) × ERP 5.0% (มาตรฐานตลาด, กลาง 4-6%)
  - ใช้ cost of equity ตรงๆ เป็น WACC เพราะ net industrial debt (ดูด้านล่าง) เล็กมากเทียบ market cap (~3.5%) การปรับ weighted cost of debt แทบไม่กระทบผลลัพธ์
- **Shares outstanding:** 269.94M (diluted, ตามราคาตลาดที่ระบุใน brief)
- **Net debt (industrial basis, estimated):** ~$5.81B
  - Total consolidated debt $64.16B รวม captive Financial Services debt ที่ match-funded โดย financing receivables (~$49.0B: financing receivables net $42.9B + securitized $6.1B, จาก 10-Q พ.ค. 2026) — ผมประมาณ industrial debt = total debt − financing receivables ≈ $15.14B แล้วหักด้วย cash+marketable securities $9.34B (cash $7.905B + securities $1.43B, 10-Q พ.ค. 2026) = **net industrial debt ≈ $5.81B** (เป็นการประมาณ เพราะไม่มีตัวเลข net-debt-ex-financial-services แยกชัดจากบริษัทโดยตรง)

## DCF Calculation (Base Case)

| ปี | Growth | FCF ($B) | Discount Factor @9.3% | PV ($B) |
|---|---|---|---|---|
| 1 | 7% | 5.618 | 0.9149 | 5.140 |
| 2 | 6% | 5.955 | 0.8371 | 4.985 |
| 3 | 5% | 6.252 | 0.7658 | 4.789 |
| 4 | 4% | 6.502 | 0.7007 | 4.557 |
| 5 | 3% | 6.698 | 0.6411 | 4.293 |

- Sum PV of Stage 1 FCF ≈ **$23.76B**
- Terminal Value (end ปี5) = FCF5 × (1+2.5%) ÷ (9.3%−2.5%) = 6.698 × 1.025 ÷ 0.068 ≈ **$100.95B**
- PV(Terminal Value) = 100.95 × 0.6411 ≈ **$64.71B**
- **Enterprise Value ≈ $88.47B**
- (−) Net industrial debt ≈ $5.81B
- **Equity Value ≈ $82.65B**
- ÷ 269.94M shares → **Fair Value ≈ $306/share**

## Fair Value (Sensitivity: WACC ±1%, terminal growth ±0.5%)

- Bear case (WACC 10.3%, g 2.0%): **$251/share**
- **Base case (WACC 9.3%, g 2.5%): $306/share**
- Bull case (WACC 8.3%, g 3.0%): **$393/share**

## เทียบราคาปัจจุบัน $624.45

🔴 **Expensive** — สูงกว่า Base case FV ($306) ประมาณ **+104%** และยังสูงกว่าแม้แต่ Bull case ($393) ถึง +59% — ทุก scenario ใน sensitivity range ($251–$393) ยังต่ำกว่าราคาตลาดอย่างมีนัยสำคัญ

Implied FCF yield ที่ราคาตลาด = $5.25B ÷ $168.6B market cap ≈ 3.1% ซึ่งต่ำผิดปกติสำหรับผู้ผลิตเครื่องจักรหนักที่เป็น cyclical business (ปกติเทรดที่ FCF yield 5-7%) — ตลาดกำลัง price-in การฟื้นตัวและ AI-construction boom ต่อเนื่องระยะยาวกว่าที่ fundamentals ปัจจุบันสนับสนุน

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $550** — ไกลจาก conquest base case มาก (+80% เทียบ base) เพราะ Morningstar ให้ Wide Moat premium กับ terminal assumption (มักใช้ terminal growth/margin สูงกว่าและ WACC ต่ำกว่าจาก moat-adjusted framework) และมองข้าม cyclical bounce ว่าเป็นจุดเริ่มของ growth ต่อเนื่อง ขณะที่ conquest มองว่าปัจจุบันคือ recovery จาก 2-year down-cycle ไม่ใช่ secular re-rating
- **GuruFocus GF Value $365.53** — ใกล้กว่ามาก (+19.5% เทียบ base, อยู่ในช่วง Bull case ของ conquest ด้วยซ้ำ) แม้วิธีคิดต่างกัน (historical-multiple regression vs bottom-up DCF) แต่ทั้งคู่สรุปตรงกันว่าหุ้น "Significantly Overvalued" ที่ราคาปัจจุบัน
- **สรุป:** Conquest เห็นด้วยกับฝั่ง GuruFocus (undervalued-multiple-regression มองว่าแพง) มากกว่า Morningstar อย่างชัดเจน — จุดขัดแย้งหลักคือ Morningstar ให้เครดิต moat/growth ต่อเนื่องมากเกินไปกับสิ่งที่ยังเป็นแค่ cyclical recovery + one-time tariff refund + AI-construction demand spike ซึ่งยังไม่มีหลักฐานว่าเป็น secular shift ของธุรกิจ ag/construction equipment ที่ mature แล้ว
