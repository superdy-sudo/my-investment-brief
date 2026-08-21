# 💰 Conquest DCF: PSX (Phillips 66) — 2026-08-21
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (normalized, ไม่ใช่ TTM ดิบ)**
TTM FCF $6,394M ถูกดันขึ้นโดย crack spread ที่พุ่งจาก $10.11/bbl (Q1'26) → $24.08/bbl (Q2'26) — เป็น cyclical spike ไม่ใช่ baseline ใหม่ (utilization 96% คือการฟื้นตัวจาก turnaround ปี 2025 ไม่ใช่ capacity เพิ่ม, revenue หด 3 ปีติดก่อนหน้า FY23 -13.3%/FY24 -2.9%/FY25 -7.5%)

ใช้ weighted blend แทนการเอา TTM มาต่อยอดตรงๆ:
- 40% TTM FCF ($6,394M) + 60% เฉลี่ย FY2024-FY2025 FCF (avg $2,530.5M)
- = 0.4×6,394 + 0.6×2,530.5 = **$4,080M** (Base/mid-cycle-normalized FCF)

**Stage 1 — Growth fade (ปี 1-5), เหตุผล: mean-reversion จาก crack-spread peak กลับสู่ mid-cycle ก่อน แล้วค่อยโตแบบโครงสร้าง (midstream/chemicals buildout)**
| ปี | Growth | FCF ($M) | เหตุผล |
|---|---|---|---|
| 1 | -8% | 3,753.6 | crack spread ปรับลงจาก peak $24/bbl กลับสู่ระดับปกติกว่า |
| 2 | -3% | 3,641.0 | ยังปรับฐานต่อ ก่อนเข้าสู่ growth ที่มาจาก midstream ไม่ใช่ refining margin |
| 3 | +2% | 3,713.8 | เริ่มเห็นผลจาก Iron Mesa/Coastal Bend midstream buildout |
| 4 | +3% | 3,825.2 | midstream EBITDA target $4.5B by 2027 ใกล้ mature, CPChem crackers เริ่ม online 2027 |
| 5 | +3% | 3,939.9 | เข้าใกล้ terminal growth |

**Terminal growth: 2.5%** — ผูกกับ long-run GDP/inflation มาตรฐาน ไม่ให้ premium เพราะ Layer 1 ยืนยันแล้วว่า No Wide Moat (refining เป็น price-taker commodity business, ไม่มี durable competitive advantage ที่จะ justify terminal growth สูงกว่าตลาดรวม)

**WACC: 9.2%**
- Risk-free rate: 4.70% (10Y UST, ณ 2026-08-21)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด)
- Beta: **1.10 (ประมาณ)** — WebSearch เจอ beta ติดลบ (-0.72 ถึง -0.84) จากบางแหล่งซึ่งขัดกับพฤติกรรมจริงของหุ้น cyclical/commodity ที่ปกติ correlate กับตลาดและ oil price สูง (ไม่น่าเชื่อถือ ใช้ estimate มาตรฐานของ refiner แทน)
- Cost of equity = 4.70% + 1.10×5.0% = 10.20%
- Cost of debt (pretax) ≈ 5.5% (ประมาณ, BBB+-grade integrated refiner) → after-tax (21% tax) ≈ 4.35%
- Weights: E/V = 82.6% (market cap $97.9B), D/V = 17.4% (total debt $20.57B)
- WACC = 0.826×10.20% + 0.174×4.35% = 8.43% + 0.76% = **9.2%**

**Shares outstanding:** ~404M (implied จาก TTM Net Income $7,085M ÷ TTM EPS $17.51)
**Net Debt:** $16.5B (total debt $20.57B − cash $4.10B)

## DCF Calculation (Base Case)

| ปี | FCF ($M) | Discount factor @9.2% | PV ($M) |
|---|---|---|---|
| 1 | 3,753.6 | 0.9158 | 3,438.0 |
| 2 | 3,641.0 | 0.8387 | 3,053.9 |
| 3 | 3,713.8 | 0.7681 | 2,852.4 |
| 4 | 3,825.2 | 0.7034 | 2,690.6 |
| 5 | 3,939.9 | 0.6442 | 2,538.0 |

Sum PV of Stage-1 FCF = **$14,572.9M**

Terminal Value = FCF₅×(1+g)/(WACC−g) = 3,939.9×1.025/(0.092−0.025) = 4,038.4/0.067 = **$60,275M**
PV of Terminal Value = 60,275×0.6442 = **$38,829.2M**

Enterprise Value = 14,572.9 + 38,829.2 = **$53,402.1M**
Equity Value = EV − Net Debt = 53,402.1 − 16,500 = **$36,902.1M**
Fair Value per share = 36,902.1 / 404 = **$91.34**

## Fair Value (Sensitivity: WACC ±1%, terminal growth ±0.5%)
- Bear case (WACC 10.2%, g 2.0%): **$68.9**
- **Base case (WACC 9.2%, g 2.5%): $91.3**
- Bull case (WACC 8.2%, g 3.0%): **$126.4**

## เทียบราคาปัจจุบัน $242.25
🔴 **Expensive** — ราคาสูงกว่า Base case FV ($91.3) ประมาณ **+165%** และยังสูงกว่าแม้แต่ Bull case ($126.4) ถึง +92% — ไม่ใช่ borderline เลย ทุก sensitivity scenario ยืนยันว่าตลาดให้ราคาสูงเกินกว่าที่ fundamental รองรับได้มาก

## เทียบกับ Morningstar/GuruFocus
- Morningstar (proxy ~$207-211): **ไกลจาก conquest base case มาก** — Morningstar-proxy น่าจะใช้ forward-DCF ที่ต่อยอด TTM/forward EPS ซึ่งฝัง crack-spread peak ($24/bbl) เข้าไปเป็น baseline โดยไม่ normalize กลับสู่ mid-cycle เหมือนที่ conquest ทำ นี่คือจุดต่างหลัก — Morningstar treat การพุ่งของ margin ไตรมาสนี้เป็นสัญญาณเชิงบวกต่อเนื่อง ในขณะที่ conquest มองเป็น cyclical spike ที่ต้อง fade ลง
- GuruFocus GF Value ($136-138): **ใกล้กว่า Morningstar แต่ยังสูงกว่า conquest base case ~$45-47 (+49-51%)** — ทั้งสองฝั่งเห็นตรงกันว่าหุ้นแพงเกินราคาตลาด (ทิศทางเดียวกัน) แต่ GuruFocus ใช้ regression บน historical multiple (ซึ่งรวมทั้งปีที่ margin ดีและแย่ในอดีตเข้าด้วยกัน) ในขณะที่ conquest คำนวณจาก DCF ที่ปรับ base FCF ลงมากกว่า (weighted 60% ไปทางค่าเฉลี่ย FY24-25 ที่ยังต่ำ) และใช้ terminal growth ต่ำ (2.5%) เพราะ Layer 1 ยืนยัน No Wide Moat ชัดเจน
- **สรุป:** conquest เห็นด้วยกับทิศทางของ **GuruFocus (Expensive)** ไม่ใช่ Morningstar (Fair) — เสียงส่วนใหญ่ 2 ใน 3 (GuruFocus + Conquest) ยืนยันว่าราคาตลาด $242.25 แพงกว่ามูลค่าที่แท้จริงอย่างมีนัยสำคัญ Morningstar-proxy กลายเป็น outlier ที่น่าจะได้รับอิทธิพลจาก forward-EPS ที่ยังไม่ได้ normalize crack-spread cyclicality ออก ผลลัพธ์นี้สอดคล้องกับ Layer 1/2 conclusion (No Wide Moat, revenue growth เป็น mirage จาก margin ไม่ใช่ volume) ที่นำไปสู่ 🔴 Avoid ใน Layer 4 อยู่แล้ว
