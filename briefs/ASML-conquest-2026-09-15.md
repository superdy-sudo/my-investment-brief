# 💰 Conquest DCF: ASML — 2026-09-15
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — REFRESH ของรอบ 2026-08-17 (เดิม base case $728)*

## Assumptions

- **Base FCF (FY2026E, ปีฐาน ปี 0):** revenue midpoint guidance €44.0B (จาก guidance ล่าสุด €43-45B หลัง Q2 beat) × FCF margin 27.5% (ใกล้เคียง FY2025 actual 27.67% GuruFocus) = **€12.1B**
  - ใช้ FY2026E เป็นฐานแทน FY2025 actual (€9.1B) เพราะ ณ วันประเมิน (ก.ย. 2026) ปีงบเกือบจบแล้วและ guidance ราย quarter (Q3: €11-12B) ยืนยันตัวเลขนี้แล้ว
- **Growth fade (ปี 1-5, FY2027-2031):** ปี1: +12% → ปี2: +8% → ปี3: +6% → ปี4: +5% → ปี5: +4%
  - **เหตุผลสำคัญ:** guidance FY2026 ที่เพิ่งปรับขึ้นเป็น €43-45B นั้น **ชนขอบล่างของ 2030 long-term scenario (€44-60B) ไปแล้วตั้งแต่ปีนี้ — เร็วกว่าที่ Investor Day (พ.ย. 2024) วางไว้ถึง 4 ปี** แต่บริษัท "reaffirm" ตัวเลข 2030 เดิม (€44-60B) ต่อเนื่องใน Q1/Q2 2026 ไม่ได้ยกระดับขึ้นตาม guidance ที่ raise 2 รอบ → นัยว่าการเติบโตส่วนใหญ่ที่ตลาดคาดไว้ถึงปี 2030 ถูก "pull forward" มาที่ปี 2026 แล้ว เหลือ runway ให้โตต่อในช่วง Stage 1 ไม่มากเท่าที่ guidance ปัจจุบันทำให้ดูตื่นเต้น — จึงให้ fade ลงเร็วกว่าธุรกิจ high-growth ทั่วไป ไปจบที่ revenue ปี 2031 ~€61.6B ซึ่งอยู่ในกรอบบนของ 2030 target พอดี (self-consistency check ผ่าน)
  - หากบริษัท re-raise 2030 target ในงาน Investor Day ครั้งถัดไป (คาดปลายปี 2026/ต้นปี 2027) — นี่คือ **swing factor เดียวที่กระทบ fair value มากกว่า WACC/terminal growth ทั้งหมด** (ดูหมายเหตุท้ายไฟล์)
- **FCF margin ขยายตัวคู่กับ gross margin guidance (54-60% by 2030):** ปี1: 28% → ปี2: 28.5% → ปี3: 29% → ปี4: 29.5% → ปี5: 30%
- **Terminal growth: 3%** — ผูกกับ long-run GDP/inflation มาตรฐาน ไม่ปรับสูงกว่านี้แม้ moat จะแข็งมาก เพราะ semiconductor capex มี cyclicality โดยธรรมชาติ (ไม่ใช่ recurring subscription-like) การให้ terminal growth สูงกว่านี้จะประเมิน cyclical downturn ต่ำเกินไป
- **WACC ≈ 11.5%:** risk-free rate 4.5% (10Y Treasury ประมาณการช่วง ก.ย. 2026) + beta 1.4 (กลางช่วง 1.3-1.5 ที่ให้มา) × ERP 5% (กลางช่วงมาตรฐาน 4-6%) = 4.5% + 7.0% = 11.5% — ใช้ cost of equity ตรงๆ เพราะ net-cash position (Debt/Equity 0.09 ไม่ต้อง weighted กับ cost of debt)
- **Net cash: ~€10B (ประมาณการ)** — อิงจาก €13.3B สิ้นปี 2025 → ลดเหลือ €8.4B สิ้น Q1 2026 (seasonal) → คาดฟื้นตัวหลัง Q2 beat (net income €2.9B) แต่ไม่มีตัวเลข Q3 actual ชัดเจน จึงประมาณกลางๆ ที่ €10B — เป็นสัดส่วนเล็ก (~5%) ของ EV จึงผลกระทบต่อ fair value ต่ำแม้ประมาณคลาดเคลื่อน
- **Shares outstanding (diluted): 385.27M**
- **FX EUR/USD: 1.157** — ใช้ rate เดียวกับที่ brief แปลง Morningstar EUR 1,800 → $2,083 เพื่อความสอดคล้องภายในไฟล์เดียวกัน (ไม่ได้ไป fetch FX ใหม่)

## DCF Calculation (หน่วย: €B)

| ปี | Revenue | FCF margin | FCF |
|---|---|---|---|
| Base (FY26E) | 44.0 | 27.5% | 12.1 |
| ปี1 (FY27) | 49.3 | 28.0% | 13.80 |
| ปี2 (FY28) | 53.2 | 28.5% | 15.17 |
| ปี3 (FY29) | 56.4 | 29.0% | 16.36 |
| ปี4 (FY30) | 59.2 | 29.5% | 17.47 |
| ปี5 (FY31) | 61.6 | 30.0% | 18.48 |

**Base case (WACC 11.5%, terminal g 3%):**
- Terminal Value (ปี5) = 18.48 × 1.03 / (0.115−0.03) = €223.9B
- PV ของ FCF ปี1-5 (discount factor 0.897→0.580) = €58.4B
- PV ของ Terminal Value = €129.9B
- Enterprise Value = €188.3B
- + Net cash €10B = **Equity Value €198.3B**
- ÷ 385.27M shares = **€514.7/share → $595.5/share** (×1.157)

## Fair Value (sensitivity: WACC ±1%, terminal g ±0.5%)

- **Bear case** (WACC 12.5%, g 2.5%): EV €162.0B + cash → Equity €172.0B → €446.4/share → **$516.5**
- **Base case** (WACC 11.5%, g 3.0%): → **$595.5**
- **Bull case** (WACC 10.5%, g 3.5%): EV €225.9B + cash → Equity €235.9B → €612.2/share → **$708.3**

## เทียบราคาปัจจุบัน $1,589.73

🔴 **Expensive** — สูงกว่า Base case FV **+167%** และสูงกว่าแม้แต่ Bull case FV ($708.3) ถึง **+125%**

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $2,083** — ไกลจาก conquest base case มาก (Morningstar สูงกว่า conquest 3.5 เท่า) เพราะ Morningstar เป็น forward-DCF ที่ผูกกับ moat rating (Wide Moat) มักให้ terminal growth/margin สูงกว่า และอาจไม่ได้ปรับลด growth runway ลงตาม logic "2030 target ถูก pull-forward" ที่ conquest ใช้ — Morningstar อาจมองว่า 2030 target จะถูก re-raise ในอนาคตจึงยังให้ growth ต่อเนื่องยาวกว่า 5 ปีที่ conquest จำกัดไว้
- **GuruFocus GF Value $1,264.44** — ใกล้กับ conquest base case มากกว่า Morningstar (แม้ยังห่างกันเยอะ ~112%) เพราะ GuruFocus เป็น backward historical-multiple regression ที่ไม่ได้ปรับตาม guidance ใหม่เร็วเท่า forward-DCF ใดๆ — ตัวเลขที่ต่ำกว่าราคาตลาดสะท้อนว่า valuation multiple ปัจจุบันแพงกว่า historical norm
- **สรุป:** conquest เห็นด้วยกับทิศทางของ **GuruFocus ว่าแพง** แม้ตัวเลขดอลลาร์จะต่างกันมาก (conquest base $596 vs GuruFocus $1,264) — ทั้งสองฝั่ง **independent-of-Morningstar** เห็นตรงกันว่าราคาปัจจุบันสูงเกิน fundamental value อย่างมีนัยสำคัญ conquest ยิ่ง bearish กว่าเพราะใช้ WACC ที่สูงกว่าที่ตลาด implied (~11.5% จาก beta 1.4) และเพราะ assumption สำคัญที่ว่า 2030 revenue target ที่ reaffirm ไว้ (€44-60B) ถูกชนขอบล่างไปแล้วตั้งแต่ปีนี้ — ทำให้ growth runway ในช่วง 5 ปีข้างหน้าแคบกว่าที่ guidance raise ล่าสุดทำให้ตลาดตื่นเต้น

## หมายเหตุสำคัญ (key swing factor)

ตัวแปรที่กระทบ fair value มากที่สุดไม่ใช่ WACC หรือ terminal growth (สร้าง range แค่ $517-$708) แต่คือ **สมมติฐานว่า 2030 target จะไม่ถูก re-raise** — ถ้า ASML ยกระดับ 2030 scenario ขึ้นในงาน Investor Day ครั้งถัดไป (เป็นไปได้สูงเพราะ TSMC/Samsung capex ยังเร่งต่อเนื่องจาก AI demand ตามที่ระบุใน brief) fair value จากวิธีนี้จะขยับขึ้นมากกว่าการปรับ WACC/terminal growth เพียงอย่างเดียว — เป็นความเสี่ยงด้าน upside ที่ scenario นี้ยังไม่ได้ capture ไว้ตรงๆ
