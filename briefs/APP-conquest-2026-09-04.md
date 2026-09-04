# 💰 Conquest DCF: APP (AppLovin) — 2026-09-04
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Raw Inputs (จาก 10-Q/earnings release, ไม่ใช่ "fair value" สำเร็จรูป)
- TTM Revenue (Q3'25 $1.40B + Q4'25 $1.658B + Q1'26 $1.84B + Q2'26 $1.924B) = **$6.82B**
- FCF margin (ตามที่ brief ระบุ) ~45% → **Base FCF = $3.07B**
- Diluted shares outstanding: **~336M** (335.94M common shares, stockanalysis.com)
- Cash (Q2'26 10-Q): $3.05B | Total debt: $3.52B → **Net debt ≈ $0.47B** (เกือบ net-cash, สอดคล้อง Net Debt/EBITDA ~0.1x ใน brief)
- Beta: **2.48** (stockanalysis.com — สูงกว่ากลุ่ม ad-tech ทั่วไปที่มักอยู่ 1.3-1.8x เพราะราคาหุ้นเพิ่งร่วงจาก ATH $745.61 → $297.50 ใน 52 สัปดาห์ ทำให้ historical-volatility beta สูงขึ้นผิดปกติ — ระบุเป็น caveat ด้านล่าง)
- 10Y Treasury yield: **~4.2%** (ปัจจุบัน)
- Growth trajectory จริง: Q3'25 +68% → Q4'25 +66% → Q1'26 +59% → Q2'26 +53% → Q3'26 guide +46-48% (deceleration ต่อเนื่อง ~6-8pp/ไตรมาส)

## Assumptions
**Growth fade (Stage 1, ปี 1-5):**
ปี1: 35% → ปี2: 26% → ปี3: 19% → ปี4: 13% → ปี5: 8%
เหตุผล: ต่อแนวโน้ม deceleration ที่เกิดขึ้นจริง 5-6 ไตรมาสติด (guide Q3 ~47% กำลังจะลงต่อผ่าน Q4); ตัวเลขปีที่ 1 ตั้งสูงกว่า guide ไตรมาสปัจจุบันเล็กน้อยเพราะเฉลี่ยทั้งปียังมีไตรมาสต้นปีที่โตแรงกว่าปนอยู่ mean-reversion มาตรฐานของธุรกิจ hyper-growth เมื่อ base สูงขึ้นเรื่อยๆ และคู่แข่งรายใหญ่ (Meta/Google/TikTok) มีโอกาส replicate algorithmic moat ตามที่ bear thesis สาธารณะชี้

**Terminal growth: 2.5%**
ผูกกับ long-run GDP/inflation มาตรฐาน — ไม่ให้ premium เพิ่มเพราะ moat เป็น "narrow, contested" (Morningstar + GuruFocus Moat Score 6/10) ไม่ใช่ wide moat ที่ยั่งยืนแน่นอน

**WACC: 16.6%** (cost of equity ตรงๆ เพราะ net debt เล็กน้อยเทียบ EV)
= Risk-free 4.2% + Beta 2.48 × ERP 5.0%
*Caveat: beta 2.48 สูงผิดปกติเพราะดึงจาก historical volatility ช่วงที่ราคาร่วงแรง หากใช้ beta ที่ conservative กว่า (1.5, ใกล้เคียง ad-tech peer เฉลี่ย) WACC จะลดเหลือ ~11.7% และ Fair Value ฐาน (growth/terminal เดิม) จะขยับขึ้นเป็น ~$207 — ยังต่ำกว่าราคาปัจจุบันอยู่ดี (~34%) แต่ bucket ยังเป็น Expensive ไม่เปลี่ยน*

## DCF Calculation (Base Case, WACC 16.6%, terminal g 2.5%)
| ปี | Growth | FCF ($B) | Discount Factor | PV ($B) |
|---|---|---|---|---|
| 1 | 35% | 4.145 | 0.858 | 3.56 |
| 2 | 26% | 5.222 | 0.736 | 3.84 |
| 3 | 19% | 6.214 | 0.631 | 3.92 |
| 4 | 13% | 7.022 | 0.541 | 3.80 |
| 5 | 8% | 7.584 | 0.464 | 3.52 |

Sum PV of Stage-1 FCF ≈ **$18.64B**
Terminal Value = 7.584 × 1.025 / (0.166 − 0.025) ≈ $55.13B → PV ≈ **$25.59B**
Enterprise Value ≈ $44.22B
− Net debt $0.47B → Equity Value ≈ **$43.76B**

## Fair Value (÷336M diluted shares)
- Bear case (WACC 17.5%, g 2.0%): **$119**
- **Base case (WACC 16.6%, g 2.5%): $130**
- Bull case (WACC 15.5%, g 3.0%): **$146**

## เทียบราคาปัจจุบัน $313.58
🔴 **Expensive** — ราคาสูงกว่า Base case FV ($130) ประมาณ **+141%**
(แม้ใช้ bull case สูงสุด $146 ราคาก็ยังสูงกว่า >100%)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV $360 — **ไกลจาก conquest base case มาก** ($130 vs $360, conquest ต่ำกว่า ~64%) เพราะ Morningstar ใช้ WACC ที่ต่ำกว่ามาก (ไม่ผูกกับ beta 2.48 ที่สูงผิดปกติจาก volatility ล่าสุด) และให้ terminal growth/moat premium สูงกว่า จาก wide-moat-adjacent assumption แม้ rating จริงจะเป็น narrow moat + Very High Uncertainty
- GuruFocus GF Value $508-576 — **ไกลที่สุด** เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ยังจับ growth rate ช่วงพีค (70-90% YoY) ก่อนหน้านี้ ไม่ทันปรับกับ deceleration 5-6 ไตรมาสล่าสุด และไม่ discount ความเสี่ยง moat/beta เหมือน DCF
- **สรุป:** Conquest **ไม่เห็นด้วยกับทั้งสองแหล่ง** — เป็นมุมมองอิสระที่เข้มที่สุดในสามแหล่ง เพราะ (1) ใช้ discount rate ที่สะท้อน beta/volatility จริงของหุ้นนี้ (2.48, สูงกว่าค่าเฉลี่ย ad-tech มาก) และ (2) ไม่ให้ terminal-growth premium กับ moat ที่ยังถูกโต้แย้งว่า narrow/replicable ตามที่ระบุใน memory ว่า conquest มี bias เอียงไปทาง Expensive โดยธรรมชาติจาก WACC/terminal-growth ที่ conservative — ควรอ่านผลนี้เป็น "มุมมองเข้มที่สุด" (stress case) ไม่ใช่คำตัดสินสุดท้าย โดยเฉพาะเมื่อ beta assumption เป็นตัวแปรที่อ่อนไหวสูงสุดในโมเดลนี้
