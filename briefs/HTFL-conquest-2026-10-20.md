# 💰 Conquest DCF: HTFL (Heartflow) — 2026-10-20
*Independent bottom-up 2-stage DCF (Claude-only) — **ผล: คำนวณไม่ได้อย่างมีหลักฐาน (N/A)** ไม่มี Bear/Base/Bull FV*

ราคาอ้างอิง $54.90 | shares 86,953,627 | mkt cap ≈ $4.77B | net cash $246.84M | EV ≈ $4.53B (ตัวเลขจาก brief HTFL-2026-10-20 ส่วน Raw Fundamentals)

## ทำไมคำนวณไม่ได้
DCF ต้องมี Base FCF ที่เป็นบวก และ margin ปลายทาง (terminal FCF margin) ที่มีฐานหลักฐาน ข้อมูลที่มีไม่พอ 4 ข้อ:

1. **Base FCF ติดลบ** — operating cash use 6M 2026 = -$38.7M (~-33% ของ revenue $116.7M) และเป็นตัวเลข third-party summary ยังไม่ตรวจกับงบกระแสเงินสดต้นทาง ไม่พบ capex จึงไม่รู้ FCF margin แน่ชัด
2. **ไม่มีประวัติกำไรให้ยึด** — accumulated deficit $1.1B, net loss 6M $(43.1)M ไม่มีปีไหนที่ FCF เป็นบวก จึงไม่มีฐานข้อมูลจริงสำหรับกำหนด steady-state FCF margin (ค่านี้คุม terminal value ซึ่งโดยปกติเป็น >80% ของ EV ของบริษัทโตเร็ว) ต้องเลือกตัวเลขลอยๆ เอง ซึ่งขัดกฎ "ห้ามใส่ตัวเลขลอย"
3. **เส้นทางไปสู่ breakeven มีแหล่งเดียวและ second-hand** — เป้า cash-flow profitable กลางปี 2028 มาจากผลค้นสรุปงบ Q2 ยังไม่ได้เปิด press release ต้นทาง และเป็นเป้าฝ่ายบริหาร ไม่ใช่ตัวเลขที่ตรวจสอบได้
4. **Revenue base ปีก่อนขัดกัน** — guidance FY2026 $246-250M implied FY2025 ≈ $175M แต่ aggregator ระบุ $158.6M ใช้ growth rate เทียบปีก่อนไม่ได้อย่างมั่นใจ (มีแค่ guidance ปีนี้ที่ใช้ได้)

ผลของการฝืนทำ: เปลี่ยน terminal FCF margin จาก 15% เป็น 30% (ทั้งสองเป็นการเดา) FV จะเปลี่ยนเกือบ 2 เท่า และ WACC/terminal growth sensitivity ตามกฎไม่สะท้อนความไม่แน่นอนหลักนี้ จึงให้ range ที่ดูมีความหมายแต่จริงๆ ไม่มี

## ข้อเท็จจริงที่ใช้ได้ (ไม่ใช่ FV)
- มูลค่าตลาดที่ราคา $54.90: EV ≈ $4.53B ≈ 18.3x revenue guidance FY2026 กึ่งกลาง $248M (คำนวณเลขคณิตตรงๆ ไม่ใช่การประเมินมูลค่า)
- จุดแข็งที่เห็นเป็นตัวเลข: GM 75.5% → 83.0% YoY, revenue +47.6% Q2, ไม่มีหนี้, cash runway ค่อนข้างยาว (cash use ~$77M/ปี เทียบ cash $246.8M — คำนวณเลขคณิตจาก 6M x2 ถ้า burn คงที่)
- ตัวเลขที่ต้องมีก่อนทำ DCF ได้: (a) งบกระแสเงินสดต้นทางจาก 10-Q (CFO, capex, SBC) (b) press release Q2 ยืนยันเป้า breakeven (c) FY2025 revenue จาก 10-K (d) งบ Q3 (คาดรายงาน ~11/10-11/16) ถ้าเห็น operating cash use แคบลงชัด ค่อย re-run

## เทียบราคา $54.90
⚪ **ไม่มี bucket (🟢/🟡/🔴 ไม่ให้)** — ไม่มี Base FV ให้เทียบ

## เทียบกับ Morningstar/GuruFocus
- Morningstar: Quantitative rating ถูก lock ไม่เห็นค่า ⚪
- GuruFocus: ไม่พบ GF Value ⚪
- **สรุป:** ไม่มี FV ที่ใช้ได้จากแหล่งใดเลย (รวม conquest) → Valuation = ⚪ Unknown / Inconclusive จนกว่าข้อมูลข้างบนจะครบ (ไม่นำ analyst PT $38.50 หรือ Simply Wall St มาแทนเป็น FV ตามกฎ)
