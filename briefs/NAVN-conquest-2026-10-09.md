# 💰 Conquest DCF: NAVN — 2026-10-09
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — single-source, บริษัทยังขาดทุน GAAP จึงอ่อนไหวต่อ assumption สูงมาก*

## Raw fundamentals ที่ใช้ (source)
- Revenue FY26 (ปีจบ 2026-01-31) $702.3M vs FY25 $536.8M (+30.8%) — SEC XBRL companyfacts (10-K), ดึง 2026-10-09
- Revenue Q2 FY27 (จบ 2026-07-31) $232.8M vs $172.0M (+35.4%); H1 FY27 $453.0M vs $329.4M (+37.5%) — SEC 10-Q
- Revenue TTM ≈ $825.9M (คำนวณ: FY26 + H1 FY27 − H1 FY26)
- Guidance FY27 revenue $927–933M (+32%), Q3 $253–255M (~+30%) — Navan Q2 FY27 press release 2026-09-09 (ผ่าน Quartr/TIKR/Fool summary; เข้าถึง Business Wire ตรงไม่ได้ 403)
- OCF TTM ≈ $47.3M; capex ≈ $1.8M; capitalized software ≈ $19.8M → FCF TTM ≈ $25.7M (3.1% margin) (คำนวณจาก SEC 10-K/10-Q) | บริษัทรายงาน FCF TTM $28.3M (Quartr summary — นิยามต่างเล็กน้อย)
- SBC TTM ≈ $225.3M (27% ของ revenue, รวมค่าใช้จ่ายครั้งเดียวช่วง IPO); H1 FY27 $79.2M (17.5% ของ revenue) — SEC
- Cash & equivalents 2026-07-31 $653.0M (SEC 10-Q); debt ≈ $125M (10-K FY26 $124.8M; Quartr Q2 $125M) → net cash ≈ $528M (ใช้ตัวเลข SEC ที่ยืนยันได้ ไม่ใช้ $820M ของ Quartr ที่ไม่ทราบนิยาม)
- Shares: 260.4M (Webull getQuote totalShares 2026-10-09) — ยังไม่รวม dilution จาก options/RSU
- ราคา $23.08 (ปิด Oct 8, Yahoo curl); market cap ≈ $6.0B (Webull)

## Assumptions
- Base: Revenue FY27E $930M (กลางช่วง guidance) → growth fade ปี1 28% → 22% → 17% → 13% → ปี5 9% (เหตุผล: เริ่มต่ำกว่า guide ปัจจุบัน ~30-32% ตาม mean-reversion; TAM บริษัทประเมินเอง $185B (S-1) แต่คู่แข่งหนัก Concur/Amex GBT/BCD/Brex/Ramp)
- FCF margin ก่อน SBC: 10% → 14% → 17% → 19% → 20% (ปีล่าสุด TTM 3.1%, Q2 ≈ 8%; guidance non-GAAP op margin Q3 ~14%)
- หัก SBC เป็นต้นทุนจริง (owner FCF): SBC 14% → 12% → 10% → 9% → 8% ของ revenue → margin สุทธิ −4% → 2% → 7% → 10% → 12% (เหตุผล: SBC เป็นต้นทุนที่ถูกโอนจากผู้ถือหุ้นจริง — ถ้าไม่หักจะ overstate)
- Terminal growth 3.0% (เหตุผล: ธุรกิจ software/payments ที่ยังโตเหนือ GDP ได้ระยะหนึ่ง)
- WACC 12.74% = rf 5.242% (^TNX ปิด Oct 8 จาก portfolio.md) + beta 1.5 × ERP 5% — **beta 1.5 เป็นค่าประมาณ** (หุ้น IPO ล่าสุด 52wk range $8.11–$30.88; หาค่า beta จริงไม่ได้) ไม่มี debt weight สำคัญ (net cash)
- Net cash $528M; shares 260.4M

## DCF Calculation (Base, $M)
| ปี | Revenue | FCF margin (หัก SBC) | FCF | PV @12.74% |
|---|---|---|---|---|
| 1 | 1,190 | −4% | −48 | −42 |
| 2 | 1,452 | 2% | 29 | 23 |
| 3 | 1,699 | 7% | 119 | 83 |
| 4 | 1,920 | 10% | 192 | 119 |
| 5 | 2,093 | 12% | 251 | 138 |
- PV stage 1 = $320M | Terminal value = 251 × 1.03 ÷ (12.74% − 3%) = $2,655M → PV $1,458M
- EV ≈ $1,778M + net cash $528M = Equity $2,306M ÷ 260.4M shares

## Fair Value
- Bear case (WACC 13.74%, g 2.5%): **$7.83**
- **Base case: $8.86**
- Bull case (WACC 11.74%, g 3.5%): **$10.26**
- ข้อมูลอ้างอิงเท่านั้น (ไม่ใช่ base): ถ้า *ไม่หัก SBC* (FCF margin ปี5 20%) ได้ ≈ $14.90

## เทียบราคาปัจจุบัน $23.08 (ปิด Oct 8)
🔴 Expensive — ราคาสูงกว่า Base FV ≈ +160% (สูงกว่าแม้ในกรณีไม่หัก SBC $14.90 ≈ +55%) — single-source, ห้ามฟันธงขาดเกินกว่า bucket
- Morningstar: quant-only ไม่พบตัวเลข (⚪) | GuruFocus GF Value: ไม่มี (บริษัทขาดทุน)
- **สรุป:** ไม่มีแหล่งอื่นเทียบ — conquest บอกว่า ณ ราคานี้ตลาดจ่ายล่วงหน้าสำหรับ growth + margin expansion ที่มากกว่า base มาก (ราคาปัจจุบันบ่งชี้ว่าต้องได้ FCF margin หลัง SBC สูงกว่า 12% ที่ปี 5 หรือโตเร็วกว่า fade ที่ใช้) — DCF นี้อ่อนไหวต่อ SBC และ beta มาก
