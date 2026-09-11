# 💰 Conquest DCF: DELL — 2026-09-11
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (Year 0, FY27 current-year run-rate):** ≈ $20.4B
- H1 FY27 actual adjusted FCF = $3.17B (Q1) + $8.1B (Q2) = $11.27B บน revenue $90.8B
- H2 FY27 guided revenue ≈ $101.2B (จาก full-year guidance $192B ลบ H1 actual) — สมมติ FCF margin ปรับลงมาที่ 9% (ลด lumpy prepayment tailwind ของ Q2 ที่ margin พุ่งถึง 17.2%) → H2 FCF ≈ $9.1B
- รวม FY27 FCF ≈ $20.4B บน revenue $192B → margin ~10.6%
- **หมายเหตุ:** เลือกใช้ FY27 guided full-year (ไม่ใช่ TTM ธรรมดา) เป็นฐาน เพราะ TTM ที่ปนไตรมาสเก่า (Q3/Q4 FY26 ก่อน AI supercycle เร่งตัว) จะทำให้ base ต่ำเกินจริงเทียบกับ run-rate ปัจจุบันที่บริษัท guide เอง

**Revenue growth fade (Year 1-5, เหตุผล):**
| ปี | Growth |
|---|---|
| Y1 (FY28) | 35% |
| Y2 (FY29) | 22% |
| Y3 (FY30) | 15% |
| Y4 (FY31) | 10% |
| Y5 (FY32) | 7% |

เหตุผล: ปัจจุบันโต ~70% YoY (FY27 guidance) ขับเคลื่อนจาก AI server backlog $95B ที่ให้ visibility ล่วงหน้า 1-2 ปี แต่เป็นการเร่งตัวจาก supercycle เฉพาะช่วง ไม่ใช่ growth เชิงโครงสร้างถาวร — ธุรกิจ ISG/AI server เป็น commodity hardware (แข่งกับ Supermicro/HPE/Lenovo/ODM โดยตรง ตามที่ Layer 1 สรุปว่า No Moat) จึงต้อง fade ลงเร็วกว่าธุรกิจที่มี moat ปกติ บวกกับความเสี่ยงระยะยาวจาก hyperscaler ทำ custom silicon เอง (Google TPU, AWS Trainium, Meta MTIA) ที่จะกัดกร่อน TAM ของ Dell ในปีที่ 4-5 เป็นต้นไป

**FCF margin fade (Year 1-5):**
| ปี | FCF margin |
|---|---|
| Y1 | 10.5% |
| Y2 | 9.0% |
| Y3 | 8.0% |
| Y4 | 7.5% |
| Y5 | 7.0% |

เหตุผล: margin ปัจจุบัน (Q2 FY27 17.2%) ถูกยกด้วย working-capital tailwind จาก AI order prepayment/deposit ที่ไม่ยั่งยืนเมื่อ growth ของ order ชะลอตัว — operating margin โดยรวมยังอยู่แค่ ~7-8% (ตัวเลขจริงจาก brief) สะท้อนธุรกิจ hardware assembly margin ต่ำเชิงโครงสร้าง จึง fade FCF margin ลงมาบรรจบกับระดับ ~7% ซึ่งใกล้เคียง operating margin ปัจจุบัน มากกว่าจะคง margin สูงแบบไตรมาสพีค

**Terminal growth: 2.5%** — ใช้ค่าอยู่กลาง-ล่างของช่วงปกติ 2-3% (ไม่ให้ premium) เพราะ Layer 1 สรุปชัดว่า Dell **No Moat** (ไม่มี pricing power/switching cost/cornered resource ที่ยั่งยืน) จึงไม่มีเหตุผลให้ terminal growth สูงกว่า GDP/inflation ทั่วไป

**WACC: 10.8%**
- Risk-free rate: 4.95% (10Y Treasury, 11 ก.ย. 2026 — bond selloff ดัน yield ใกล้ 5%)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด)
- Beta: 1.3 (ประมาณ — แหล่งข้อมูลขัดแย้งกันมาก: Yahoo 1.41, Zacks/Macroaxis ~1.08-1.93 ขึ้นกับช่วงเวลา/วิธีคำนวณ จึงใช้ค่ากลางที่สมเหตุสมผล ระบุชัดว่าเป็นการประมาณ)
- Cost of equity = 4.95% + 1.3 × 5.0% = 11.45%
- Cost of debt (pre-tax) ≈ interest expense annualized $1.576B ÷ debt $34.47B ≈ 4.57%; after-tax (~21%) ≈ 3.6%
- Weights: E = market cap $364B, D = $34.47B, V = $398.47B → E/V = 91.4%, D/V = 8.6%
- WACC = 0.914×11.45% + 0.086×3.6% ≈ **10.8%**

**Shares outstanding:** 646.14M
**Net debt:** $22.9B (debt $34.47B − cash $11.57B)

## DCF Calculation (Base Case: WACC 10.8%, terminal g 2.5%)

| ปี | Revenue ($B) | FCF margin | FCF ($B) | PV @ 10.8% ($B) |
|---|---|---|---|---|
| Y0 (FY27) | 192.0 | 10.6% | 20.4 (ฐาน) | — |
| Y1 (FY28) | 259.2 | 10.5% | 27.22 | 24.57 |
| Y2 (FY29) | 316.2 | 9.0% | 28.46 | 23.18 |
| Y3 (FY30) | 363.7 | 8.0% | 29.09 | 21.38 |
| Y4 (FY31) | 400.1 | 7.5% | 30.01 | 19.91 |
| Y5 (FY32) | 428.1 | 7.0% | 29.97 | 17.94 |

- Sum PV of Stage 1 FCF ≈ **$107.0B**
- Terminal Value (end Y5) = 29.97 × 1.025 / (0.108 − 0.025) ≈ **$370.1B**
- PV of Terminal Value ≈ 370.1 / 1.6701 ≈ **$221.6B**
- Enterprise Value ≈ 107.0 + 221.6 = **$328.6B**
- (−) Net Debt $22.9B → Equity Value ≈ **$305.7B**
- ÷ Shares 646.14M → **Fair Value ≈ $473/share**

## Fair Value

- **Bear case** (WACC 11.8%, terminal g 2.0%): **≈ $403/share**
- **Base case** (WACC 10.8%, terminal g 2.5%): **≈ $473/share**
- **Bull case** (WACC 9.8%, terminal g 3.0%): **≈ $575/share**

## เทียบราคาปัจจุบัน $562.99

🟡 **Fair (ขอบบน / เกือบ Expensive)** — สูงกว่า Base case FV +19.0% (อยู่ในขอบ ±20% พอดี แต่ชิดขอบบนมาก) — ราคาตลาดตอนนี้อยู่ใกล้เคียง **Bull case ($575)** มากกว่า Base case มาก แปลว่าตลาดกำลัง price-in สถานการณ์ที่เกือบจะดีที่สุด (WACC ต่ำ + terminal growth สูงกว่าที่สมเหตุสมผลสำหรับธุรกิจ No Moat) — ไม่ใช่ "ถูก" อย่างชัดเจน แต่ก็ยังไม่ถึงขั้น "แพงมาก" แบบที่ GuruFocus บอก

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $460** (report พ.ค. 2026 หลัง Q1 FY27) — ใกล้กับ conquest base case มาก (+2.8% เท่านั้น) แม้คำนวณคนละวิธี ทั้งคู่เป็น forward-looking DCF ที่มองเห็น AI backlog/order acceleration เป็นตัวขับเคลื่อนมูลค่าหลัก — ส่วนต่างเล็กน้อยอาจมาจาก Morningstar ยังไม่ได้ update หลัง Q2 FY27 beat (1 ก.ย.) และ AI booking $60.9B ที่ทำให้หุ้นพุ่ง +11% เมื่อ 10 ก.ย.
- **GuruFocus GF Value $206.28** — ห่างจาก conquest base case มาก (+129%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ยึดกับ multiple ในอดีตตอน Dell ยังเป็น PC/hardware margin ต่ำล้วนๆ ก่อน AI server supercycle จะสะท้อนใน earnings/FCF จริง — โครงสร้างวิธีคิดแบบนี้ "มองไม่เห็น" step-change ของ backlog $95B จนกว่าจะมีอีกหลายไตรมาสของผลจริงป้อนเข้า regression
- **สรุป:** Conquest เห็นด้วยกับ **Morningstar** (~$460-475 zone) มากกว่า GuruFocus อย่างชัดเจน — เข้าเกณฑ์ 2-ใน-3 (Conquest + Morningstar) → fair value ที่สมเหตุสมผลกว่าอยู่ในโซน **$400-575** (bear-bull range) ไม่ใช่ $206 — GuruFocus น่าจะเป็น outlier จากข้อจำกัดเชิงวิธีวิทยาที่มองแต่อดีต ราคาตลาด $562.99 จึงไม่ใช่ "Significantly Overvalued" แบบที่ GuruFocus บอก แต่อยู่ในโซนขอบบนของ Fair ที่ priced-for-optimistic-scenario ซึ่งยังต้องระวังความเสี่ยง cyclical ของธุรกิจ No Moat นี้ตามที่ Layer 1 สรุปไว้
