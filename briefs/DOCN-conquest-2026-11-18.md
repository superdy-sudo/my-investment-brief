# 💰 Conquest DCF: DOCN — 2026-11-18
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — single-source (ไม่มี Morningstar/GuruFocus FV ที่ใช้ได้)*

## Assumptions
- Revenue FY26 (base year): ~$1,210M (guide $1.208–1.211B [หลัก 8-K 2026-11-03])
- Growth fade (FY27→FY31): 50% → 36% → 26% → 18% → 12%
  เหตุผล: mgmt guide FY27 ≥60% [หลัก] แต่ haircut เพราะ capacity-constrained/ต้องพึ่ง AI demand + แข่ง hyperscaler/neocloud และ NDR เดิมแค่ 101% (Q4'25); หลังจากนั้นลดตาม mean-reversion ของธุรกิจโตเร็ว (ฐานใหญ่ขึ้น 3.4x)
- FCF margin "เศรษฐกิจจริง" (หลังหัก capex ที่จ่ายผ่าน finance lease): 8% → 12% → 15% → 17% → 18% (ปี 1–5)
  เหตุผล: Adjusted FCF ของบริษัท 20–22% (FY26 guide) ไม่รวมอุปกรณ์ finance lease/equipment financing ($923.6M obligations) จึงสูงเกินจริง; GAAP op margin Q3 แค่ 10%, gross margin ตกเหลือ 50.1% — ปีแรกใช้ 8% (≈ base FCF จริง ~$100–120M เทียบ adjusted ~$254M) แล้วค่อยปรับขึ้นเมื่อ capex intensity ลดและ scale. **นี่คือ assumption ประมาณการ ไม่ใช่ตัวเลขที่รายงาน** (ไม่มี GAAP FCF หลัง lease capex ในมือ)
- Terminal growth: 3.0% (base) — สูงกว่าปกติเล็กน้อยเพราะยังเป็นธุรกิจโตเร็วใกล้ปีที่ 5 แต่ moat อ่อน-กลาง จึงไม่เกิน 3%
- WACC: 12.0% (base)
  - Risk-free 5.10% (10Y UST 5.103% ปิด 2026-11-17 [daily-brief])
  - Beta ≈ 1.6 **(ประมาณ — ไม่ได้ดึงจากแหล่งยืนยัน; อิงความผันผวนสูง 52wk $42–$187.5 และ high-growth cloud)**
  - ERP 5.0% → cost of equity 13.1%
  - Cost of debt หลังภาษี ~6% (ประมาณ), น้ำหนักหนี้+lease ~14% ของ capital → WACC ≈ 12.1% ปัดเป็น 12.0%
- Shares: 128.5M diluted (Q4 guide 128–129M [หลัก]) — ใช้ conservative; ทางเลือก 117.6M basic (equibles 2026-10-01 [รอง]) ให้ FV สูงขึ้น ~9%
- Net debt: cash+securities $844.7M − debt $461.6M − finance lease/equipment financing $923.6M = **−$540.5M** (นับ lease เป็นหนี้เต็มจำนวน) [หลัก 2026-09-30]

## DCF Calculation (Base: WACC 12%, g 3%) — หน่วย $M
| ปี | Revenue | FCF | PV(FCF) |
|---|---|---|---|
| 1 (FY27) | 1,815 | 145 | 130 |
| 2 | 2,468 | 296 | 236 |
| 3 | 3,110 | 467 | 332 |
| 4 | 3,670 | 624 | 397 |
| 5 | 4,110 | 740 | 420 |

- PV Stage 1 = $1,514M
- Terminal value = 740 × 1.03 ÷ (0.12 − 0.03) = $8,467M → PV = $4,805M (~76% ของ EV — อ่อนไหวต่อ terminal มาก)
- EV = $6,319M; ลบ net debt (รวม lease) $540.5M → Equity = $5,778M
- ÷ 128.5M sh = **$44.97/share** (ถ้าใช้ 117.6M sh = $49.14)

## Fair Value
- Bear case (WACC 13%, g 2.5%): **$37.72** ($41.22 ที่ 117.6M sh)
- **Base case (WACC 12%, g 3.0%): $44.97** ($49.14 ที่ 117.6M sh)
- Bull case (WACC 11%, g 3.5%): **$55.11** ($60.21 ที่ 117.6M sh)

## เทียบราคาปัจจุบัน $79.44 (ปิด 2026-11-17)
🔴 Expensive — ราคาสูงกว่า Base FV +76.6% (Base FV ต่ำกว่าราคา -43.4%); สูงกว่า Bull case ($55.11) ด้วย +44%
ความมั่นใจ: ต่ำ-กลาง — range แคบ (~$38–55) แต่ผลขึ้นกับ FCF margin หลัง lease และ growth FY27 มากกว่า WACC. Sanity check: ที่ราคา $79.44 ต้องใช้สมมติฐานประมาณ growth สูงกว่า guide FY27 ≥60% ต่อเนื่อง + margin หลัง lease ≥20% จึงจะรองรับ

## เทียบกับ Morningstar/GuruFocus
- Morningstar: ⚪ ไม่มี (quant-only ล็อก) — ใช้เทียบไม่ได้
- GuruFocus: ⚪ snapshot ขัดกันเอง (Price/GF Value 2.53 vs 0.63) — ใช้เทียบไม่ได้
- (ข้อมูลอ้างอิงเฉย ๆ ไม่ได้นำมาปนคำนวณ: DCF site vcpscanner $45.26 ในบรีฟ — บังเอิญใกล้ base ของ conquest แต่คนละที่มา ไม่ใช้ยืนยัน)
- **สรุป:** valuation เป็นแหล่งเดียว (conquest) จึงเป็น indicative ไม่ใช่ 2-ใน-3; ผลชี้ว่าราคาปัจจุบัน price in ฉากทัศน์ที่ดีกว่า bull case แม้หลังร่วง -57.6% จาก high. ข้อจำกัดหลัก: beta ประมาณ, FCF margin หลัง lease เป็นประมาณการ, share count ไม่ชัด
