# Knowledge Base Index

> อ่านไฟล์นี้ก่อนเสมอแทนการอ่าน Thesis Change Log เต็มใน portfolio.md — เปิด atom file เฉพาะ ticker ที่จำเป็น (เปลี่ยนแรง/มี earnings/ตอบคำถามเรื่องนั้น) ประหยัด token

## Holdings (active)

| Ticker | สถานะล่าสุด | Moat | Growth bar (≥30% YoY) | ไฟล์ |
|--------|-------------|------|------------------------|------|
| PLTR | [2026-08-04] 🔴 Full re-score เสร็จ: Action ยัง Avoid (Provisional) เท่า 8/2 แต่เหตุผลเปลี่ยน — growth ไม่ใช่ปัญหาแล้ว (US Commercial +149% YoY), ตัวที่ยังติดคือ TAM ratio แย่ลง (~4.02x, ราคาพุ่งเร็วกว่า TAM re-rate) + Morningstar ยืนยัน Narrow Moat (Dominant Incumbent Exception ใช้ไม่ได้) — Kill Condition ยังไม่ trigger (ห่างไกลกว่าเดิม) → HOLD คงเดิม, Dynamic TP Reset Provisional TP1 $217.88/TP2 $290.50 รอ confirm ราคาเปิดตลาด | Narrow (Switching Cost + Intangible Assets) | ✅ ผ่านชัดเจน (US Commercial +149% YoY) | [PLTR.md](PLTR.md) |
| AVGO | [2026-09-04] ✅ Thesis ดีขึ้น — Google concentration risk (7/27 flagged, 8/20 confirmed) แก้แล้วด้วยหลักฐานจาก Q3 FY2026 earnings call — Google ยืนยันสัญญาซื้อ TPU multi-tens-of-billions/ปีต่อเนื่อง + ประกาศชื่อลูกค้าใหม่ครั้งแรก: Anthropic (จะขึ้นเป็นลูกค้า XPU รายใหญ่สุดปี 2027), OpenAI (Jalapeño 1.3GW→5GW+), Meta (MTIA production เริ่มแล้ว) | Q3 revenue $29.6B +86% YoY, AI semi $16.7B +221% YoY, Q4 guide AI semi +236% YoY | ราคาร่วง -2.75% เหลือ $357.16 เป็น sell-the-news ไม่ใช่ fundamental อ่อน | Dynamic TP Reset ผ่านเกณฑ์ growth แต่ไม่ reset (ราคายังต่ำกว่า TP1 มาก reset จะหดเป้าแทนขยาย) — คง TP1/TP2 $558.32/$744.42 | Wide (XPU IP + VMware) | ✅ ผ่าน (AI rev +221%) | [AVGO.md](AVGO.md) |
| GWRE | [2026-08-17] 🚨 หลุดใต้ TP1 $172.42 ครั้งแรกในรอบ 6 วัน จากแรงขายกลุ่ม software ("AI fears") ไม่ใช่ thesis เปลี่ยน — user ตัดสินใจ trim 30% ที่ราคา $175 (รอ execute) | Switching Cost | ⚠️ ต่ำกว่าเกณฑ์ใหม่ (ARR +19%) | [GWRE.md](GWRE.md) |

## Sold (archived — reference only)

| Ticker | ผลลัพธ์ | ไฟล์ |
|--------|---------|------|
| MBGL | Realized loss -$0.19 (-5%) — Avoid ตาม /brief (Compounder 2/5) | [_sold/MBGL.md](_sold/MBGL.md) |
| MDLZ | Realized gain +$0.88 (+0.78%) | [_sold/MDLZ.md](_sold/MDLZ.md) |
| MA | Realized gain +$0.42 (+1.69%) | [_sold/MA.md](_sold/MA.md) |
| CME | Realized loss -$5.29 (-15.14%) — Kill triggered | [_sold/CME.md](_sold/CME.md) |
| SPGI | Realized gain +$8.08 (+11.35%) — ขายเพื่อ fund GWRE/PLTR/AVGO (growth style ไม่ใช่ thesis พัง) | [_sold/SPGI.md](_sold/SPGI.md) |
| V | Realized gain +$9.11 (+12.33%) — ปิด position ตาม Avoid signal ยืนยันต่อเนื่องตั้งแต่ 07-16 (growth ❌, DOJ risk, Berkshire ขายทิ้ง) | [_sold/V.md](_sold/V.md) |

## วิธีใช้ (สำหรับ daily-brief / brief / topup)

1. อ่าน `INDEX.md` นี้ก่อนเสมอ — ได้สถานะล่าสุดแบบสรุปทุก ticker ในบรรทัดเดียว
2. เปิด `[TICKER].md` เฉพาะตัวที่: ราคาเปลี่ยน >3%, มี earnings ภายใน 3 วัน, หรือ user ถามเจาะจงเรื่อง ticker นั้น
3. เมื่อ thesis เปลี่ยน → prepend entry ใหม่ใน `knowledge/[TICKER].md` (ไม่ใช่ portfolio.md) แล้วอัปเดตบรรทัดสรุปใน INDEX.md นี้ให้ตรงกับ entry ล่าสุด
4. Ticker ที่ขายแล้ว → ย้ายไฟล์ไป `knowledge/_sold/[TICKER].md` และย้ายแถวมาลงตาราง Sold ด้านบน
