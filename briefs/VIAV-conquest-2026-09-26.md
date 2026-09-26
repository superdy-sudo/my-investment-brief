# 💰 Conquest DCF: VIAV — 2026-09-26
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (FY26, ปิดบัญชี 27 มิ.ย. 2026):** $82.8M (OCF $113.9M − capex $31.1M) บน revenue $1,518M (margin 5.4%)
- **Growth fade (Stage 1, ปีที่ 1-5):** ปี1 18% → ปี2 15% → ปี3 12% → ปี4 8% → ปี5 5%
  - เหตุผล: ไม่ใช้ reported growth +40% YoY เพราะพองจาก M&A (Spirent $145.0M + Inertial Labs $86.1M ของ revenue เพิ่มขึ้น $434M ทั้งหมด) — ยึด **organic growth ~19-21%** เป็นฐาน ปี1 ตั้งต้นที่ 18% (ต่ำกว่า organic ปัจจุบันเล็กน้อย เพราะ synergy จาก AI data-center optical supercycle + defense cert ใหม่จะเริ่มชะลอเมื่อ comp ฐานสูงขึ้น) แล้ว fade ลงเรื่อยๆ สู่ระดับใกล้เคียง **TAM CAGR ของอุตสาหกรรม network test & measurement ~4.6%** (ตามที่ระบุใน brief: $39.12B → $46.83B, 2026-2030) เพราะตลาดกระจัดกระจายมาก (100+ คู่แข่ง, top 5 ผู้เล่นรวมกันแค่ 33.7% share) ทำให้ยากที่จะรักษา growth premium เหนือ industry ต่อเนื่องได้เกิน 5 ปี
- **Terminal growth: 2.5%** — มาตรฐาน GDP + inflation blend ทั่วไป ไม่ให้ premium สูงกว่านี้เพราะ Moat เป็นแค่ Narrow (เข้า 2/7 Powers: Cornered Resource + Switching Costs) ไม่ใช่ Wide Moat ที่มี pricing power ยั่งยืนพอจะให้ terminal growth สูงกว่าค่าเฉลี่ยตลาด
- **FCF margin path (Stage 1):** ปี1 7% → ปี2 8.5% → ปี3 10% → ปี4 11% → ปี5 12% (terminal คงที่ 12%)
  - เหตุผล: full-year FY26 margin 5.4% ถูกกดจากต้นทุน integration ของ Spirent/Inertial Labs + interest expense ที่เพิ่มขึ้น 58% YoY แต่ **Q4 FY26 เดี่ยวกระโดดเป็น ~12.5%** (OCF $66.7M vs $23.8M ปีก่อน) — สมมติว่า margin ขยายตัวแบบค่อยเป็นค่อยไปสู่ระดับใกล้เคียง Q4 exit-rate ภายใน 5 ปี ไม่ใช่กระโดดทันที เพราะ non-GAAP op margin เต็มปีอยู่ที่ 20.6% เท่านั้น (ยังมี cash interest ~$47.4M/ปี + capex ~2% of revenue + cash tax ที่กิน margin) — 12% เป็นค่าที่ conservative กว่า non-GAAP op margin พอสมควร
- **Discount rate (WACC): 11.0%**
  - Risk-free rate: 5.18% (10Y US Treasury yield, ข้อมูลล่าสุดที่ระบบใช้ ณ 26 ก.ย. 2026 — สูงผิดปกติเทียบกับ historical average)
  - Equity Risk Premium: 5.0% (มาตรฐานตลาด)
  - Beta: **1.1 (ปรับประมาณเอง)** — หาได้จาก stockanalysis.com sourced beta = 0.87 แต่ตัวเลขนี้ต่ำผิดปกติเมื่อเทียบกับความผันผวนจริงที่สังเกตได้ (52-week range $12.05–$60.43 คือช่วงกว้างกว่า 5 เท่า) จึงปรับขึ้นเป็น 1.1 เพื่อสะท้อน realized volatility ที่สูงกว่า long-window regression beta บอกไว้ — ระบุชัดว่าเป็นการปรับประมาณ ไม่ใช่ตัวเลข sourced ตรงๆ
  - Cost of equity = 5.18% + 1.1 × 5.0% = 10.68% ≈ **11.0%** — ใช้ตรงเป็น WACC เพราะ net cash เกือบเป็นศูนย์ (+$6M) ไม่ต้อง weight กับ cost of debt
- **Shares outstanding:** 246.75M (diluted, ณ 23 ก.ย. 2026 — source: stockanalysis.com/Yahoo Finance)
- **Net cash/debt:** +$5.9M (cash $647.8M − total debt carrying value $641.9M)

## DCF Calculation (Base Case, WACC 11.0% / TG 2.5%)

| ปี | Growth | Revenue ($M) | FCF margin | FCF ($M) | Discount factor | PV FCF ($M) |
|---|---|---|---|---|---|---|
| FY26 (base) | — | 1,518.0 | 5.4% | 82.8 | — | — |
| ปี1 | 18% | 1,791.2 | 7.0% | 125.4 | 0.9009 | 113.0 |
| ปี2 | 15% | 2,059.9 | 8.5% | 175.1 | 0.8116 | 142.1 |
| ปี3 | 12% | 2,307.1 | 10.0% | 230.7 | 0.7312 | 168.7 |
| ปี4 | 8% | 2,491.7 | 11.0% | 274.1 | 0.6587 | 180.6 |
| ปี5 | 5% | 2,616.3 | 12.0% | 314.0 | 0.5935 | 186.3 |

- **Sum of PV of Stage-1 FCF ≈ $790.7M**
- **Terminal Value** = FCF₅ × (1+2.5%) ÷ (11.0%−2.5%) = 314.0 × 1.025 ÷ 0.085 ≈ **$3,785.9M**
- **PV of Terminal Value** = 3,785.9 × 0.5935 ≈ **$2,246.5M**
- **Enterprise Value** = 790.7 + 2,246.5 ≈ **$3,037.2M**
- **Equity Value** = EV + net cash 5.9 ≈ **$3,043.2M**
- **Fair Value/share** = 3,043.2M ÷ 246.75M ≈ **$12.33**

## Fair Value (Sensitivity: WACC ±1%, Terminal Growth ±0.5%)

- **Bear case (WACC 12.0%, TG 2.0%):** $10.50
- **Base case (WACC 11.0%, TG 2.5%): $12.33**
- **Bull case (WACC 10.0%, TG 3.0%):** $14.95

*(growth fade schedule และ margin path เดียวกันทั้ง 3 สถานการณ์ — ปรับเฉพาะ WACC/terminal growth ตามกฎ)*

## เทียบราคาปัจจุบัน $40.68

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($12.33) ถึง **+230%** และยังสูงกว่า **Bull case** ($14.95) ถึง +172% — ราคาตลาดปัจจุบันอยู่นอกช่วง sensitivity ทั้งหมดที่คำนวณได้ (bear-to-bull $10.50–$14.95) แสดงว่าตลาดกำลัง price-in สมมติฐานที่มองโลกในแง่ดีกว่าโมเดล bottom-up นี้มาก (เช่น สมมติว่า reported growth +40% หรือ margin ขยายเร็ว/สูงกว่านี้มากอย่างต่อเนื่องหลายปี หรือใช้ discount rate ต่ำกว่านี้มาก)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $40.43** — ไกลจาก conquest base case มาก (ต่างกัน +228%) — เหตุผลที่เป็นไปได้: Morningstar quant-model อาจยึด reported growth +40% (ไม่ตัด M&A) เป็นฐานต่อเนื่องหลายปี และ/หรือสมมติ margin ขยายตัวเข้าใกล้ non-GAAP op margin (20.6%) เร็วกว่าที่ conquest ประมาณ และ/หรือใช้ discount rate ต่ำกว่ามาก (โมเดล quant มักผูกกับ moat rating ที่ให้ credit สูงเกินจริงสำหรับ Narrow-moat ในตลาดกระจัดกระจาย)
- **GuruFocus GF Value $14.86** — **ใกล้เคียง conquest มาก** โดยเฉพาะใกล้กับ **Bull case ($14.95)** เกือบพอดี (ต่างกันแค่ ~0.6%) — สอดคล้องกันเพราะ historical-multiple regression ของ GuruFocus สะท้อน FCF margin ต่ำในอดีต (5.4% full-year) ได้ตรงกับสิ่งที่ DCF อิสระคำนวณได้จาก fundamentals จริง
- **สรุป:** conquest **เห็นด้วยกับ GuruFocus อย่างชัดเจน** (ทั้งคู่ชี้ว่า Expensive อย่างมาก) และ**ขัดแย้งกับ Morningstar อย่างรุนแรง** — เหตุผลหลักคือ Morningstar ดูเหมือนจะให้เครดิต growth ที่พองจาก M&A และ margin expansion ที่เร็ว/ยั่งยืนเกินกว่าที่ raw fundamentals (organic growth ~19-21%, FCF margin เต็มปีแค่ 5.4%, Narrow moat ในตลาดกระจัดกระจาย 100+ คู่แข่ง) จะสนับสนุนได้ → **2-ใน-3 แหล่ง (GuruFocus + conquest) ชี้ไปทาง Expensive อย่างสอดคล้องกัน**
