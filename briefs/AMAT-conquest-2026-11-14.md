# 💰 Conquest DCF: AMAT — 2026-11-14
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — ราคา T-1 (Nov 13) $362.54*

## Assumptions
- **Base FCF:** FY26 non-GAAP FCF $6,196M (18.0% margin บน revenue $34,446M) — แหล่ง: brief AMAT-2026-11-14 (Applied PR 2026-11-12)
- **วิธีสร้าง FCF:** revenue x FCF margin (แทนการ fade FCF ตรงๆ) เพราะเป็น cyclical WFE — margin รายปีผันผวนมาก (FY25 20.1%, FY26 18.0%, Q4 FY26 25.1%)
- **Revenue growth fade (Base):** FY27 +28% → FY28 +10% → FY29 +6% → FY30 +6% → FY31 +5%
  - FY27 ($44.1B): Q1 guide $11.1B (14 สัปดาห์ — ยังไม่ยืนยันกับ filing) + mgmt อ้าง WFE CY2027 >+30% → ปรับลดเพราะ Q1 มี สัปดาห์ที่ 14 ช่วย (รายสัปดาห์ ≈ แบนเมื่อเทียบ Q4) และ supply/clean-room เป็นคอขวด
  - FY28-31: เฉลี่ยข้าม cycle — WFE เป็นวัฏจักร มักมีปีถอย/ชะลอหลังปีพีค จึงใส่ +10% แล้ว +5-6% (ต่ำกว่า CAGR ที่ mgmt วาดจาก AI/HBM/adv. packaging) เพื่อไม่ capitalize ยอดพีคเป็นถาวร
- **FCF margin (Base): 20% คงที่** — เท่า FY25 (20.1%) และสูงกว่า FY26 เล็กน้อย; ไม่ใช้ 25% ของ Q4 เพราะเป็นไตรมาสพีค/ได้ working-capital timing
- **Terminal growth:** 3.0% — บน cap ของช่วง 2-3% เพราะ moat กว้างและ AGS (installed base) โตต่อเนื่อง แต่ยังไม่เกิน nominal GDP
- **WACC:** 11.9% = risk-free 5.13% (10Y UST 5.127% ตาม daily brief 2026-11-13) + beta 1.5 x ERP 4.5%
  - **Beta 1.5 = ค่าประมาณ** (ไม่ได้ดึงตัวเลขจริง; semi-equipment beta ทั่วไป 1.4-1.7 + 52wk range $203-$740 สะท้อนความผันผวนสูง) | บริษัท net cash → ใช้ cost of equity ตรงๆ
  - หมายเหตุ: risk-free 5.1% สูงมาก ทำให้ WACC สูง — เป็นตัวกดมูลค่าหลัก
- **Shares:** ~793.6M (Webull; ตาม brief — ไม่ใช่ diluted เป๊ะ)
- **Net cash:** +$7.56B (cash+inv $14.095B − debt $6.532B ณ 2026-10-25)

## DCF Calculation (Base, $B)
| ปี | Revenue | FCF (20%) | PV @11.9% |
|---|---|---|---|
| FY27 | 44.1 | 8.82 | 7.88 |
| FY28 | 48.5 | 9.70 | 7.75 |
| FY29 | 51.4 | 10.28 | 7.34 |
| FY30 | 54.5 | 10.90 | 6.95 |
| FY31 | 57.2 | 11.44 | 6.52 |

- PV Stage 1 = $36.4B
- Terminal value = 11.44 x 1.03 / (0.119 − 0.03) = $132.4B → PV = $75.5B
- Enterprise Value = $111.9B | + net cash $7.56B = Equity $119.5B
- Fair Value/share = $119.5B / 0.7936B = **~$151**
- (Terminal value = ~67% ของ EV)

## Fair Value
| Scenario | WACC | g | FCF margin | Growth FY27-31 | FV/share |
|---|---|---|---|---|---|
| Bear | 12.9% | 2.5% | 17% | +22/+3/−2/+5/+4% (มีปีถอยแบบ cyclical) | **$96** |
| **Base** | 11.9% | 3.0% | 20% | +28/+10/+6/+6/+5% | **$151** |
| Bull | 10.9% | 3.5% | 22→23% | +32/+14/+8/+7/+6% | **$221** |

Sensitivity เฉพาะ WACC/g (operating case = Base): WACC 12.9% → $136 | WACC 10.9% → $169 | g 2.5% → $145 | g 3.5% → $157. ผลต่อ WACC/g อย่างเดียวค่อนข้างแคบ; ความไม่แน่นอนหลักอยู่ที่ margin และ cycle.

## เทียบราคาปัจจุบัน $362.54
🔴 **Expensive** — ราคาสูงกว่า Base FV ~+140% (Base FV ต่ำกว่าราคา ~58%); แม้ Bull case ($221) ราคายังสูงกว่า ~+64%

ความมั่นใจ: ปานกลาง-สูงในทิศทาง (ทั้ง 3 scenario ต่ำกว่าราคา) แต่ระดับตัวเลขขึ้นกับ WACC สูง (risk-free 5.1%, beta ประมาณ) และการเลือก FCF margin 20% — ตลาดกำลังตีราคาที่ต้องมี margin/growth พีคนานกว่าสมมติฐานนี้มาก หรือ discount rate ต่ำกว่า 10% ซึ่งควรดูเป็นข้อโต้แย้งฝั่ง bull. หลักฐานเชิงวัฏจักร: หุ้นลงจาก $740 → ~$333 → $362 ภายใน ~1 เดือน แสดงว่าตลาดเองก็ไม่แน่ใจ.

## เทียบกับ Morningstar/GuruFocus (หลังคำนวณเสร็จ — ไม่ได้ใช้ในสมการ)
- Morningstar FV $520 — ไกลมาก (conquest Base ต่ำกว่า ~71%); ต่างที่ Morningstar ใช้ forward mid-cycle margin/EPS ที่สูงกว่าและ discount rate ต่ำกว่า (conquest ใช้ WACC 11.9% จาก risk-free 5.1%) + นับ growth ถึง 2030 โดยไม่ดึง cycle ลง
- GuruFocus GF Value $253.05 (stale Oct 6) — ไกลกว่า conquest ~+68% (conquest ต่ำกว่า); stale ก่อน Q4 beat และก่อนราคาร่วง จึงอ้างอิงได้จำกัด
- **สรุป:** conquest อยู่ต่ำกว่าทั้งสองแหล่ง และต่ำกว่าราคาตลาดอย่างมีนัยสำคัญ — เห็นด้วยกับ "ตลาดแพง" มากกว่า Morningstar; ช่องว่างส่วนใหญ่มาจาก WACC สูง + margin 20% ปรับตามวัฏจักร ซึ่งเป็นสมมติฐานเชิงอนุรักษ์ที่ควรระบุเมื่อใช้ตัดสิน
