# Knowledge Base Index

> อ่านไฟล์นี้ก่อนเสมอแทนการอ่าน Thesis Change Log เต็มใน portfolio.md — เปิด atom file เฉพาะ ticker ที่จำเป็น (เปลี่ยนแรง/มี earnings/ตอบคำถามเรื่องนั้น) ประหยัด token

## Holdings (active)

| Ticker | สถานะล่าสุด | Moat | Growth bar (≥30% YoY) | ไฟล์ |
|--------|-------------|------|------------------------|------|
| PLTR | [2026-07-15] 🟢 ปิด $133.76 (+0.03%) ทรงตัวตาม prediction, thesis ไม่เปลี่ยน | Switching Cost (Ontology) | ✅ ผ่าน (US Commercial accelerating) | [PLTR.md](PLTR.md) |
| AVGO | [2026-07-15] 🟢 +1.33% ตาม macro rally (PPI เย็นกว่าคาด) ไม่ใช่ company-specific, thesis ไม่เปลี่ยน | Wide (XPU IP + VMware) | ✅ ผ่าน (AI rev +143%) | [AVGO.md](AVGO.md) |
| GWRE | [2026-07-15] 🔴 -0.12% ทรงตัว ไม่มีข่าวเฉพาะตัว thesis ไม่เปลี่ยน | Switching Cost | ⚠️ ต่ำกว่าเกณฑ์ใหม่ (ARR +19%) | [GWRE.md](GWRE.md) |
| V | [2026-07-15] 🔴 -0.25% ทรงตัว ไม่มีข่าวเฉพาะตัว thesis ไม่เปลี่ยน | Wide (network effect) | ❌ ไม่ผ่านเกณฑ์ใหม่ (defensive/quality) | [V.md](V.md) |

## Sold (archived — reference only)

| Ticker | ผลลัพธ์ | ไฟล์ |
|--------|---------|------|
| MBGL | Realized loss -$0.19 (-5%) — Avoid ตาม /brief (Compounder 2/5) | [_sold/MBGL.md](_sold/MBGL.md) |
| MDLZ | Realized gain +$0.88 (+0.78%) | [_sold/MDLZ.md](_sold/MDLZ.md) |
| MA | Realized gain +$0.42 (+1.69%) | [_sold/MA.md](_sold/MA.md) |
| CME | Realized loss -$5.29 (-15.14%) — Kill triggered | [_sold/CME.md](_sold/CME.md) |
| SPGI | Realized gain +$8.08 (+11.35%) — ขายเพื่อ fund GWRE/PLTR/AVGO (growth style ไม่ใช่ thesis พัง) | [_sold/SPGI.md](_sold/SPGI.md) |

## วิธีใช้ (สำหรับ daily-brief / brief / topup)

1. อ่าน `INDEX.md` นี้ก่อนเสมอ — ได้สถานะล่าสุดแบบสรุปทุก ticker ในบรรทัดเดียว
2. เปิด `[TICKER].md` เฉพาะตัวที่: ราคาเปลี่ยน >3%, มี earnings ภายใน 3 วัน, หรือ user ถามเจาะจงเรื่อง ticker นั้น
3. เมื่อ thesis เปลี่ยน → prepend entry ใหม่ใน `knowledge/[TICKER].md` (ไม่ใช่ portfolio.md) แล้วอัปเดตบรรทัดสรุปใน INDEX.md นี้ให้ตรงกับ entry ล่าสุด
4. Ticker ที่ขายแล้ว → ย้ายไฟล์ไป `knowledge/_sold/[TICKER].md` และย้ายแถวมาลงตาราง Sold ด้านบน
