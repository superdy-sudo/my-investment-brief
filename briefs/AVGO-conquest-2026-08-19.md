# 💰 Conquest DCF: AVGO (Broadcom Inc.) — 2026-08-19
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (FY2026 estimate):**
- Q1 FY2026 revenue (actual): $19.311B
- Q2 FY2026 revenue (actual, from brief): $22.19B
- Q3 FY2026 revenue (guidance): $29.4B
- Q4 FY2026 revenue (estimate): ~$34.6B — derived from company's own full-year AI semiconductor guidance ($56B) minus Q1-Q3 AI semi ($8.4B+$10.8B+$16B=$35.2B) = $20.8B implied Q4 AI semi, plus non-AI-semi/software portion extrapolated (~$13.8B, based on Q1-Q3 trend of $10.9B→$11.4B→$13.4B)
- **FY2026 total revenue estimate: ~$105.5B** (+65% YoY vs FY2025's $63.9B actual — this is a Claude estimate, not company guidance, since Broadcom does not guide a full fiscal year)
- FCF margin: 46% (per brief, current run-rate)
- **Base FCF (FY2026): ~$48.5B**

**Growth fade schedule, FY2027–FY2031 (Stage 1, ปี 1-5):**
| Year | Growth | Rationale |
|---|---|---|
| Y1 (FY2027) | 35% | ลงจาก ~65% blended FY2026 — เริ่ม lap ฐานที่สูงขึ้นมากจาก AI ramp ปีนี้ |
| Y2 (FY2028) | 25% | AI semi ยังโตแรงแต่ hyperscaler capex growth เริ่ม normalize; Google/Meta อาจกระจาย custom silicon supplier (ความเสี่ยงที่เคยถูกแฟลกใน prior brief: TPU revenue share risk) |
| Y3 (FY2029) | 17% | แข่งขันเข้ามาเต็มที่ในตลาด custom XPU; VMware/software segment โตช้าลงมาถ่วง blended growth |
| Y4 (FY2030) | 11% | เข้าใกล้ maturity ของ AI infra capex cycle |
| Y5 (FY2031) | 6% | ใกล้ terminal, moat (cornered-resource IP + VMware switching cost) ยังให้โตเหนือ GDP ได้บ้าง |

เหตุผลโดยรวมของ fade: ธุรกิจ AI semiconductor ของ Broadcom กำลังอยู่ใน parabolic phase (Q3 guide +84% YoY) ซึ่งไม่ยั่งยืนในระยะยาว — mean-reversion ทั่วไปของธุรกิจ hypergrowth semis บวกกับความเสี่ยง customer concentration (Google/Meta เป็นลูกค้าหลักของ custom XPU และมีแรงจูงใจกระจาย supplier) ทำให้ fade ค่อนข้างเร็วในปีที่ 1-3

**Terminal growth rate: 3%**
- สูงกว่า GDP มาตรฐาน (2-2.5%) เล็กน้อย เพราะ Wide Moat ที่ยั่งยืนจริง — Cornered Resource (custom XPU IP ที่ hyperscaler ลงทุนร่วมออกแบบ, switching cost สูงมาก) + VMware software switching costs — ให้ pricing power ต่อเนื่องแม้ในระยะยาว

**WACC: 11.7%**
- Risk-free rate: 4.70% (US 10Y Treasury, 2026-08-19)
- Beta: 1.45 (เฉลี่ยจาก Finbox 1.43, Investing.com 1.46, Yahoo Finance 1.47)
- Equity risk premium: 5.0% (มาตรฐานตลาด)
- Cost of equity = 4.70% + 1.45 × 5.0% = **11.95%**
- Cost of debt (pre-tax) = interest expense Q2 annualized ($776M×4=$3.104B) ÷ total debt ($64.907B) = 4.78%; after-tax (21% tax) ≈ 3.78%
- Weights: E = $1,719.6B (price $361.38 × 4.758B diluted shares), D = $64.907B (LT debt $62.655B + ST debt $2.252B), V = $1,784.5B
- WACC = (1719.6/1784.5)×11.95% + (64.907/1784.5)×3.78% = 11.56% + 0.14% = **11.7%**
- (Debt is small relative to Broadcom's ~$1.7T market cap, so WACC ≈ cost of equity effectively)

**Shares outstanding:** 4,758M diluted (per 10-Q, as of 2026-05-29)
**Net debt:** $64.907B debt − $19.6B cash = **$45.3B net debt**

## DCF Calculation (Base Case, WACC 11.7%, terminal g 3%)

| Year | FCF ($B) | Growth | Discount Factor | PV ($B) |
|---|---|---|---|---|
| FY2026 (base) | 48.53 | — | — | — |
| Y1 (FY2027) | 65.52 | 35% | 0.8954 | 58.68 |
| Y2 (FY2028) | 81.90 | 25% | 0.8015 | 65.64 |
| Y3 (FY2029) | 95.82 | 17% | 0.7175 | 68.75 |
| Y4 (FY2030) | 106.36 | 11% | 0.6424 | 68.33 |
| Y5 (FY2031) | 112.74 | 6% | 0.5751 | 64.84 |

Sum of PV (Y1-Y5) = **$326.2B**

Terminal Value = FCF5 × (1+g) ÷ (WACC−g) = 112.74 × 1.03 ÷ (0.117−0.03) = **$1,334.7B**
PV of Terminal Value = 1,334.7 × 0.5751 = **$767.6B**

Enterprise Value = 326.2 + 767.6 = **$1,093.8B**
Equity Value = EV + Cash − Debt = 1,093.8 + 19.6 − 64.907 = **$1,048.5B**

## Fair Value

- **Bear case** (WACC 12.7%, terminal g 2.5%): **$188/share**
- **Base case** (WACC 11.7%, terminal g 3.0%): **$220/share**
- **Bull case** (WACC 10.7%, terminal g 3.5%): **$266/share**

*หมายเหตุความอ่อนไหว: ถ้าใช้ TTM FCF (4 ไตรมาสล่าสุด, ~$34.7B ที่ margin 46%) เป็น base แทน FY2026 forward estimate จะได้ base case ต่ำกว่านี้อีก (~$177/share) — สะท้อนว่าผลลัพธ์ DCF อ่อนไหวมากต่อการเลือก base-year ในธุรกิจที่กำลังเร่งตัวแบบ parabolic (Q2 +48% YoY → Q3 guide +84% YoY) ตัวเลข base case ที่รายงานด้านบนใช้ FY2026 forward estimate ซึ่งให้น้ำหนักกับ momentum ปัจจุบันมากกว่า จึงเป็นค่าที่ conservative น้อยกว่าในสองวิธี*

## เทียบราคาปัจจุบัน $361.38

🔴 **Expensive** — สูงกว่า Base case FV ($220) อยู่ **+64%**

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $550** — ห่างจาก conquest base case มาก (+150%). ต่างกันหลักๆ ที่ horizon ของ high-growth stage: Morningstar (moat wide, uncertainty สูง) น่าจะใช้ explicit forecast period ยาวกว่า 5 ปี (10+ ปี) และ fade ช้ากว่านี้มาก เพื่อจับมูลค่าของ AI supercycle ทั้งช่วง ในขณะที่ conquest ใช้ 2-stage model แบบ 5 ปีมาตรฐานซึ่ง foreshortens high-growth window เร็วกว่า — ทำให้ terminal value (ที่โตแค่ 3%) กินสัดส่วนน้อยกว่าที่ Morningstar อาจให้กับปีท้ายๆ ของ high growth
- **GuruFocus GF Value $341.69** — ใกล้กว่า Morningstar แต่ยังห่างจาก conquest base case ~55%. GF Value เป็น backward-looking historical-multiple regression ที่ผูกกับ multiple ในอดีตของ Broadcom (ซึ่งช่วงหลังเทรดที่ multiple สูงมากจาก AI narrative) จึงยังสูงกว่าตัวเลขที่ได้จากการคำนวณ DCF ตรงๆ จาก cash flow
- **สรุป:** Conquest ให้มุมมองระมัดระวังกว่าทั้งสองแหล่ง — ใกล้เคียงทิศทางเดียวกับ GuruFocus (ทั้งคู่มองว่าราคาปัจจุบันแพงกว่ามูลค่าที่ควรจะเป็น) แต่ conquest เข้มงวดกว่ามาก เพราะวิธี DCF จากล่างขึ้นบนที่ fade growth เร็วภายใน 5 ปีมี sensitivity สูงต่อสมมติฐาน terminal growth/WACC และต่อการเลือก base-year ในธุรกิจที่กำลังโตแบบ parabolic — ผลลัพธ์นี้ควรอ่านเป็น "sanity check ฝั่งระมัดระวัง" ไม่ใช่คำตอบสุดท้าย โดยเฉพาะถ้าเชื่อว่า AI semiconductor demand ของ Broadcom จะยั่งยืนได้นานกว่า 5 ปีที่โมเดลนี้สมมติ
