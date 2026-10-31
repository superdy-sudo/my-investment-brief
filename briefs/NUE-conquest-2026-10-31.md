# 💰 Conquest DCF: NUE — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — cyclical steel: normalize กำไรข้ามวัฏจักรเป็น 3 scenario*

## Assumptions
- ราคา $273.87 (Oct 30 close, จาก brief) | diluted shares 226.7M (Q3'26) | net debt $3,453M | NCI ~$1,280M [หลัก — brief NUE-2026-10-31 / 8-K 2026-10-26]
- **Normalized earnings (3 scenario, เหตุผล: กำไร steel mills 9M swing 2.4x ตาม spread):**
  - Bear = 9M'25 annualized: EPS $5.88 (9M'25, 10-Q Q3'25 [หลัก]) x4/3 = $7.84 → NI ≈ $1.78B
  - Base = 9M'26 annualized: EPS $14.06 x4/3 = $18.75 → NI ≈ $4.25B (หมายเหตุ: 9M'26 รวม Helion gain $0.20 + refund $130M ใน Q2 ที่ไม่เกิดซ้ำ — ทำให้ base ออกสูงเล็กน้อย)
  - Bull = Q3'26 annualized: EPS $5.80 x4 = $23.20 → NI ≈ $5.26B (Q4 guide "in-line/modestly higher" รองรับว่า peak ยังไม่ตกทันที)
- **Base FCF = NI x 85%** [สมมติฐาน: 9M'26 FCF $2.66B เทียบ NI ~$3.2B ≈ 83%; capex 9M'26 $1.86B ยังสูงกว่า D&A เพราะ growth capex (WV sheet mill) — ปัดเป็น 85%]. FCF ปีฐาน: Bear $1,511M | Base $3,612M | Bull $4,471M
- **Growth fade (ปี1→5) — สะท้อน mean-reversion ของ spread ไม่ใช่การโตต่อเนื่อง:**
  - Bear: +3/+3/+3/+3/+3% (ฐานต่ำอยู่แล้ว โตตามปริมาณ capacity ใหม่)
  - Base: -12/-10/-6/0/+3% (spread ค่อยๆ ไหลกลับเข้าหาระดับกลางวัฏจักร ชดเชยบางส่วนด้วยปริมาณจาก capacity ใหม่; ปี5 FCF ≈ $2.77B ≈ EPS ~$12 ซึ่งอยู่ระหว่าง 9M'25 ($7.84) กับ 9M'26 ($18.75) [mid-cycle ประมาณ $13.3 = ค่าเฉลี่ยสองปี])
  - Bull: -2/-6/-6/-2/+2% (ราคาเหล็ก/tariff ประคอง spread สูงนาน)
- **Terminal growth 2.5%** (GDP/inflation ปกติ; ไม่ใส่สูงกว่านี้เพราะ moat ยืนยันข้ามวัฏจักรไม่ได้)
- **WACC 11.0%:** risk-free 4.929% (10Y, daily-brief 2026-10-31) + beta 1.4 [ประมาณการ ไม่ได้ดึงจริง — steel cyclical มักสูงกว่าตลาด] x ERP 5% = cost of equity 11.9%; น้ำหนักหนี้ ~10% (debt $7.1B vs mkt cap $62B) ต้นทุนหลังภาษี ~4.1% [ประมาณ] → WACC ≈ 11.0%

## DCF Calculation ($M, WACC 11.0%, g 2.5%)
| Scenario | FCF Y1 | Y2 | Y3 | Y4 | Y5 | PV Stage1 | TV (ปี5) | PV TV | EV | Equity (หัก ND+NCI) |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 1,556 | 1,603 | 1,651 | 1,700 | 1,751 | 6,069 | 21,119 | 12,533 | 18,602 | 13,869 |
| Base | 3,179 | 2,861 | 2,689 | 2,689 | 2,770 | 10,568 | 33,403 | 19,823 | 30,391 | 25,658 |
| Bull | 4,381 | 4,118 | 3,871 | 3,794 | 3,870 | 14,915 | 46,663 | 27,692 | 42,608 | 37,875 |

TV ≈ 65% ของ EV ในทุก scenario → ผลอ่อนไหวต่อ WACC/g มาก

## Fair Value (ต่อ share, ÷ 226.7M)
| Scenario | ตามด้านบน (11%/2.5%) | Sensitivity: WACC 12%/g 2.0% | WACC 10%/g 3.0% |
|---|---|---|---|
| Bear (9M'25 ann.) | **$61.2** | $49.9 | $77.2 |
| **Base (9M'26 ann.)** | **$113.2** | $95.3 | $138.5 |
| Bull (Q3'26 ann.) | **$167.1** | $142.1 | $202.5 |

ช่วงเต็ม (ทุก scenario x ทุก WACC/g): $50–$203

## เทียบราคาปัจจุบัน $273.87
🔴 Expensive — ราคาสูงกว่า Base FV $113 ≈ +142% (Base FV ต่ำกว่าราคา ≈ -59%); ราคายังสูงกว่า Bull ที่ดีที่สุดในกรอบ sensitivity ($203) ราว +35% → ราคาปัจจุบันสะท้อนการสมมติว่า Q3'26 EPS ($5.80/ไตรมาส) ยั่งยืนถาวร + discount rate ต่ำกว่า ~9%

ข้อควรระวังของ conquest นี้: (1) WACC 11% สูงจาก beta ที่ประมาณเอง — ถ้า beta 1.0/WACC ~9% ตัวเลข Base จะขยับขึ้นแต่ยังต่ำกว่าราคา (แนวโน้มจากช่วง sensitivity); (2) Bull ไม่ได้ใส่ผลของ buyback ต่อ per-share; (3) NCI ใช้ book value ~$1.28B

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่พบค่าปัจจุบัน (ตามที่ brief ระบุ) → เทียบไม่ได้
- GuruFocus GF Value: ไม่พบค่าปัจจุบัน → เทียบไม่ได้
- (บริบทเท่านั้น ไม่ใช่แหล่งตัดสิน) Simply Wall St analyst consensus ≈ $283.56 (13 Aug 2026) ใกล้ราคาตลาด แต่ห่างจาก conquest มาก เพราะ sell-side capitalize กำไร peak-spread
- **สรุป:** conquest ชี้ชัดว่าราคา $273.87 ไม่ถูกรองรับด้วยกำไรข้ามวัฏจักร — P/E ~11.8x บน Q3 annualized เป็น peak-cycle trap ตามที่ brief เตือน; ต้องเชื่อว่า spread ปัจจุบันถาวรจึงจะ justify ราคา

*Sources: brief NUE-2026-10-31 (8-K 2026-10-26 EX-99.1), Nucor 10-Q Q3'25 (SEC EDGAR; 9M'25 EPS $5.88). Beta, FCF conversion 85%, ภาษีต้นทุนหนี้ = สมมติฐาน*
