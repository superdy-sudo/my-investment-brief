# 💰 Conquest DCF: AVGO — 2026-09-04
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- **Base FCF (Year 0, TTM ~ สิ้นสุด Q3 FY2026):** ~$40.0B
  - ที่มา: GuruFocus TTM FCF ending Q2 FY2026 (Apr 2026) = $32.76B, บวก Q3 FY2026 FCF ที่รายงานจริง $13.7B (record, 46% margin), ลบ Q3 FY2025 FCF ประมาณการ ~$6.0B (revenue ปีก่อน ~$15.95B implied จาก +86% YoY, margin ~35-38% ก่อนช่วง AI ramp) → TTM ≈ $32.76B + $13.7B − $6.0B ≈ **$40.0B**
- **Growth fade (ปี 1-5):** ปี1 35% → ปี2 25% → ปี3 18% → ปี4 12% → ปี5 8%
  - เหตุผล: รายได้รวม guide Q4 +93% YoY / AI semi +236% YoY เป็นตัวเลขที่สูงเกินจะยั่งยืน — ส่วนหนึ่งมาจาก base effect (เทียบกับปีก่อนที่ยังเล็ก) และ VMware anniversary lapping ปี1 ยังได้แรงหนุนจาก committed roadmap ที่เปิดเผยแล้ว (Anthropic 1GW→5GW→10GW ถึง 2028, OpenAI 1.3GW→5GW+, Google LTA, Meta MTIA) แต่เมื่อฐานรายได้ AI semi โตจาก ~$20B/ปี annualized ไปสู่ >$80-100B ใน 3-4 ปี % growth ต้องลดลงตามกฎเลขคณิต (law of large numbers) + คู่แข่ง in-house chip ของ hyperscaler เองจะเข้ามากดดันมากขึ้นในปีหลังๆ
- **Terminal growth: 3%** (สูงกว่า GDP มาตรฐาน 2% เล็กน้อย) — เหตุผล: moat Cornered Resource (custom XPU IP) + Switching Cost (VMware) แข็งแรงและมี pricing power ต่อเนื่อง สมควรได้ premium เล็กน้อยเหนือ terminal ปกติ แต่ไม่สูงเกินไปเพราะเป็นธุรกิจ hardware/semi ที่ cyclical และเผชิญคู่แข่งระยะยาว
- **WACC: 11.8%**
  - Risk-free rate: 4.75% (10Y Treasury, 3 ก.ย. 2026)
  - Equity risk premium: 5.0% (มาตรฐานตลาด)
  - Beta: 1.47 (Yahoo Finance 5Y Monthly)
  - Cost of equity = 4.75% + 1.47×5% = 12.1%
  - Cost of debt (after-tax, ประมาณ): ~3.56% (pretax ~4.5%, tax 21%)
  - Weight: equity ~96.8% (market cap ~$1.74T ณ ราคา $357.16 × 4.876B diluted shares), debt ~3.2% (long-term debt $57.2B)
  - WACC = 0.968×12.1% + 0.032×3.56% ≈ **11.8%**
- **Diluted shares outstanding:** ~4,876M (weighted-avg diluted, Q3 FY2026 10-Q)
- **Net debt:** $57.2B debt − $24.0B cash = **$33.2B net debt**

## DCF Calculation
| Year | Growth | FCF ($B) | Discount factor (11.8%) | PV ($B) |
|---|---|---|---|---|
| 1 | 35% | 54.00 | 0.8945 | 48.30 |
| 2 | 25% | 67.50 | 0.8001 | 54.00 |
| 3 | 18% | 79.65 | 0.7156 | 56.99 |
| 4 | 12% | 89.21 | 0.6402 | 57.11 |
| 5 | 8% | 96.35 | 0.5727 | 55.17 |

Sum of PV explicit FCF ≈ **$271.6B**

Terminal Value (Year 5) = 96.35 × 1.03 / (0.118 − 0.03) = **$1,128.0B**
PV of Terminal Value = 1,128.0 / 1.7464 = **$645.9B**

Enterprise Value = 271.6 + 645.9 = **$917.4B**
Equity Value = 917.4 − 33.2 (net debt) = **$884.2B**
Fair Value per share = 884.2B / 4.876B shares = **~$181**

## Fair Value
- Bear case (WACC 12.8%, terminal g 2.5%): **~$155**
- **Base case: ~$181**
- Bull case (WACC 10.8%, terminal g 3.5%): **~$218**

## เทียบราคาปัจจุบัน $357.16
🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV ~97% (และสูงกว่าแม้แต่ Bull case FV ~64%)

**Implied Entry Zone (Base case):**
- Cheap ≤ ~$145
- Fair $145–$217
- Expensive > $217
- ราคา $357.16 อยู่เหนือ Expensive threshold มาก — ไม่เข้าเกณฑ์ Size-Up ตาม conquest DCF

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV ~$650-675** — ห่างจาก conquest base case มาก (~3.6x) แนวโน้มสาเหตุ: Morningstar (forward-DCF แบบ analyst) น่าจะใช้ explicit forecast period ยาวกว่า 5 ปี (มักเป็น 10 ปี) ที่ยอมให้ growth สูงต่อเนื่องนานกว่า fade schedule ของเรา, terminal growth/WACC ที่เอื้อกว่า (WACC ต่ำกว่าเพราะให้เครดิต wide moat เต็มที่), และอาจไม่ fade AI semi growth ลงเร็วเท่าที่ conquest สมมติ
- **GuruFocus GF Value ~$343** — ใกล้กับช่วง conquest มากกว่า Morningstar แต่ยังสูงกว่า base case ของเรา ~90% (ใกล้ bull case $218 มากกว่า base) เพราะ GuruFocus เป็น backward-looking historical-multiple regression ที่ยังจับ multiple expansion ช่วง AI boom ที่ผ่านมา ไม่ได้ fade growth ลงแรงเท่า assumption ของเรา
- **สรุป:** conquest เห็นด้วยทิศทางกับ GuruFocus (Expensive/Fair มากกว่า Cheap) มากกว่า Morningstar อย่างชัดเจน แต่ยังอนุรักษ์นิยมกว่า GuruFocus เองด้วยซ้ำ — ผลนี้สอดคล้องกับ pattern ที่เคยสังเกต (conquest DCF มักบอก Expensive เกือบทุกครั้งเพราะ WACC/terminal-growth ที่เลือกใช้ conservative โดยธรรมชาติ) จึงควรอ่านเป็น **"มุมมองที่เข้มที่สุดในสามแหล่ง"** ไม่ใช่คำตัดสินสุดท้ายเพียงลำพัง — แต่เมื่อรวมกับ GuruFocus แล้วมี 2/3 แหล่งเห็นตรงกันว่าราคาปัจจุบันไม่ถูก (Fair-to-Expensive) จึงเพียงพอที่จะคลี่คลาย "Valuation Inconclusive" เดิมไปทาง **ไม่เข้าเกณฑ์ Size-Up**
