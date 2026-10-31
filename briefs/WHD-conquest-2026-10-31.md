# 💰 Conquest DCF: WHD (Cactus, Inc.) — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — single-source: ไม่มี Morningstar/GF Value ให้เทียบ*

## Assumptions
- **Base FCF (normalized): ~$310M** — คำนวณเอง: revenue run-rate = Q3'26 $430.9M x 4 = ~$1,724M [8-K ex.99.1 ผ่าน brief WHD-2026-10-31]; FCF margin ที่ใช้ 18% (Q3 ex-ก้อนจ่าย Baker Hughes $91.0M = ~$93.3M หรือ ~21.7% ของ revenue [brief]; haircut ลงเป็น 18% เพราะ Q3 เดียวอาจมี working capital เอื้อ, ธุรกิจ cyclical และ capex ปี 2026 ~$65M) — **18% เป็นการประมาณของ agent ไม่ใช่ตัวเลขที่บริษัทรายงาน**; ไม่นับ $91.0M จ่ายครั้งเดียว
- **Growth fade (ปี1→5): 5% → 6% → 5% → 4% → 3%** — เหตุผล: revenue Q3 -4.1% q/q, Q4 guide "modestly increase", US land rig count คาดทรงตัว, backlog $615.6M (ส่วนใหญ่ Cactus International) [brief]; +63% YoY ปน acquisition (Baker Hughes) ไม่แยก organic จึงไม่ extrapolate; ใช้ run-rate ของ Q3 ที่รวม acquisition แล้วโตแบบ low-single-digit ตามวัฏจักรน้ำมัน/ gas ปี 2 ขยับขึ้นเล็กน้อยจาก backlog/ผลเต็มปีของ int'l
- **Terminal growth: 2.5%** — ผูกกับ long-run GDP/inflation; ไม่ให้สูงกว่านี้เพราะ moat ยังไม่ยืนยันด้วยแหล่งอิสระและธุรกิจ cyclical
- **WACC: 11.43%** = risk-free 4.929% (10Y, brief daily 2026-10-30 ใน git log) + beta 1.30 x ERP 5.0% — beta 1.30 เป็น**ค่าประมาณ**จากช่วงที่พบ (Google Finance 1.38, Snowball 1.373, MarketChameleon 1.24, eToro 1.19; WebSearch 2026-10-31); ไม่มี bank debt → ใช้ cost of equity ตรงๆ
- **Shares: 80.2M (fully-exchanged)** = Class A 70.1M + Class B 10.1M (ผูกกับ CC Units ที่แลกเป็น Class A ได้ 1:1) ณ 30 ก.ย. 2026 [10-Q Q3'26 sec.gov/Archives/edgar/data/0001699136/000162828026068341/whd-20260930.htm ผ่าน WebSearch]; ตรงกับ ~80.2M ของ Webull; **ไม่ได้รวม RSU dilution** (ไม่พบตัวเลข diluted ใน search — ผลจริงอาจต่ำกว่าเล็กน้อย)
- **Net cash: $336.3M** = เงินสด $354.2M - finance lease $17.9M (ไม่มี bank debt) [8-K]; ไม่หัก noncontrolling interest เพราะใช้ share count แบบ fully-exchanged แล้ว; ไม่ได้ปรับ TRA liability (ไม่พบตัวเลข — ข้อจำกัด)

## DCF Calculation (หน่วย $M; ส่วนลดปลายปี)
| ปี | Growth | FCF | DF (11.43%) | PV |
|---|---|---|---|---|
| 1 | 5% | 325.5 | 1.1143 | 292.1 |
| 2 | 6% | 345.0 | 1.2417 | 277.8 |
| 3 | 5% | 362.2 | 1.3836 | 261.8 |
| 4 | 4% | 376.7 | 1.5418 | 244.3 |
| 5 | 3% | 388.0 | 1.7180 | 225.8 |

- PV Stage 1 = $1,301.8M
- Terminal value = 388.0 x 1.025 / (0.1143 - 0.025) = $4,453.6M → PV = $2,592.2M (**TV ~67% ของ EV** — อ่อนไหวต่อ assumption มาก)
- EV = $3,894.0M; + net cash $336.3M = Equity $4,230.3M; / 80.2M = **$52.75/หุ้น**

## Fair Value
| Case | WACC | Terminal g | FV/หุ้น |
|---|---|---|---|
| Bear | 12.43% | 2.0% | $46.36 |
| **Base** | 11.43% | 2.5% | **$52.75** |
| Bull | 10.43% | 3.0% | $61.69 |

## เทียบราคาปัจจุบัน $65.70 (Yahoo ปิด Oct 30 ผ่าน price_check.py ใน brief)
🔴 **Expensive** — ราคาสูงกว่า Base FV +24.5% (FV ต่ำกว่าราคา -19.7%); ราคาสูงกว่า Bull case ($61.69) อีก ~6.5% ด้วย

*หมายเหตุความอ่อนไหว:* ถ้า FCF margin ยืนที่ 21.7% (ไม่ haircut) Base FV ≈ $63.6 (สเกลตรงตัว 21.7/18) — ใกล้ราคา → ผลสรุปขึ้นกับว่า FCF margin 21.7% ยั่งยืนหรือไม่ ซึ่งยังไม่ยืนยัน (มีแค่ไตรมาสเดียว)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบ | GF Value: ไม่พบ → เปรียบเทียบไม่ได้ ตัวเลขนี้เป็น single-source
- อ้างอิงเสริม (ไม่ใช่ FV): Investing.com avg analyst PT ~$70.22, Benzinga avg $61 [brief, รอง] — Base FV ต่ำกว่าทั้งสองค่า
- **สรุป:** ภายใต้สมมติฐานอนุรักษ์ (growth ต่ำ, WACC 11.4% จาก beta ~1.3) ราคา $65.70 มีความคาดหวังเกินกว่า DCF ที่รองรับ; ความมั่นใจปานกลาง-ต่ำ เพราะ FCF base มาจากไตรมาสเดียว, ไม่แยก organic, TV ~67% ของ EV
