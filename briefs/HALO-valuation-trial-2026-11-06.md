# HALO (Halozyme) — Valuation Trial 2026-11-06
ทดลองคำนวณ fair value เอง 2 วิธี แยกกัน (ไม่ใช่ตัวเลข Morningstar/GuruFocus จริง) | ราคา $106.70 [หลัก: price_check.py/Yahoo intraday 2026-11-06]

ป้ายข้อมูล: [หลัก]=filing/Yahoo ตรง | [รอง]=aggregator (stockanalysis.com ดึง 2026-11-06) | [สมมติฐาน]=เราตั้งเอง | [คำนวณ]=มาจากตัวเลขข้างบน
ข้อจำกัด: ไม่มีงบ Q3 ฉบับเต็ม/10-Q, ไม่มีรายได้แยกรายผลิตภัณฑ์, ไม่มีวันหมดอายุสิทธิบัตรรายผลิตภัณฑ์ที่ยืนยันแล้ว -> "แยกตาม product/patent cliff" ทำได้แค่ระดับ block (royalty vs product sales + cliff แบบสมมติฐาน) ไม่ใช่ตัวเลขรายยา

## Inputs ร่วม (ทั้ง A และ B ใช้ชุดเดียวกัน)
| รายการ | ค่า | ป้าย |
|---|---|---|
| FY26 guide Revenue | $1.860-1.925B (mid $1,892.5M) | [หลัก: 8-K Q3 Ex.99.1 ตาม brief 11-06] |
| FY26 guide Royalty | $1.235-1.255B (mid $1,245M) | [หลัก] |
| FY26 guide Adj EBITDA | $1.240-1.290B (mid $1,265M = margin 66.8%) | [หลัก] |
| FY26 guide non-GAAP EPS | $8.75-9.05 (mid $8.90) | [หลัก] |
| Product+อื่นๆ FY26 | 1,892.5 - 1,245 = $647.5M | [คำนวณ] |
| Debt / Cash / Net debt | $3.25B / $1.07-1.08B / ~$2.18B | [หลัก: 8-K ผ่าน brief] / [รอง: stockanalysis] |
| Shares | 113.5M basic (ใช้ทั้ง A และ B; หนี้ convert นับเป็น debt เต็มจำนวนจึงไม่นับหุ้น convert ซ้ำ) | [รอง] |
| TTM FCF | $885.9M | [รอง] |
| Beta 5Y | 0.88 | [รอง] |
| GAAP/non-GAAP EPS ratio | 0.85 (Q3: ~$2.04 GAAP ประมาณ / $2.39) -> FY26E GAAP EPS ~$7.57 | [สมมติฐาน] (หุ้น diluted ~121M ใช้หารเอง) |

---
## (A) MS-style estimate (ไม่ใช่ Morningstar จริง)
### สมมติฐาน
| รายการ | ค่า | ป้าย / เหตุผล |
|---|---|---|
| Moat rating | **Narrow** (ไม่ยืนยัน Wide) -> fade 10 ปี | [สมมติฐาน] Alteogen/Merck ทำให้ Wide ยังไม่ยืนยัน (brief Layer 2 ข้อ 4 = ⚠️) |
| Uncertainty | High -> cost of equity 10.5% | [สมมติฐาน] biotech royalty ที่พึ่งไม่กี่ blockbuster |
| WACC base | 9.3% = 79% x 10.5% + 21% x 4.8% | [คำนวณ] weight จาก mktcap $12.03B vs debt $3.25B [รอง]; Kd ก่อนภาษี 6% [สมมติฐาน] x (1-20%) |
| Terminal growth | 2.5% | [สมมติฐาน] |
| Royalty growth ปี FY27-31 | +22% / +16% / +10% / +5% / **-3%** | [สมมติฐาน] ปี 2031 = patent cliff/step-down ของ blockbuster รุ่นแรก (วันที่หมดอายุจริงรายยาไม่ได้ยืนยันรอบนี้ จึงใส่เป็น haircut เชิงสมมติฐาน — เข้มตามคำสั่ง) |
| Product sales growth | +15 / +10 / +7 / +5 / +3% | [สมมติฐาน] Q3 product sales ~+46% YoY [หลัก] แต่ถือว่าส่วนหนึ่งเป็นจังหวะ |
| Adj EBITDA margin | 66 / 65 / 64 / 63 / 62% | [สมมติฐาน] FY26 guide 66.8% [หลัก] แล้ว mix เอียงไป product margin ต่ำ |
| SBC | 5% ของรายได้ หักเป็นต้นทุนจริง | [สมมติฐาน] ไม่มี SBC ยืนยันจากงบรอบนี้ (adj EBITDA ไม่หัก SBC) |
| D&A | 3% ของรายได้ | [สมมติฐาน] |
| ภาษี | 20% | [สมมติฐาน] |
| ROIC / reinvestment | ROIC ปีที่ 1-5 = 100% (asset-light) reinvestment = growth/ROIC x NOPAT ; ROIC เส้นตรงลดลงสู่ WACC ตลอด fade 10 ปี ; terminal ROIC = WACC (value-driver TV) | [สมมติฐาน] |
| Cross-check FCF | FCFF FY27E $912M เทียบ TTM FCF $886M [รอง] | [คำนวณ] สมเหตุสมผล ไม่ได้ตั้งสูงเกินจริง |

### Forecast 5 ปี ($M) [คำนวณจากสมมติฐาน]
| ปี | Revenue | Royalty | Product | Adj EBITDA | SBC | NOPAT | Reinvest | FCFF |
|---|---|---|---|---|---|---|---|---|
| FY27 | 2,263 | 1,519 | 745 | 1,494 | 113 | 1,050 | 206 | 912 |
| FY28 | 2,581 | 1,762 | 819 | 1,678 | 129 | 1,177 | 165 | 1,089 |
| FY29 | 2,815 | 1,938 | 876 | 1,801 | 141 | 1,261 | 114 | 1,231 |
| FY30 | 2,955 | 2,035 | 920 | 1,862 | 148 | 1,300 | 65 | 1,324 |
| FY31 | 2,922 | 1,974 | 948 | 1,812 | 146 | 1,262 | 0 | 1,350 |
Fade FY32-41: NOPAT โตเส้นตรง 0% -> 2.5%, ROIC 100% -> WACC ; FCFF ~$1.24-1.29B (ปี 10 ของ fade ลดเหลือ ~$1.06B เพราะ reinvestment ขึ้นตาม ROIC ที่ลด)

### ผล (WACC 9.3%, g 2.5%)
PV(5 ปี + fade 10 ปี) $9,586M + PV(TV) $4,200M = EV ~$13,787M -> หัก net debt $2,180M -> equity $11.6B / 113.5M = **$102.3/หุ้น (MS-style base)** ; TV เป็น 30% ของ EV

### Sensitivity (ต่อหุ้น)
| WACC \ g | 1.5% | 2.5% | 3.5% |
|---|---|---|---|
| 8.3% | 115.3 | 118.0 | 120.9 |
| 9.3% | 100.1 | **102.3** | 104.5 |
| 10.3% | 87.9 | 89.6 | 91.5 |

อื่นๆ (ปรับทีละตัว): Uncertainty Medium (CoE 9% -> WACC 8.1%) $121.3 | Very High (CoE 12% -> WACC 10.5%) $87.5 | fade 0 ปี (None moat) $98.9 | fade 20 ปี (Wide) $103.1 | royalty growth -5pt/ปี $88.4 | +5pt/ปี $118.5 | SBC 8% ของรายได้ $95.7
**Range A (WACC +-1% x g +-1%): $87.9-120.9 ; base $102.3**
ข้อสังเกต: fade period (moat rating) ขยับค่าน้อยมาก ($98.9-103.1) เพราะ TV แบบ value-driver ให้ ROIC=WACC ที่ปลายทางอยู่แล้ว ; ตัวแปรที่ขยับจริงคือ WACC/uncertainty และ royalty growth

### Bucket (กฎ conquest: ต่ำกว่า base >=20% = Cheap, +-20% = Fair, สูงกว่า >20% = Expensive)
ราคา $106.70 สูงกว่า base A $102.3 อยู่ +4.3% -> **🟡 Fair** (อยู่ในช่วง range $87.9-120.9)

---
## (B) GF-style estimate (ไม่ใช่ GF Value จริง)
ข้อมูลย้อนหลัง: **5 ปี (FY2021-FY2025, ปลายปี)** [รอง: stockanalysis.com/stocks/halo/financials/ratios] — สั้นกว่า GuruFocus จริงที่ใช้ ~10 ปี และไม่มี P/B/growth-adjust ของ GF จริง
| ปี | P/E | P/S | P/FCF | EV/EBITDA |
|---|---|---|---|---|
| FY21 | 14.05 | 12.76 | 18.99 | 20.63 |
| FY22 | 38.06 | 11.66 | 32.70 | 26.60 |
| FY23 | 17.34 | 5.89 | 13.08 | 14.22 |
| FY24 | 13.70 | 5.99 | 12.99 | 11.09 |
| FY25 | 24.98 | 5.67 | 12.28 | 9.75 |
| **Median 5y** | **17.34** | **5.99** | **13.08** | **14.22** |
(เตือน: ค่าคิดจากราคาปลายปี ไม่ใช่ราคาปัจจุบัน; stockanalysis เองมีความไม่สอดคล้องภายในบางตัว เช่น P/FCF ปัจจุบัน 15.75 vs mktcap/FCF ~13.6 -> ใช้เป็น [รอง] เท่านั้น)

Metric ต่อหุ้น (113.5M หุ้น) ใช้ FY26 guide mid เป็น forward [หลัก/คำนวณ]: EPS GAAP-est $7.57 [สมมติฐาน 0.85 x 8.90] | Revenue $1,892.5M -> $16.67/หุ้น | FCF ใช้ TTM $886M -> $7.81/หุ้น (ไม่มี FY26 FCF guide ที่ยืนยัน) | Adj EBITDA $1,265M
| วิธี | คำนวณ | FV/หุ้น |
|---|---|---|
| P/E | 17.34 x 7.57 | $131.2 |
| P/S | 5.99 x 16.67 | $99.9 |
| P/FCF | 13.08 x 7.81 | $102.1 |
| EV/EBITDA | (14.22 x 1,265 - 2,180) / 113.5 | $139.3 |
| **ถัวเฉลี่ย 4 วิธี (median multiples)** | | **$118.1 (GF-style base)** |

Range: ใช้ multiple quartile ล่าง (อันดับ 2 ใน 5) -> $102.6 ; quartile บน (อันดับ 4 ใน 5) -> $185.6 ; ถ้า roll ไป FY27E (+16-17% growth [สมมติฐาน]) -> ~$138
**Range B: $102.6-185.6 ; base $118.1** (กว้างมาก เพราะ FY21-22 multiple สูงตอน growth/ฟองตลาด)
Bucket: ราคา $106.70 ต่ำกว่า base B 9.7% -> **🟡 Fair** (ใกล้ขอบล่างของ range)
ข้อควรระวัง: P/E และ EV/EBITDA สูงสุด ($131-139) แต่ P/S และ P/FCF ต่ำ (~$100) -> 4 วิธีไม่ลู่เข้ากัน ; GF จริงมี growth-adjustment ที่ไม่ได้ทำ

---
## เทียบกับ conquest DCF เดิม (10-20: Base ~$150, Bear $123, Bull $190)
- A $102.3 ต่ำกว่า conquest base 32% ; B $118.1 ต่ำกว่า 21% -> ทั้งสองวิธีต่ำกว่า conquest ยก ราคา $106.70 อยู่ต่ำกว่า conquest base 28.9% (🟢) แต่เป็น 🟡 ใน A และ B
- สาเหตุ A ต่ำกว่า: (1) ใส่ SBC เป็นต้นทุน, (2) patent cliff -3% ปี FY31 + fade ROIC ลง, (3) TV แบบ value-driver (conquest ใช้ Gordon บน FCF ปี 5, TV ~74% ของ EV ; ของนี้ ~30%), (4) WACC 9.3% vs 9.8% (ผลตรงข้าม), (5) หุ้น 113.5M vs 121.2M, net debt $2.18B vs ~$1.9B
- conquest 10-20 ยก base จากก่อนงบ Q3 ไม่ได้ recompute ; ผลนี้คำนวณใหม่ด้วย guide Q3 แต่เป็นสมมติฐานคนละชุด จึงเทียบกันได้เพียงเชิงทิศทาง
- ข้อสรุปเชิงระบบ: FV 3 ตัว ($102 / $118 / $150) ต่างกัน 47% ; ราคา $106.70 ต่ำกว่า conquest, สูงกว่า A เล็กน้อย, ต่ำกว่า B ไม่มาก -> ไม่ฟันธง Cheap ; ถ้านับ A+B (+conquest) ก็ยังเป็นตัวเลขที่ไม่เป็นอิสระ (ดูหัวข้อถัดไป) ไม่ควรใช้เป็น "2-ใน-3" ตามกฎระบบ

## ความไวต่อสมมติฐาน
- B ไวที่สุด: เปลี่ยนเลือก percentile ของ multiple ย้อนหลัง $102.6 -> $185.6 (+81%) และขึ้นกับ 5 ปีที่มี FY22 ผิดปกติ
- A ไวรองลงมา: WACC +-1% = ~$88-118 (-14%/+15%), royalty growth +-5pt/ปี = $88-119 ; g +-1% แทบไม่ขยับ ($100-105) ; moat fade ไม่ขยับ ($99-103)

## "อิสระต่อกัน" จริงไหม
**ไม่เป็นอิสระจริง** — ต่างกันแค่วิธีประมวลผล ไม่ใช่ข้อมูล:
1. ทั้ง A และ B (และ conquest) ใช้ FY26 guide ตัวเดียวกัน (rev/royalty/EBITDA/EPS) จาก 8-K ฉบับเดียว ถ้า guide ผิด ทุกตัวผิดพร้อมกัน
2. ใช้ net debt และจำนวนหุ้นชุดเดียวกัน และผู้ทำคือโมเดลเดียวกัน (bias การตั้งสมมติฐานเหมือนกัน)
3. B ใช้ multiple ที่เกิดจาก "ราคาตลาด" ของ HALO เอง (ย้อนหลัง 5 ปีปลายปี) -> anchor กับตลาดบางส่วน ; A อิงสมมติฐานล้วน จึงต่างเชิงวิธีจริงตรงนี้ จุดเดียว
4. ที่ต่างจริง: A (forward/สมมติฐาน growth+cliff) vs B (backward multiples) — เหมือนโครงของ Morningstar vs GF จริง แต่เป็นแค่ "สองมุมของข้อมูลชุดเดียว" ห้ามนับเป็น FV ตัวที่ 2 อิสระ ตามกฎ 2-ใน-3 ของ conquest.md ; ยังต้องการ Morningstar/GF Value จริงอยู่
5. ทั้งสองไม่รวม: เหตุผลที่ราคาลง -13% ยังไม่รู้ (brief 11-06), ผลอุทธรณ์ Dutch ruling/Alteogen, ตัวเลขรายผลิตภัณฑ์จริง

ข้อกำหนดการใช้: ผลนี้เป็นการทดลอง ไม่ใช่ buy/sell recommendation ไม่ได้แก้ Action ใน brief (คง Watch Provisional) ไม่ commit
