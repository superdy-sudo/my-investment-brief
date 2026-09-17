# 💰 Conquest DCF: PWR (Quanta Services) — 2026-09-17
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (TTM, Jun'26):** $2,288M (margin 6.95% ของ revenue TTM $32,905M) — ใช้ actual ล่าสุดแทน FY26 guidance midpoint เพื่อความอนุรักษ์นิยม (guidance $2-2.5B ใกล้เคียงกันอยู่แล้ว)
- **Growth fade (FCF growth, ปี 1-5):** 32% → 25% → 18% → 12% → 8%
  - เหตุผล: FY26 guidance revenue growth ~38.7% YoY (midpoint $39.5B จาก FY25 $28.48B) เป็นจุดเริ่มที่สูงกว่านี้ แต่ใช้ FCF growth (ไม่ใช่ revenue growth ตรงๆ) ปีแรกที่ 32% เพราะธุรกิจ E&C ระดับนี้มักกิน working capital หนักตอนขยายเร็ว (megaproject mobilization, equipment/labor ramp-up) ทำให้ FCF growth มักช้ากว่า revenue growth เล็กน้อยในช่วงเร่งตัว
  - Backlog $53.4B ≈ 1.35x TTM revenue ให้ visibility ที่มั่นคงแค่ ~1.3-1.5 ปีข้างหน้า (ปี 1-2 ของ DCF พึ่ง backlog ที่เซ็นแล้วได้มาก) — ปี 3-5 ต้องพึ่ง backlog ใหม่ที่ยังไม่เซ็น (เช่น NiSource program) ซึ่งไม่แน่นอนกว่า จึงให้ fade ลงเร็ว
  - คู่แข่งตลาดเดียวกัน (MasTec, STRL, EMCOR) กำลังแย่งแรงงานทักษะสูงและโครงการเดียวกัน — mean reversion ปกติของธุรกิจ E&C ที่โตเร็วในช่วง supercycle มักชะลอกลับเข้าสู่ high-single-digit ถึง teens ภายใน 4-5 ปี
- **Terminal growth: 2.5%** (กลางช่วง 2-3%) — ไม่ใช้ปลายสูงเพราะ Layer 1 ยังมี **⚠️ Data Conflict บน moat status** (Morningstar official 2026 rating ยืนยันไม่ได้ ล่าสุดที่ confirmed คือ "No Moat" ปี 2023) จนกว่าจะยืนยัน durable pricing power ได้ชัดเจนกว่านี้ ไม่ควรให้ terminal growth สูงกว่าระดับ GDP-linked ปกติ
- **WACC: 10.0%**
  - Risk-free rate: 4.99% ≈ 5.0% (10Y Treasury, 17 ก.ย. 2026, หลัง FOMC hike)
  - Equity Risk Premium: 5.0% (มาตรฐานตลาด)
  - Beta: **ประมาณ 1.0** — source ขัดแย้งกันชัดเจน (CNBC รายงาน 1.27, TradingView รายงาน 0.71) ใช้ค่ากลางปัดเป็น 1.0 แทน ไม่ใช่ตัวเลขจริงที่ยืนยันได้แหล่งเดียว
  - ใช้ cost of equity ตรงๆ (ไม่ weighted กับ cost of debt) เพราะ net debt เทียบ market cap เล็กมาก (~5.9% ของ market cap) ผลต่อ WACC จาก debt weighting ต่ำมากจนไม่คุ้มความซับซ้อนเพิ่ม
  - WACC = 5.0% + 1.0 × 5.0% = **10.0%**
- **Shares outstanding:** 150.34M
- **Net debt:** $5,589.8M (Total debt $6,096.2M รวม current maturities − Cash $506.4M, ข้อมูล 10-Q Q2 2026 ณ 30 มิ.ย. 2026)

## DCF Calculation (Base Case, WACC 10.0%, terminal g 2.5%)

| Year | Growth | FCF ($M) | Discount Factor | PV ($M) |
|---|---|---|---|---|
| 1 | 32% | 3,020.2 | 0.9091 | 2,745.6 |
| 2 | 25% | 3,775.2 | 0.8264 | 3,119.2 |
| 3 | 18% | 4,454.7 | 0.7513 | 3,346.6 |
| 4 | 12% | 4,989.3 | 0.6830 | 3,407.1 |
| 5 | 8% | 5,388.5 | 0.6209 | 3,345.9 |

- Sum PV of Stage-1 FCF (ปี 1-5): **$15,964.4M**
- Terminal Value (ปี 5) = $5,388.5M × 1.025 ÷ (0.10 − 0.025) = **$73,642.1M**
- PV of Terminal Value = $73,642.1M × 0.6209 = **$45,732.9M**
- **Enterprise Value = $15,964.4M + $45,732.9M = $61,697.3M**
- **Equity Value = $61,697.3M − Net Debt $5,589.8M = $56,107.5M**
- **Fair Value per share = $56,107.5M ÷ 150.34M shares = $373.14**

## Fair Value

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| Bear case | 11.0% | 2.0% | **$307.15** |
| **Base case** | **10.0%** | **2.5%** | **$373.14** |
| Bull case | 9.0% | 3.0% | **$471.98** |

## เทียบราคาปัจจุบัน $627.22

- vs Base case ($373.14): **+68.1%** 🔴 Expensive
- vs Bull case ($471.98): **+32.9%** 🔴 ยังคง Expensive แม้ใช้ assumption ที่ optimistic ที่สุด (WACC ต่ำสุด + terminal growth สูงสุดในช่วงที่กำหนด)
- vs Bear case ($307.15): **+104.2%**

**สรุป: 🔴 Expensive ในทุกสถานการณ์** — แม้ bull case (WACC 9%, terminal growth 3%) ราคายังสูงกว่า fair value เกิน 20% threshold ทำให้ conclusion นี้ค่อนข้าง robust ไม่ใช่แค่ base case เดียวที่บอก Expensive

Sanity check เพิ่มเติม: EV/TTM FCF ที่ตลาดให้ราคาอยู่ปัจจุบัน (Market cap $94.27B + net debt $5.59B = EV ~$99.86B ÷ FCF TTM $2.288B) ≈ **43.6x** ขณะที่ conquest DCF (ทุก scenario) ให้ implied EV/FCF อยู่ระหว่าง ~21x (bear) ถึง ~31x (bull) — สอดคล้องกับที่ Morningstar เคยตั้งข้อสังเกตไว้ในรายงาน Jul 2026 ว่า "the market is pricing in a prolonged supercycle" (อ้างใน brief หลัก Layer 1)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV:** หาตัวเลข official 2026 ไม่ได้ (เว็บบล็อก, ตัวเลขล่าสุดที่ยืนยันได้คือ $138-175 จากปี 2023-2024 ซึ่ง stale เกินใช้เทียบ) — ข้ามการเทียบเชิงตัวเลข ใช้ได้แค่ทิศทางเชิงคุณภาพ ("overvalued at current prices" ตามที่อ้างใน aggregator, Jul 30 2026) ซึ่ง**สอดคล้องทิศทางเดียวกับ conquest** (ทั้งคู่ชี้ Expensive)
- **GuruFocus GF Value $480.69** (Sep 7, 2026): อยู่**ใกล้กับ conquest bull case ($471.98) มาก** (ห่างกันแค่ +1.8%) แต่**สูงกว่า conquest base case ($373.14) อยู่ +28.8%** — ตีความได้ว่า GuruFocus (backward-looking historical-multiple regression) implicitly ให้น้ำหนักกับ growth/margin trajectory แบบ optimistic เทียบเท่า bull-case assumption ของ conquest (WACC ต่ำ + terminal growth สูง) ซึ่งสมเหตุสมผลเพราะ GF Value มักสะท้อน historical multiple ที่ตลาดเคยให้ในช่วงที่ momentum แรง ไม่ได้ discount downside execution risk ของ backlog ที่ยังไม่เซ็นเท่า DCF ทำ
- **สรุป:** conquest เห็นด้วยกับทิศทาง Expensive ของทั้งสองแหล่ง แต่**อนุรักษ์นิยมกว่า GuruFocus** อย่างชัดเจน — จุดต่างหลักคือ conquest ไม่ให้ terminal growth เกิน 2.5% (เพราะ moat status ยัง ⚠️ Data Conflict ที่ Layer 1 ยังคลี่ไม่จบ) ขณะที่ GF Value แบบ historical-regression มักไม่มีการ discount ความไม่แน่นอนของ moat แบบนี้โดยตรง — ราคาปัจจุบัน $627.22 อยู่สูงกว่าทั้ง 3 มุมมอง (conquest bull, GuruFocus, และ conquest base) แสดงว่าตลาดกำลัง price-in สถานการณ์ที่ optimistic กว่าทุกแหล่งประเมินอิสระที่มีอยู่ในตอนนี้
