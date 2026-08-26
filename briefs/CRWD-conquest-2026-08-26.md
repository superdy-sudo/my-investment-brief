# 💰 Conquest DCF: CRWD — 2026-08-26
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (TTM, ปีปัจจุบัน):** $1.73B
  - วิธีคำนวณ: TTM revenue = FY2026 revenue ($4.81B) − Q1 FY26 revenue (~$1.10B, คำนวณย้อนจาก Q1 FY27 $1.39B ที่ +26% YoY) + Q1 FY27 revenue ($1.39B) = **$5.10B**
  - ใช้ FCF margin 34% (ตัวเลขจริง Q1 FY27 = $468.5M/$1.39B) คูณ TTM revenue → **$1.73B**
- **Growth fade (Stage 1, ปี 1-5):** ปี1 22% → ปี2 18% → ปี3 14% → ปี4 10% → ปี5 7%
  - เหตุผล: เริ่มใกล้เคียง run-rate ปัจจุบัน (Q1 FY27 +26%, Q2 FY27 guide +23.2% — ไม่ accelerating ต่อเนื่อง สลับขึ้นลง 23-26%) แต่ปรับลงเร็วกว่า pattern ทั่วไปของ hyper-growth SaaS เพราะ TAM constraint ที่ Layer 2 ระบุไว้ชัดเจน: TAM $149B vs market cap $192.7B = 0.77x เท่านั้น (ต่ำกว่าเกณฑ์ 5x มาก ไม่เข้าเกณฑ์ Dominant Incumbent Exception เพราะ FCF margin 34% ไม่ถึง 40%) — บ่งชี้ runway การเติบโตแบบ hyper-growth มีจำกัดกว่าที่ multiple ตลาดสะท้อนอยู่ นอกจากนี้มี net new ARR ที่แม้ Q1 FY27 โต +32% YoY แต่เป็นฐาน incremental บนรายได้ที่ใหญ่ขึ้นเรื่อยๆ (law of large numbers) และมีคู่แข่งเพิ่มเข้ามาในตลาด endpoint/XDR (Microsoft Defender, SentinelOne, Palo Alto Cortex)
- **Terminal growth rate:** 3% — ใช้ตัวเลขมาตรฐานผูกกับ long-run GDP + inflation ไม่ให้ premium สูงกว่านี้ แม้มี Wide Moat เพราะ Layer 2 ยืนยันแล้วว่า TAM ไม่กว้างพอจะรองรับ perpetual high growth (TAM/mkt cap เพียง 0.77x)
- **WACC:** 11% (cost of equity ล้วน เพราะ net cash position — ใช้ cost of debt ไม่คุ้มความซับซ้อนเพราะหนี้ ~$750-801M เทียบ market cap $192.7B คิดเป็น <0.4% ของ capital structure)
  - Risk-free rate: 4.6% (10Y US Treasury yield ปัจจุบัน ปลาย ส.ค. 2026, อยู่ในช่วง 4.6-4.7% ตามข้อมูลตลาดล่าสุด)
  - Equity risk premium: 5% (มาตรฐานตลาด กลางช่วง 4-6%)
  - Beta: 1.3 (**ประมาณ** — ไม่พบตัวเลข beta ที่แน่ชัดจาก search โดยตรง ใช้ค่าประมาณตามลักษณะหุ้น high-growth cybersecurity SaaS ที่ผันผวนสูงกว่าตลาด ซึ่งทั่วไปอยู่ในช่วง 1.2-1.5)
  - WACC = 4.6% + 1.3 × 5% = 4.6% + 6.5% = 11.1% ≈ **11%**
- **Shares outstanding:** ~1.02B (หลัง 4:1 forward split ก.ค. 2026)
- **Net cash:** ~$3.77B (cash $4.55B − debt ~$750-801M, ใช้ midpoint)

## DCF Calculation (Base Case: WACC 11%, terminal g 3%)

| ปี | Growth | FCF ($B) | Discount factor (11%) | PV ($B) |
|---|---|---|---|---|
| 0 (TTM base) | — | 1.730 | — | — |
| 1 | 22% | 2.111 | 0.9009 | 1.901 |
| 2 | 18% | 2.490 | 0.8116 | 2.022 |
| 3 | 14% | 2.839 | 0.7312 | 2.076 |
| 4 | 10% | 3.123 | 0.6587 | 2.057 |
| 5 | 7% | 3.342 | 0.5935 | 1.983 |

- Sum PV of FCF (ปี 1-5): **$10.04B**
- Terminal Value = FCF ปี5 × (1+3%) / (11%−3%) = 3.342 × 1.03 / 0.08 = **$43.03B**
- PV of Terminal Value = 43.03 × 0.5935 = **$25.54B**
- **Enterprise Value = $10.04B + $25.54B = $35.58B**
- **Equity Value = EV + Net Cash = $35.58B + $3.77B = $39.35B**
- **Fair Value per share = $39.35B ÷ 1.02B shares = $38.58**

## Fair Value (Sensitivity: WACC ±1%, terminal g ±0.5%)

- Bear case (WACC 12%, terminal g 2.5%): **$33.33**
- **Base case (WACC 11%, terminal g 3.0%): $38.58**
- Bull case (WACC 10%, terminal g 3.5%): **$46.20**

## เทียบราคาปัจจุบัน $188.89 (26 ส.ค. 2026, ก่อนงบ Q2 FY27 คืนนี้)

🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV ($38.58) อยู่ **+389.6%** (แม้เทียบกับ Bull case $46.20 ก็ยังสูงกว่า +308.8%) — market กำลัง price-in growth/multiple ที่สูงกว่าที่ fundamentals ราคาปัจจุบัน (TTM P/FCF ≈ 111x) จะรองรับได้ในกรอบ DCF แบบ conservative-to-moderate นี้

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $530** — ไกลจาก conquest base case มาก ($530 vs $38.58 = ต่างกัน ~13.7 เท่า) เพราะ Morningstar ใช้ forward-DCF ที่สมมติ Wide Moat คงทนกับ growth ที่ยั่งยืนสูงกว่านี้มาก (น่าจะ fade ช้ากว่า และ/หรือใช้ terminal growth/WACC ที่เอื้อต่อ valuation สูงกว่านี้อย่างมีนัยสำคัญ) — คะแนน Uncertainty "Very High" ของ Morningstar เองก็สะท้อนว่าตัวเลขนี้มี range กว้างมาก
- **GuruFocus GF Value $130.19** — ใกล้ conquest มากกว่า Morningstar แต่ก็ยังสูงกว่า base case ~3.4 เท่า เพราะ GuruFocus ใช้ backward-looking historical-multiple regression ที่ยังอิงกับ multiple ในอดีตของหุ้น high-growth ซึ่งสูงกว่าที่ DCF จาก raw fundamentals ปัจจุบันจะรองรับได้ (แม้ historical multiple จะต่ำกว่าราคาตลาดตอนนี้ก็ตาม)
- **สรุป:** Conquest DCF เห็นด้วยกับ **ทิศทาง Expensive ของ GuruFocus** ไม่ใช่ Morningstar — และยิ่งไปกว่านั้น conquest ยัง conservative กว่า GuruFocus เองอีก เพราะ DCF อิสระที่คำนวณจาก raw fundamentals (revenue growth deceleration ที่ยืนยันแล้วใน Layer 2, TAM ที่จำกัดกว่าที่ market cap สะท้อน) ชี้ว่าราคาปัจจุบันสูงกว่ามูลค่าที่ปัจจัยพื้นฐานรองรับได้อย่างมีนัยสำคัญ ไม่ใช่แค่ Fair/Cheap ตาม Morningstar's optimistic forward-DCF ที่ผูกกับ Wide Moat premium สูง
