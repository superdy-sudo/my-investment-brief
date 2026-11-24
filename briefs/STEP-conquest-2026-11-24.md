# 💰 Conquest DCF: STEP (StepStone Group) — 2026-11-24
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — ฐานคือ FRE after-tax + realized carry แบบ normalize ไม่ใช้ GAAP FCF*

## Assumptions
- **ทำไมไม่ใช้ GAAP FCF:** TTM FCF -$817.6M (third-party) ผิดเพี้ยนจาก consolidated funds/การลงทุนใน fund (brief Layer 1) ไม่สะท้อน cash earnings → ใช้ FRE เป็นฐาน
- **Base FRE (annualized):** $440M [assumption] — ที่มา: FRE 6 เดือน FY27 $231.8M (จากไฟล์) x2 = $463.6M แล้ว haircut ~5% เพราะ CFO เตือน Q2 ($126.2M) มี fund closing catch-up + retro fees $4.2M (core FRE $122M) ไม่ใช่ run rate. ไม่มี TTM FRE ในไฟล์
- **Cash tax:** 22% [assumption — ไม่มีในไฟล์] → after-tax FRE ≈ $343M
- **Realized carry (normalized):** gross realized performance fees Q2 $65.1M (flat YoY) → ~$260M/ปี annualized; สมมติ net หลังหัก carry comp 35% [assumption] และหลังภาษี 22% ≈ $71M; **ลดน้ำหนัก 50%** เพราะ episodic → ≈ $35M. **ไม่นับ unrealized carry ($301.7M Q2) และ Greenspring legacy carry ($115M) เลย** (ไม่ให้นับซ้ำ; accrued carry $2.38B เป็น upside ไม่ใส่ใน base)
- **Base cash earnings (ปี 0): ≈ $378M** (343 + 35)
- **Growth fade:** ปี1 20% → ปี2 16% → ปี3 12% → ปี4 9% → ปี5 6%. เหตุผล: fee revenue +37% / FRE +61% Q2 มี catch-up เกินจริง; ฐานโครงสร้างคือ FEAUM +19%, management fees 6 เดือน +32%, UFEC $42.4B +42% (backlog fee) รองรับเริ่มต้น ~20%; แล้วลดหลั่นตามกฎ mean-reversion + ความเสี่ยง fee compression ใน private wealth/evergreen และคู่แข่ง KKR/Blackstone/Apollo (brief Layer 2 ข้อ 4)
- **Terminal growth:** 3.0% (สูงกว่าช่วงปกติ 2-3% เล็กน้อย เพราะ alternatives AUM โตเร็วกว่า GDP ในระยะยาว (Preqin ~$32T ปี 2030) แต่ moat ยังไม่ยืนยันจาก Morningstar จึงไม่ตั้งสูงกว่านี้)
- **WACC:** 12.0% = risk-free 5.07% (10Y Treasury 5.066% ณ brief 2026-11-19) + beta 1.4 [ประมาณ ไม่ใช่ตัวเลขจริง — alt asset manager มัก beta สูง ไม่พบในไฟล์] x ERP 5.0% = 12.07% ปัดเป็น 12.0%; net cash เกือบศูนย์ ใช้ cost of equity ตรงๆ
- **Net cash:** +$10.8M (cash $297.0M − debt $286.2M, 30 ก.ย. 2026, จากไฟล์) — ไม่รวมหนี้ consolidated funds
- **Shares:** ~120.8M (Webull, mkt cap $5.57B ÷ $46.11) **x dilution factor** จาก Private Wealth buy-in [assumption]: base 1.08 → **130.5M**, bear 1.12 → 135.3M, bull 1.04 → 125.6M. ที่มา: ไฟล์ระบุ share count implied +10.6% FY25→FY26 (ประมาณ), ไม่มี dividend พิเศษเพราะเก็บทุน buy-in ใช้ equity ได้สูงสุด 75%; ใช้ 8% สะสมเป็น haircut กลาง (ไม่ใช่ตัวเลขจริง)
- Dividend $1.32/ปี ไม่ได้แยกคิด (cash earnings ทั้งก้อนถือเป็นของผู้ถือหุ้นรวม)

## DCF Calculation (Base: WACC 12%, g 3%) — $M
| ปี | growth | Cash earnings | PV @12% |
|---|---|---|---|
| 1 | 20% | 453.6 | 405.0 |
| 2 | 16% | 526.2 | 419.5 |
| 3 | 12% | 589.3 | 419.5 |
| 4 | 9% | 642.4 | 408.2 |
| 5 | 6% | 680.9 | 386.4 |

- PV Stage 1 = $2,038.5M
- Terminal value = 680.9 x 1.03 ÷ (0.12 − 0.03) = $7,792M → PV = $4,422M (**TV = 68% ของ EV** — อ่อนไหวต่อ WACC/g สูง)
- EV ≈ $6,461M + net cash $10.8M = Equity ≈ $6,471M
- ÷ 130.5M shares = **$49.6/หุ้น**

## Fair Value
| Case | WACC | g | Dilution | Equity ($M) | FV/หุ้น |
|---|---|---|---|---|---|
| Bear | 13% | 2.5% | x1.12 | 5,604 | **$41.42** |
| **Base** | 12% | 3.0% | x1.08 | 6,471 | **$49.6** |
| Bull | 11% | 3.5% | x1.04 | 7,681 | **$61.14** |

(growth fade ใช้ชุดเดียวกันทุก case — range นี้สะท้อน discount rate/terminal/dilution เท่านั้น ยังไม่รวมความเสี่ยงที่ FRE โตต่ำกว่าที่สมมติ)

## เทียบราคาปัจจุบัน $46.15
🟡 Fair — ราคาต่ำกว่า Base case FV **-7.0%** (อยู่ในช่วง ±20%); สูงกว่า Bear +11%, ต่ำกว่า Bull -25%

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบ (brief ระบุ quantitative rating ไม่มีตัวเลข) — เทียบไม่ได้
- GuruFocus GF Value ~$86 (implied, single-source, regression + GAAP EPS ติดลบ + flag Value Trap): ไกลกว่า conquest base +73% — GF Value อิงมัลติเพิลย้อนหลัง/ไม่ได้ตัด carry ที่ไม่ใช่เงินสด จึงสูงเกินจริง; ต่ำกว่า bull case ของ conquest ด้วยซ้ำที่ $61
- (ข้อมูลประกอบ ไม่ใช่ FV) Analyst target เฉลี่ย ~$64.60 ใกล้ bull case ของ conquest
- **สรุป:** conquest อยู่ใกล้ราคาตลาดมากกว่า GF Value — ราคา $46.15 สะท้อนมูลค่าธุรกิจ fee-based ที่เหมาะสมโดยไม่มี margin of safety ชัดเจน; upside ต้องพึ่ง realized carry จาก accrued carry $2.38B ซึ่งไม่ได้นับใน base

## ข้อจำกัด
Base FRE/tax/carry comp ratio/beta/dilution เป็น assumption ทั้งหมดที่ระบุไว้ข้างบน (ไม่มีใน brief); ไม่มี TTM FRE และ 10-Q cash flow ยืนยัน; moat ยังไม่ยืนยันจาก Morningstar
