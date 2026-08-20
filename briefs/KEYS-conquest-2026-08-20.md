# 💰 Conquest DCF: KEYS — 2026-08-20
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF:** $1.33B
- อ้างอิง Q3 FY26 FCF margin 21.8% ($403M FCF / $1.846B quarterly revenue) × TTM revenue $6.09B
- หมายเหตุ: เป็นค่าประมาณ เพราะไม่มีตัวเลข TTM FCF สะสม 4 ไตรมาสตรงๆ ในข้อมูลที่มี ใช้ margin ล่าสุดคูณ TTM revenue แทน — ถือว่า margin คงที่ตลอด forecast (ไม่ได้สมมติ operating leverage เพิ่ม แม้จะมีความเป็นไปได้ที่ margin ขยายจริง — เป็นสมมติฐานระมัดระวัง)

**Growth fade (revenue/FCF เติบโตอัตราเดียวกัน, margin คงที่):**
| ปี | Growth |
|---|---|
| ปี 1 (FY27) | 30% |
| ปี 2 (FY28) | 22% |
| ปี 3 (FY29) | 16% |
| ปี 4 (FY30) | 11% |
| ปี 5 (FY31) | 7% |
| Terminal | 3% |

เหตุผล fade: growth ปัจจุบัน (+36% YoY Q3, orders +56% YoY 2 ไตรมาสติด, guidance Q4 +37%) เป็นผลจาก AI-datacenter capex supercycle ที่เป็นวงจร ไม่ใช่ growth ระดับ structural — Test & Measurement TAM โตแค่ ~4.1% CAGR (2026-2031) เท่านั้น การที่ KEYS โต 30%+ ต่อเนื่องคือ market-share gain + cyclical upcycle ซึ่งวงจร capex แบบนี้มักปรับฐานภายใน 3-5 ปีตามประวัติศาสตร์ semicap/test-equipment cycle ปีที่ 1 ยังได้แรงหนุนจาก backlog ออเดอร์ที่แน่นเกิน $2B/ไตรมาส แต่ปีถัดๆ ไปจะ mean-revert ลงมาใกล้ TAM growth + market-share gain ที่เหลืออยู่

**Terminal growth: 3%** — สูงกว่า GDP มาตรฐาน (2%) เล็กน้อยเพราะ Wide Moat (switching cost + process power) ที่ Morningstar ยืนยันซ้ำ ให้ pricing power ต่อเนื่องกว่าธุรกิจทั่วไป และมี secular driver รุ่นถัดไป (6G, defense modernization, AI infra รุ่นต่อไป) ที่ยังไม่รวมอยู่ใน stage 1

**WACC: 11.1%**
- Risk-free rate: 4.64% (10Y UST, 20 ส.ค. 2026)
- Equity risk premium: 5.0% (มาตรฐานตลาด)
- Beta: 1.3 (ประมาณ — Zacks รายงาน 1.54 แต่ปรับลงเป็นค่ากลางเพราะ 1.54 สะท้อนความผันผวนช่วงสั้นหลังราคาร่วง -6.3% วันนี้ ไม่ใช่ beta ระยะยาวปกติของธุรกิจ test-equipment ที่มักอยู่โซน 1.1-1.4)
- Cost of equity = 4.64% + 1.3 × 5.0% = 11.14% ≈ 11.1%
- Net debt ($594M) เทียบ market cap ($54.8B) ต่ำมาก (<2% of capital) → ใช้ cost of equity ตรงเป็น WACC โดยไม่ปรับ weighted cost of debt (ผลกระทบเล็กน้อยจนไม่มีนัยสำคัญ)

**Shares outstanding:** 171.5M
**Net debt:** ~$594M (Cash $2.18B, Debt $2.77B)

## DCF Calculation

| ปี | Growth | FCF ($B) | Discount Factor (11.1%) | PV ($B) |
|---|---|---|---|---|
| 1 | 30% | 1.729 | 1.111 | 1.556 |
| 2 | 22% | 2.110 | 1.234 | 1.710 |
| 3 | 16% | 2.447 | 1.371 | 1.784 |
| 4 | 11% | 2.716 | 1.524 | 1.783 |
| 5 | 7% | 2.907 | 1.693 | 1.717 |

Sum PV (Stage 1) = **$8.55B**

Terminal Value = FCF5 × (1+g) ÷ (WACC−g) = 2.907 × 1.03 ÷ (0.111−0.03) = **$36.97B**
PV of Terminal Value = 36.97 ÷ 1.693 = **$21.85B**

Enterprise Value = 8.55 + 21.85 = **$30.40B**
Equity Value = EV − Net Debt = 30.40 − 0.594 = **$29.81B**
Fair Value/share = 29.81B ÷ 171.5M shares = **≈ $174**

## Fair Value (Sensitivity)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| Bear | 12.1% | 2.5% | $147 |
| **Base** | **11.1%** | **3.0%** | **$174** |
| Bull | 10.1% | 3.5% | $212 |

แม้แต่ bull case ($212) ก็ยังต่ำกว่าราคาตลาดปัจจุบันมาก — ความมั่นใจในทิศทาง "แพงกว่ามูลค่าที่แท้จริง" ค่อนข้างสูง ไม่ใช่แค่ borderline

## เทียบราคาปัจจุบัน $319.45

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($174) ถึง **+83.6%** (สูงกว่าเกณฑ์ >20% มาก)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $323** — ไกลจาก conquest base case มาก (+85.6% เทียบกัน) เพราะ Morningstar ใช้ forward-DCF ที่ผูกกับ Wide Moat premium และน่าจะสมมติ growth fade ช้ากว่ามาก (คงอัตราเติบโตสูงยาวนานกว่า 5 ปี หรือใช้ terminal growth/moat premium สูงกว่า) และอาจไม่ discount cyclical AI-capex upcycle ว่าจะ normalize เร็วเท่าที่ conquest สมมติ
- **GuruFocus GF Value $205** — ใกล้กว่า conquest base case ($174) มาก เทียบกันต่างแค่ ~15% ทั้งคู่ชี้ไปทิศทางเดียวกันคือ "overvalued ที่ราคาปัจจุบัน" แม้วิธีคิดต่างกัน (GuruFocus ใช้ historical-multiple regression, conquest ใช้ bottom-up DCF) แต่ conclusion สอดคล้องกัน
- **สรุป:** conquest เห็นด้วยกับฝั่ง **GuruFocus** (overvalued) มากกว่า Morningstar อย่างชัดเจน — เกิดเป็น **2 ใน 3 แหล่ง (GuruFocus + Conquest) เห็นตรงกันว่า KEYS แพงกว่ามูลค่าที่แท้จริง ณ ราคา $319.45** ประเด็นสำคัญคือ conquest DCF สมมติว่า growth +36% YoY ปัจจุบันเป็นวงจร cyclical (AI-capex supercycle) ที่ต้อง fade เร็วภายใน 5 ปีตาม TAM growth ระยะยาวแค่ ~4% CAGR ไม่ใช่ growth ที่ sustain ได้ยาวแบบที่ Morningstar's Wide-Moat DCF ดูจะสมมติไว้
