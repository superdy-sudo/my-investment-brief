# 💰 Conquest DCF: SNPS — 2026-10-02
*Independent bottom-up 2-stage DCF (Claude-only, คำนวณใหม่ทั้งหมดจาก RAW FUNDAMENTALS ใน briefs/SNPS-2026-10-02.md ไม่ reuse FV เก่า ไม่อิงตัวเลข fair value ของแหล่งอื่น)*

## Assumptions
- **ปี 1 = FY27 (ปีงบ ต.ค. 2027). Base FCF ปี 1: $2,945M** = FY27 FCF guide ~$3.1B (Investor Day 2026-10-01, press release/8-K) × 0.95 (haircut 5%)
  - เหตุผล haircut: (1) guide ผูกกับ margin non-GAAP 44% และ FCF ~27.8% ของ revenue $11.15B ซึ่งต้องพึ่งการ execute ของ Ansys synergies + IP/royalty ที่เพิ่งประกาศ (2) FCF ไม่หัก SBC (ไม่มีตัวเลข SBC ใน source) จึงเป็น FCF ที่ "สวย" กว่า owner-earnings (3) guide FY26 FCF ~$2.0B เดิมเคยขัดกับ actual 9mo $2.14B แสดงว่า guide ของบริษัทไม่แม่นยำสองทาง จึงไม่ใช้ตัวเลขเต็ม 100% เป็น base แต่แสดงเป็น sensitivity ด้านล่าง
- **Growth fade (FCF ปี 2-5 = FY28-FY31):** ปี2 17% → ปี3 14% → ปี4 11% → ปี5 8%
  - บริษัทตั้งเป้า FCF growth mid-20s% CAGR FY26-FY30 (revenue ~15% CAGR, non-GAAP margin 44% → ~50%). **Haircut ชัดเจน (เหลือ ~17% → 8% เทียบ ~25%)** เพราะ: (a) mid-20s% ส่วนใหญ่มาจาก margin expansion ซึ่งมีเพดาน (50% non-GAAP margin) ไม่ใช่ growth ยั่งยืน (b) organic revenue โตคงที่ ~15% ไม่ accelerate (FY25 +15.1% → FY27E +14.9%) (c) TAM บริษัทระบุ $31B vs revenue ~$9.7B, share 31-38% และเป็น duopoly กับ Cadence จำกัดพื้นที่โต (d) เป้าบริษัทเป็น target ไม่ใช่ actual — ใส่ conservative ใน base แล้วแสดงเป้าเต็มเป็น sensitivity
  - ปี2 17% = revenue ~14-15% + margin/FCF conversion ยังขยับขึ้นต่อ (44% → 50% target) ทั้งหมดนี้ลดหลั่นเข้าหา terminal
- **Terminal growth: 3.0%** — ขอบบนของช่วง 2-3% เพราะ Wide Moat (switching costs, duopoly, retention ใกล้ 100%) ไม่สูงกว่านี้เพราะ TAM/mkt cap เพียง 0.33x
- **WACC: 10.68%**
  - Risk-free 5.237% (10Y Treasury, daily brief 2026-10-02) + beta 1.22 (Yahoo, ยังไม่ re-verify) × ERP 5.0% (กลางช่วง 4-6%) = cost of equity 11.337%
  - Cost of debt ~4.5% หลังภาษี (interest 9mo $429.3M annualize ~$572M / debt $10,037M ≈ 5.7% pre-tax, ภาษี ~21% ประมาณการ)
  - น้ำหนักหนี้ $10.04B / ($10.04B + mkt cap $94.0B) = 9.6% → WACC = 0.904 × 11.337% + 0.096 × 4.5% = **10.68%**
- **Shares: 191.64M** (Webull 2026-10-01; SEC 10-Q ~189.6M ต่าง ~1%)
- **Net debt: $6,431.1M** (Debt $10,037.4M − Cash $3,606.3M, 10-Q 2026-07-31). ไม่ปรับ buyback ~$1B (ใช้เงินสด/หนี้ไปซื้อหุ้นคืน เป็นกลางต่อมูลค่า/หุ้นโดยประมาณ)
- Convention: discount แบบสิ้นปี (ปี 1 หาร (1+WACC)^1)

## DCF Calculation (Base: FCF ปี1 $2,945M, WACC 10.68%, g 3.0%)
| ปี | Growth | FCF ($M) | PV ($M) |
|---|---|---|---|
| 1 (FY27) | guide ×0.95 | 2,945 | 2,661 |
| 2 | 17% | 3,446 | 2,813 |
| 3 | 14% | 3,928 | 2,897 |
| 4 | 11% | 4,360 | 2,906 |
| 5 | 8% | 4,709 | 2,835 |

- PV ของ FCF ปี 1-5 = $14,112M
- Terminal value = 4,709 × 1.03 / (0.1068 − 0.03) = $63,175M → PV = $38,041M
- Enterprise Value = $52,153M
- Equity Value = 52,153 − 6,431 = $45,722M
- **FV/หุ้น = 45,722 / 191.64 = $238.6**
- TV คิดเป็น ~73% ของ EV (sensitivity ต่อ WACC/g สูง)

## Fair Value (3 scenario: WACC ±1%, terminal g ∓0.5%, growth schedule เดิม)
- Bear (WACC 11.68%, g 2.5%): **$196.1**
- **Base (WACC 10.68%, g 3.0%): $238.6**
- Bull (WACC 9.68%, g 3.5%): **$301.6**

### Sensitivity: Base FCF ปี 1 (fade เดิม + WACC/g ของแต่ละ scenario)
| FCF ปี1 (FY27) | Bear | Base | Bull |
|---|---|---|---|
| $2,600M (haircut ~16%) | $169.2 | $206.7 | $262.3 |
| **$2,945M (ที่เลือก, guide −5%)** | $196.1 | $238.6 | $301.6 |
| **$3,100M (FY27 FCF guide เต็ม)** | $208.2 | $252.9 | $319.2 |

### Sensitivity: ใช้เป้าบริษัทเต็ม (FCF ปี1 $3,100M แล้วโต 25%/ปี ปี 2-5 = mid-20s% CAGR ไม่ haircut)
| Bear | Base | Bull |
|---|---|---|
| $312.2 | $380.1 | $480.8 |

- แม้เชื่อ guide FY27 เต็ม + FCF โต 25% ทุกปีถึง FY31 + WACC/g แบบ bull = $480.8 ซึ่งยังต่ำกว่าราคา $490.54 เล็กน้อย → ราคาปัจจุบันสะท้อน "ทำได้ตามเป้าบริษัททุกข้อ + discount rate ต่ำกว่า bull" เท่ากับไม่มี margin of safety เหลือ
- Stress growth (ไม่อยู่ในตารางหลัก): growth ต่ำ (12→5%) + bear WACC/g = $168.0; growth สูง (20→10%, haircut น้อยกว่า) + bull WACC/g = $331.8
- Reverse check: ที่ WACC 8.0% + g 3% + fade base → $390.3; ต้องใช้ WACC ~7% + เป้าบริษัทเต็ม (25%) จึงได้ ~$797 → ราคา $490 อยู่ระหว่างสองกรณี หมายถึงตลาดสมมติ discount rate ~8% ขึ้นไปบวกเป้าบริษัท
- หมายเหตุ: FCF ไม่หัก SBC → owner-earnings FV จริงอาจต่ำกว่านี้อีก

## เทียบราคาปัจจุบัน $490.54 (ปิด 2026-10-01 หลัง Investor Day, +12.78%)
🔴 **Expensive** — ราคาสูงกว่า Base FV $238.6 อยู่ **+105.6%** (ราคา = 2.06x ของ base; FV base = 48.6% ของราคา)
- เทียบ Bull $301.6: ราคาสูงกว่า +62.6%
- เทียบ Bear $196.1: ราคาสูงกว่า +150.1%
- เทียบ case "guide เต็ม + 25% growth + bull WACC/g" $480.8: ราคาสูงกว่า +2.0%
- Bucket: 🔴 Expensive (เกณฑ์ >+20% เหนือ base)
- เทียบรอบ 09-30 (base $211.1, ราคา $423.23): FV ขึ้น +13% (FCF base สูงขึ้น, rf ต่ำลง 5.285% → 5.237%) แต่ราคาขึ้น +15.9% → gap กว้างขึ้นเล็กน้อย (+100.5% → +105.6%)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ยืนยันไม่ได้ (403) — ช่วงอ้างอิง $480-$520 (snippet/เก่า ไม่ verify) → conquest base ต่ำกว่า ~50-54% สาเหตุหลักคือ WACC 10.7% (rf 5.237% + beta 1.22) ที่สูงกว่า discount rate ที่ forward DCF ของนักวิเคราะห์มักใช้ + การ haircut เป้า FCF growth mid-20s% ของบริษัท
- GuruFocus GF Value $658.73 (ต่ำกว่า 25.5% → 🟢) — conquest base = 36% ของ GF Value; GF อิง historical multiples ไม่สะท้อน yield 10Y ที่ 5.2% (FCF yield ที่ guide FY27: 3.1/94.0 = 3.3% ต่ำกว่า risk-free)
- **สรุป:** conquest ยังอยู่ต่ำกว่าทั้งสองแหล่งมาก และไม่เห็นด้วยกับ GF Value; แม้รวม FY27 guide ใหม่ + เป้า LT ของบริษัทแบบไม่ haircut ได้แค่ ~$381 base / $481 bull → ราคา $490.54 แพงภายใต้ rf ปัจจุบัน ต้องเชื่อทุกเป้าบริษัทและ WACC ต่ำกว่า ~9.7% จึงเข้าใกล้ราคา ข้อจำกัด: DCF ไวต่อ WACC/g มาก (TV ~73% ของ EV) ใช้เป็นช่วง ไม่ใช่ตัวเลขแม่นยำ; AWS >$1B/OpenAI ไม่มีตัวเลข $ ที่ระบุแยกใน guide จึงไม่ได้ใส่เป็น upside เพิ่ม (ถือว่าอยู่ใน FY27 guide/LT model แล้ว)
