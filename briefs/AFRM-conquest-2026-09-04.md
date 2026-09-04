# 💰 Conquest DCF: AFRM — 2026-09-04
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (FY26 actual, ปีสิ้นสุด 30 มิ.ย. 2026):** Revenue $4,260M, FCF ≈ $605M (margin ~14.2%) — จาก 10-K/cash flow statement (stockanalysis/gurufocus, ~$601-609M consistent)
- **Revenue growth fade (5 ปี):** Y1 29% → Y2 24% → Y3 18% → Y4 12% → Y5 7%
  - เหตุผล: Y1 ใช้ FY27 guidance ตรง ๆ (GMV >$64B = growth ~27-29% จาก FY26 GMV $50.2B, take rate ~8.5% คงที่ → revenue growth ~29%); Y2-Y5 fade ลงตาม mean-reversion ทั่วไปของ high-growth fintech หลัง IPO+scale, บวกแรงกดดันแข่งขัน (Klarna, PayPal, banks) ที่ brief ระบุเป็น bear case, และ law of large numbers เมื่อ GMV ผ่าน $50B
- **FCF margin expansion:** 14.2% (FY26) → 15% (Y1) → 17% (Y2) → 19% (Y3) → 21% (Y4) → 23% (Y5)
  - เหตุผล: operating leverage ที่กำลังเกิดจริง (operating income +153% YoY, GAAP profitable แล้ว), FY27 guide adjusted operating margin >30.5% สนับสนุนทิศทาง margin expansion ต่อเนื่อง แต่ conquest ใช้ FCF margin ระดับต่ำกว่า adjusted-OM มาก (conservative gap เพราะ SBC dilution ยังไม่หมดไป)
- **Terminal growth:** 3% (ผูก long-run GDP+inflation มาตรฐาน ไม่ได้ให้ premium เพิ่มเพราะ moat เป็น Narrow ไม่ใช่ Wide ตาม Morningstar และแข่งขันในตลาด BNPL รุนแรงขึ้นเรื่อย ๆ)
- **WACC:** 18.3% = risk-free 4.79% (10Y UST ต้น ก.ย. 2026) + beta 2.70 × ERP 5%
  - Beta 2.70 เป็นตัวเลขจาก market data ปัจจุบัน (สูงผิดปกติเทียบหุ้นทั่วไป แต่สมเหตุสมผลสำหรับ balance-sheet lender ที่ sensitivity สูงกับดอกเบี้ย — ราคาหุ้นเพิ่งร่วง 5% จาก 10Y yield พุ่งขึ้นเมื่อต้นเดือนนี้) — ใช้ cost of equity ตรง ๆ เพราะปรับ net cash ที่ corporate level แล้ว (ดูด้านล่าง)
- **Net cash/debt (corporate-level เท่านั้น):** Cash+investments ~$1,770M − Convertible notes 2029 $800M = **+$970M net cash**
  - หมายเหตุสำคัญ: total debt งบดุลจริงอยู่ที่ ~$9.1-10B แต่เกือบทั้งหมดเป็น **warehouse funding debt** ที่ผูกกับ loans receivable โดยตรง (non-recourse, asset-backed) — สินทรัพย์ (receivables) หักล้างหนี้ก้อนนี้ในตัวอยู่แล้ว จึงไม่รวมเข้า EV bridge ตรง ๆ (ตรงกับที่ brief ระบุว่า Net Debt/EBITDA คำนวณตรงไม่ได้ชัดเพราะเหตุผลเดียวกัน)
- **Diluted shares outstanding:** ~305M (ประมาณจาก 284.4M Class A shares + Class B + dilution จาก options/RSU/convertible — เป็นค่าประมาณ ไม่ใช่ตัวเลขแม่นยำ)

## DCF Calculation (Base case)

| ปี | Revenue ($M) | Growth | FCF margin | FCF ($M) | Discount factor @18.3% | PV FCF ($M) |
|---|---|---|---|---|---|---|
| Y1 | 5,495 | 29% | 15% | 824 | 0.845 | 697 |
| Y2 | 6,814 | 24% | 17% | 1,158 | 0.715 | 828 |
| Y3 | 8,041 | 18% | 19% | 1,528 | 0.604 | 923 |
| Y4 | 9,006 | 12% | 21% | 1,891 | 0.511 | 966 |
| Y5 | 9,636 | 7% | 23% | 2,216 | 0.432 | 957 |

Sum PV of FCF (Y1-Y5) ≈ **$4,371M**

Terminal Value = FCF_Y5 × (1+3%) / (18.3% − 3%) = 2,216 × 1.03 / 0.1529 ≈ **$14,928M**
PV of Terminal Value = 14,928 × 0.432 ≈ **$6,448M**

**Enterprise Value ≈ $10,819M**
+ Net cash (corporate-level) $970M
**Equity Value ≈ $11,789M**
÷ Diluted shares ~305M

## Fair Value

- Bear case (WACC 19.3%, terminal g 2.5%): **$35.50**
- **Base case: $38.65**
- Bull case (WACC 17.3%, terminal g 3.5%): **$42.49**

## เทียบราคาปัจจุบัน $74.30

🔴 **Expensive** — สูงกว่า Base case FV ($38.65) ประมาณ **+92%**

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $53** — ไกลจาก conquest base case ($38.65) ~+37%; ทั้งคู่เห็นตรงกันว่าราคาปัจจุบันแพงเกินพื้นฐาน แต่ conquest เข้มกว่า เพราะ WACC ที่ใช้ (18.3%, ขับเคลื่อนโดย beta 2.70 ที่สูงมากในภาวะดอกเบี้ยขาขึ้นตอนนี้) สูงกว่าที่ Morningstar น่าจะใช้ในโมเดล analyst ของเขา
- **GuruFocus GF Value $73.72** — ไกลจาก conquest base case มาก (~+91%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่สะท้อน sentiment/multiple ของตลาดปัจจุบัน ไม่ใช่ DCF จาก cash flow จริง — เมื่อตลาดให้ multiple สูงต่อเนื่อง (growth story), GF Value จะไล่ตามราคาขึ้นไปด้วย ทำให้ดูเหมือน "Fair" ทั้งที่ cash flow พื้นฐานยังไม่สนับสนุนราคานี้
- **สรุป:** conquest เห็นด้วยกับฝั่ง Morningstar (Expensive) ชัดเจน และเข้มกว่าด้วยซ้ำ — สาเหตุหลักคือ WACC สูงจาก beta 2.70 (หุ้น balance-sheet lender ที่ sensitivity สูงกับ 10Y yield ซึ่งกำลังพุ่งขึ้นช่วงนี้พอดี) ทำให้ terminal value ถูก discount แรงกว่าโมเดล analyst ทั่วไป ควรอ่าน conquest number นี้เป็น "มุมมองที่เข้มที่สุดในสามแหล่ง" ไม่ใช่คำตัดสินสุดท้าย — ถ้า beta แท้จริงต่ำกว่า 2.70 (ตัวเลขนี้เป็นค่าประมาณจาก market data ปัจจุบัน ไม่ใช่ตัวเลขที่ยืนยัน 100%) fair value จะขยับขึ้นได้พอสมควร แต่ด้วย gap ขนาด ~90% จากราคาปัจจุบัน ต่อให้ปรับ beta ลงเหลือ ~1.5 (WACC ~12.3%) ก็ยังต่ำกว่าราคาตลาดอยู่ดี → valuation risk เป็นประเด็นจริง ไม่ใช่แค่ noise จาก assumption
