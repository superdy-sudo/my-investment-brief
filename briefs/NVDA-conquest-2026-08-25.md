# 💰 Conquest DCF: NVDA — 2026-08-25
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — คำนวณเป็นแหล่งที่ 3 เพราะ Morningstar ($280) กับ GuruFocus ($354-370) ต่างกัน 32% เกินเกณฑ์*

**หมายเหตุ timing:** NVDA มี earnings (Q2 FY2027) วันที่ 2026-08-26 หลังตลาดปิด — DCF นี้ใช้ fundamentals ที่ยืนยันแล้วถึง Q1 FY2027 เท่านั้น ไม่รวมตัวเลขที่ยังไม่ประกาศ

## Assumptions

**Base FCF (TTM ประมาณการ ณ สิ้น Q1 FY2027):** ~$118B
- อ้างอิง: FY2026 full year (ปีปิดงบ 25 ม.ค. 2026) FCF ยืนยันแล้ว = $96.68B (revenue $215.9B, +65% YoY)
- Q1 FY2027 (ปิด 26 เม.ย. 2026) เดี่ยวไตรมาส: revenue $81.6B (+85% YoY), FCF $49B (margin ~60%)
- Q1 FY2026 (ไตรมาสเดียวกันปีก่อน) FCF ประมาณ ~$25.8B (ประมาณการจาก revenue $44.1B และ margin ระดับนั้น — ตัวเลขที่ค้นเจอจากเว็บขัดแย้งกันเอง จึงใช้ประมาณการจาก margin แทน)
- TTM FCF = FY2026 FCF ($96.68B) − Q1 FY2026 FCF (~$25.8B) + Q1 FY2027 FCF ($49B) ≈ **$118B** (นี่คือค่าประมาณ ไม่ใช่ตัวเลขที่บริษัทรายงานตรงๆ เพราะบริษัทไม่รายงาน TTM แยก)

**Growth fade (ปีที่ 1-5) — เหตุผล:**
| ปี | Growth | เหตุผล |
|---|---|---|
| ปี 1 | 50% | ใกล้เคียง guidance ไตรมาสถัดไป (Q2 FY27 ~+56% YoY ตาม guide) แต่ full-year FY2027 จะช้าลงจาก comp ฐานสูงขึ้นเรื่อยๆ |
| ปี 2 | 35% | Blackwell/Vera ramp ยังหนุนอยู่ แต่ custom ASIC (Google/Amazon/Microsoft/Meta) เริ่มแย่ง incremental capex มากขึ้น (custom silicon share คาด 20.9%→27.8% ปี 2026) |
| ปี 3 | 22% | ฐานรายได้ใหญ่ขึ้นมาก ($400B+ level) กฎ mean-reversion ของธุรกิจโตเร็วเริ่มมีผล + hyperscaler capex cycle มักมี pause/digestion period |
| ปี 4 | 14% | เข้าใกล้ mature growth ของ infrastructure buildout ระยะแรก |
| ปี 5 | 8% | ใกล้ terminal มากขึ้น เหลือ premium เล็กน้อยจาก replacement cycle (GPU upgrade ทุก 2-3 ปี) |

**Terminal growth: 3.0%** — ผูกกับ long-run GDP nominal growth ทั่วไป ไม่ใส่ premium สูงกว่านี้แม้ moat แข็งแรง เพราะ custom ASIC เป็นภัยคุกคามเชิงโครงสร้างที่เริ่มเป็นรูปเป็นร่างแล้ว (ไม่ใช่แค่ทฤษฎี) — ไม่มั่นใจพอจะให้ pricing power คงอยู่ไม่จำกัดแบบ terminal growth สูงกว่าตลาด

**WACC: 13.0%** (คำนวณจาก cost of equity ล้วน เพราะบริษัท net-cash — ไม่มีหนี้สุทธิที่ต้อง weight)
- Risk-free rate: 4.65% (US 10Y Treasury, 24 ส.ค. 2026)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด, กลางช่วง 4-6%)
- Beta: ~1.7 (ประมาณการของฉันเอง — ตัวเลขที่หาเจอจากเว็บกระจาย 1.98 (GuruFocus) ถึง 2.21 (แหล่งอื่น) ซึ่งสูงจากความผันผวนช่วง AI hype cycle ปี 2024-2026; เลือกใช้ค่าต่ำกว่าที่หาเจอเล็กน้อยเพราะ raw beta ช่วงนี้สะท้อน sentiment volatility ของตลาดทั้งหมดที่ผูกกับ NVDA มากกว่าความเสี่ยงเชิงธุรกิจจริง แต่ยังคงสูงกว่า 1 มากเพราะหุ้นเหวี่ยงแรงจริง)
- WACC = 4.65% + 1.7 × 5.0% = 4.65% + 8.5% = **13.15%** ≈ 13.0%

**Shares outstanding (diluted):** 24.39B (Q1 FY2027)

**Net cash (ไม่ใช่ net debt):** Cash + marketable securities $50.3B − Total debt $12.8B = **+$37.5B net cash** (ตรวจสอบใหม่จากตัวเลขล่าสุด — ต่างจาก "$2.43B net debt" ที่อยู่ใน brief เดิม ซึ่งน่าจะอ้างอิงช่วงเวลา/นิยามต่างกัน ใช้ตัวเลขที่ค้นสดวันนี้แทน)

## DCF Calculation ($B)

| | Y1 | Y2 | Y3 | Y4 | Y5 | Terminal |
|---|---|---|---|---|---|---|
| Growth | 50% | 35% | 22% | 14% | 8% | 3% |
| FCF | 177.0 | 239.0 | 291.6 | 332.4 | 359.0 | — |
| Discount factor (13%) | 0.885 | 0.783 | 0.693 | 0.613 | 0.543 | 0.543 |
| PV of FCF | 156.6 | 187.2 | 202.1 | 203.9 | 194.9 | — |

Terminal Value = $359.0B × 1.03 ÷ (0.13 − 0.03) = **$3,697.7B**
PV of Terminal Value = $3,697.7B × 0.543 = **$2,007.4B**

Sum PV of Stage-1 FCF = $944.7B
Enterprise Value = $944.7B + $2,007.4B = **$2,952.1B**
Equity Value = EV + net cash $37.5B = **$2,989.6B**

**Fair Value per share = $2,989.6B ÷ 24.39B shares = $122.6**

## Fair Value

| Scenario | WACC | Terminal g | FV/share |
|---|---|---|---|
| 🐻 Bear | 14.0% | 2.5% | **$107.4** |
| ⚪ Base | 13.0% | 3.0% | **$122.6** |
| 🐂 Bull | 12.0% | 3.5% | **$143.1** |

(Fade schedule คงเดิมทั้ง 3 scenario — ปรับแค่ WACC ±1% และ terminal growth ±0.5% ตามมาตรฐาน sensitivity)

## เทียบราคาปัจจุบัน $213.13
🔴 **Expensive** — ราคาสูงกว่า Base case FV ($122.6) อยู่ **+73.8%**

แม้กระทั่ง Bull case ($143.1) ราคาปัจจุบันก็ยังสูงกว่าอยู่ +49%

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $280** — ไกลจาก conquest base case ($122.6) มาก (Morningstar สูงกว่า +128%) เหตุผลหลักที่ต่าง: Morningstar น่าจะใช้ WACC ต่ำกว่ามาก (มักอยู่ราว 8-9% สำหรับ wide-moat mega-cap เพราะใช้ beta ที่ปรับ smooth แล้วไม่ใช่ raw beta ระดับ 2.0) และให้ terminal growth/moat premium สูงกว่า เพราะเชื่อมั่นใน Cornered Resource moat ระยะยาวมากกว่าที่ conquest ให้เครดิต
- **GuruFocus GF Value $354-370** — ไกลจาก conquest base case มากกว่าอีก (+189% ถึง +202%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ผูกกับ P/E, P/S ในอดีตของ NVDA เอง (ซึ่งช่วงที่ผ่านมาตลาดให้ multiple สูงมากตลอด AI cycle) ไม่ใช่ DCF จาก cash flow จริง — จึงสะท้อน "ราคาที่ตลาดเคยยอมจ่าย" มากกว่า "มูลค่าจาก cash flow future" ทั้งที่ GuruFocus เองยังติดป้าย "Possible Value Trap" บนหุ้นนี้ (valuation score 4/10) ซึ่งขัดแย้งกับตัวเลข GF Value สูงๆ ที่ตัวเองคำนวณออกมา — เป็นสัญญาณว่า GF Value อาจ over-extrapolate multiple ในอดีตที่ไม่ยั่งยืน
- **สรุป:** Conquest **ไม่เห็นด้วยกับทั้งสองแหล่ง** และให้มุมมองที่อนุรักษ์นิยมกว่ามาก ตัวขับเคลื่อนหลักของช่องว่างคือ (1) WACC ที่สูงกว่ามาก (13% จาก raw beta ~1.7-2.0 ของหุ้นที่เหวี่ยงแรงช่วง AI cycle เทียบกับที่ analyst มักใช้ WACC ต่ำกว่าสำหรับ wide-moat) และ (2) growth fade ที่อนุรักษ์นิยมกว่า เพราะให้น้ำหนักกับความเสี่ยง custom ASIC ที่เป็นรูปเป็นร่างแล้วมากกว่าที่ทั้งสองแหล่งดูเหมือนจะให้เครดิต — ผลคือ 3-way split จริงๆ ไม่ใช่ "2 ใน 3 เห็นตรงกัน": ทั้ง 3 แหล่งประเมิน fair value ต่างกันมาก ($122.6 vs $280 vs $354-370) ซึ่งหมายความว่าแม้จะเรียก conquest เป็น "tie-breaker" ไม่ได้เพราะไม่มีคู่ไหนเห็นตรงกันเลย — Valuation ยังคงต้องระบุเป็น **สูงมาก-inconclusive-แต่เอนไปทาง overvalued** เพราะ DCF จาก raw cash flow (แหล่งเดียวที่ไม่พึ่ง multiple ในอดีตหรือ moat-premium ที่ประเมินเชิงคุณภาพ) บอกว่าแพงกว่ามูลค่าจริงชัดเจนที่สุดในบรรดา 3 แหล่ง
