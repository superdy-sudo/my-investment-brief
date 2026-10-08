# 💰 Conquest DCF: ELF — 2026-10-08
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — ใช้ raw fundamentals จาก briefs/ELF-2026-10-08.md เท่านั้น ไม่ได้ WebSearch เพิ่ม*

## Assumptions
- Base FCF (unlevered, normalized, FY27E ปีสิ้น 2027-03): ~$205M = 10.5% ของ net sales guide midpoint $1,953M
  - ที่มา: FY26 FCF $190.1M (11.6%) + after-tax interest โดยประมาณ → unlevered ~13%; แต่ FY27 ต้อง normalize ออก: tariff refund ครั้งเดียว $51.1M (Adj EBITDA guide $401-407M midpoint $404M → ex-refund ~$353M ≈ 18.1% margin เทียบ FY26 20.5%) และ OCF บวก SBC กลับ (ไม่ทราบตัวเลข SBC ในไฟล์ จึงหักเผื่อโดยประมาณ) → ใช้ 10.5% (ประมาณการ ไม่ใช่ตัวเลขรายงาน)
- Revenue fade (หลัง FY27): ปี1 +8% → ปี2 +7% → ปี3 +6% → ปี4 +5% → ปี5 +4%
  - เหตุผล: FY27 +18-20% มาจาก rhode (inorganic, ปิดดีล Aug 2025 จะ lap ใน H2 FY27); e.l.f. core organic ติดลบ high single digit (Q1 FY27, ex-rhode derived -9.7%); หลัง lap เหลือ rhode โตต่อ + core ฟื้นช้า จึงตั้งต้นที่ 8% แล้วลดสู่ใกล้ terminal
- FCF margin: 10.7% → 11.0% → 11.4% → 11.7% → 12.0% (operating leverage + tariff ลดจาก ~55%→35%; ไม่ถึง 13%+ เพราะ price/volume pressure และดอกเบี้ย/ภาษี)
- Terminal growth: 3.0% (ระดับบนของช่วงปกติ เพราะ brand/shelf share gain แต่ moat ยังไม่ยืนยัน จึงไม่สูงกว่านี้)
- WACC: 11.3% = risk-free 5.30% (10Y 5.303% จาก commit ล่าสุดของระบบ 2026-10-08) + beta 1.4 (**ประมาณการ** ไม่ได้ดึงจริง; consumer/beauty high-growth, หุ้นผันผวนสูง 52wk $48.82-$147.75) × ERP 5.0% = cost of equity 12.3%; ผสม debt ~12% weight (หนี้ $834M / mkt cap ~$6.2B, cost 5.4% pre-tax, after-tax ~4.1%) → WACC ≈ 11.3%
- Diluted shares: 60.5M (ตาม guide; basic 58.9M)
- Net debt: $490.0M (06-30-2026)
- Discount convention: end-of-year, ปี1 = FY28 (ไม่ปรับ stub period)

## DCF Calculation (Base)
| ปี | Revenue ($M) | FCF margin | FCF ($M) | DF @11.3% | PV ($M) |
|---|---|---|---|---|---|
| FY27E (base) | 1,953 | 10.5% | 205 | — | — |
| 1 | 2,109 | 10.7% | 225.7 | 0.8985 | 202.8 |
| 2 | 2,257 | 11.0% | 248.3 | 0.8073 | 200.4 |
| 3 | 2,392 | 11.4% | 272.7 | 0.7253 | 197.8 |
| 4 | 2,512 | 11.7% | 293.9 | 0.6517 | 191.5 |
| 5 | 2,612 | 12.0% | 313.4 | 0.5855 | 183.5 |
- PV Stage 1 = $976M
- Terminal value = 313.4 × 1.03 / (0.113 − 0.03) = $3,889M → PV = $2,277M (70% ของ EV)
- EV = $3,253M → − net debt $490M = Equity $2,763M → ÷ 60.5M = **$45.7/หุ้น**

## Fair Value
- Bear (WACC 12.3%, g 2.5%): **$38.0**
- **Base (WACC 11.3%, g 3.0%): $45.7**
- Bull (WACC 10.3%, g 3.5%): **$56.8**
(Bear/Bull ปรับเฉพาะ WACC ±1% และ g ±0.5% ตามสเปก ไม่ได้ปรับ margin/growth)

## เทียบราคาปัจจุบัน $104.80
🔴 Expensive — ราคาสูงกว่า Base FV ~+129% (Base FV ต่ำกว่าราคา ~-56%); แม้ Bull ($56.8) ราคายังสูงกว่า ~+85%
- ตลาดกำลัง price-in margin/growth สูงกว่ามาก: reverse check คร่าวๆ — ต้องใช้ FCF margin ยั่งยืนระดับสูง (≥~18-20%) และ/หรือ growth สูงกว่า fade นี้มาก จึงจะเข้าใกล้ $105

## เทียบกับ Morningstar/GuruFocus
- ไม่ได้อ่านตัวเลข FV ของแหล่งอื่นตามกฎ (brief ระบุ Morningstar ไม่มีค่าที่ยืนยันได้; มี GF Value ใน brief แต่ตั้งใจไม่ใช้ในการคำนวณ)
- สรุป: conquest ไม่สนับสนุนมุมมองว่าหุ้น undervalued; FV ที่ได้ต่ำกว่าราคามาก ผลขึ้นกับ FCF margin และ rhode durability เป็นหลัก

## ข้อจำกัด
- Beta, SBC, และ FCF margin ปี FY27 normalized เป็นการประมาณ ไม่ได้ดึงจริง; refund $51.1M normalize ตามที่ brief ระบุ แต่ไม่ทราบว่า guide EBITDA รวม refund เต็มจำนวนหรือไม่ (สมมติรวม)
- ไม่แยก DCF ราย segment (rhode vs core); ไม่ปรับ stub period
- TV คิดเป็น ~70% ของ EV → ไวต่อ WACC/g
