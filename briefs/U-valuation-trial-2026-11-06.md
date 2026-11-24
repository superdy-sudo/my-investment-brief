# U (Unity) — Valuation Trial: MS-style vs GF-style estimate — 2026-11-06
ทดลองจำลองวิธีคิด 2 แหล่งด้วยตัวเอง — **ไม่ใช่ตัวเลข Morningstar / GuruFocus จริง** ราคาอ้างอิง $51.33 [หลัก — Yahoo/price_check 2026-11-06 intraday]
Tags: [หลัก]=filing/Yahoo/Webull ตรง | [รอง]=aggregator | [สมมติฐาน]=ตั้งเอง | [อนุมาน]=คำนวณจากข้อมูลข้างบน
สองวิธีคำนวณแยกกัน ไม่ปรับผลหากัน (แต่ใช้ข้อมูลดิบชุดเดียวกัน — ดูหัวข้อสุดท้าย)

## ข้อมูลดิบที่ใช้ร่วม
| รายการ | ค่า | Tag |
|---|---|---|
| Revenue 9M'26 | $1,676.8M | [หลัก — 8-K Q3'26 ตาม briefs/U-2026-11-06.md] |
| Revenue FY25 / 9M'25 | $1,849.6M / $1,346.6M → Q4'25 ≈ $503M | [หลัก — FY25 press release / brief] |
| Revenue TTM (Q4'25+9M'26) | ≈ $2,179.8M | [อนุมาน] |
| FY26E revenue (9M + Q4 guide strategic $683-691M + non-strategic ~$5M, ใช้กลาง ≈ $693M) | ≈ $2,369.8M | [หลัก+อนุมาน] |
| Adj EBITDA Q4 guide | $290-295M | [หลัก] |
| SBC 9M'26 | $219.9M (13.1% ของ rev) | [หลัก/อนุมาน] |
| FCF 9M'26 | $488.1M; Q4'25 FCF $119M → TTM FCF ≈ $607.1M | [หลัก]; [อนุมาน] |
| Cash / Convert carrying (30 ก.ย.) | $2,646.4M / $2,238.4M → net cash ≈ $408M (ไม่รู้ principal) | [หลัก]; [อนุมาน] |
| Shares | 443.8M (basic); adj EPS diluted 498.2M | [หลัก] |
| Equity (book) ≈ mkt cap $22.6B / P/B 7.45 | ≈ $3.03B | [อนุมาน จาก Webull] |
| Invested capital (equity + convert − cash) | ≈ $2.62B | [อนุมาน] |
| 10Y yield ~4.94% (30 ต.ค. 2026, FRED ตามที่ prediction-market page อ้าง) ; beta ไม่ได้ดึง | | [รอง] |

---
## (A) MS-style estimate — forecast 5 ปี + fade 10 ปี ผูก moat

### สมมติฐานทั้งหมด
| ตัวแปร | ค่า | เหตุผล / Tag |
|---|---|---|
| Moat rating | **Narrow (ยังไม่ยืนยัน)** → fade 10 ปี | Morningstar moat ไม่พบ (brief) ; กฎ: ไม่ยืนยัน → Narrow [สมมติฐาน] |
| Uncertainty rating | **High → cost of equity 10.5%** (alt: Very High 12%) | GAAP profitable ไตรมาสแรกเพิ่งเกิด แต่ ad cyclical + Runtime Fee history ; เลือก High ตรงกลาง [สมมติฐาน] |
| WACC | = cost of equity 10.5% | net cash โดยประมาณ convert ≈ cash จึงไม่ถ่วงหนี้ [สมมติฐาน] |
| Revenue FY26E (ฐาน) | $2,370M | guide-anchored [หลัก+อนุมาน] |
| Revenue growth FY27-31 | 25% / 20% / 16% / 13% / 10% | Q4'26 total ≈ +38% YoY, FY26 ≈ +28%; fade ตาม mean-reversion + Create โตแค่ ~5-11% [สมมติฐาน] |
| Operating margin **หัก SBC เป็นต้นทุนจริง** (ไม่รวม amortization/restructuring one-off) FY27-31 | 24% / 27% / 29% / 31% / 32% | Q4 guide EBITDA ≈ 42% − SBC ~13% − D&A ~2% ≈ 27%; ขยับช้า [สมมติฐาน] |
| Cash tax rate FY27-31 | 12% / 14% / 16% / 18% / 21% | มี NOL/ค่อยๆ เข้า statutory [สมมติฐาน] |
| Incremental sales-to-capital | 4.0x (reinvest = ΔRev / 4.0) | capex 9M แค่ $12.7M [หลัก], asset-light [สมมติฐาน] |
| Fade FY32-41 (10 ปี) | growth linear 10% → terminal g; margin คงที่ 32% (Narrow = ไม่ขยายต่อ); tax 21%; **ROIC linear → WACC** ; reinvest = NOPAT × g/ROIC | ตามกรอบ Morningstar [สมมติฐาน] |
| Terminal | ROIC = WACC → TV = NOPAT×(1+g)/WACC | growth หลัง fade ไม่สร้างมูลค่าเพิ่ม |
| Terminal growth | 3.0% | [สมมติฐาน] |
| Net cash / shares | +$408M / 443.8M basic | SBC หักเป็นต้นทุนแล้ว + convert นับเป็นหนี้ [สมมติฐาน] |
| Discounting | ปลายปี t=1..15, ณ ต้น FY27 (ละเลย Q4'26 FCF ~ครึ่งไตรมาส) | ประมาณ |

### ผลรายปี (ย่อ, $M) [อนุมาน]
| FY | Rev | EBIT(หัก SBC) | NOPAT | Reinvest | FCF | ROIC |
|---|---|---|---|---|---|---|
| 27 | 2,962 | 711 | 626 | 148 | 478 | 22.6% |
| 28 | 3,555 | 960 | 825 | 148 | 677 | 28.3% |
| 29 | 4,123 | 1,196 | 1,004 | 142 | 862 | 32.8% |
| 30 | 4,660 | 1,444 | 1,184 | 134 | 1,050 | 37.1% |
| 31 | 5,125 | 1,640 | 1,296 | 116 | 1,179 | 39.2% |
| 32-41 fade | 5,602 → 9,293 | | 1,416 → 2,349 | | FCF 1,053 → 1,678 | 36% → 10.5% (→ WACC) |

EV ≈ $13.1B (PV of terminal ≈ 39%) + net cash $0.41B → equity ≈ $13.5B → **MS-style base ≈ $30.5/share** [อนุมาน]

### Sensitivity (fair value/share) [อนุมาน]
| WACC \ terminal g | 2% | 3% | 4% |
|---|---|---|---|
| 9.5% | $34.1 | $34.7 | $35.4 |
| **10.5%** | $30.0 | **$30.5** | $31.0 |
| 11.5% | $26.7 | $27.1 | $27.5 |
Alt: cost of equity 12% (Very High) → $25.6 | ใช้ diluted 498M แทน 443.8M (WACC 10.5%) → $27.2
**Range (WACC ±1%, g ±1%): $26.7–$35.4 ; base $30.5**
หมายเหตุ: terminal g ไวต่ำ **โดยโครงสร้าง** (ROIC→WACC ทำให้ growth ช่วง terminal ไม่เพิ่มมูลค่า) — ความไวจริงอยู่ที่ margin/growth ปีที่ 1-5 ซึ่ง sensitivity ที่ขอไม่ได้ครอบคลุม (ไม่ได้รัน; ควรรันถ้าจะใช้จริง)

### ราคา $51.33 vs MS-style base $30.5
สูงกว่า +68% → bucket (เกณฑ์ conquest: >+20% = Expensive) **🔴 Expensive** ; สูงกว่า upper-range $35.4 อีก +45%

---
## (B) GF-style estimate — historical median multiples × per-share metric
**ความน่าเชื่อถือต่ำ**: U เพิ่ง GAAP profitable ไตรมาสแรก, multiple ย้อนหลังอยู่ในช่วงธุรกิจคนละแบบ (ก่อน/หลัง ironSource, ก่อน/หลังตัดขาดทุน), และ aggregator ขัดแย้งกันเอง

### ข้อมูลย้อนหลังที่หาได้ (ไม่ใช่ทุก multiple)
| Multiple | ข้อมูลที่เจอ | จำนวนปี | Tag |
|---|---|---|---|
| P/S (tickerleague) | 2021 36.9x, 2022 7.2x, 2023 7.1x, 2024 5.0x, 2025 10.3x ; (5y avg 11.8x ; หน้าอ้าง as of 5 มิ.ย. 2026) | 5 ปี | [รอง] |
| P/S (TipRanks) | 2021 33.77x, 2022 36.34x, 2023 6.38x, 2024 7.11x | 4 ปี (ขัดกับ tickerleague ปี 2022) | [รอง] |
| P/S (Macrotrends, annual avg) | 2022 11.49, 2023 6.91, 2024 4.29, 2021 ≈30 (ย้อนจาก % ที่หน้าระบุ) | 3-4 ปี | [รอง] |
| P/FCF (tickerleague) | 2023 87.3x, 2024 33.3x, 2025 47.0x (ปีที่ FCF ติดลบไม่แสดง); ณ มิ.ย. 2026 27.4x | **3 ปี** | [รอง] |
| P/B | **ไม่พบ** — ไม่คำนวณ (book value ถูกบิดจาก goodwill/impairment อยู่แล้ว) | 0 | — |
| EV/S | **ไม่พบ** — ไม่คำนวณ | 0 | — |
| P/E | ไม่มีความหมาย (กำไร GAAP เพิ่งบวก) | — | — |

### Median ที่ใช้ [อนุมาน]
- P/S median **7.15x** (tickerleague 2022-2025, ตัด 2021 ซึ่งเป็นยุค bubble/ZIRP — **การตัดเป็นดุลยพินิจของเรา**; median 5 ปีเต็มก็ได้ 7.2x เท่ากัน แต่ TipRanks 4 ปี median จะ ≈ 21.7x)
- P/FCF median **47.0x** (3 จุด; ช่วง 33.3–87.3x — ตัวหาร FCF ในอดีตต่ำมาก จึงทำให้ multiple สูง)

### Per-share metrics (หาร 443.8M shares) [อนุมาน]
Revenue/share TTM $4.91 | Revenue/share FY26E $5.34 | FCF/share TTM $1.37 (FCF ก่อนหัก SBC ตามนิยามบริษัท — สอดคล้องกับ P/FCF ย้อนหลัง)

### ผล
| ชุด | คำนวณ | ค่า/หุ้น |
|---|---|---|
| P/S × Rev/share TTM | 7.15 × 4.91 | $35.1 |
| P/S × Rev/share FY26E (forward, guide) | 7.15 × 5.34 | $38.2 |
| P/FCF × FCF/share TTM | 47.0 × 1.37 | $64.3 |
| ถัวเฉลี่ย (P/S forward-avg กับ P/FCF, น้ำหนักเท่ากัน) | (36.7 + 64.3) / 2 | **≈ $50.5 (GF-style base)** |
| Range | P/S ต่ำสุด 6.91x×TTM = $33.9 ↔ P/FCF 87.3x = $119.4 | $34–$119 |
(ไม่ได้ปรับ growth เพิ่มเกิน FY26E ที่ guide — เพื่อไม่ยืม forecast ของวิธี A)

### ราคา $51.33 vs GF-style
- เฉลี่ย 2 family $50.5 → ราคา +1.6% → **🟡 Fair** (แต่เป็นผลจาก P/FCF ที่แกว่งมาก)
- ถ้าเอาเฉพาะ P/S ($35-38) → ราคา +35-46% → 🔴 Expensive
- ผลสรุปไม่ robust: bucket พลิกตามว่าเลือก family ไหน

---
## เปรียบเทียบ
| | ค่า base | range | ราคา $51.33 |
|---|---|---|---|
| (A) MS-style | $30.5 | $26.7–35.4 | 🔴 Expensive (+68%) |
| (B) GF-style | $50.5 (P/S-only $35-38) | $34–119 | 🟡 Fair (+2%) / P/S-only 🔴 |
| conquest เดิม | $35 (30–42) | | 🔴 (+46%) |
- A ใกล้ conquest ($30.5 vs $35, −13%) ทั้งที่โครงสร้างต่างกัน — เพราะใช้ forecast ฐานเดียวกัน (guide-anchored) และ WACC/margin สรุปคล้ายกัน
- B ห่างจาก A/conquest มาก (+44-65%) เพราะ multiple ย้อนหลัง (โดยเฉพาะ P/FCF) สะท้อนยุคที่ FCF ต่ำ/ตลาดจ่าย premium
- **ไวต่อสมมติฐานที่สุด: วิธี B** (range 3.5x; แกว่งตามปีที่ตัด/แหล่ง aggregator ที่เลือก และ P/FCF 3 จุด) ; วิธี A ไวปานกลางต่อ WACC (±~12%) และน่าจะไวมากต่อ margin ปี 5 (ยังไม่ได้รัน)

## ความเป็นอิสระของสองวิธี
**ไม่อิสระจริง** : (1) ทั้งคู่ใช้ revenue/FCF/shares ชุดเดียวกันจาก 8-K Q3'26 และ guide Q4 ตัวเดียวกัน — ถ้าตัวเลขเหล่านี้ผิดหรือไม่ยั่งยืน (เช่น Vector ชะลอ) ทั้งสองผิดไปทางเดียวกัน ; (2) ผู้ประมวลผลเป็นคนเดียว/โมเดลเดียว เลือกสมมติฐาน (Narrow, High, ตัดปี 2021) จึงมี bias ร่วม ; (3) conquest ก็ใช้ข้อมูลชุดนี้ ไม่นับเป็นแหล่งที่ 3 อิสระเช่นกัน ; ที่ต่างกันจริงคือ "ตรรกะ" (forward cash flow vs ย้อนอดีตของ multiple) ซึ่งเป็นเหตุให้ผลต่างกัน — แต่ความต่างนี้ไม่ใช่ข้อมูลเพิ่มเกี่ยวกับมูลค่าจริง
ข้อห้าม: ไม่ใช่ buy/sell recommendation ; ไม่ได้แทน Morningstar/GF Value จริง

Calc script: scratchpad dcf.py (ไม่ commit)
