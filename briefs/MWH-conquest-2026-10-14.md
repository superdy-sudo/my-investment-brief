# 💰 Conquest DCF: MWH (SOLV Energy) — 2026-10-14
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — แหล่งเดียว เพราะไม่มี Morningstar/GF*

## ข้อจำกัดสำคัญ (อ่านก่อน)
- **ไม่มี FCF ระดับปีเต็ม/TTM** — มีแค่ H1'26: CFO $46.0M − capex $16.0M = FCF ~$30.1M (~1.8% ของ rev) และไม่มี H1'25 เทียบ; EPC มี working-capital swing สูง ใช้ 1.8% ต่อยอดตรงๆ ไม่สะท้อน earning power
- จึง **สร้าง Base FCF แบบ normalized** จาก revenue/Adj EBITDA guidance FY26 × FCF margin ที่ผมสมมติเอง (ไม่ใช่ตัวเลขรายงาน) → ผลอ่อนไหวต่อ FCF margin มาก และ **ความมั่นใจต่ำ-ปานกลาง**
- Beta ไม่มีข้อมูล (IPO Feb 2026 ไม่ถึงปี) → ประมาณการ

## Assumptions
- Base year (FY26E): Revenue $3,920M (midpoint guidance $3.87–3.97B); Adj EBITDA midpoint $495M (12.6%) — ใช้เป็น reference ของ margin
- FCF margin (normalized, **สมมติ**): ปี1 4.5% → 5.0% → 5.5% → 5.5% → 5.5% ของ revenue. เหตุผล: ~36–44% ของ Adj EBITDA 12.6% หลังหักภาษี ~25%, SBC/ที่ Adj EBITDA บวกกลับ, capex เบา (~$16M/H1), และ working capital ที่โตตาม revenue; ต่ำกว่า H1'26 จริง (1.8%) แต่ H1 ถูกกดจาก WC ของ revenue +72% — ถ้า WC ยังกิน cash ต่อ ค่านี้สูงเกินจริง
- Revenue growth fade: ปี1 22% → 16% → 12% → 8% → 5%. เหตุผล: backlog $8.9B (+44%) ให้ visibility ถึง 2027-28, FY26 โตสูงส่วนหนึ่งจาก M&A; หลังนั้น EPC cyclical/พึ่ง policy จึง mean-revert ลงใกล้ terminal ไว (ไม่มี TAM ยืนยัน)
- Terminal growth: 2.5% (moat ไม่ชัด, EPC project-based → ไม่ให้สูงกว่ากลาง)
- Discount rate: Cost of equity = Rf 5.217% (10Y, brief 2026-10-14) + beta 1.4 (**ประมาณ**: EPC/cyclical/IPO ใหม่) × ERP 5% = **12.2%**; net cash จึงใช้ Ke เป็น WACC
- Diluted shares: 201.7M (Class A+B) | Net cash: ~$340M (cash $364.0M − equipment financing $24.4M; ไม่นับ lease $59.2M)

## DCF Calculation (Base, $M)
| ปี | Revenue | FCF | PV @12.2% |
|---|---|---|---|
| 1 | 4,782 | 215 | 192 |
| 2 | 5,548 | 277 | 220 |
| 3 | 6,213 | 342 | 242 |
| 4 | 6,710 | 369 | 233 |
| 5 | 7,046 | 388 | 218 |

- PV Stage 1 = $1,105M
- Terminal value = 388 × 1.025 ÷ (12.2% − 2.5%) = $4,095M → PV = $2,303M (~68% ของ EV)
- EV = $3,408M + net cash $340M = Equity $3,748M ÷ 201.7M = **$18.58/หุ้น**

## Fair Value
- Bear (WACC 13.2%, g 2.0%): **$16.43**
- **Base (WACC 12.2%, g 2.5%): $18.58**
- Bull (WACC 11.2%, g 3.0%): **$21.51**
- ทดสอบเพิ่ม (ไม่ใช่ base): ถ้า FCF margin ค้างที่ 1.8% ตลอด → FV ~$7.32 (downside ของ assumption FCF); ทั้ง 3 สถานการณ์ต่ำกว่าราคาปัจจุบันทั้งหมด

## เทียบราคาปัจจุบัน $25.73
🔴 Expensive — ราคาสูงกว่า Base FV +38.5% (FV ต่ำกว่าราคา −27.8%); ราคายังสูงกว่า Bull case ($21.51) ด้วย +19.6%

## เทียบกับแหล่งอื่น
- Morningstar / GuruFocus: ไม่มีข้อมูล (n/a) — conquest เป็นแหล่งเดียว ไม่มี 2-ใน-3
- Analyst consensus ~$45.18 (ไม่นับเป็น FV): ไกลจาก conquest มาก; ช่วงต่างมาจาก analyst น่าจะใช้ margin/growth ที่ยั่งยืนกว่าและ multiple EBITDA, ส่วนผมคิด FCF จริงที่ EPC เก็บเป็นเงินสดได้ต่ำ
- **สรุป:** DCF นี้ไวต่อ FCF margin (สมมติ) — เพื่อให้ FV = $25.73 ต้อง FCF margin ระยะยาวคงที่ราว ~7.7% ทุกปี (คำนวณ: 7.5% → $25.16, 7.0% → $23.60) ซึ่งสูงกว่าที่ข้อมูลปัจจุบันยืนยันได้ จึงไม่มีฐานรองรับราคาปัจจุบัน; ผลไม่ใช่การทำนายราคา
