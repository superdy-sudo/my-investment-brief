# 💰 Conquest DCF: GKOS — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — ใช้ raw fundamentals จาก briefs/GKOS-2026-10-31.md เท่านั้น*

## Assumptions
- Base: ไม่มี FCF TTM เต็มปีที่ใช้ได้ (9M'26 FCF +$32.1M, Q3 +$36.5M ไตรมาสเดียว) -> **ใช้ revenue-driven DCF**: Rev FY26 guide mid $780M -> 2027 prelim guide $1.0B [หลัก 8-K] แล้ว fade; FCF = Rev x FCF margin ramp
- Growth fade (ปี1=FY27): $1,000M (+28%, guide) -> +22% $1,220M -> +18% $1,440M -> +14% $1,642M -> +10% $1,806M. เหตุผล: ปัจจุบัน +58% แต่บางส่วนเป็น Epioxa launch base ต่ำ; mean-reversion ของธุรกิจโตเร็ว, Alcon แข่ง MIGS, Intl Glaucoma โตแค่ +13%
- FCF margin ramp (**ประมาณการของ conquest ไม่ใช่ guidance**): 15% -> 20% -> 24% -> 27% -> 28%. เหตุผล: Q3 17.3%, 9M 5.9%, GM 85% จึงมี operating leverage แต่ยังไม่มี trend หลายไตรมาส
- FCF: $150M / $244M / $346M / $443M / $506M
- Terminal growth 3.0% (base) — medtech กับ patent moat; 2.5%/3.5% ใน bear/bull
- WACC 10.4% = rf 4.93% (10Y, brief 10-31) + beta 1.1 (**ประมาณการ ไม่ได้ตรวจ**) x ERP 5% ; net cash ใช้ cost of equity ตรง
- Shares 58.98M (Webull 10-28 [รอง], ไม่ได้ตรวจ 10-Q/diluted)
- Net cash +$339.8M (ไม่หัก finance lease $66.9M; กระแสเงินสดเป็นตัวสะท้อนค่าเช่าอยู่แล้ว). Discount timing: t = 1.17, 2.17 ... (วัดจาก ต.ค. 2026 ถึงสิ้น FY27)

## DCF Calculation (base)
- PV ของ FCF 5 ปี ≈ $1,180M
- Terminal value (FCF ปี5 $506M x 1.03 / (10.4%-3%)) ≈ $7.0B, PV ≈ $4,220M
- EV ≈ $5.40B + cash $340M = Equity ≈ $5.74B -> / 58.98M

## Fair Value
- Bear (WACC 11.4%, g 2.5%): **$82**
- **Base (WACC 10.4%, g 3.0%): $97**
- Bull (WACC 9.4%, g 3.5%): **$121**

## เทียบราคาปัจจุบัน $237.60
🔴 Expensive — ราคาสูงกว่า Base FV ~+145% (สูงกว่าแม้ Bull case ~+96%). ตลาดสะท้อน growth/margin สูงกว่าสมมติฐานนี้มาก (EV ~$13.7B ≈ 14x sales 2027)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบ ใน brief
- GuruFocus GF Value $153.16 (stale ก่อน beat+raise): conquest base ต่ำกว่า ~37% แต่ทั้งคู่ต่ำกว่าราคา; อ่อนไหวมากต่อ FCF margin terminal (28%) — ถ้า margin 35% และ growth สูงกว่านี้ FV จะขยับขึ้น แต่ต้อง bull ต่อเนื่องหลายปีเพื่อให้ถึง $237
- **สรุป:** conquest เห็นด้วยกับ GF Value ในทิศทาง (ราคาแพงกว่า fair) และเข้มกว่า; ความมั่นใจในระดับ FV ต่ำ-กลาง (หลายตัวแปรเป็นประมาณการ) แต่ bucket Expensive มั่นใจสูง เพราะ Bull case ยังต่ำกว่าราคามาก
