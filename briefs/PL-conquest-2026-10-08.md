# 💰 Conquest DCF: PL (Planet Labs PBC) — 2026-10-08
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*
*Input ทั้งหมดมาจาก briefs/PL-2026-10-08.md (raw fundamentals: Q2 FY27 8-K, guidance, ราคา Yahoo/Webull 2026-10-08)*

## Assumptions
- **Base (ปี 0 = FY27E):** revenue $435.5M (midpoint guide $430-441M); FCF margin 8% -> Base FCF ~ $35M
  - เหตุผล: 6M FY27 FCF margin 10.1% แต่ capex guide เพิ่มเป็น $100-115M (FY26 ~$81.5M) จึงตั้งต่ำกว่า 6M และ FY26 (17.2%) เพื่อสะท้อน capex ที่เร่งขึ้น (ประมาณการ ไม่ใช่ตัวเลขที่บริษัท guide)
- **Revenue growth fade:** ปี1 28% -> ปี2 24% -> ปี3 20% -> ปี4 16% -> ปี5 12%
  - เหตุผล: Q3 guide +27% YoY, backlog โตแค่ +11% (ชะลอ), TAM EO ภายนอก ~$5.6B -> $7.2B (2030) ทำให้ share gain ต้องมาก, คู่แข่งหนา, ธุรกิจ sovereign lumpy
- **FCF margin ramp:** 10% -> 13% -> 16% -> 18% -> 20% (operating leverage จาก adj. EBITDA ที่เริ่มบวก แต่ capex-intensive ถ่วงเพดาน)
- **Terminal growth:** 3.0% (บน; สูงกว่า baseline 2-3% เล็กน้อยเพราะเป็นข้อมูล/สัญญา recurring ACV 98% แต่ moat ยังพิสูจน์ไม่ได้ จึงไม่ตั้งสูงกว่านี้)
- **WACC:** 14.3% = risk-free 5.3% (10Y Treasury ~5.30% จาก daily-brief 2026-10-08) + beta 1.8 x ERP 5.0%
  - beta 1.8 = **ค่าประมาณ** (ไม่ได้ดึงค่าจริง; หุ้นผันผวนสูง ตกจาก $51.76 เหลือ $16.9 ใน ~4 เดือน, small/mid-cap space) ; ใช้ cost of equity ตรงๆ เพราะ net cash
- **Shares:** 363.8M (Webull 2026-10-08) — **ยังไม่รวม dilution ต่อจาก ATM $1.5B authorized และ SBC** (ทำให้ FV ต่อหุ้นจริงน่าจะต่ำกว่าที่คำนวณ)
- **Net cash:** +$417M (cash+ST inv $865.4M - convertible $448.3M, 2026-07-31)
- หมายเหตุ: FCF ที่ใช้ยังไม่หัก SBC (ไม่มีตัวเลข SBC ใน brief) -> bias ขึ้น

## DCF Calculation ($M, Base case: WACC 14.3%, g 3%)
| ปี | Revenue | FCF margin | FCF | PV |
|---|---|---|---|---|
| 1 | 557.4 | 10% | 55.7 | 48.8 |
| 2 | 691.2 | 13% | 89.9 | 68.8 |
| 3 | 829.5 | 16% | 132.7 | 88.9 |
| 4 | 962.2 | 18% | 173.2 | 101.5 |
| 5 | 1,077.6 | 20% | 215.5 | 110.5 |

- PV ของ FCF ปี 1-5 = $418.4M
- Terminal value = 215.5 x 1.03 / (0.143 - 0.03) = $1,964.6M -> PV = $1,007.0M
- Enterprise value = $1,425.4M
- + net cash $417M = Equity value $1,842.4M
- / 363.8M shares = **$5.06/share**

## Fair Value
| Case | WACC | g | FV/share |
|---|---|---|---|
| Bear | 15.3% | 2.5% | **$4.59** |
| **Base** | 14.3% | 3.0% | **$5.06** |
| Bull | 13.3% | 3.5% | **$5.68** |

Range แคบ ($4.59-$5.68) เพราะ assumption operating (growth/margin) เป็นตัวกำหนดหลัก ไม่ใช่ WACC/g; ทุก case ต่ำกว่าราคาปัจจุบันมาก
(ความอ่อนไหวสำคัญอยู่ที่ growth/margin ไม่ได้ sensitivity ใน 3 case ข้างบน — ราคา $16.905 ต้องการ FCF ปี 5 สูงกว่านี้หลายเท่า)

## เทียบราคาปัจจุบัน $16.905
🔴 **Expensive** — ราคาสูงกว่า Base case FV $5.06 ประมาณ +234% (Base FV ต่ำกว่าราคา ~70%)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่มีตัวเลข (Quantitative Rating, ล็อก) — เทียบไม่ได้
- GuruFocus GF Value $5.63 (2026-10-02) — **ใกล้** conquest base ($5.06; ต่างราว -10%) แม้วิธีต่างกัน (GF = historical-multiple regression, conquest = forward DCF) ; Bull case $5.68 ใกล้ GF Value เกือบเท่ากัน
- **สรุป:** conquest เห็นด้วยกับ GuruFocus ว่าหุ้นแพงมากเทียบ fundamentals; DCF ที่อนุมัติ growth 40%+ ต้นปีลดลงตาม fade และ margin 20% ปีที่ 5 ยังให้ FV ราว 1/3 ของราคา -> ราคาตลาดต้องพึ่ง growth/margin/TAM ที่สูงกว่า assumption นี้มาก (เช่น TAM ขยายด้วย AI/analytics) ซึ่งยังไม่มีหลักฐานยืนยัน

## ข้อจำกัด
- Beta, FCF margin path, terminal margin เป็นค่าประมาณของ conquest ไม่ใช่ guidance ของบริษัท
- ไม่รวม dilution ATM/SBC (FV จริงต่อหุ้นน่าจะต่ำกว่า) ; ไม่ได้ stress test แบบ growth สูงกว่านี้มาก (ไม่ได้คำนวณ)
