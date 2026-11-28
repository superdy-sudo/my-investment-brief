# 💰 Conquest DCF: APP (AppLovin) — 2026-11-28
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Raw Inputs (จาก brief 11-28 / 8-K Q3'26)
- TTM Revenue = Q4'25 $1.658B + 9M'26 $5.951B = **$7.61B**
- FCF: Q3'26 ~$1.4B (~64% margin, ตัวเลขปัด) แต่ไม่ได้ดึง FCF TTM จาก 10-Q → **สมมติ FCF margin TTM 55%** (Q3 64% สูงกว่า ~45% ที่ใช้ใน conquest 09-04; ถ่วงเฉลี่ย 4 ไตรมาสจึงอยู่กลางๆ — เป็นการประมาณ ไม่ใช่ตัวเลขจริง) → **Base FCF = $4.19B**
- Net debt ≈ $0.34B (cash $3.174B, debt $3.516B ณ 30 ก.ย.) | Shares 331M
- Q4'26 guide revenue +43-44% YoY | ราคา $399.21 (ปิด 11-27)
- Risk-free ~4.2% (ยกจาก conquest 09-04 ไม่ได้ดึงใหม่ — สมมติ), ERP 5.0%

## Assumptions
- **Growth fade (revenue = FCF growth, margin คงที่):** ปี1 38% → ปี2 28% → ปี3 20% → ปี4 14% → ปี5 8%
  เหตุผล: Q4 guide +43-44% (guide มัก conservative, Q3 ชนะ guide ~$100M) แต่ base ใหญ่ขึ้นและเคยชะลอต่อเนื่อง; ปี1 เฉลี่ยทั้งปีจึงตั้ง 38% (สูงกว่า 09-04 ที่ 35% เพราะ Q3 reaccelerate); ปีหลังใช้ mean-reversion มาตรฐาน + ความเสี่ยง Meta/Google/TikTok replicate algorithm
- **Terminal growth 2.5%** (GDP/inflation; moat ยัง narrow + contested จึงไม่ให้ premium)
- **Beta (โปร่งใส):** raw 2.48 [stockanalysis ณ 09-04, ไม่ได้ re-check] ถูกดันโดย volatility ช่วงร่วงจาก ATH; Base ใช้ **Blume-adjusted ≈ 2.0** (0.67×2.48+0.33) เป็นทางสายกลาง; เทียบ sensitivity ที่ 2.48 และ 1.5
- **WACC base = 4.2% + 2.0×5.0% = 14.2%** (cost of equity ตรงๆ เพราะ net debt เล็ก)

## DCF Calculation (Base: WACC 14.2%, g 2.5%, FCF base $4.19B)
| ปี | Growth | FCF ($B) | DF | PV ($B) |
|---|---|---|---|---|
| 1 | 38% | 5.78 | 0.876 | 5.06 |
| 2 | 28% | 7.39 | 0.767 | 5.67 |
| 3 | 20% | 8.87 | 0.671 | 5.96 |
| 4 | 14% | 10.11 | 0.588 | 5.95 |
| 5 | 8% | 10.92 | 0.515 | 5.62 |

Sum PV Stage-1 ≈ $28.25B | TV = 10.92×1.025/(0.142−0.025) ≈ $95.7B → PV ≈ $49.27B
EV ≈ $77.5B − net debt $0.34B → Equity ≈ $77.2B ÷ 331M

## Fair Value
- Bear (WACC 16.2%, g 2.0%): **$192**
- **Base (WACC 14.2%, g 2.5%): $233**
- Bull (WACC 12.2%, g 3.0%): **$297**

## Sensitivity เพิ่มเติม (g 2.5%, growth fade เดิม)
| Beta | WACC | FV @FCF margin 50% | 55% | 60% |
|---|---|---|---|---|
| 2.48 (raw) | 16.6% | $173 | $190 | $208 |
| 2.0 (base) | 14.2% | $212 | $233 | $254 |
| 1.5 (peer-like) | 11.7% | $274 | $302 | $329 |

แม้ beta 1.5 + FCF margin 60% (กรณีเข้าข้างที่สุด) FV ≈ $329 ยังต่ำกว่าราคา $399

## เทียบราคาปัจจุบัน $399.21
🔴 **Expensive** — ราคาสูงกว่า Base FV ($233) ประมาณ **+71%** (ราคาสูงกว่า Bull $297 ~+34%)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV $360 (ไม่ update หลัง Q3) — conquest base ต่ำกว่า ~35%; Morningstar ใช้ discount rate ต่ำกว่าและ terminal assumption สูงกว่า; ราคา $399 ใกล้ MS มากกว่า conquest
- GuruFocus GF Value $591.88 (เก่า ~2 เดือน) — ไกลที่สุด (backward-looking, จับ growth ช่วงพีค)
- **สรุป:** FV conquest ขยับขึ้นจาก $130 (09-04) เป็น $233 เพราะ FCF base สูงขึ้น (margin 64% Q3, TTM ~55% สมมติ), growth reaccelerate, และใช้ beta ปรับ (2.0 แทน 2.48); ยังเป็นมุมมองเข้มกว่าทั้งสองแหล่ง ควรอ่านเป็น stress/conservative case ไม่ใช่คำตัดสิน — ตัวแปรอ่อนไหวสุดคือ beta/WACC และ FCF margin TTM ที่ยังไม่ได้ยืนยันจาก 10-Q
