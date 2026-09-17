# 💰 Conquest DCF: SNPS — 2026-09-17
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (FY2026E): $2,600M**
  - ที่มา: 9-month FY2026 actual FCF (SEC 10-Q, ended 2026-07-31) = Operating CF $2,298.6M − Capex $156.1M = **$2,142.5M**
  - ปัญหา: annualized run-rate จาก 9mo (÷9×12) = **$2,857M** แต่ company FY26 full-year guidance = **$1,900M** (ต่ำกว่า 9-month actual ที่เกิดขึ้นแล้ว — เลขขัดแย้งกันเอง ตามที่ระบุใน brief)
  - เลือกใช้ **$2,600M** เป็นจุดกึ่งกลางระหว่างสอง extreme นี้ โดยให้น้ำหนักไปทาง actual run-rate มากกว่า guidance (เพราะ guidance ดูเหมือนเก่ากว่าตัวเลขจริงที่ทยอยออกมา) แต่หัก haircut ไว้สำหรับ Q4 seasonal cash outflow (bonus/tax payment) ที่ Synopsys มักมีตามฤดูกาล — **นี่คือค่าประมาณ ไม่ใช่ตัวเลขที่ประกาศตรงๆ**
  - Sensitivity ต่อ base FCF (นอกเหนือจาก bear/bull ด้านล่าง): ถ้าใช้ guidance ต่ำสุด $1.9B → FV base-case ≈ $166/share; ถ้าใช้ annualized run-rate $2.857B → FV base-case ≈ $250/share — ช่วงนี้ยังต่ำกว่าราคาปัจจุบันมากทุกกรณี

- **Growth fade (Stage 1, ปี 1-5):** 15% → 12% → 10% → 8% → 6% → terminal 3%
  - เหตุผล: FY26 guided growth +37.6% YoY (จาก $7.05B → ~$9.7B) เป็น growth ที่พองจาก Ansys consolidation (ปีก่อนมี Ansys แค่ ~3.5 เดือน ปีนี้เต็มปี) ไม่ใช่ organic — ตัวเลขนี้ **ไม่ยั่งยืน** ใช้เป็น starting growth ไม่ได้
  - Organic growth ก่อน Ansys deal (FY23→FY24 +15%, FY24→FY25 +15.12%) อยู่ที่ **~15%** ต่อเนื่อง — ใช้เป็นจุดเริ่ม Stage 1 ปีที่ 1 (ปีแรกที่ comp กับฐาน Ansys เต็มปีแล้ว)
  - Fade ลงเหลือ terminal 3% ภายใน 5 ปี เพราะ: (1) TAM ที่บริษัทระบุเองหลังดีล = **$31B** ขณะที่ market cap ปัจจุบันอยู่ที่ **$72.75B** (TAM/MktCap ≈ 0.43x — ต่ำกว่าเกณฑ์ 5x มาก ตามที่เจอใน Layer 2 checklist) แปลว่าไม่มี TAM เหลือมากพอจะ sustain double-digit growth ยาวๆ โดยไม่ต้อง expand TAM เพิ่มเอง; (2) EDA เป็น duopoly ที่โตช้ากว่า software ทั่วไป (Cadence คู่แข่งหลักก็โตใกล้เคียงกัน ไม่มีใครแย่ง market share ได้เร็ว); (3) mean-reversion ทั่วไปของธุรกิจ high-growth enterprise software เมื่อ integration synergies หมดไปหลัง 2-3 ปี
  - สมมติฐานย่อย: FCF margin คงที่ตลอด 5 ปี (ไม่ได้ผูก FCF growth แยกจาก revenue growth) — เป็นการลดความซับซ้อน ถ้า synergies จริงทำให้ margin ขยายเร็วกว่านี้ (บริษัท guide non-GAAP op margin ระยะยาวที่ mid-40s%) FV จะสูงกว่านี้ได้บ้าง — ไม่ได้รวม upside นี้ไว้ใน base case

- **Terminal growth rate: 3.0%**
  - สูงกว่า GDP nominal เล็กน้อย (ปกติ 2-2.5%) เพราะ Wide Moat จาก switching cost สูงมาก (customer retention ~near-100%) น่าจะรักษา pricing power ได้ต่อเนื่องแม้ industry จะ mature — แต่ไม่ใช้สูงกว่านี้เพราะ TAM constraint ที่เจอใน Layer 2 (TAM $31B เทียบ market cap ที่สูงกว่ามากแล้ว)

- **WACC: 10.3%**
  - Risk-free rate: 4.99% (10Y Treasury, 2026-09-17 หลัง FOMC hike) [source: CNBC US10Y]
  - Beta: 1.22 (5Y monthly, Yahoo Finance) [source: finance.yahoo.com/quote/SNPS]
  - Equity risk premium: 5.0% (มาตรฐานตลาด, จุดกึ่งกลางของช่วง 4-6%)
  - Cost of equity = 4.99% + 1.22 × 5.0% = **11.1%**
  - บริษัทมี debt มาก ($10.04B) จากดีล Ansys จึงไม่ใช้ cost of equity ตรงๆ — weighted WACC:
    - Equity weight = market cap $72.75B / (market cap + total debt $82.79B) = **87.9%**
    - Debt weight = $10.04B / $82.79B = **12.1%**
    - Cost of debt (pretax) = interest expense annualized ($429.3M×12/9 ≈ $572M) / total debt $10.04B ≈ 5.7%; after-tax (tax rate 21%) ≈ **4.5%**
    - WACC = 0.879 × 11.1% + 0.121 × 4.5% ≈ **10.3%**

- **Shares outstanding:** 191M [source: brief, stockanalysis.com/SEC 10-Q]
- **Net debt:** $6,431.1M (total debt $10,037.4M − cash $3,606.3M) [source: SEC 10-Q ended 2026-07-31]

## DCF Calculation (Base case: WACC 10.3%, terminal g 3.0%)

| ปี | Growth | FCF ($M) | PV @10.3% ($M) |
|---|---|---|---|
| Base (FY26E) | — | 2,600 | — |
| Year 1 | 15% | 2,990 | 2,711 |
| Year 2 | 12% | 3,349 | 2,753 |
| Year 3 | 10% | 3,684 | 2,745 |
| Year 4 | 8% | 3,978 | 2,688 |
| Year 5 | 6% | 4,217 | 2,583 |

- Sum PV of Stage-1 FCF (ปี1-5) = **$13,480M**
- Terminal Value (ปลายปี 5) = $4,217M × 1.03 / (0.103 − 0.03) = **$59,501M**
- PV of Terminal Value = **$36,446M**
- Enterprise Value = $13,480M + $36,446M = **$49,925M**
- (−) Net debt $6,431M → Equity Value = **$43,494M**
- (÷) 191M shares → **Fair Value = $227.72/share**

## Fair Value

- Bear case (WACC 11.3%, terminal g 2.5%): **$185.61**
- **Base case (WACC 10.3%, terminal g 3.0%): $227.72**
- Bull case (WACC 9.3%, terminal g 3.5%): **$291.42**

## เทียบราคาปัจจุบัน $379.68

🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV ถึง **+66.7%** ($379.68 vs $227.72)

แม้ใช้ Bull case (WACC ต่ำสุด 9.3% + terminal growth สูงสุด 3.5%) ราคาก็ยังสูงกว่า FV ที่ได้ ($291.42) อยู่ **+30.3%** — สรุปคือทุก scenario (bear/base/bull) ชี้ไปทาง Expensive ทั้งหมด ไม่มี scenario ไหนที่ราคาปัจจุบันดูสมเหตุสมผล

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $480** — ห่างจาก Conquest base case ($227.72) ประมาณ **−52.6%** (Morningstar สูงกว่ามาก)
  - สาเหตุที่ต่างกันมาก: Morningstar เป็น forward-analyst DCF ที่ผูกกับ Wide Moat rating โดยตรง มักสมมติ (1) growth fade ที่ช้ากว่านี้มาก / คงอัตราสูงไว้นานกว่า 5 ปี และ (2) discount rate ต่ำกว่า (Wide Moat มักได้ discount rate premium ต่ำ ~7-8% แทนที่จะเป็น 10.3% ที่คำนวณจาก beta 1.22 จริง) — Conquest ใช้ TAM constraint ($31B) เป็นเพดาน fade ที่ Morningstar น่าจะไม่ได้ผูกไว้แน่นเท่า
- **GuruFocus GF Value ~$667** — ห่างจาก Conquest base case มากกว่าอีก ประมาณ **−65.9%**
  - GuruFocus ใช้ historical-multiple regression (backward-looking) ซึ่งจะ extrapolate จาก multiple ที่ตลาดเคยให้ SNPS ในอดีต (ช่วงที่ยังไม่มีหนี้ $10B จากดีล Ansys และยังไม่มี GAAP margin ที่ถูกกดจาก amortization) — ไม่ได้ re-base สำหรับความเสี่ยงจาก leverage ใหม่หรือ TAM ceiling ที่ Conquest ให้น้ำหนักตรงๆ ตัว GuruFocus เองก็แปะป้าย "Possible Value Trap" (7 warning signs) ซึ่งสอดคล้องกับสิ่งที่ Conquest เจอ
- **สรุป:** Conquest **ไม่เห็นด้วยกับทั้งสองแหล่ง** — ทั้ง Morningstar และ GuruFocus ชี้ทาง Cheap แต่ Conquest ซึ่งคำนวณจาก raw fundamentals ตรงๆ (ไม่พึ่ง moat-premium assumption แบบ Morningstar และไม่พึ่ง historical-multiple แบบ GuruFocus) เห็นว่า Expensive ชัดเจนในทุก sensitivity scenario ประเด็นสำคัญที่สุดที่ผลักให้ FV ต่ำคือ **TAM/Market Cap ratio ที่ต่ำกว่าเกณฑ์มาก** (TAM $31B ที่บริษัทระบุเองเทียบ market cap $72.75B ≈ 0.43x) — ตลาดกำลัง price-in growth/TAM expansion ที่ไกลเกินกว่าตัวเลขที่บริษัทเปิดเผยไว้ตอนนี้มาก ทำให้ทั้ง Morningstar และ GuruFocus (ซึ่งทั้งคู่ให้ Cheap) น่าจะประเมิน optimistic เกินไปเมื่อเทียบกับ fundamentals ดิบที่มีอยู่จริง
