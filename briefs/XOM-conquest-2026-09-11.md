# 💰 Conquest DCF: XOM — 2026-09-11
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น — Morningstar $156 / GuruFocus $114.15 ไม่ถูกใช้เป็น input)*

## Assumptions

- **Base FCF:** $26.4B — ค่าเฉลี่ยของตัวเลข FY2025 (ปีงบล่าสุดที่ปิดแล้ว, "ปีปกติ" ไม่ใช่ปีที่ราคาน้ำมันพุ่งจากสงคราม) สองแหล่ง: $26.1B และ $26.77B (ต่างกันเล็กน้อยจาก rounding/แหล่งรายงาน) → FCF margin ที่ implied ≈7.8% ของ revenue $339.8B — **นี่คือจุดตั้งต้นสำคัญที่สุดของโมเดล**: ตั้งใจไม่ใช้ Q2 2026 FCF $17.2B ($68.8B annualized) เพราะเป็น quarter ที่ราคาน้ำมัน/ค่าการกลั่นพุ่งจากสงคราม US-Iran ซึ่งไม่ยั่งยืน
- **Growth fade (Stage 1, ปี 1-5):** ปี1 7% → ปี2 6% → ปี3 5% → ปี4 4% → ปี5 3%
  เหตุผล: ไม่ใช้ growth rate ปัจจุบัน (Q2 2026 +42% YoY) เป็นจุดเริ่มเพราะเป็นตัวเลขที่ปนราคาน้ำมัน ใช้แทนด้วย volume-driven growth ที่ตรวจสอบได้จริง — Permian guidance 9% CAGR ถึง 2030 + Guyana เพิ่ม Uaru/Whiptail (~250kbd ต่อโครงการ, เริ่ม 2026-2027) หนุน production growth ปี 1-2 แรงกว่า แต่ FCF growth มักช้ากว่า production growth เพราะ capex intensity สูง (YTD capex $13.0B) และสินทรัพย์เก่า/conventional ที่ decline หักลบบางส่วน จึง fade ลงตาม mean-reversion ทั่วไปของ mature commodity major
- **Terminal growth:** 2.5% — กลางช่วง 2-3% มาตรฐาน ผูกกับ long-run GDP/inflation ไม่ให้สูงกว่านี้เพราะ Moat เป็นแค่ Narrow (Morningstar, Uncertainty High) — ไม่มี pricing power เหนือราคาน้ำมัน/ก๊าซที่ตลาดโลกกำหนด และมี energy-transition demand risk ระยะยาวถ่วงไว้
- **Discount rate (WACC): 8.5%**
  - Risk-free rate: 4.95% (US 10Y Treasury, 11 ก.ย. 2026 — ระดับสูงสุดตั้งแต่ 2023 จาก inflation ที่ถูกดันโดยสงคราม Iran)
  - Equity Risk Premium: 5.0% (กลางช่วงมาตรฐาน 4-6%)
  - Beta: **ปรับเอง = 0.90** — Yahoo Finance รายงาน Beta (5Y Monthly) จริงแค่ 0.16-0.17 แต่ตัวเลขนี้ไม่น่าเชื่อถือสำหรับ DCF: มันสะท้อนช่วง decoupling ผิดปกติที่ราคาน้ำมันพุ่งจากสงครามสวนทางกับตลาดกว้าง (ซึ่งขับเคลื่อนโดยปัจจัยอื่น เช่น rate/tech) ไม่ใช่ risk เชิงโครงสร้างจริงของธุรกิจ commodity-price-taker ถ้าใช้ 0.16 ตรงๆ จะได้ cost of equity ~5.75% ซึ่งต่ำเกินจริงสำหรับหุ้นน้ำมัน จึงใช้ 0.90 แทน ซึ่งใกล้เคียง long-run beta ของ oil major ทั่วไป (XOM/CVX ในอดีตอยู่ราว 0.8-1.0) — **ระบุชัดว่านี่คือค่าประมาณเชิงวิจารณญาณ ไม่ใช่ตัวเลขสถิติดิบ**
  - Cost of equity = 4.95% + 0.90 × 5.0% = 9.45%
  - Cost of debt (pretax) ≈ 5.0% (ประมาณจาก credit quality AA-level ของ XOM), effective tax rate ≈40% (ค่าเฉลี่ยของ oil major ที่มี severance/foreign tax สูงกว่า US statutory 21%) → after-tax cost of debt ≈3.0%
  - Weight: Debt 14% / Equity 86% (ตาม debt-to-capital 14.0% ที่ให้มา)
  - WACC = 0.86×9.45% + 0.14×3.0% ≈ **8.5%**
- **Shares outstanding:** 4.202B
- **Net debt:** $39.3B (Q1 2026, Net Debt/EBITDA 0.7x)

## DCF Calculation (Base Case, WACC 8.5%, terminal g 2.5%)

| ปี | Growth | FCF ($B) | Discount Factor | PV ($B) |
|---|---|---|---|---|
| 0 (base) | — | 26.4 | — | — |
| 1 | 7% | 28.25 | 0.9217 | 26.04 |
| 2 | 6% | 29.94 | 0.8495 | 25.43 |
| 3 | 5% | 31.44 | 0.7830 | 24.62 |
| 4 | 4% | 32.70 | 0.7217 | 23.60 |
| 5 | 3% | 33.68 | 0.6653 | 22.41 |

- Sum PV of Stage-1 FCF ≈ **$122.1B**
- Terminal Value (ปีที่ 5) = 33.68 × 1.025 / (0.085 − 0.025) = **$575.3B**
- PV of Terminal Value = 575.3 × 0.6653 ≈ **$382.7B**
- Enterprise Value = 122.1 + 382.7 ≈ **$504.8B**
- Equity Value = EV − Net Debt = 504.8 − 39.3 ≈ **$465.5B**
- **Fair Value per share = 465.5 / 4.202 ≈ $110.8**

## Fair Value (Sensitivity: WACC ±1%, terminal g ±0.5%)

- Bear case (WACC 9.5%, g 2.0%): **$88.2**
- **Base case (WACC 8.5%, g 2.5%): $110.8**
- Bull case (WACC 7.5%, g 3.0%): **$148.3**

## Sensitivity: ถ้าราคาน้ำมัน/ค่าการกลั่นที่พุ่งสูงอยู่ตอนนี้ยืนอีก 2-3 ปี

สมมติ FCF ปี 1-2 ยังสูงใกล้ระดับสงคราม (annualized run-rate จาก Q2 2026 ที่ $17.2B/ไตรมาส ≈$65-68B/ปี) แล้วค่อยๆ คลายตัวกลับสู่ normalized ภายในปีที่ 4-5:

| ปี | FCF ($B) | PV ($B) (WACC 8.5%) |
|---|---|---|
| 1 | 65 | 59.91 |
| 2 | 60 | 50.97 |
| 3 | 45 | 35.24 |
| 4 | 33 | 23.82 |
| 5 | 33.68 (= base-case terminal FCF) | 22.41 |

- Sum PV ≈ $192.4B, PV of Terminal Value เดิม $382.7B (ปีที่ 5 กลับมาบรรจบกับ base case)
- EV ≈ $575.1B → Equity ≈ $535.8B → **Fair Value ≈ $127.5/share**

แม้สมมติสงครามยืดเยื้อ/ราคาน้ำมันสูงต่ออีก 2-3 ปีเต็ม fair value ก็ยังขึ้นไปแค่ ~$127.5 — **ยังต่ำกว่าราคาปัจจุบัน ($164.90) และต่ำกว่า Morningstar ($156)** สะท้อนว่าตลาดปัจจุบัน pricing บางอย่างที่ optimistic กว่าแค่ "สงครามยืดเยื้อ" (เช่น terminal growth/margin สูงกว่านี้ หรือ discount rate ต่ำกว่านี้มาก)

## เทียบราคาปัจจุบัน $164.90

Base case ($110.8): ส่วนต่าง = (164.90 − 110.8) / 110.8 ≈ **+48.8%**

🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV เกิน 20% อย่างชัดเจน (แม้ใช้ Bull case $148.3 ราคาก็ยังสูงกว่าอยู่ +11.2%)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $156** — ห่างจาก conquest base case มาก (+40.9%) แม้แต่ conquest bull-case ($148.3, WACC 7.5% + terminal g 3.0%) ก็ยังต่ำกว่า Morningstar เล็กน้อย เป็นไปได้ว่า Morningstar ใช้ normalized margin ที่สูงกว่า FY2025 (~7.8%) มาก หรือใช้ discount rate ต่ำกว่า/terminal growth สูงกว่าที่ conquest ให้เหตุผลไว้ข้างบน — สอดคล้องกับที่ brief เดิมตั้งข้อสังเกตว่า analyst forward-DCF มักมี bias เชิงบวก
- **GuruFocus GF Value $114.15** — ใกล้เคียง conquest base case มาก (diff เพียง ~3%, $114.15 vs $110.8) แม้วิธีคิดต่างกันโดยสิ้นเชิง (backward-looking historical-multiple regression ของ GuruFocus vs bottom-up 2-stage DCF ของ conquest ที่สร้างจาก normalized FCF ปี 2025) — การที่สองวิธีที่เป็นอิสระจากกันจริงๆ มาบรรจบใกล้กันเป็นสัญญาณที่แข็งแรง
- **สรุป:** conquest เห็นด้วยกับ **GuruFocus** ชัดเจนกว่า Morningstar มาก (2 ใน 3 แหล่ง — GuruFocus + conquest — เห็นตรงกันว่าราคาปัจจุบัน Expensive อย่างมีนัยสำคัญ ขณะ Morningstar เป็นแหล่งเดียวที่มองว่าใกล้ fair value) เหตุผลหลักที่ conquest ต่างจาก Morningstar คือการเลือก **ไม่ extrapolate FCF ของไตรมาสที่ราคาน้ำมันพุ่งจากสงคราม** และใช้ terminal growth ที่จำกัดไว้ที่ 2.5% ตาม Narrow-Moat/no-pricing-power ที่ Morningstar เองก็ยอมรับ (Uncertainty Rating: High)
