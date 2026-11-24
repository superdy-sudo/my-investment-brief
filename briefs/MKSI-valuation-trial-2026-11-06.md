# MKSI — ทดลองคำนวณ Fair Value เอง 2 วิธี (2026-11-06) | ราคา $185.37 [หลัก — price_check/Yahoo intraday]

> ทดลองเท่านั้น: "MS-style estimate" และ "GF-style estimate" เป็นการจำลองวิธีคิดโดย Claude — **ไม่ใช่ตัวเลข Morningstar / GuruFocus จริง** และไม่ใช่คำแนะนำซื้อ/ขาย
> ป้าย: [หลัก]=filing/Yahoo/SEC ตรง | [รอง]=aggregator | [สมมติฐาน]=เราตั้งเอง | [คำนวณ]=คำนวณจากตัวเลขที่ระบุ
> สองวิธีคำนวณแยกกัน ไม่ใช้ผลของกันและกัน (มี input ร่วมกันบางตัว ดูหัวข้อสุดท้าย)

## Input ร่วม
| รายการ | ค่า | ป้าย |
|---|---|---|
| Revenue Q1/Q2/Q3'26 | $1,078M / $1,248M / $1,413M | [หลัก — 8-K] |
| Q4'26 guide | Rev $1,490M, Adj. EBITDA $461M (midpoint) | [หลัก — 8-K guide] |
| FY26E revenue = 3Q จริง + guide | $5,229M | [คำนวณ] |
| Adj. EBITDA FY26E = 277+358+434+461 | $1,530M (margin 29.3%) | [คำนวณ] |
| Net debt 2026-09-30 (debt $3,777M − cash $676M) | $3,101M | [หลัก-คำนวณ] |
| Shares | 67.6M | [รอง — Webull] |
| Convertible $1.4B 1.25% due 2030 | conversion price ~$154.29 (เดิม $154.32), principal จ่ายเงินสด ส่วนเกินเป็นเงินสด/หุ้น, capped call cap $237.42 | [หลัก — 10-Q Q2'26 / 8-K 2024 ตามผล search; ไม่ได้เปิดอ่านเต็ม] |

---
## (A) MS-style estimate

### สมมติฐาน
| รายการ | ค่า | ป้าย / เหตุผล |
|---|---|---|
| Revenue growth FY27→FY31 | +12% / −8% / +8% / +6% / +5% | [สมมติฐาน] FY27 = $5,857M ต่ำกว่า Q4'26 annualized ($5,960M) เล็กน้อย; ปี FY28 ถดถอยตามวงจร semi-cap (ไม่ได้ลอกจาก conquest) |
| Adj. EBITDA margin FY27→FY31 | 29% / 24% / 25.5% / 25.5% / 25.5% | [สมมติฐาน] Peak ปัจจุบัน 30.7% (Q3'26 [คำนวณ]); mid-cycle ตั้ง 25.5% ≈ ระดับ Q1'26 25.7% [คำนวณ] ไม่ใช้ peak |
| หัก depreciation / SBC / รายการ adj. อื่น | 3.5% / 2.5% / 0.5% ของ revenue | [สมมติฐาน] ไม่ได้อ่านจาก filing รอบนี้ — SBC ถือเป็นต้นทุนจริง; amortization ของ intangible Atotech ไม่หัก (non-cash) |
| Economic EBIT margin mid-cycle | 19.0% | [คำนวณ] |
| Tax | 18% | [สมมติฐาน] |
| Reinvestment | Δrevenue ÷ sales-to-capital 2.0 (ปีถดถอย = 0) | [สมมติฐาน] |
| Moat / fade | Narrow (moat ยังไม่ยืนยัน) → fade 10 ปี; ROIC ใหม่ 15% → WACC | [สมมติฐาน] ROIC 15% ประมาณจาก NOPAT FY26E ~$976M ÷ invested capital ~$6.4B (equity ที่ derive จาก P/B + net debt) [คำนวณ หยาบ] |
| Terminal growth | 2.5% (RONIC = WACC → growth ไม่เพิ่มมูลค่าใน TV) | [สมมติฐาน] |
| Uncertainty rating / Cost of equity | High → 10.5% (Medium 9% / Very High 12% เป็น sensitivity) | [สมมติฐาน] semi-cap cyclical + leverage |
| Cost of debt / weights | 6% pre-tax (4.9% หลังภาษี); E 76.8% : D 23.2% (market cap $12.5B vs debt $3.78B) | [สมมติฐาน] |
| WACC | 9.2% | [คำนวณ] |
| Discounting | mid-year, จาก 2026-11-06; ไม่นับ cash flow Q4'26 (net debt ณ 9/30) | [สมมติฐาน] |

### ผล
**Base ~$118/หุ้น** (equity = EV − net debt $3,101M ÷ 67.6M) [สมมติฐาน+คำนวณ]

| Sensitivity | FV/หุ้น |
|---|---|
| Cost of equity Medium 9% (WACC 8.1%) | $146 |
| **Base High 10.5% (WACC 9.2%)** | **$118** |
| Very High 12% (WACC 10.4%) | $97 |
| WACC −1% / +1% | $141 / $100 |
| Terminal g 1.5% / 3.5% (RONIC=WACC) | $117 / $120 (ไวน้อยเพราะ TV ไม่สร้างมูลค่าเพิ่ม) |
| Terminal g 1.5% / 3.5% ถ้า RONIC = WACC+2% | $120 / $130 |
| Fade ~0-1 ปี (No moat) / 10 (Narrow) / 20 (Wide) | $110 / $118 / $125 |
| **ใช้ margin peak 31% ตลอด (ไม่ปรับ cycle)** | **$182** |
| ไม่มี down-year, margin mid-cycle คงที่ 25.5% | $123 |

**Range ที่ใช้รายงาน: ~$97–$146** (Ke 12%→9%); WACC±1% = $100–$141.

**Dilution convertible:** FV base $118 < conversion price $154.29 → ไม่มี dilution; ตัวหนี้ $1.4B นับใน net debt แล้ว. ถ้า FV > $154.29 ส่วนเกินเป็นหุ้นใหม่ แต่ capped call (cap $237.42) ชดเชยถึง $237 → ผลต่อ FV ที่ range นี้ ≈ 0 [คำนวณ/อนุมานจากเงื่อนไขที่ search พบ ไม่ได้อ่าน indenture].

**ราคา $185.37 vs Base $118 = +57% → 🔴 Expensive (>+20%)**. ราคาปัจจุบันใกล้เคียงกรณีที่ตลาดเชื่อว่า margin peak (~31%) คงอยู่ ($182).

---
## (B) GF-style estimate

### ข้อมูลย้อนหลัง (ข้อจำกัดสำคัญ)
แหล่ง: stockanalysis.com ratios (annual, **ค่า ณ สิ้นปีงบ FY2021–FY2025 = 5 ปี เท่านั้น**) [รอง]. Macrotrends/GuruFocus โหลดไม่ได้ (403) จึงไม่ได้ median 10 ปี. ค่าแต่ละปีเป็น point-in-time สิ้นปี ไม่ใช่ median รายวัน.

| ปี | P/E | P/S | P/B | P/FCF | EV/EBITDA |
|---|---|---|---|---|---|
| FY21 | 17.53 | 3.27 | 3.35 | 17.47 | 11.63 |
| FY22 | 16.92 | 1.59 | 1.26 | 15.44 | 11.25 |
| FY23 | n/a (ขาดทุน) | 1.90 | 2.78 | 29.65 | 14.25 |
| FY24 | 36.98 | 1.96 | 3.03 | 17.14 | 12.99 |
| FY25 | 36.39 | 2.73 | 3.95 | 21.60 | 16.30 |
| **Median (5 ปี; P/E 4 จุด)** | **26.96** | **1.96** | **3.03** | **17.47** | **12.99** |
| ปัจจุบัน (stockanalysis, 2026-11-06) | 22.28 | 2.51 | 3.64 | 21.66 | 12.28 |

**คำเตือนการบิดเบือน:**
- Atotech ปิดดีลปี 2022 (ความรู้เดิม ไม่ได้ verify): FY21 เป็นบริษัทคนละขนาด/โครงสร้างทุน; P/B FY22 ต่ำ 1.26 เพราะ book เพิ่งรวม goodwill + ราคาหุ้นลงท้ายปี trough; หนี้เพิ่มหลังดีล ทำให้ P/S, P/B ก่อน/หลัง ไม่เทียบกันตรง
- FY23 ถดถอย (P/E n/a, P/FCF 29.65 บิดเบือนจาก FCF ต่ำ); FY24–25 P/E ~36-37 บิดเบือนจาก earnings ต่ำ + amortization Atotech
- 5 จุดปลายปี ครอบคลุมแค่ 1 วงจรเต็ม; ผลจึงเป็น "ประมาณ" มาก

### Per-share metric ที่ใช้
| Metric | ค่า | ป้าย |
|---|---|---|
| Sales/share FY26E | $77.35 ($5,229M ÷ 67.6M) | [คำนวณ] |
| Book/share | $48.65 (ราคา $185.365 ÷ P/B Webull 3.81) | [รอง-คำนวณ] |
| EPS TTM | $8.42 | [รอง — Webull] (GAAP, ไม่ปรับ growth) |
| FCF/share FY26E | $10.58 = (FCF Q1–Q3 $459M + Q4 สมมติ 17.2%×$1,490M)÷67.6M | [คำนวณ+สมมติฐาน] (Q4 margin ใช้เท่า Q3) |
| EBITDA FY26E | $1,530M | [คำนวณ] |

หมายเหตุ "ปรับ growth": ใช้ forward FY26E สำหรับ S/FCF/EBITDA (ซึ่ง +43% YoY ล่าสุดอยู่ในตัว) แต่ P/E, P/B ใช้ TTM/ปัจจุบัน — ไม่ได้ใส่ growth regression แบบ GF จริง

### ผล
| Multiple | Median × metric | FV/หุ้น |
|---|---|---|
| P/S | 1.96 × $77.35 | $152 |
| P/B | 3.03 × $48.65 | $147 |
| P/E | 26.96 × $8.42 | $227 |
| P/FCF | 17.47 × $10.58 | $185 |
| EV/EBITDA | (12.99 × $1,530M − $3,101M) ÷ 67.6M | $248 |
| **ค่าเฉลี่ย 5 วิธี** | | **~$192** (median ของ 5 = $185) |
| Range (ใช้ min/max multiple ในตาราง) | | ~$140–$279 |
| ค่าเฉลี่ยตัดวิธีที่บิดเบือนมาก (P/E, EV/EBITDA) | P/S, P/B, P/FCF | ~$161 |

**GF-style estimate ≈ $192 (กรอบ $140–$279); ราคา $185.37 ต่ำกว่า ~3% → 🟡 Fair** (ถ้าตัด P/E+EV/EBITDA ได้ $161 → ราคาสูงกว่า ~15% ยังอยู่ Fair). ปัญหา: ใช้ median multiple คูณ earnings/EBITDA ที่ใกล้ peak วงจร จึงให้ค่าสูง.

---
## เปรียบเทียบ
| | ค่า | ราคา $185.37 อยู่ |
|---|---|---|
| conquest DCF เดิม (WACC 11.5%, beta ~1.95) | Base ~$98 (Bear $79 / Bull $123) [อนุมาน — brief] | +90% 🔴 |
| (A) MS-style | Base ~$118 (range $97–$146) | +57% 🔴 Expensive |
| (B) GF-style | ~$192 (range $140–$279) | −3% 🟡 Fair |

A สูงกว่า conquest ~+20% เพราะ WACC ต่ำกว่า (9.2% vs 11.5%), fade 10 ปีเพิ่มมูลค่า และ margin mid-cycle 25.5% (conquest FCF margin 16%→14%).

## ไวต่อสมมติฐานที่สุด
- B ไวที่สุดในแง่ range (กว้าง $140–$279 ขึ้นกับว่าเลือก multiple ไหน/ปีไหน/metric peak หรือไม่)
- A ไวที่สุดต่อ **margin (cycle treatment)**: mid-cycle $118 vs peak $182 (+54%) มากกว่า WACC ±1% ($100–$141) และ terminal g (±$1–$3)

## สองวิธี "อิสระ" จริงไหม
ไม่เต็มที่ — เป็นข้อมูลชุดเดียวกัน: FY26E revenue/EBITDA (3Q จริง + guide), net debt, จำนวนหุ้นร่วมกัน; B ยังผูกกับราคาตลาดผ่าน P/B (derive จากราคาปัจจุบัน) และ multiple ย้อนหลังที่เป็นราคาตลาดเอง (เป็น market-relative ไม่ใช่ intrinsic). ความต่างของผล ($118 vs $192) มาจากการจัดการวงจรเป็นหลัก (A ปรับ mid-cycle, B คูณ metric ใกล้ peak) ไม่ใช่การยืนยันกัน. และทั้ง A กับ conquest ถูกคิดโดยผู้ทำเดียวกัน ไม่ถือเป็น 2-ใน-3 อิสระ. ผลทั้งหมดเป็น single-author estimate ไม่ควรใช้ทดแทน Morningstar/GuruFocus จริง.
