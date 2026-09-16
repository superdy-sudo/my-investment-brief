# 💰 Conquest DCF: AVGO — 2026-09-16
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — refresh ของ briefs/AVGO-conquest-2026-09-04.md*

## สรุปเหตุผลที่ refresh
ไม่มี earnings/10-Q ใหม่ตั้งแต่ Q3 FY2026 (~2026-09-04) — fundamentals ฝั่งบริษัท (FCF, growth trajectory, balance sheet) จึงคงเดิมทั้งหมด **สิ่งที่เปลี่ยนจริงคือปัจจัยตลาดสองอย่าง:**
1. ราคาหุ้นลดจาก $357.16 → **$339.27** (-5.0%) จาก sector-wide AI-safety sentiment selloff (ไม่ใช่ AVGO-specific)
2. **10Y Treasury yield พุ่งจาก 4.75% (3 ก.ย.) → ~5.01% (15 ก.ย.)** ทะลุ 5% ครั้งแรกตั้งแต่ปี 2007 จาก oil surge + inflation outlook — นี่คือ input อิสระต่อ WACC ที่ต้อง update แม้ไม่มี earnings ใหม่

## Assumptions
- **Base FCF (Year 0, TTM ~ สิ้นสุด Q3 FY2026):** ~$40.0B *(คงเดิมจาก 2026-09-04 — ไม่มี earnings ใหม่)*
  - ที่มา: GuruFocus TTM FCF ending Q2 FY2026 = $32.76B + Q3 FY2026 FCF จริง $13.7B (record, 46% margin) − Q3 FY2025 FCF ประมาณการ ~$6.0B ≈ **$40.0B**
- **Growth fade (ปี 1-5):** ปี1 35% → ปี2 25% → ปี3 18% → ปี4 12% → ปี5 8% *(คงเดิม — ยังไม่มีข้อมูลใหม่ที่กระทบ AI semi roadmap ของ Anthropic/OpenAI/Google/Meta)*
  - เหตุผล: law of large numbers เมื่อฐาน AI semi โตจาก ~$20B/ปี ไปสู่ >$80-100B ใน 3-4 ปี % growth ต้องลดลงตามกฎเลขคณิต + คู่แข่ง in-house chip ของ hyperscaler จะกดดันมากขึ้นปีหลังๆ
- **Terminal growth: 3%** *(คงเดิม)* — moat Cornered Resource (custom XPU IP) + Switching Cost (VMware) ยังแข็งแรงเหมือนเดิม ไม่มีเหตุผลใหม่ให้ปรับ
- **WACC: 12.1%** (เพิ่มจาก 11.8% เมื่อ 2026-09-04) — **ตัวขับเคลื่อนหลักคือ risk-free rate ที่พุ่งขึ้น ไม่ใช่ราคาหุ้น**
  - Risk-free rate: **5.00%** (10Y Treasury, ~15 ก.ย. 2026 ปิดที่ 5.01% — ทะลุ 5% ครั้งแรกตั้งแต่ ก.ค. 2007 จาก oil >$100/บาร์เรล + inflation risk) ← เปลี่ยนจาก 4.75%
  - Equity risk premium: 5.0% (คงเดิม)
  - Beta: 1.47 (คงเดิม, Yahoo Finance 5Y Monthly)
  - Cost of equity = 5.00% + 1.47×5.0% = **12.35%** (เพิ่มจาก 12.1%)
  - Cost of debt (after-tax, ประมาณ): ~3.56% (pretax ~4.5% เป็น embedded coupon เฉลี่ยของหนี้เดิม ไม่ใช่ต้นทุนหนี้ใหม่ — คงเดิม, tax 21%)
  - Weight: equity ~96.7% (market cap ~$1,654.3B ที่ราคา $339.27 × 4,876M diluted shares), debt ~3.3% (long-term debt $57.2B) — weight แทบไม่ขยับจากเดิม (96.8%→96.7%) เพราะ market cap ยังใหญ่กว่าหนี้มาก การเปลี่ยนราคาหุ้นแทบไม่กระทบ WACC
  - WACC = 0.967×12.35% + 0.033×3.56% ≈ **12.06%** ปัดเป็น **12.1%**
- **Diluted shares outstanding:** ~4,876M *(คงเดิม)*
- **Net debt:** $57.2B debt − $24.0B cash = **$33.2B net debt** *(คงเดิม)*

## DCF Calculation
| Year | Growth | FCF ($B) | Discount factor (12.1%) | PV ($B) |
|---|---|---|---|---|
| 1 | 35% | 54.00 | 0.8920 | 48.17 |
| 2 | 25% | 67.50 | 0.7958 | 53.72 |
| 3 | 18% | 79.65 | 0.7099 | 56.54 |
| 4 | 12% | 89.21 | 0.6333 | 56.49 |
| 5 | 8% | 96.34 | 0.5649 | 54.43 |

Sum of PV explicit FCF ≈ **$269.4B**

Terminal Value (Year 5) = 96.34 × 1.03 / (0.121 − 0.03) = **$1,090.5B**
PV of Terminal Value = 1,090.5 / 1.7702 = **$616.1B**

Enterprise Value = 269.4 + 616.1 = **$885.5B**
Equity Value = 885.5 − 33.2 (net debt) = **$852.3B**
Fair Value per share = 852.3B / 4.876B shares = **~$175**

## Fair Value
- Bear case (WACC 13.1%, terminal g 2.5%): **~$150**
- **Base case: ~$175**
- Bull case (WACC 11.1%, terminal g 3.5%): **~$209**

*(เทียบกับ 2026-09-04: Bear $155→$150, Base $181→$175, Bull $218→$209 — ลดลงทุกช่อง ~3-4% ล้วนมาจาก WACC ที่สูงขึ้นจาก 10Y yield พุ่ง ไม่ใช่จาก fundamentals ที่แย่ลง)*

## เทียบราคาปัจจุบัน $339.27
🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV ~93.9% (และสูงกว่าแม้แต่ Bull case FV ~62.3%)

**Implied Entry Zone (Base case):**
- Cheap ≤ ~$140
- Fair $140–$210
- Expensive > $210
- ราคา $339.27 อยู่เหนือ Expensive threshold มาก — ไม่เข้าเกณฑ์ Size-Up ตาม conquest DCF (เหมือนเดิมกับ 2026-09-04 แม้ราคาจะลดลง 5% ก็ตาม เพราะ WACC ที่สูงขึ้นหักล้าง fair value ที่ควรจะขยับตามราคาที่ถูกลง)

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $650** — ห่างจาก conquest base case มาก (~3.7x) เหตุผลเดิม: explicit forecast period ยาวกว่า (มักเป็น 10 ปี), terminal growth/WACC ที่เอื้อกว่าจาก wide-moat premium เต็มที่, ไม่ fade AI semi growth ลงเร็วเท่า assumption ของเรา — ยังไม่มีอะไรเปลี่ยนจาก 2026-09-04
- **GuruFocus GF Value $402.86 (ณ 2026-09-13)** — ขยับขึ้นจาก ~$343 เมื่อ 2026-09-04 (+17.5%) ขณะที่ราคาหุ้นลดลง (-5.0%) ทำให้ช่องว่างแคบลงมาก: ราคา $339.27 ต่ำกว่า GuruFocus FV เพียง **15.8%** (เดิมราคาสูงกว่า GuruFocus FV เล็กน้อย +4.1%) — GuruFocus จึงเลื่อนจากโซน "Fair/เฉียด Expensive" มาเป็น **"Fair" ที่ใกล้เกณฑ์ Cheap (20%) มากขึ้น** แต่ยังไม่ข้ามเกณฑ์
- **สรุป:** conquest ยังคง Expensive ชัดเจนที่สุดในสามแหล่ง (ราคาสูงกว่า base case เกือบ 94%) — ไม่เปลี่ยนทิศทางจาก 2026-09-04 เพราะ WACC ที่สูงขึ้นจาก 10Y yield หักล้างผลจากราคาหุ้นที่ถูกลง ทำให้ fair value ของเราเองก็ลดลงตาม (~$181→$175) ไม่ใช่ราคาไล่ตาม fair value เข้ามาใกล้

## Directional-agreement check: เปลี่ยนจาก 2026-09-04 หรือไม่?

**สรุปสั้น: ไม่เปลี่ยน — บทสรุป "ไม่เข้าเกณฑ์ Size-Up" ยังคงยืนตามเดิม แต่ margin ของ GuruFocus แคบลงจนควรจับตา**

รายละเอียด bucket ของแต่ละแหล่ง ณ ราคา $339.27:
| แหล่ง | Fair Value | ห่างจากราคา | Bucket |
|---|---|---|---|
| Morningstar | $650 | ราคาต่ำกว่า FV 47.8% | 🟢 Cheap |
| GuruFocus | $402.86 | ราคาต่ำกว่า FV 15.8% | 🟡 Fair (ไม่ถึงเกณฑ์ Cheap ที่ต้อง ≥20%) |
| Conquest (นี่) | $175 (base) | ราคาสูงกว่า FV 93.9% | 🔴 Expensive |

- 2026-09-04: GuruFocus (Fair, ราคาสูงกว่า FV เล็กน้อย +4.1%) + Conquest (Expensive) เห็นตรงกันว่า **"ไม่ Cheap"** → 2/3 โหวตค้าน Morningstar's Cheap → resolve เป็น "ไม่เข้าเกณฑ์ Size-Up"
- 2026-09-16: GuruFocus ยังคงเป็น **"ไม่ Cheap"** (Fair, 15.8% < เกณฑ์ 20%) + Conquest ยังเป็น Expensive → **บทสรุป 2/3 เดิมยังคงอยู่** ไม่เปลี่ยนทิศทาง
- **แต่มีสัญญาณเตือน:** GF Value ขยับขึ้น +17.5% ใน 12 วัน (เร็วกว่าปกติมาก) ขณะราคาหุ้นลดลง ทำให้ margin จาก "Fair" ไปสู่ "Cheap" แคบลงจาก ~16pp เหลือ ~4pp (15.8% ห่างจากเกณฑ์ 20% แค่ 4.2 จุด) — ถ้า GF Value ขึ้นต่อ หรือราคาหุ้นลงต่ออีกเล็กน้อย GuruFocus อาจข้ามเกณฑ์ไปเป็น Cheap ได้ ซึ่งจะทำให้เกิด 3-way split จริง (Morningstar Cheap, GuruFocus Cheap, Conquest Expensive) แทนที่จะเป็น 2-1 ที่ชัดเจนแบบตอนนี้ — ควร monitor GF Value รอบถัดไปใกล้ชิด

Sources:
- [US Stock Futures Drop as 10-Year Treasury Yield Passes 5%](https://www.bloomberg.com/news/articles/2026-09-15/us-stock-futures-drop-as-10-year-treasury-yield-passes-5)
- [Treasury Rates Today: September 15, 2026 - Forbes Advisor](https://www.forbes.com/advisor/investing/treasury-rates/)
