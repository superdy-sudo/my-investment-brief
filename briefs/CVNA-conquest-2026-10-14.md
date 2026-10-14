# Conquest DCF: CVNA — 2026-10-14
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- Base FCF: $740M (TTM ฐาน Q1 2026: OCF $911M - capex $171M, opencapital.sh ผ่าน WebSearch 2026-10-14) -- ไม่ใช่ TTM ฐาน Q2; Q2 FCF $187M (stocktaper). ยืนยันกับ 10-Q ไม่ได้ [ข้อมูลไม่แน่นอน]
- Growth fade (FCF): ปี1 50% -> 40% -> 30% -> 22% -> ปี5 15% (revenue โต +52% YoY และ margin FCF ยังบาง ~2.5-7% จึงให้ FCF โตเร็วกว่า revenue ปีแรก แล้ว fade ตาม mean-reversion ของธุรกิจโตเร็ว/ส่วนแบ่ง 1-1.5% ของ TAM $1-1.2T) -- เป็นสมมติฐานของผู้วิเคราะห์ ไม่ใช่ guidance
- Terminal growth: 3% (moat ไม่ได้รับการยืนยันจาก Morningstar จึงไม่ใช้สูงกว่า 3%)
- WACC base 11% (ประมาณ): rf 10Y 5.217% (daily-brief 2026-10-14); Yahoo 5Y beta ~3.6 (WebSearch) ถ้าใช้ตรงๆ จะได้ cost of equity >20% ซึ่งไม่สมเหตุผลสำหรับ DCF ระยะยาว จึงใช้ beta ปรับ/normalize ~1.2-1.3 + ERP ~4.5-5% = ~11% (การประมาณ ไม่ใช่ตัวเลขจริง) ช่วงทดสอบ 10-15%
- Shares: 1.100B (Webull รวมทุก class)
- Net debt: ~$2.5B (ประมาณ: Net Debt/TTM Adj. EBITDA 1.0x ณ Q2 2026 x TTM adj. EBITDA ราว $2.5B ซึ่งเป็นการประมาณจากไตรมาส Q2 $769M / guide FY26 $2.7-3.0B; ไม่ได้ดึงงบดุลจริง; ไม่รวม floor plan)

## DCF Calculation
- FCF ปี5 = $2,834M | PV Stage 1 (base) = $7,044M | PV terminal (base) = $21,656M
- EV = $28.7B | Equity = EV - $2.5B = $26.2B | /1.100B shares

## Fair Value (ต่อหุ้น post-split)
- Bear (WACC 12%, g 2.5%): $19.72
- **Base (WACC 11%, g 3%): $23.82**
- Bull (WACC 10%, g 3.5%): $29.80
- Stress ทดสอบ: WACC 13% = $18.18, WACC 15% = $14.44

## เทียบราคาปัจจุบัน $60.39
Expensive (แดง) -- ราคาสูงกว่า Base FV ~153% (Base FV ต่ำกว่าราคา ~60.6%) และสูงกว่า Bull case ~103%

## เทียบกับ GuruFocus
- GF Value $83.09 (stale) ไกลมาก (~3.5x ของ conquest base) เพราะ DCF นี้ใช้ FCF จริง TTM ที่ $740M (market cap ~$66.5B = ~90x FCF) ซึ่งต้องการ margin expansion อย่างมากกว่าที่ fade นี้ให้ เพื่อรองรับราคาปัจจุบัน
- Morningstar FV: Unknown
- สรุป: conquest ไม่เห็นด้วยกับ GF Value; ราคาปัจจุบันสะท้อน FCF margin ที่ขยายมากกว่าสมมติฐานนี้ (reverse-DCF: ต้องการ FCF ปี5 ราว $7-8B+ ที่ WACC 11%) ผลอ่อนไหวต่อ base FCF และ growth สูง
