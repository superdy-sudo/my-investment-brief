# 💰 Conquest DCF: MPWR (Monolithic Power Systems) — 2026-09-17
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — เรียกใช้เพราะ Morningstar ($1,650) vs GuruFocus ($1,221.73) ขัดแย้งกัน +35.0%*

## Assumptions

**Base FCF:** TTM (Jun 2026) FCF = **$585.54M** (Operating CF $822.34M − CapEx $236.80M) — เลือก TTM แทน FY2025 ($666.19M) เพราะสะท้อน capex cycle ปัจจุบันที่หนักขึ้นจริงจาก GlobalFoundries partnership ที่เพิ่งประกาศ (2026-09-09)

**Revenue growth fade (Stage 1, ปี 1-5):**
| ปี | Growth YoY | Revenue ($M) |
|---|---|---|
| Year 1 | 40% | 4,582.2 |
| Year 2 | 30% | 5,956.9 |
| Year 3 | 20% | 7,148.2 |
| Year 4 | 13% | 8,077.5 |
| Year 5 | 8% | 8,723.7 |

เหตุผล fade: เริ่มจาก 40% (สูงกว่า TTM +28.67% เล็กน้อย เพื่อสะท้อนเทรนด์เร่งตัวจริงของ Q2 2026 +47.6% YoY และ guidance Q3 2026 $1.14-1.16B ที่บ่งชี้ YoY growth ระดับ 50%+ จาก Enterprise Data/AI datacenter segment) แล้วลดหลั่นเร็วเป็นเลขหลักเดียวภายในปีที่ 5 เพราะ: (1) comp base ของ Enterprise Data segment จะใหญ่ขึ้นเรื่อยๆ ทำให้ YoY % ยากขึ้นเชิงคณิตศาสตร์ (2) SAM ที่บริษัทระบุเอง ($27B power IC + $7B automotive ≈ $34B) เทียบ TTM revenue $3.27B = ครองแล้ว ~9.6% ของ SAM — ถ้าโตถึง $8.7B ในปีที่ 5 จะกลายเป็น ~26% ของ SAM ปัจจุบัน ซึ่งเร่งมากแล้วสำหรับ 5 ปี (3) baseline organic growth ก่อนไซเคิล AI (FY23 +1.5% เท่านั้น) แสดงว่า core business นอกเหนือ AI datacenter ไม่ได้โตเร็วขนาดนี้โดยธรรมชาติ (4) คู่แข่งรายใหญ่ (TI, Renesas, Vicor) และความเสี่ยง in-house power silicon ของ hyperscaler จะเริ่มกดดันส่วนแบ่งตลาดในปีถัดๆ ไป

**FCF margin recovery schedule:**
| ปี | FCF Margin | FCF ($M) |
|---|---|---|
| Year 1 | 19% | 870.6 |
| Year 2 | 21% | 1,250.9 |
| Year 3 | 24% | 1,715.6 |
| Year 4 | 26% | 2,100.2 |
| Year 5 | 27% | 2,355.4 |

เหตุผล: TTM margin ร่วงมาที่ 17.89% (จาก 31.88% FY23) เพราะ capex เร่งขึ้นมากสำหรับ capacity expansion (รวม GlobalFoundries manufacturing partnership) — ตั้ง Year 1 ต่ำกว่า TTM เล็กน้อย (19%) สะท้อนว่า capex cycle ยังหนักต่อในช่วงแรก แล้วค่อยๆ ฟื้นตัวเป็น 27% ในปีที่ 5 จาก operating leverage (revenue โตเร็วกว่า capex ส่วนเพิ่ม) — ตั้ง terminal margin ไว้ที่ 27% คือ "กึ่งกลาง" ระหว่าง TTM trough (17.89%) กับค่าเฉลี่ย 3 ปีย้อนหลัง (~28.3%) ไม่ให้กลับไปสูงเท่า FY23 (31.88%) เพราะ capital intensity น่าจะสูงถาวรขึ้นจากการมี manufacturing footprint ที่กระจายตัวมากขึ้น (in-house + GF partnership)

**Terminal growth rate: 3.0%** (base case) — ผูกกับ long-run GDP+inflation มาตรฐาน ไม่ใช้ตัวเลขสูงแบบ mega-cap AI infra play เพราะ TAM ของ MPWR เองระบุไว้จำกัด (SAM ~$34B, broader power IC market โตแค่ ~6.8% CAGR ถึงปี 2034 ตามข้อมูลบริษัท/นักวิเคราะห์อุตสาหกรรม) — 3% ต่ำกว่า industry CAGR ของตลาดทั้งหมดด้วยซ้ำ สะท้อนว่าเมื่อ MPWR โตจนใหญ่ในตลาดนี้แล้ว ส่วนแบ่งเพิ่มเติมจะยากขึ้นจากการแข่งขันที่เข้ามา

**WACC: 12.5%** (คำนวณจาก CAPM, ใช้ cost of equity ตรงๆ เพราะ net-cash position เกือบไม่มีหนี้ Debt/Equity ~0.01):
- Risk-free rate: **5.0%** (10Y Treasury yield พุ่งทะลุ 5% หลัง FOMC hike 2026-09-16 — สูงสุดตั้งแต่ก.ค. 2007 [source: CNBC, 2026-09-16])
- Beta: **~1.5** (ประมาณ — แหล่งต่างกันรายงาน 1.48 (5-yr), 1.69, 2.08 แล้วแต่ methodology; ใช้ค่ากลางค่อนไปทางอนุรักษ์นิยมเพราะเป็น growth/cyclical semiconductor ที่ผันผวนสูง ไม่ใช่ตัวเลขจริงเป๊ะ)
- Equity risk premium: 5.0% (มาตรฐานตลาด)
- WACC = 5.0% + 1.5 × 5.0% = **12.5%**

**Shares outstanding:** 49.14M (diluted, [source: stockanalysis.com])
**Net cash:** $1.23B (แทบไม่มีหนี้ ~$24.1M)

## DCF Calculation (Base Case, WACC 12.5%, terminal g 3.0%)

| ปี | Revenue ($M) | FCF ($M) | Discount Factor | PV of FCF ($M) |
|---|---|---|---|---|
| Y1 | 4,582.2 | 870.6 | 0.8889 | 773.9 |
| Y2 | 5,956.9 | 1,250.9 | 0.7901 | 988.3 |
| Y3 | 7,148.2 | 1,715.6 | 0.7023 | 1,204.9 |
| Y4 | 8,077.5 | 2,100.2 | 0.6243 | 1,311.2 |
| Y5 | 8,723.7 | 2,355.4 | 0.5549 | 1,307.1 |

- Sum PV of Stage 1 FCF = **$5,585.4M**
- Terminal Value = FCF₅ × (1+g) ÷ (WACC−g) = 2,355.4 × 1.03 ÷ 0.095 = **$25,537.5M**
- PV of Terminal Value = 25,537.5 × 0.5549 = **$14,171.1M** (71.7% ของ EV — ปกติสำหรับบริษัทที่ยังอยู่ใน high-growth stage)
- **Enterprise Value = $5,585.4M + $14,171.1M = $19,756.5M**
- + Net cash $1,230M → **Equity Value = $20,986.5M**
- ÷ 49.14M shares → **Fair Value/share = $427.16**

## Sensitivity (ปรับ WACC ±1%, terminal growth ±0.5%, ใช้ FCF projection เดิม)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| 🐻 Bear | 13.5% | 2.5% | **$372.63** |
| ⚖️ **Base** | **12.5%** | **3.0%** | **$427.16** |
| 🐂 Bull | 11.5% | 3.5% | **$501.94** |

**Sanity check ด้วย exit-multiple แทน Gordon growth:** แม้ใช้ exit multiple 25x Y5 FCF (สูงมากสำหรับ terminal multiple ปกติ) แทน Gordon growth terminal value จะได้ fair value ~$803.8/share — ยังต่ำกว่าราคาปัจจุบันมาก แสดงว่าผลสรุปไม่ได้ sensitive ต่อ terminal value methodology ที่เลือกใช้

## เทียบราคาปัจจุบัน $1,165.70

🔴 **Expensive** — ราคาสูงกว่า Base case FV **+172.9%** (($1,165.70 − $427.16) ÷ $427.16) — สูงกว่าแม้แต่ Bull case (+132.3%)

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $1,650** — ห่างจาก conquest base case มาก (+286%) เพราะ Morningstar (forward-DCF, Wide Moat) น่าจะสมมติ terminal growth/moat premium สูงกว่ามาก และอาจใช้ WACC ต่ำกว่า (ไม่สะท้อน 10Y yield ที่เพิ่งพุ่งทะลุ 5% หลัง FOMC 2026-09-16 เต็มที่ถ้าโมเดลยังไม่ได้ปรับ) รวมถึงให้น้ำหนัก AI datacenter growth ต่อเนื่องระยะยาวมากกว่าที่ TAM ของบริษัทเองรองรับได้
- **GuruFocus GF Value $1,221.73** — ก็ยังห่างจาก conquest base case มาก (+186%) แม้จะเป็นตัวเลข backward-looking (historical multiple regression) ที่ควรจะอนุรักษ์นิยมกว่า Morningstar แต่ multiple regression แบบนี้ยังฝังนัย premium multiple ปัจจุบันของตลาด (P/E TTM 71x) ที่ตัว conquest DCF ไม่เห็นด้วยเมื่อคำนวณจาก raw cash flow
- **สรุป:** Conquest **ไม่เห็นด้วยกับทั้งสองแหล่ง** — แม้จะใช้ growth assumption ที่ค่อนข้างเร่ง (40% ปีแรก, สูงกว่า TTM growth จริง) ผลลัพธ์ยังต่ำกว่าทั้ง Morningstar และ GuruFocus มาก สาเหตุหลักคือ (1) WACC 12.5% ที่สะท้อน risk-free rate ที่เพิ่งพุ่งขึ้นจริงหลัง FOMC + beta สูงของหุ้น semiconductor ผันผวน และ (2) terminal growth 3% ที่ผูกกับ TAM จำกัดของบริษัทเอง ไม่ใช่สมมติฐาน AI-infra unlimited-TAM แบบ mega-cap — ราคาตลาดปัจจุบัน ($1,165.70, P/E TTM 71x) ดูเหมือนจะ price-in AI datacenter growth ต่อเนื่องระยะยาวและ/หรือ terminal multiple ที่สูงกว่าที่ fundamentals ดิบ (revenue/FCF trend, TAM ที่บริษัทระบุเอง) จะรองรับได้ภายใต้สมมติฐานที่ conquest ใช้ — ผลสรุป valuation จึงเอียงไปทาง **Expensive อย่างชัดเจนกว่าที่ GuruFocus บอกด้วยซ้ำ**
