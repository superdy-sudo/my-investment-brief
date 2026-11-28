# 💰 Conquest DCF: VIAV — 2026-11-28
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — ใช้เฉพาะ Raw Fundamentals ใน briefs/VIAV-2026-11-28.md*

## Assumptions
- **Base revenue / FCF:** ไม่ annualize Q1 FY27 (14 สัปดาห์ + tariff refund ~$11M one-time + working capital ช่วย; FCF $92.7M/19.8% สูงเกิน run-rate) → ใช้ FY27 revenue ที่ anchor จาก guidance: Q1 $469.3M (จริง) + Q2 $510M (กลาง guide $505–515M) + Q3 ~$525M + Q4 ~$541M (สมมติ sequential +3%/ไตรมาส [อนุมาน]) ≈ **$2,045M** (+34.7% vs FY26 $1,518M — อยู่ในช่วง organic ~29–38% [อนุมานใน brief])
- **FCF margin (normalized):** FY27 14% → 15% → 16% → 16.5% → 17% เหตุผล: Q1 19.8% เกินจริงจากปัจจัย one-time, Q4 FY26 12.5%, FY26 5.4% (ถูกกดจากการรวม Spirent/ดอกเบี้ย term loan); non-GAAP op margin 24–29% แต่ต้องหัก tax/capex/SBC-related cash → ไม่เกิน 17% ในปีที่ 5
- **Growth fade (ปี1–5 = FY27–FY31):** +34.7% (guidance-anchored) → +18% → +13% → +9% → +6% เหตุผล: ปี 1 รวมแรงจาก Spirent + 14 สัปดาห์ + data center/defense; หลังนั้น organic ล้วน ลดลงตามกฎ mean-reversion, ลูกค้ากระจุก AI/data center capex (analyst ถามเรื่องความยั่งยืน), OSP โตต่ำ (+12%)
- **Terminal growth:** 3.0% (ขอบบนของช่วงปกติ 2–3% — niche leadership/RPO $664M แต่เป็น Narrow Moat, ตลาด test & measurement กระจัดกระจาย จึงไม่สูงกว่านี้)
- **WACC:** ~11.0% = Ke 11.8% (risk-free 4.3% [ประมาณ ไม่ได้ดึงค่าวันนี้] + beta 1.5 [ประมาณจากความผันผวน 52wk $16.69–$60.43, ไม่ใช่ค่าจริง] × ERP 5.0%) ถ่วงกับหนี้ ~8.5% ของ cap (cost of debt 3.75% senior notes, หลังภาษีประมาณ) 
- **Diluted shares:** 266.2M (Q1 FY27 10-Q; รวม convertible/RSU)
- **Net debt:** ~$107M (debt $642.5M − cash+ST inv+restricted $535.3M)
- ข้อจำกัด: discount ปีที่ 1–5 เป็น t=1..5 เต็มปี (ปีงบ 1 ผ่านมาแล้ว ~4 เดือน → ค่อนข้างอนุรักษ์เล็กน้อย)

## DCF Calculation (base, WACC 11.0%, g 3.0%, หน่วย $M)
| ปี | Revenue | FCF margin | FCF |
|---|---|---|---|
| FY27 | 2,045 | 14.0% | 286.3 |
| FY28 | 2,413 | 15.0% | 362.0 |
| FY29 | 2,727 | 16.0% | 436.3 |
| FY30 | 2,972 | 16.5% | 490.4 |
| FY31 | 3,151 | 17.0% | 535.6 |

- PV ของ FCF ปี 1–5 = $1,512M
- Terminal value = 535.6 × 1.03 ÷ (0.11 − 0.03) = $6,896M → PV = $4,092M (**~73% ของ EV** — อ่อนไหวต่อ assumption สูง)
- EV = $5,604M − net debt $107M = Equity $5,497M ÷ 266.2M = **$20.65/หุ้น**

## Fair Value
- Bear (WACC 12.0%, g 2.5%): EV $4,749M → Equity $4,642M → **$17.44**
- **Base (WACC 11.0%, g 3.0%): $20.65**
- Bull (WACC 10.0%, g 3.5%): EV $6,850M → Equity $6,743M → **$25.33**

## เทียบราคาปัจจุบัน $28.15 (ปิด 2026-11-27)
🔴 **Expensive** — ราคาสูงกว่า Base case FV +36.3% และสูงกว่าแม้แต่ Bull case ($25.33) ~+11% → ตลาดราคาในการเติบโต/margin ที่สูงกว่า assumption นี้ (เช่น FCF margin ยั่งยืน >17% หรือโตเร็วกว่า fade ที่ใช้)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบตัวเลขที่เชื่อถือได้ใน brief (ตัวเลข $40.43 เดิมไม่ใช่หน้า Morningstar และ stale) → เทียบไม่ได้
- GuruFocus GF Value: ระบุเฉพาะ Price/GF Value, implied GFV ≈ $12.4–$14.9 บน snapshot เก่า → stale/เชื่อถือไม่ได้ (ตามกฎ 2026-10-03); ถ้าใช้ก็ต่ำกว่า conquest base
- **สรุป:** conquest อิสระให้ FV ต่ำกว่าราคา — ไม่มีแหล่งภายนอกที่ใช้ได้มา arbitrate แต่ทิศทาง (ราคา > FV) สอดคล้องกับ GF Value ที่ต่ำ; single-source ไม่ใช่ข้อสรุปเด็ดขาด เนื่องจาก beta/risk-free เป็นการประมาณ และ TV ครอบคลุม ~73% ของมูลค่า
