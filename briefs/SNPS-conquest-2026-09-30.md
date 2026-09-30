# 💰 Conquest DCF: SNPS — 2026-09-30
*Independent bottom-up 2-stage DCF (Claude-only, คำนวณใหม่ทั้งหมดจาก RAW FUNDAMENTALS ใน briefs/SNPS-2026-09-30.md ไม่ reuse FV เก่า ไม่อิงตัวเลข fair value ของแหล่งอื่น)*

## Assumptions
- **Base FCF (FY26E): $2,400M** — ค่ากลางที่เลือกเองระหว่างสองเลขที่ขัดกัน: guidance ~$2.0B (ต่ำกว่า 9mo actual $2.14B จึงน่าจะ stale/conservative) กับ 9mo annualized $2,142.5M / 0.75 = $2,857M (ประเมินสูงเกินถ้า Q4 ตามฤดูกาลอ่อนกว่า และ 9mo อาจรับประโยชน์ timing ของ working capital) ตั้ง $2.4B = ≈ 25% ของ revenue guide $9.69-9.74B ซึ่งต่ำกว่า 9mo margin 29.9% อย่างตั้งใจ (haircut ความไม่แน่นอน + FCF ไม่หัก SBC)
- **Growth fade (FCF):** ปี1 15% → ปี2 14% → ปี3 12% → ปี4 10% → ปี5 8%
  - เหตุผล: Ansys lap เสร็จหลัง FY26 → revenue โตลงมา double-digit ตามที่บริษัทระบุ (long-term model) ส่วนประมาณการภายนอก ~14% CAGR ถึง FY2030 เป็นแค่ Tier 5 ใช้อ้างอิงทิศทาง; FCF โตเร็วกว่า revenue เล็กน้อยใน 2-3 ปีแรกจาก synergies ($400M สะสมภายปี 4) + revenue synergy $400M เริ่ม FY27 + ดอกเบี้ย/integration cost ลดลง; ลดหลั่นเข้าหา terminal เพราะ TAM/ราคาบริษัทระบุ $31B (ขณะที่ revenue ~$9.7B, share 31-38%) จำกัดพื้นที่โต และ duopoly กับ Cadence
- **Terminal growth: 3.0%** — ขอบบนของช่วงปกติ 2-3% เพราะ Wide Moat (switching costs, retention ~ใกล้ 100%, duopoly) แต่ไม่สูงกว่านี้เพราะ TAM/mkt cap เพียง 0.38x
- **WACC: 10.63%**
  - Risk-free 5.285% (10Y, daily brief 2026-09-30) + beta 1.22 (Yahoo, ยังไม่ re-verify วันนี้) × ERP 5.0% (กลางของช่วง 4-6%) = cost of equity 11.385%
  - Cost of debt: interest 9mo $429.3M annualize $572M / debt $10,037M ≈ 5.7% pre-tax → after-tax ~4.5% (ภาษี ~21% ประมาณการ)
  - น้ำหนัก: debt $10.04B / (debt + mkt cap $81.1B) ≈ 11% → WACC = 0.89 × 11.385% + 0.11 × 4.5% ≈ **10.63%**
- **Diluted shares: 191.64M** (Webull totalShares 2026-09-30; SEC 10-Q ~189.6M — ต่างกัน ~1% ไม่มีนัยสำคัญ)
- **Net debt: $6,431.1M** (Debt $10,037.4M − Cash $3,606.3M, 10-Q 2026-07-31) → ลบออกจาก EV

## DCF Calculation (Base: FCF0 $2,400M, WACC 10.63%, g 3.0%)
| ปี | Growth | FCF ($M) | PV ($M) |
|---|---|---|---|
| 1 | 15% | 2,760 | 2,495 |
| 2 | 14% | 3,146 | 2,571 |
| 3 | 12% | 3,524 | 2,603 |
| 4 | 10% | 3,876 | 2,588 |
| 5 | 8% | 4,186 | 2,526 |

- PV ของ FCF ปี 1-5 = $12,782M
- Terminal value = 4,186 × 1.03 / (0.1063 − 0.03) = $56,515M → PV = $34,103M
- Enterprise Value = $46,885M
- Equity Value = 46,885 − 6,431 = $40,454M
- **FV/หุ้น = 40,454 / 191.64 = $211.1**
- TV คิดเป็น ~73% ของ EV (พึ่ง terminal สูง → sensitivity ต่อ WACC/g สูง)

## Fair Value (3 scenario: ปรับ WACC ±1%, terminal g ±0.5%, growth schedule เดิม)
- Bear (WACC 11.63%, g 2.5%): **$172.9**
- **Base (WACC 10.63%, g 3.0%): $211.1**
- Bull (WACC 9.63%, g 3.5%): **$267.9**

### Sensitivity ของ Base FCF (ใช้ fade + WACC/g ของแต่ละ scenario เดิม)
| Base FCF | Bear | Base | Bull |
|---|---|---|---|
| $2,000M (guidance) | $138.5 | $170.3 | $217.7 |
| **$2,400M (ที่เลือก)** | $172.9 | $211.1 | $267.9 |
| $2,857M (9mo annualized) | $212.1 | $257.7 | $325.3 |

- แม้ใช้ตัวเลขที่เอื้อที่สุด (9mo annualized + bull WACC/g) FV = $325.3 ยังต่ำกว่าราคา $423.23 ~23%
- Stress เพิ่ม (ไม่อยู่ในตาราง): ถ้าเปลี่ยน growth schedule ด้วย — bear growth (10→6%) + bear WACC/g = $143.4; bull growth (18→10%) + bull WACC/g = $296.1 (base FCF $2.4B)
- หมายเหตุ: FCF ที่ใช้ไม่หัก SBC (ไม่มีตัวเลข SBC ใน raw fundamentals) → FV จริงแบบ owner-earnings อาจต่ำกว่านี้อีก

## เทียบราคาปัจจุบัน $423.23 (2026-09-30 13:00 ET)
🔴 **Expensive** — ราคาสูงกว่า Base FV $211.1 อยู่ **+100.5%** (ราคา = 2.00x ของ base; FV base = 49.9% ของราคา)
- เทียบ Bull $267.9: ราคาสูงกว่า **+58.0%** (ราคา = 1.58x ของ bull)
- เทียบ Bear $172.9: ราคาสูงกว่า +144.8%
- Bucket: 🔴 Expensive (เกณฑ์ >+20% เหนือ base)

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: $480 (ยืนยันไม่ได้ อาจเก่าจากปี 2024) หรือ ~$379 (snippet ไม่ verify) — conquest base ต่ำกว่า 56%/44% ตามลำดับ; สาเหตุน่าจะเป็น WACC 10.6% ที่สูง (rf 5.285% ระดับสถิติใหม่ + beta 1.22) และการไม่ให้ premium ต่อ growth/synergies ระยะยาว ขณะที่ forward DCF ของนักวิเคราะห์มักใช้ discount rate ต่ำกว่า
- GuruFocus GF Value $658.56: ห่างมาก (conquest base = 32% ของ GF Value) — GF Value อิง historical multiples (ช่วงที่ SNPS เทรดที่ multiple สูง) ไม่ได้สะท้อน yield 10Y ที่ 5.3% ส่วน FCF yield ปัจจุบัน = 2.4/81.1 = 3.0% (ต่ำกว่า risk-free)
- **สรุป:** conquest อยู่ต่ำกว่าทั้งสองแหล่ง และไม่เห็นด้วยกับ GF Value ที่ 🟢 Cheap เลย — ที่ราคา $423 ตลาดกำลังตีราคา SNPS ด้วย implied discount rate ต่ำกว่ามาก (ต้องการ growth/margin สูงกว่า fade นี้ หรือ WACC ~7-8%) ความต่างนี้ไวต่อ WACC มาก จึงควรอ่านเป็น "ราคาแพงภายใต้ rf ปัจจุบัน" มากกว่าเป็นตัวเลขแม่นยำ; ข้อจำกัด: Investor Day (2026-09-30) ยังไม่สะท้อนในราคา/สมมติฐาน (เช่น TAM หรือ LT target ใหม่)
