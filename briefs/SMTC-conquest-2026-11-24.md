# 💰 Conquest DCF: SMTC (Semtech) — 2026-11-24
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — rerun หลังงบ Q3 FY27 (ออก 2026-11-23). ราคา intraday ไม่ใช่ราคาปิด*

## Inputs จาก brief (ไม่ได้ค้นเพิ่ม)
ราคา $86.81 (intraday 11-24) | shares ~93.3M basic, guide non-GAAP diluted Q4 = 97.9M | net debt $242.1M (cash $251.4M, หนี้ $493.5M — PR 11-23) | Q3 rev $423.0M +58% YoY | Q3 FCF $55.5M (13.1%; Q2 $61.4M/17.8%) | Q4 guide rev $480M ±5, adj op margin 33.3% | FY28 data center >$1B = expectation ผู้บริหาร (แหล่งรอง ไม่ใช่ guidance) | FY30 framework (8-K 10-15): rev $3.2B, FCF 35% = $1.12B (target ไม่ใช่ guidance)

## Assumptions (ทุกตัวที่เป็นดุลยพินิจระบุ [ดุลยพินิจ])
- **FY27E FCF (base) = $240M [ดุลยพินิจ]** — Q2 $61.4M + Q3 $55.5M (จริง) + Q4E ~$67M (rev $480M x ~14% [ดุลยพินิจ]) = ~$184M + Q1 ที่ไม่มีใน brief (สมมติ ~$55M) — เป็นตัวเลขประมาณ ไม่ใช่ข้อมูลแหล่ง (รอบก่อนใช้ $280M; ลดลงเพราะ FCF margin Q3 ตกเป็น 13.1%)
- **FY30 FCF (Base) = $762M [ดุลยพินิจ]** — คง haircut เดิมจากรอบ 10-20 เพื่อเทียบกันได้: rev -15% จาก $3.2B = $2.72B x FCF margin 28% (เป้า 35%). เหตุผลคงเดิม: Q3 beat ด้าน revenue แต่ FCF margin จริงลดเหลือ 13.1% และ CFO เตือนต้นทุน capacity photonics + R&D → ไม่มีหลักฐานให้ยก margin; ก็ไม่มีเหตุลด rev เพราะ Q3/Q4 guide เหนือเส้นทาง
- **Growth fade FCF:** FY28 +47% ($353M) → FY29 +47% ($518M) → FY30 +47% ($762M) [interpolate เรขาคณิตจาก FY27E ไป FY30] → FY31 +18% ($899M) → FY32 +10% ($989M). เหตุผล: 3 ปีแรกผูกกับเส้นทางสู่ framework; FY31-32 fade ตาม mean-reversion ของธุรกิจโตเร็ว + การแข่งขัน Marvell/Broadcom ในปี data center [ดุลยพินิจ]
- **Terminal growth 3%** — บน moat ที่พิสูจน์แล้วเฉพาะ LoRa; data center ยังเป็นผู้ท้าชิง จึงไม่ใช้ >3% ใน Base
- **WACC 13.9% (คงเดิมจาก 10-20)** — 10Y ~5.07% (brief 11-19: 5.066%) + beta x ERP 5%; raw beta 5Y 2.35 (brief 10-20) ปรับเข้าหา 1 (Blume) ประมาณ 1.77 [ดุลยพินิจ] → 5.07% + 1.77x5% ≈ 13.9%. Net leverage ~0.4x จึงใช้ cost of equity ตรงๆ
- **Shares 97.9M** (diluted guide Q4) — ใช้ diluted เพราะ convert/SBC ไม่ใช่ 93.3M basic; framework FY30 ใช้ 104M (ทดสอบ sensitivity ด้านล่าง)
- **Net debt $242.1M** — ไม่รวมเงินสดจากการขาย cellular module (held for sale; assets $148.0M / liabilities $102.8M, ราคาขายไม่ทราบ) → ไม่นับ upside
- Timing: end-of-year convention, FY27 สิ้นสุดราว ม.ค. 2027 (~0.19 ปีจากวันนี้) → FY28 FCF discount t=1.19; Q4 FY27 FCF discount t=0.1

## DCF Calculation (Base, $M)
| ปีงบ | FCF | PV @13.9% |
|---|---|---|
| Q4 FY27E | 67 | 66 |
| FY28 | 353 | 302 |
| FY29 | 518 | 390 |
| FY30 | 762 | 503 |
| FY31 | 899 | 521 |
| FY32 | 989 | 503 |
- PV ของ FCF ทั้งหมด ≈ $2,285M
- Terminal value = 989 x 1.03 / (0.139-0.03) = $9,341M → PV $4,754M (**TV ~68% ของ EV**)
- EV ≈ $7,039M − net debt $242.1M = Equity $6,797M ÷ 97.9M = **$69.4/หุ้น**
- ถ้าใช้ 104M หุ้น (ตาม framework) → $65.4

## Fair Value
| Case | สมมติฐาน | FV/หุ้น |
|---|---|---|
| Bear | WACC 14.9%, g 2.5%, **และ** downside operating: rev -30% ($2.24B) x margin 24% = FY30 FCF $538M [ดุลยพินิจ] | **$43.3** |
| **Base** | WACC 13.9%, g 3%, FY30 FCF $762M | **$69.4** |
| Bull | WACC 12.9%, g 3.5%, บริษัททำได้ตาม framework 100% (FY30 FCF $1.12B) | **$117.9** |

เทียบรอบ 10-20: Base $64.3 → $69.4 (+8%) | Bear $33.7 → $43.3 | Bull $112.5 → $117.9. ที่เพิ่มขึ้นเกิดจาก net debt ลด ($338.3M→$242.1M), shares 104M→97.9M, และเวลาเลื่อนเข้าใกล้ปีเป้าหมาย ชดเชยกับ FY27E FCF ที่ลดลง ($280M→$240M)
ตัวเลขช่วย: เปลี่ยนเฉพาะ WACC/g (ไม่ปรับ operating) — Bear $60.8 / Bull-WACC เท่านั้น $80.8; ถ้าได้ framework 100% ที่ WACC 13.9%/g 3% = $101.2

## เทียบราคาปัจจุบัน $86.81
🔴 **Expensive** — ราคาสูงกว่า Base FV **+25.1%** (เกินเส้น 20% ไม่มาก → ใกล้ขอบ 🟡/🔴) | ต่ำกว่า Bull ($117.9) 26.4% | สูงกว่า Bear ($43.3) +100%
Market cap ที่ 97.9M หุ้น ≈ $8.5B (EV ≈ $8.74B)

## Reverse DCF (สั้น)
ที่ WACC 13.9%/g 3%/97.9M หุ้น และรูปทรงการโตเดิม ราคา $86.81 ต้องการ **FY30 FCF ≈ $957M** = สูงกว่า Base ของเรา +26% แต่ **ต่ำกว่าเป้า FCF บริษัท ($1.12B) ~15%** (≈ rev $3.2B ที่ margin ~30%, หรือ margin 35% ที่ rev ~$2.73B) ที่ WACC 12.9%/g 3.5% ต้องการ ~$820M
ความหมาย: ตลาดเชื่อประมาณ ~85% ของ framework FY30 (รอบ 10-20 ที่ $139.80 ต้องการ FCF สูงกว่าเป้า +33-49%) → ความคาดหวังที่ราคา price-in ลดลงมากแล้ว แต่ยังเกินระดับที่เราให้ (haircut 32%) และ FCF margin จริงวันนี้ (13.1%) ห่างจาก 35% มาก

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ⚪ ไม่มี coverage
- GuruFocus GF Value $47.97 (10-08 stale ไม่ refresh) — ต่ำกว่า Base ของเรา ~31%; GF เป็น historical-multiple regression ไม่คิด growth ใหม่ จึงล้าหลังบริษัทที่ rev โต +58%; ใกล้ Bear ($43.3) มากกว่า Base
- **สรุป:** Conquest Base ($69.4) อยู่ระหว่าง GF stale ($48) กับราคา ($86.81) และ Bull ($117.9) ต้องการให้บริษัททำตาม framework เต็ม 100% — ราคาปัจจุบันยัง 🔴 แต่ใกล้ขอบ; ผลไม่ทนทานต่อ assumption (TV ~68% EV)

## ข้อจำกัด
- FY27E FCF $240M เป็นประมาณ (ไม่มี Q1 FY27 ในไฟล์); ไม่ได้อ่าน 10-Q/transcript ต้นฉบับ — DC $145M และ FY28 >$1B มาจากแหล่งรอง และ**ไม่ได้ใส่ใน model โดยตรง** (model ผูกกับ FY30 framework + haircut)
- FCF ไม่ได้ปรับ SBC (ไม่มีตัวเลข SBC ใน brief) และไม่ได้รวมเงินจากขาย cellular module
- ราคา $86.81 intraday แกว่งได้ ±14-19%/วัน; DCF ไม่ใช่ price target / คำแนะนำซื้อขาย
