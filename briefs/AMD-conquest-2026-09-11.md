# 💰 Conquest DCF: AMD — 2026-09-11
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (Year 0 = FY2026E):**
- Revenue FY2026E ≈ $49.3B — สร้างจาก Q1 2026 actual $10.3B + Q2 2026 actual $11.536B + Q3 2026 guide $13.0B + Q4 2026E ~$14.5B (ประมาณจาก sequential growth ที่กำลังเร่งตัว ~10-13%/ไตรมาส ไม่มีตัวเลข guide จริง — เป็นการประมาณ) → YoY growth ~44% สอดคล้องกับ trajectory ที่ประกาศ
- FCF margin FY2026E ≈ 14.0% (อิง Q2 2026 actual 13.9%, สมมติใกล้เคียงตลอดปี)
- **Base FCF ≈ $6.9B**

**Stage 1 — Revenue growth fade (ปี 1-5, FY2027-2031):**
| ปี | Growth YoY | เหตุผล |
|---|---|---|
| 1 (FY27) | +55% | CFO Jean Hu guide data center segment "โตเป็น 2 เท่าอีกครั้ง" ปี 2027 และ data center เป็น ~58% ของรายได้รวมแล้ว — แม้ gaming/embedded โตช้า/ทรงตัว blended growth ก็ยังสูงมาก |
| 2 (FY28) | +35% | ฐานใหญ่ขึ้น, AI capex cycle ยังแข็งแรงตาม TAM ที่ยกระดับเป็น $2-3T แต่ hyperscaler capex growth เริ่ม normalize |
| 3 (FY29) | +23% | Mean-reversion เริ่มเข้ามา, คู่แข่ง custom silicon (Google TPU, AWS Trainium, Broadcom ASIC) แย่งส่วนแบ่งจาก merchant silicon มากขึ้น |
| 4 (FY30) | +15% | ใกล้ normalized semiconductor cyclical growth, TAM penetration เริ่มอิ่มตัวในกลุ่มลูกค้าหลัก |
| 5 (FY31) | +8% | Converge เข้าใกล้ terminal, สะท้อนว่า AMD เป็น Narrow Moat ไม่ใช่ Wide — ไม่มี switching-cost/network-effect ระดับ Nvidia ที่จะรักษา growth premium ระยะยาวได้ |

**FCF margin expansion (operating leverage + data center mix shift, แต่ถูก cap ต่ำกว่า Nvidia เพราะ Narrow Moat = pricing power จำกัดกว่า):**
Y0 14.0% → Y1 15.5% → Y2 17.0% → Y3 18.5% → Y4 20.0% → Y5 21.0%
(เทียบ Nvidia FCF margin ~40%+ — AMD ไม่ควรไปถึงระดับนั้นเพราะไม่มี CUDA-style lock-in ที่ให้ pricing power เทียบเท่า)

**Terminal growth: 3.0%** — ผูกกับ long-run GDP/inflation มาตรฐาน ไม่ให้ premium สูงกว่านี้เพราะ Morningstar เองก็จัด AMD เป็น Narrow Moat ไม่ใช่ Wide Moat (ไม่มี durable moat พอจะสมควรได้ terminal growth เกิน GDP)

**Discount rate (WACC):**
- Risk-free rate: 4.90% (10Y Treasury, 2026-09-11 — หมายเหตุ: วันนี้ยีลด์พุ่งจาก US-Iran conflict/น้ำมัน >$100 ซึ่งอาจสูงกว่าระดับปกติชั่วคราว)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด)
- Beta: ใช้ **1.8 (moderated)** สำหรับ base case — เหตุผล: raw trailing beta จาก market data อยู่ที่ ~2.47-2.9 (สูงผิดปกติ สะท้อน momentum/speculative trading ในธีม AI มากกว่าความเสี่ยงเชิงพื้นฐานของธุรกิจ) ใช้ 1.8 เป็นค่าประมาณที่ปรับลงเพื่อสะท้อน risk เชิงโครงสร้างจริง (cyclicality + customer concentration + competitive intensity) ระบุชัดว่าเป็นการประมาณ/judgment call ไม่ใช่ตัวเลขดิบ
- **WACC = 4.90% + 1.8 × 5.0% = 13.9%** (บริษัท net-cash จึงใช้ cost of equity ตรงๆ ไม่ weighted กับ cost of debt)
- Stress test ด้วย raw beta 2.47 → WACC 17.25% → ให้ผลลัพธ์ต่ำกว่า base case มาก (ดูหมายเหตุท้ายตาราง)

**Shares outstanding:** ~1.631B
**Net cash:** $9.9B (cash + ST investments $13.111B − total debt $3.226B, ณ Q2 2026 10-Q)

## DCF Calculation (Base case: WACC 13.9%, terminal g 3.0%)

| ปี | Revenue ($B) | FCF margin | FCF ($B) | Discount factor | PV FCF ($B) |
|---|---|---|---|---|---|
| 1 | 76.4 | 15.5% | 11.85 | 0.878 | 10.40 |
| 2 | 103.2 | 17.0% | 17.54 | 0.771 | 13.52 |
| 3 | 126.9 | 18.5% | 23.48 | 0.677 | 15.89 |
| 4 | 145.9 | 20.0% | 29.19 | 0.594 | 17.35 |
| 5 | 157.6 | 21.0% | 33.10 | 0.522 | 17.27 |

- Sum PV of explicit FCF (ปี 1-5) ≈ **$74.4B**
- Terminal Value = $33.10B × 1.03 ÷ (13.9% − 3.0%) ≈ **$312.8B**
- PV of Terminal Value ≈ **$163.2B**
- Enterprise Value ≈ $74.4B + $163.2B ≈ **$237.6B**
- + Net cash $9.9B → Equity Value ≈ **$247.5B**
- ÷ 1.631B shares → **Fair Value ≈ $152/share**

## Fair Value

- Bear case (WACC 14.9%, g 2.5%): **$134**
- **Base case (WACC 13.9%, g 3.0%): $152**
- Bull case (WACC 12.9%, g 3.5%): **$175**
- *(Stress test เพิ่มเติม ใช้ raw market beta 2.47 → WACC 17.25%, g 3.0% → ~$113 — ยิ่งต่ำกว่า base case)*

## เทียบราคาปัจจุบัน $517.41

🔴 **Expensive** — สูงกว่า Base case FV ($152) ประมาณ **+240%** (สูงกว่าแม้แต่ Bull case ($175) ถึง +196%) — เกินเกณฑ์ >20% หลายเท่าตัว ไม่ว่าจะใช้ scenario ไหนในสามสถานการณ์

เพื่อให้เห็นภาพว่าต้องใช้สมมติฐานสุดโต่งแค่ไหนถึงจะ justify ราคาปัจจุบัน — ลองปรับเป็น "aggressive bull" (WACC 10%, terminal g 3.5%, FCF margin ไต่ถึง 30% ในปีที่ 5 ใกล้เคียง Nvidia, growth ปีแรก +60%) ยังได้ fair value เพียง **~$365** คือยังต่ำกว่าราคาปัจจุบันและต่ำกว่า Morningstar FV — สะท้อนว่าตลาดกำลัง price-in สมมติฐานที่เกินกว่ากรอบ 5-ปี + terminal-GDP-growth แบบมาตรฐานไปมาก

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $450** — ไกลจาก conquest base case ($152) มาก สาเหตุที่เป็นไปได้: (1) Morningstar น่าจะใช้ explicit forecast period ยาวกว่า 5 ปี (มักเป็น 10 ปีสำหรับ moat-based DCF) ทำให้ high-growth period ยาวนานกว่าที่ conquest ประเมินไว้ (fade เร็วกว่าเพราะมองว่า Narrow Moat ไม่ยั่งยืนพอ) (2) Morningstar อาจสมมติ terminal/steady-state FCF margin สูงกว่า 21% ที่ conquest ใช้ ใกล้เคียง moat-premium ของบริษัทที่มี pricing power สูงกว่า (3) อาจใช้ WACC ต่ำกว่าเพราะไม่ได้ปรับ beta ขึ้นตาม volatility ปัจจุบันที่สูงผิดปกติ
- **GuruFocus GF Value $272.45** — ใกล้กับทิศทาง (Expensive) ของ conquest มากกว่า Morningstar แม้ตัวเลขจริงจะสูงกว่า conquest base case ($152) พอสมควร — GuruFocus ใช้ historical-multiple regression (mean-revert กลับไปยัง P/E, P/S, P/FCF เฉลี่ยในอดีตของ AMD เอง) ซึ่งเป็นค่าเฉลี่ยจากยุคก่อน AI-boom ไม่ได้ model cash flow แบบ forward-looking เลย ต่างวิธีคิดกับ conquest DCF อย่างสิ้นเชิง แต่บังเอิญตกในทิศทางเดียวกัน (Expensive)
- **สรุป:** Conquest เห็นด้วยกับทิศทางของ GuruFocus (Expensive) มากกว่า Morningstar (Fair) อย่างชัดเจน — และจริงๆ แล้ว conquest ให้ fair value ต่ำกว่า GuruFocus เสียอีก ($152 vs $272) ทำให้ตอนนี้มี **2 ใน 3 วิธีที่เป็นอิสระต่อกันจริง** (bottom-up DCF ของ conquest + backward-looking multiple regression ของ GuruFocus) เห็นตรงกันว่าราคา $517.41 แพงเกินพื้นฐานอย่างมีนัยสำคัญ เทียบกับ Morningstar เพียงแหล่งเดียวที่มองว่า Fair — ข้อขัดแย้งเดิม (~65% ระหว่าง Morningstar-GuruFocus) จึงคลี่คลายไปทาง **🔴 Expensive** เป็นข้อสรุป 2-ใน-3
