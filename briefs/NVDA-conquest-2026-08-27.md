# 💰 Conquest DCF: NVDA — 2026-08-27
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — refresh จาก 25 ส.ค. ด้วยตัวเลข Q2 FY2027 actual ที่ยืนยันแล้ว (ไม่ใช่ estimate)*

## ⚠️ Data correction สำคัญก่อนเริ่ม (ต้องแจ้งผู้ใช้)

Brief วันนี้ (`NVDA-2026-08-27.md`) และ prompt ที่ได้รับระบุว่า **Q3 FY2027 guidance = $91B ±2%** (ต่ำกว่า Q2 actual $96.2B — sequential deceleration ครั้งแรก) แต่จากการค้นสด (WebSearch/WebFetch) วันนี้ ตัวเลขที่ยืนยันจาก **3 แหล่งอิสระ** (NVIDIA Newsroom press release, StockTitan ที่ดึงจาก SEC filing โดยตรง, และบทความ preview ของ Tech Times ที่อ้างอิง BofA analyst) ตรงกันหมดว่า:

> **Q3 FY2027 revenue guidance = $108.0B ±2%** (ไม่ใช่ $91B)

นี่คือ **+12.3% QoQ จาก Q2 actual ($96.2B)** — ไม่ใช่ sequential decline — และ**สูงกว่า** Street consensus ที่ตั้งไว้ $103.9B ด้วยซ้ำ (guide beat ไม่ใช่ guide miss) แม้ YoY growth rate จะชะลอจาก +106% (Q2) เหลือ ~+89% (Q3 guide เทียบ Q3 FY26 $57.0B) ตามกฎ comp ฐานสูงขึ้นตามปกติ

**ผลกระทบ:** narrative ใน brief วันนี้เรื่อง "guidance ผิดหวัง/sequential ชะลอครั้งแรก" คลาดเคลื่อนจากข้อเท็จจริง — ควรแก้ไข brief และ Layer 4 ใหม่ แต่ DCF นี้จะใช้ **ตัวเลข $108.0B ที่ยืนยันแล้ว** เป็นฐานการคำนวณ growth fade (ไม่ใช้ $91B ที่ผิด)

## Assumptions

**TTM Base FCF (ยืนยันจาก actual quarters ทั้ง 4 ไตรมาสล่าสุด ไม่มีการประมาณการแล้ว):**

| ไตรมาส | Revenue | Operating CF | Capex | FCF |
|---|---|---|---|---|
| Q3 FY26 (ต.ค. 2025) | $57.0B | $23.75B | $1.64B | $22.09B |
| Q4 FY26 (ม.ค. 2026) | $68.1B | $36.2B | $1.3B* | $34.9B |
| Q1 FY27 (เม.ย. 2026) | $81.6B | $50.3B | $1.7B | $48.6B |
| Q2 FY27 (ก.ค. 2026) | $96.2B | $24.08B | $2.68B | $21.34B |
| **TTM รวม** | **$302.9B** | — | — | **$126.9B** |

*capex Q4 FY26 ประมาณจาก OCF-FCF gap

**TTM FCF margin = $126.9B ÷ $302.9B = 41.9%** — ต่ำกว่า Q1 FY27 เดี่ยวไตรมาส (~60%) เพราะ Q2 FY27 FCF ร่วงเหลือ $21.3B (จาก $48.6B ใน Q1) — สาเหตุยืนยันจาก earnings: **inventory build $21.4B→$25.8B + accounts receivable $40.7B** เพื่อรองรับดีมานด์ที่มากกว่าที่จะส่งมอบได้ในอีกหลายไตรมาสข้างหน้า (ไม่ใช่ margin compression ถาวร — net income/gross margin ยังขึ้นต่อเนื่อง) — การใช้ TTM (ถัวเฉลี่ย 4 ไตรมาส) แทนการเอา Q2 เดี่ยวมา annualize ช่วย normalize ความผันผวนจาก working-capital timing นี้แล้ว ถือเป็นฐานที่อนุรักษ์นิยมกว่า Q1-only แต่สมจริงกว่าการมองข้าม working-capital drag

**Base FCF ที่ใช้ในโมเดล: $127B**

**Growth fade (ปีที่ 1-5) — เหตุผล:**

| ปี | Growth (FCF) | เหตุผล |
|---|---|---|
| ปี 1 | 50% | Q3 FY27 guide ยืนยันแล้ว $108B (+89% YoY, +12.3% QoQ) ยังแรงมาก, Blackwell/Rubin ramp เต็มสูบ + hyperscaler capex guide $1.3T ปีหน้า — แต่ FCF growth วางไว้ต่ำกว่า revenue growth เพราะคาดว่า working-capital drag (inventory/receivables build) จะยังกดดันต่อเนื่องอีก 1-2 ไตรมาสก่อนจะ normalize |
| ปี 2 | 38% | Rubin ramp เต็มปี ยังหนุนแรงอยู่ แต่ custom ASIC erosion (market share 87%→70-75% และเร่งตัว) เริ่มกัดกิน incremental capex ของ hyperscaler มากขึ้น — Broadcom-partnered ASIC (Google TPU, Meta MTIA, Microsoft Maia, OpenAI Titan) มี backlog $73B แข่งโดยตรงในงาน inference |
| ปี 3 | 25% | ฐานรายได้ใหญ่มาก ($600B+ level) กฎ mean-reversion เริ่มมีน้ำหนักจริง + hyperscaler capex cycle มักมี digestion period หลัง buildout รอบใหญ่ + ASIC share erosion สะสมมากขึ้น |
| ปี 4 | 15% | เข้าใกล้ mature growth ของ infrastructure buildout รอบแรก, ตลาด training ยังอยู่กับ NVDA เป็นหลักแต่ inference โอนไป ASIC มากขึ้นเรื่อยๆ |
| ปี 5 | 8% | ใกล้ terminal, เหลือ premium เล็กน้อยจาก replacement cycle (GPU upgrade ทุก 2-3 ปี) + next-gen platform transitions |

**Terminal growth: 3.0%** — เท่าเดิมจากรอบก่อน ผูกกับ long-run GDP nominal growth ไม่ให้ premium สูงกว่านี้ เพราะ custom ASIC เป็นภัยคุกคามเชิงโครงสร้างที่ยืนยันเป็นรูปเป็นร่างชัดเจนขึ้นทุก brief (87%→70-75% share, ASIC shipment growth +44.6% YoY vs GPU merchant +16.1% YoY) — moat ยังแข็งแรงในฝั่ง training/frontier แต่ไม่มั่นใจพอจะให้ pricing power ไม่จำกัดตลอดไปในฝั่ง inference ที่กำลังเสียส่วนแบ่ง

**WACC: 13.0%** (cost of equity ล้วน — บริษัทมี net cash ไม่ต้อง weight cost of debt)
- Risk-free rate: 4.65% (US 10Y Treasury, ปลาย ส.ค. 2026 — เท่ากับรอบก่อน)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด กลางช่วง 4-6%)
- Beta: ~1.7 (ประมาณการเดิม คงไว้ — ราคาหุ้นยังเหวี่ยงแรงในระดับ AI-hype cycle เหมือนรอบก่อน ไม่มีเหตุผลใหม่ให้ปรับ)
- WACC = 4.65% + 1.7 × 5.0% = **13.15% ≈ 13.0%**

**Shares outstanding (diluted weighted average, Q2 FY27):** 24.3B

**Net cash:** Cash $22.44B + marketable debt securities $34.14B + marketable equity securities $42.78B = **$99.37B total liquid assets** − Total debt $33.37B (short-term $1.0B + long-term $32.4B, เพิ่มขึ้นมากจาก $12.8B ตอน Q1 เพราะออกหุ้นกู้ใหม่ใน Q1-Q2 FY27) = **+$66.0B net cash** (สูงกว่ารอบก่อน $37.5B มาก เพราะทั้ง cash และ investment portfolio โตเร็วกว่าหนี้ที่เพิ่ม)

## DCF Calculation ($B)

| | Y1 | Y2 | Y3 | Y4 | Y5 | Terminal |
|---|---|---|---|---|---|---|
| Growth | 50% | 38% | 25% | 15% | 8% | 3% |
| FCF | 190.5 | 262.9 | 328.6 | 377.9 | 408.1 | — |
| Discount factor (13%) | 0.885 | 0.783 | 0.693 | 0.613 | 0.543 | 0.543 |
| PV of FCF | 168.6 | 205.8 | 227.7 | 231.8 | 221.5 | — |

Terminal Value = $408.1B × 1.03 ÷ (0.13 − 0.03) = **$4,203.8B**
PV of Terminal Value = $4,203.8B × 0.543 = **$2,282.1B**

Sum PV of Stage-1 FCF = $1,055.5B
Enterprise Value = $1,055.5B + $2,282.1B = **$3,337.5B**
Equity Value = EV + net cash $66.0B = **$3,403.5B**

**Fair Value per share = $3,403.5B ÷ 24.3B shares = $140.1**

*(Implied sanity check: Y5 FCF $408B ที่ margin ~42% ⇒ Y5 revenue ~$971B, เทียบฐานปัจจุบัน TTM $303B = CAGR รายได้ 5 ปี ~26%/ปี — aggressive แต่อยู่ในขอบเขตที่เป็นไปได้ถ้า AI infra supercycle ดำเนินต่อตาม hyperscaler capex guide $1.3T)*

## Fair Value

| Scenario | WACC | Terminal g | FV/share |
|---|---|---|---|
| 🐻 Bear | 14.0% | 2.5% | **$122.8** |
| ⚪ Base | 13.0% | 3.0% | **$140.1** |
| 🐂 Bull | 12.0% | 3.5% | **$163.4** |

(Fade schedule คงเดิมทั้ง 3 scenario — ปรับแค่ WACC ±1% และ terminal growth ±0.5% ตามมาตรฐาน sensitivity)

## เทียบราคาปัจจุบัน $209.66

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($140.1) อยู่ **+49.6%**

แม้กระทั่ง Bull case ($163.4) ราคาปัจจุบันก็ยังสูงกว่าอยู่ **+28.4%** — ทุก scenario ยัง Expensive แต่ margin แคบลงชัดเจนจากรอบก่อน

## เทียบกับ conquest รอบก่อน (25 ส.ค.)

Base case ขยับขึ้นจาก **$122.6 → $140.1 (+14.3%)** เหตุผลหลัก:
1. **TTM FCF base สูงขึ้น** ($118B ประมาณการ → $127B ยืนยันจริง) จากการใช้ actual quarters ครบ 4 ไตรมาสแทนการประมาณการ Q1 FY26
2. **Net cash สูงขึ้นมาก** ($37.5B → $66.0B) เพราะทั้ง cash และ investment portfolio โตเร็วกว่าหนี้ที่เพิ่มขึ้น
3. **Growth fade ปีแรกๆ ปรับขึ้นเล็กน้อย** (Y2 35%→38%, Y3 22%→25%) เพราะ Q3 guide ที่ยืนยันแล้ว ($108B, guide beat) แข็งแกร่งกว่าที่คาดไว้เดิมตอนยังไม่มีตัวเลข Q2 actual/Q3 guide จริง
4. Terminal growth และ WACC คงเดิม (ไม่มีเหตุผลใหม่ให้เปลี่ยน risk profile เชิงโครงสร้าง)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $310** (ปรับขึ้นจาก $280 หลัง earnings) — ยังไกลจาก conquest base case ($140.1) มาก (Morningstar สูงกว่า +121%) เหตุผลหลักที่ต่างเหมือนรอบก่อน: Morningstar ใช้ WACC ต่ำกว่ามาก (มักราว 8-9% สำหรับ wide-moat mega-cap ด้วย beta ที่ smooth แล้ว) และให้ terminal growth/moat premium สูงกว่า เพราะเชื่อมั่นใน Cornered Resource moat ระยะยาวมากกว่า — Morningstar อ้างอิง hyperscaler capex $1.3T เป็นเหตุผลหลักที่ปรับ FV ขึ้น ซึ่ง conquest ก็รับรู้ปัจจัยเดียวกันแล้วในการปรับ growth fade ปีแรกๆ ขึ้น แต่ยัง discount แรงกว่ามากด้วย WACC ที่สูงกว่า
- **GuruFocus GF Value $389.06** (ปรับขึ้นจาก $354-370) — ไกลจาก conquest base case มากที่สุด (+178%) เพราะยังเป็น backward-looking historical-multiple regression ที่ผูกกับ P/E, P/S สูงที่ตลาดเคยยอมจ่ายช่วง AI cycle ไม่ใช่ DCF จาก cash flow จริง — GuruFocus เองยังติดป้าย "Possible Value Trap" ควบคู่กับตัวเลขสูงๆ นี้ ซึ่งขัดแย้งในตัวเองเหมือนรอบก่อน
- **สรุป:** Conquest ยัง **ไม่เห็นด้วยกับทั้งสองแหล่ง** แต่ช่องว่างแคบลงกว่ารอบก่อนเล็กน้อยเพราะ Base case ขยับขึ้นจาก $122.6→$140.1 ด้วยข้อมูล actual ที่แม่นขึ้น ตัวขับเคลื่อนหลักของช่องว่างที่เหลือยังเหมือนเดิม: (1) WACC สูงกว่ามาก (13% จาก raw beta ~1.7 เทียบกับ WACC ต่ำกว่าที่ analyst มักใช้สำหรับ wide-moat) และ (2) growth fade ที่ให้น้ำหนักกับความเสี่ยง custom ASIC erosion มากกว่า — 3-way split ยังคงอยู่ ไม่มีคู่ไหนเห็นตรงกันเลย ($140.1 vs $310 vs $389.06) — **Valuation ยัง inconclusive-แต่เอนไปทาง overvalued** จาก DCF มุมมองเข้มที่สุดในบรรดา 3 แหล่ง (ตามที่บันทึกไว้ใน memory ว่า conquest มี bias เชิงอนุรักษ์นิยมโดยธรรมชาติจาก WACC/terminal-growth ที่เข้มกว่าตลาดทั่วไป — ควรอ่านผลนี้เป็น "เพดานความเข้มงวด" ไม่ใช่คำตัดสินสุดท้ายเพียงแหล่งเดียว)
