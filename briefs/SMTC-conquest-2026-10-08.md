# 💰 Conquest DCF: SMTC — 2026-10-08
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- Base FCF: $244M = Q2 FY27 FCF $61M x 4 (run-rate; ที่มา brief 10-08). อ้างอิง FY2026 FCF $171.4M (SEC 8-K / Business Wire 16 มี.ค. 2026) — ใช้ run-rate เพราะ Q3 guide $410M (+20% QoQ) สูงกว่า FY26 มาก
- Growth fade (FCF): ปี1 45% -> ปี2 35% -> ปี3 25% -> ปี4 17% -> ปี5 11%. เหตุผล: revenue Q3 guide +54% YoY, Q2 +33%; FCF โตเร็วกว่า revenue จาก operating leverage + ดอกเบี้ยจ่ายลดจาก $75M เหลือ <$3M แต่ data-center เป็นผู้ท้าชิงเทียบ Marvell/Broadcom จึง fade เข้าหา terminal ตามกฎ mean-reversion ของธุรกิจโตเร็ว
- Terminal growth: 3.0% (ตลาด semis/IoT โตเหนือ GDP เล็กน้อย, moat เฉพาะ LoRa)
- WACC 13.9% = risk-free 5.30% (10Y, brief 10-08) + adjusted beta 1.9 x ERP 4.5%. Raw beta 5Y monthly 2.35 (Yahoo Finance) ปรับแบบ Blume (0.67x2.35+0.33 = ~1.9) เป็นการประมาณ; ใช้ cost of equity ตรงๆ เพราะ net leverage 1.5x ต่ำ
- Shares: 93.3M (brief 10-08; FY26 diluted 88M)
- Net debt: $338.3M (Q2 FY27)

## DCF Calculation (Base)
FCF ($M): ปี1 354 | ปี2 478 | ปี3 598 | ปี4 700 | ปี5 775
- PV ของ FCF ปี1-5 = $1,902M
- Terminal value = 775 x 1.03 / (0.139-0.03) -> PV = $3,822M
- EV = $5,724M; Equity = 5,724 - 338 = $5,386M; /93.3M = $57.7/หุ้น

## Fair Value
- Bear (WACC 14.9%, g 2.5%, growth fade ต่ำกว่า): $40.2
- **Base: $57.7**
- Bull (WACC 12.9%, g 3.5%, growth 52/42/30/21/14%): $81.2

## เทียบราคาปัจจุบัน $195.10
🔴 Expensive — ราคาสูงกว่า Base FV ~238% (แม้ Bull case $81 ก็ต่ำกว่าราคามาก) ราคาปัจจุบัน implied ต้องการ FCF โตสูงกว่า/ WACC ต่ำกว่า assumptions นี้มาก (market cap $18.2B = ~75x FCF run-rate)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบตัวเลขที่ใช้ได้ (brief 10-08)
- GuruFocus GF Value $47.97 (10-08): ใกล้ Base conquest ($57.7) — ทั้งคู่ชี้ Expensive; SWS DCF $52.55 (23 มิ.ย.) ก็อยู่ใกล้กัน
- Analyst PT consensus ~$208 อยู่ไกลมาก (price-in re-rating AI data-center ยาวกว่า 5 ปี)
- **สรุป:** conquest เห็นด้วยกับฝั่ง GF Value/SWS DCF (Expensive) ไม่ใช่ฝั่ง analyst PT. ข้อจำกัด: DCF อ่อนไหว (Bull ที่ดันทุกตัวแปรยังได้แค่ $81) และ Teach-in 15 ต.ค. อาจให้ multiyear framework ที่เปลี่ยน growth fade ได้
