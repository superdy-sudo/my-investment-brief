# 💰 Conquest DCF: CIEN — 2026-09-18
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- **Base FCF (TTM, through Q3 FY26):** $832.66M on TTM revenue $5.57B (FCF margin ~14.95%)
- **Revenue growth fade (Stage 1, 5 ปี):**
  - ปี1: 33% → ปี2: 28% → ปี3: 18% → ปี4: 11% → ปี5: 6%
  - เหตุผล: TTM growth ปัจจุบัน ~37% (Q3 FY26 YoY) และ FY2027 prelim guidance ยืนยัน "+30%+" อีกแค่ 1 ปีข้างหน้า (ปี1-2 จึงยึดใกล้ guidance จริง) หลังจากนั้นต้อง fade แรงเพราะ (1) นี่คือ hardware capex supercycle ผูกกับ AI/hyperscaler data-center buildout ซึ่งเป็นวัฏจักร boom-bust ที่ Ciena เคยเจอมาแล้วหลายรอบ (dot-com bust, 2018-19 optical inventory correction) (2) Ciena TAM เองบอกไว้แค่ ~$25B วันนี้ → ~$50B ปี 2029 (~15% CAGR) — ถ้า revenue โต 35%+ ต่อเนื่องหลายปีเท่ากับแย่ง market share เกินจริงในเชิงคณิตศาสตร์ (3) Morningstar เองระบุชัดว่า Nokia-Infinera (vertically integrated) จะกัดส่วนแบ่ง ~50% US coherent optical ของ Ciena ในระยะยาว (4) mean-reversion ทั่วไป — ไม่มีบริษัท networking equipment รักษาการเติบโต >20% ได้เกิน 5 ปี
- **Terminal growth rate: 3%** — ผูกกับ long-run GDP/inflation ปกติ ไม่ให้ premium เพิ่มเพราะแม้ WaveLogic จะ first-to-market ต่อเนื่อง แต่ Morningstar เองให้ moat แค่ Narrow (อัพจาก None) ไม่ใช่ Wide/durable pricing power ระดับที่ควรได้ terminal growth สูงกว่าตลาดทั่วไป
- **FCF margin trajectory (Stage 1):** 16% → 17.5% → 19% → 19.5% → 20% — บริษัท guide adj operating margin ขยายจาก ~20% (FY26 Q4 guide) เป็น 25-27% (FY27 prelim) จาก operating leverage; FCF margin ตั้งไว้ต่ำกว่า adj op margin เสมอ (gap สำหรับ capex/cash tax/working capital) แต่ยังขยายตามทิศทางเดียวกัน
- **WACC: 11.5%** = risk-free rate 4.95% (10Y Treasury, 2026-09-18) + beta 1.31 (5Y monthly, จาก stock screener) × ERP 5% = 4.95% + 6.55%. ใช้ cost of equity ตรงๆ เพราะ Ciena เป็น net-cash position (debt $1.58B เทียบ market cap $48.4B บางเบามาก ไม่ปรับ weighted cost of debt อย่างมีนัยสำคัญ)
- **Shares outstanding:** 141.81M (diluted-adjacent, Sept 2026)
- **Net cash:** +$1,262.5M (cash+investments $2,843.5M − debt $1,581M)

## DCF Calculation ($M)
| ปี | Revenue | Growth | FCF margin | FCF |
|---|---|---|---|---|
| 0 (TTM) | 5,570 | — | 14.95% | 833 |
| 1 | 7,408 | 33% | 16.0% | 1,185 |
| 2 | 9,482 | 28% | 17.5% | 1,659 |
| 3 | 11,189 | 18% | 19.0% | 2,126 |
| 4 | 12,420 | 11% | 19.5% | 2,422 |
| 5 | 13,165 | 6% | 20.0% | 2,633 |

- Terminal Value (ปลายปี 5) = 2,633 × 1.03 / (0.115 − 0.03) = **$31,905M**
- PV of Stage-1 FCFs (discount @ 11.5%) = **$7,027M**
- PV of Terminal Value = **$18,508M**
- Enterprise Value = 7,027 + 18,508 = **$25,535M**
- + Net cash $1,263M → Equity Value = **$26,797M**
- ÷ 141.81M shares = **Fair Value ≈ $188.96/share**

## Fair Value
- Bear case (WACC 12.5%, terminal g 2.5%): **$162.68**
- **Base case: $188.96**
- Bull case (WACC 10.5%, terminal g 3.5%): **$226.41**

## เทียบราคาปัจจุบัน $341.30
🔴 **Expensive** — ราคาสูงกว่า Base case FV ~+80.6% (และสูงกว่าแม้แต่ Bull case ถึง +50.8%)

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $270** — สูงกว่า conquest base case ($188.96) ~+43% เพราะ Morningstar ใช้ 30x EV/adj.EBITDA 2026E (forward multiple ที่ผูกกับ moat upgrade เป็น Narrow) ซึ่ง implicitly ให้เครดิต margin expansion + market position สูงกว่าที่ conquest ให้ในเชิง cash-flow discounting ตรงๆ, และไม่ได้บังคับให้ growth fade ลงมาชนกับ TAM ceiling ใน terminal period แบบ DCF
- **GuruFocus GF Value $114.67** — ต่ำกว่า conquest base case ~-39% เพราะ GF Value เป็น backward-looking historical-multiple regression ที่คำนวณจาก valuation multiple เฉลี่ยในอดีตของ Ciena เอง (ตอนที่บริษัทยังโตช้ากว่านี้มาก และ margin ต่ำกว่านี้มาก) จึงไม่ได้ปรับให้ทันกับ margin expansion จริงที่กำลังเกิดขึ้น (adj op margin เพิ่งทำสถิติสูงสุดที่ 22.5% ใน Q3 FY26)
- **สรุป:** Conquest DCF อยู่ตรงกลางระหว่างสองแหล่ง แต่เอนไปทาง **เห็นด้วยกับ GuruFocus มากกว่า** ในทิศทาง (ราคาปัจจุบัน "แพงเกินพื้นฐาน") แม้ตัวเลขจะสูงกว่า GF Value อยู่พอสมควร เพราะ conquest ให้เครดิต margin expansion ที่กำลังเกิดขึ้นจริง (FCF margin fade ขึ้นถึง 20%) แต่ยังคง discipline ของ mean-reversion ใน growth rate และไม่ให้ terminal growth เกิน GDP-level แม้จะเป็น duopoly ที่มี TAM ceiling ชัดเจน (~$25-50B) — ต่างจาก Morningstar ที่ใช้ forward exit-multiple ซึ่งมีความเสี่ยงที่จะ "จ่ายล่วงหน้า" สำหรับ margin story ที่ยังพิสูจน์ความยั่งยืนไม่ได้เต็มที่ (เพิ่งทำสถิติสูงสุดแค่ 1 ไตรมาส)
