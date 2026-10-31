# 💰 Conquest DCF: VRT — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- Base FCF (ปีที่ 0 = FY26E): $2,700M = midpoint ของ adj FCF guide $2.6–2.8B [หลัก: IR ตาม brief]. หมายเหตุ: เป็น adjusted FCF ไม่ใช่ GAAP; margin ≈ 18.4% ของ sales guide $14.65B; ไม่ได้ใส่ cash flow ของ UIG แยก (ไม่มีตัวเลข) แต่หักราคาซื้อออกจาก net cash
- Growth fade (FCF, คง margin ~18%): ปี1 (FY27) 28% → ปี2 22% → ปี3 17% → ปี4 12% → ปี5 8%
  - เหตุผล: Q4 guide sales $4.31–4.51B annualize ≈ $17.6B (+20% เหนือ FY26) เป็น floor ของ run-rate; บวก backlog/deferred revenue สูงและ "above-market growth ปี 2027" จึงให้ปี1 สูงกว่า investor-day CAGR 20–22% เล็กน้อย; ค่าเฉลี่ย 5 ปี ≈ 17.4% CAGR ต่ำกว่าเป้า 20–22% โดยเจตนา เพราะ (ก) บริษัทเลิกเปิดเผย orders (ข) TAM ที่บริษัทอ้าง ~$75B เทียบ sales ปี5 ~ $27B+ (ค) mean-reversion ของ capex cycle AI และคู่แข่ง Schneider/nVent
- Terminal growth: 3.0% (สูงกว่าฐาน 2–3% เล็กน้อยเพราะ Narrow moat + data center secular; ไม่ใส่สูงกว่านี้เพราะ moat แค่ Narrow)
- WACC: 12.4% = risk-free 4.93% (10Y, brief 10-30) + beta 1.5 × ERP 5.0%. **Beta 1.5 เป็นค่าประมาณ** (brief ระบุ "beta สูง" แต่ไม่มีตัวเลข; หุ้นผันผวนมาก 52-wk $148–$380). หนี้ $2.9B เทียบ mkt cap $89.5B ≈ 3% จึงใช้ cost of equity ตรงๆ
- Shares outstanding: 385.06M (26 ต.ค. 2026, 10-Q)
- Net cash/debt: net cash $783M (ก่อนดีล) − UIG cash $1,450M = −$667M; earn-out ≤$1,150M ใส่ expected ~ $600M (ประมาณ ~50% จะจ่าย — **สมมติฐานประมาณ**) → Net debt ≈ $1,270M

## DCF Calculation ($M, discount ที่ 12.4%)
| ปี | FCF | PV |
|---|---|---|
| 1 | 3,456 | 3,075 |
| 2 | 4,216 | 3,337 |
| 3 | 4,933 | 3,474 |
| 4 | 5,525 | 3,462 |
| 5 | 5,967 | 3,326 |

- PV Stage 1 = $16,674M
- Terminal value (ปี5) = 5,967 × 1.03 ÷ (0.124 − 0.03) = $65,384M → PV = $36,445M (≈ 69% ของ EV)
- EV = $53,119M; − net debt $1,270M = Equity $51,849M ÷ 385.06M = **$134.7/หุ้น**

## Fair Value
- Bear case (WACC 13.4%, g 2.5%): $116.6
- **Base case (WACC 12.4%, g 3.0%): $134.7**
- Bull case (WACC 11.4%, g 3.5%): $159.5
- Sanity: ถ้าใช้ net cash $783M เดิม (ไม่หัก UIG) → $140.0; ผลต่างน้อยกว่า 4%

## เทียบราคาปัจจุบัน $232.50 (ปิด 2026-10-30)
🔴 Expensive — ราคาสูงกว่า Base case FV +72.6% (FV ต่ำกว่าราคา 42%); สูงกว่า Bull case $159.5 อยู่ +46% → ราคาปัจจุบันต้องการ growth/margin สูงกว่าสมมติฐานนี้มาก

Reverse check (คำนวณเอง): ที่ WACC 12.4% แม้ FCF โต 30% ต่อปีคงที่ 5 ปียังได้แค่ ~$211; หรือต้องใช้ WACC ~8.5% (ที่ fade เดิม) จึงจะใกล้ $232 (WACC 9% = $217) — สมมติฐานที่ตลาดคาดจึงรุนแรงกว่าเป้า investor day (CAGR 20–22%)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบ FV ปัจจุบันใน brief (ตัวเลข $103 stale ปี 2025) — ไม่ใช้ปนกับผลคำนวณนี้
- GuruFocus GF Value $169.13 (ส.ค. 2026, stale) ใกล้ Bull case ของ conquest ($159.5) แต่สูงกว่า Base ~26%; ทั้งสองชี้ทิศทางเดียวกันว่าราคา $232.50 สูงกว่ามูลค่า
- **สรุป:** conquest อยู่ฝั่งเดียวกับ GF Value (หุ้นแพง) โดย conquest เข้มงวดกว่าเพราะ WACC สูง (beta 1.5) และ fade เร็วกว่าเป้าบริษัท. ความอ่อนไหวสำคัญ: TV คิดเป็น ~69% ของ EV, และ beta ที่ประมาณไว้ ถ้า beta 1.2 (WACC ~11%) FV จะขยับขึ้นเป็น ~$161 — ยังต่ำกว่าราคาปัจจุบันอยู่ดี
