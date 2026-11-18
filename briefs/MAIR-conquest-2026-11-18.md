# 💰 Conquest DCF: MAIR (Madison Air Solutions) — 2026-11-18
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — single-source case: ไม่มี Morningstar/GuruFocus FV*
ราคาอ้างอิง: $22.51 (ปิด Nov 17 2026, Yahoo ตาม brief) | ตัวเลข fundamental ทั้งหมดมาจาก briefs/MAIR-2026-11-18.md (Q3 2026 press release 2026-11-05)

## Assumptions
- **Base FCF (FY26E): ~$400M [ประมาณการ]** — ไม่มี TTM FCF ที่ยืนยันได้ในไฟล์ จึงประมาณเอง: FCF 9M26 จริง $298.0M บน sales $3,041.7M = margin 9.8% (คำนวณเอง) × FY26 sales guide midpoint $4,088M ($4,050–4,125M) ≈ $400M (ปัดลง; Q3 FCF จริง $158.0M แข็งกว่าเฉลี่ย แต่ปีก่อน margin ~13% → trend ลง จึงไม่ extrapolate ขึ้น)
- **Growth fade (FCF):** ปี1 (2027) 20% → ปี2 15% → ปี3 11% → ปี4 8% → ปี5 5%
  - เหตุผล: ปีแรกมี backlog $3,187M (+119% YoY, >70% ส่งมอบ 2027+) รองรับ แต่ orders ชะลอ 45%→26% และผู้บริหารคาด Q4 orders ลด YoY; margin ถูกกด (EBITDA margin 26.5% vs 28.0%) ผู้บริหารบอก "gradual repair" จึงไม่ให้ FCF โตเท่า sales; หลังจากนั้น fade ตามกฎ mean-reversion ของธุรกิจโตเร็ว. สมมติ FCF margin ~10% คงที่ ไม่มี margin expansion
- **Terminal growth: 3.0%** — ปลายบนของช่วงปกติ (2–3%) เพราะเป็น structural demand data-center/air quality แต่ moat ยังพิสูจน์ไม่ได้ (⚠️) จึงไม่เกิน 3%
- **WACC: 10.5% [ประมาณการ]** — risk-free 5.103% (10Y, brief 2026-11-18) + beta 1.3 × ERP 5.0% = cost of equity 11.6%; beta **เป็นการประมาณ** (IPO เม.ย. 2026 ประวัติราคาไม่ถึงปี ไม่มี beta ที่เชื่อถือได้; เลือก 1.3 สำหรับ industrial cyclical + data-center exposure); หนี้ $3,057M ≈ 19% ของโครงสร้างทุน (หนี้ / (หนี้ + mkt cap $13.3B)); cost of debt หลังภาษี ~5.5% (ประมาณ: 7% × (1−21%)) → WACC ≈ 0.81×11.6% + 0.19×5.5% ≈ 10.4% ปัดเป็น 10.5%
- **หุ้น: 592M** (รวม Class A+B, ตรงกับที่ใช้คำนวณ market cap; มี PIPE shares อยู่แล้ว) — sensitivity ด้วย 530M และ 597M ด้านล่าง
- **Net debt: $412M** = debt $3,057.0M − cash $2,645.2M (หลัก, Q3 26) ← cash นี้รวม PIPE $2.2B ที่ผูกกับดีล ebm-papst

## DCF Calculation (Base, $M)
| ปี | FCF | PV @10.5% |
|---|---|---|
| 2027 | 480.0 | 434.4 |
| 2028 | 552.0 | 452.1 |
| 2029 | 612.7 | 454.1 |
| 2030 | 661.7 | 443.9 |
| 2031 | 694.8 | 421.8 |
- PV Stage 1 รวม ≈ $2,206M
- Terminal value (ปี5) = 694.8 × 1.03 ÷ (10.5% − 3.0%) = $9,542M → PV ≈ $5,792M (≈72% ของ EV)
- EV ≈ $7,998M; − net debt $412M = Equity ≈ $7,586M ÷ 592M หุ้น = **$12.8/หุ้น**

## Fair Value
| Case | WACC | g | FV/หุ้น (592M) |
|---|---|---|---|
| Bear | 11.5% | 2.5% | $10.7 |
| **Base** | **10.5%** | **3.0%** | **$12.8** |
| Bull | 9.5% | 3.5% | $16.0 |

Sensitivity เรื่องจำนวนหุ้น (Base): 530M → $14.3 | 592M → $12.8 | 597M → $12.7 (Bear/Bull ที่ 530M = $11.9 / $17.9)

## เทียบราคาปัจจุบัน $22.51
🔴 **Expensive** — ราคาสูงกว่า Base FV ประมาณ **+76%** (22.51/12.8); สูงกว่า Bull case ($16.0) ราว +41% และสูงกว่าแม้ใช้ 530M หุ้น + Bull ($17.9) ราว +26% → ข้อสรุปไม่เปลี่ยนในทุก scenario ที่ลอง
- แต่ความมั่นใจในตัวเลขปานกลาง-ต่ำ: ผลไวต่อ Base FCF โดยตรง (FCF ±10% ≈ FV ±10%) และ FCF margin ถ้า expand เป็น ~13% (ระดับปีก่อน) จะดัน Base FV ขึ้นราว 30% (≈ $16.6) ก็ยังต่ำกว่าราคา

## ข้อจำกัด / สิ่งที่ DCF นี้ไม่ได้จับ
1. **ebm-papst ไม่รวมในโมเดล (standalone)** — ดีลยังไม่ปิด (คาดหลังสิ้นปี 2026); enterprise price $5.4B (14.6x 2026E adj EBITDA) ไม่มี pro forma FCF/leverage ที่ยืนยันได้ จึงไม่ forecast ดีล. การปฏิบัติ: คง cash PIPE ไว้ใน net debt และ PIPE shares ไว้ในจำนวนหุ้น (สอดคล้องกัน) = สมมติว่าดีลเป็น value-neutral (จ่ายราคาเต็ม). ถ้าดีลสร้างมูลค่า (synergy) FV จะสูงกว่านี้ ถ้าไม่ก็ต่ำกว่า — ไม่ทราบทิศทาง
2. **Dilution/จำนวนหุ้นไม่ชัด** — ไฟล์ระบุ 592M (รวม), diluted ~530M, ~597M หลังดีล (รอง); ตัวเลขชุดนี้ไม่ลงตัวกันเอง (597M หลังดีลเพิ่มจาก 592M เพียง ~5M ทั้งที่ financing ใช้ PIPE ~$2.25B) จึงแสดงช่วง 530–597M แทนการเลือกตัวเดียว
3. **Base FCF เป็นประมาณการ** ไม่ใช่ TTM จริง; FCF 9M ปีก่อน $312.4M → ปีนี้ $298.0M (ต่ำกว่า) ทั้งที่ sales +26%
4. **WACC/beta เป็นการประมาณ** (ไม่มีประวัติราคา) — WACC ±1% ร่วมกับ g ∓/±0.5% ขยับ FV ราว −$2.1/+$3.2
5. Terminal value ≈ 72% ของ EV → โมเดลพึ่ง assumption ระยะยาวมาก; ไม่มี Morningstar/GuruFocus FV ให้เทียบ

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบ | GuruFocus GF Value: ไม่พบ → **ไม่มีแหล่งให้เทียบ (single-source)** ผลนี้จึงใช้เป็นสัญญาณเดียว ห้ามยกระดับ Action เหนือ Watch ตามกฎเดิม
- (ตัวเลข analyst/Simply Wall St ใน brief ไม่ได้นำมาใช้ในการคำนวณ ตามกฎ)
- **สรุป:** DCF อิสระชี้ว่าที่ $22.51 ตลาดราคาเผื่อการเติบโตและ margin recovery มากกว่า fade schedule แบบระมัดระวังนี้ (FCF margin ~10%) ถึงราวสองในสาม; ตราบที่ยังไม่มีหลักฐานว่า margin ฟื้นหรือ ebm-papst สร้างมูลค่าเพิ่ม bucket = 🔴 Expensive
