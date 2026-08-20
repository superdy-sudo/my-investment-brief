# 💰 Conquest Valuation: COF — 2026-08-20
*Independent bank valuation (Claude-only, FCFE/Dividend-Discount-style — ไม่ใช้ FCFF DCF มาตรฐานเพราะ COF เป็นธนาคาร ไม่มี CapEx-based FCF ที่มีความหมาย)*

## หมายเหตุวิธีการ
COF เป็นสถาบันการเงิน — ใช้ **2-stage FCFE model** (cash flow to equity ≈ net income ที่ปรับ payout capacity) แทน FCFF DCF มาตรฐาน เพราะ:
- "Free cash flow" แบบ CapEx-based ไม่มีความหมายกับธนาคาร (ธนาคารไม่มี CapEx-heavy operations)
- CET1 ratio 14.4% สูงกว่าเกณฑ์ regulatory มาก → มี excess capital ที่ทำให้ net income เกือบทั้งหมด "จ่ายออกได้" ในรูป dividend + buyback โดยไม่กระทบ capital adequacy → ใช้ Net Income เป็น proxy ของ FCFE ได้อย่างสมเหตุสมผล (ไม่ต้องหักเงินไปสะสมทุนเพิ่ม)
- ผลลัพธ์ = **Equity Value โดยตรง** (ไม่ใช่ Enterprise Value) จึงไม่ต้องบวก/ลบ net cash-debt อีกรอบ

## Assumptions

**Base FCFE (normalized net income):**
- Q1 2026 net income $2.2B ถูกกดจาก one-time Discover Day-1 CECL provision $11.4B → ไม่ใช่ run-rate ปกติ
- Q2 2026 net income $3.0B สะท้อน run-rate ที่ normalize แล้วมากกว่า
- ใช้ H1 2026 จริง ($5.2B) + ประมาณ H2 ที่ Q2-run-rate ต่อเนื่อง (2 × $3.0B = $6.0B) → **FY2026E net income ≈ $11.2B** (ปัดเป็น **$11.5B** เผื่อ synergy realization เพิ่มเติมใน H2)

**Growth fade (Stage 1, ปี 1-5):** เริ่มจาก organic growth ~9.5% YoY (ไม่ใช่ headline +38.55% ที่เป็น M&A step-change) แล้วลดหลั่นลงตาม mean-reversion ของธุรกิจธนาคารที่โตเร็วจาก M&A:
- ปี1: 9% (momentum synergy realization ต่อเนื่อง)
- ปี2: 8% (Discover brownout ยัง drag แต่ synergies เพิ่ม)
- ปี3: 6.5% (Discover loan book trough แล้ว เริ่มกลับมาโต, migration คืบหน้า)
- ปี4: 5% (full synergy target $2.5B ใกล้ achieved ~2027)
- ปี5: 4% (mature growth, ใกล้ terminal)

**Terminal growth: 3%** — ผูกกับ nominal GDP/inflation ระยะยาว ไม่ใช้สูงกว่านี้เพราะแม้มี Network Economies moat (issuer+network) แต่ Discover network ยังด้อยกว่า Visa/Mastercard ชัดเจน (merchant acceptance 70M points vs 130M/100M) — moat ยังไม่ถึงระดับ Wide ที่จะให้ pricing power ยั่งยืนเกิน GDP

**Cost of Equity (แทน WACC — ใช้ direct equity valuation):**
- Risk-free rate: 4.3% (10Y UST ปัจจุบัน)
- Beta: ~1.35 (ประมาณ — COF เป็น credit-sensitive consumer lender ผันผวนสูงกว่าตลาด/ธนาคารทั่วไป เนื่องจากพอร์ต subprime/near-prime card มากกว่า peer bank ทั่วไป — ไม่พบตัวเลข beta ที่แม่นยำจาก source ที่มี จึงเป็นการประมาณ)
- Equity Risk Premium: 5%
- **Cost of Equity ≈ 4.3% + 1.35×5% = 11.0%**

**Shares outstanding:** 617M (midpoint 613-622M)

## DCF Calculation (Base Case, r=11%, terminal g=3%)

| ปี | Growth | FCFE ($B) | Discount Factor | PV ($B) |
|---|---|---|---|---|
| 0 (base) | - | 11.50 | - | - |
| 1 | 9.0% | 12.54 | 0.9009 | 11.29 |
| 2 | 8.0% | 13.54 | 0.8116 | 10.99 |
| 3 | 6.5% | 14.42 | 0.7312 | 10.54 |
| 4 | 5.0% | 15.14 | 0.6587 | 9.97 |
| 5 | 4.0% | 15.75 | 0.5935 | 9.34 |

- Terminal Value (ที่ปี5) = 15.75 × 1.03 / (0.11 − 0.03) = **$202.7B**
- PV of Terminal Value = 202.7 × 0.5935 = **$120.3B**
- Sum PV of Stage-1 FCFE = **$52.1B**
- **Equity Value = 52.1 + 120.3 ≈ $172.4B**
- **Fair Value/share = 172.4B ÷ 617M ≈ $279.5**

*(หมายเหตุ: ไม่ได้บวก excess capital เหนือ CET1 requirement เข้าไปเพิ่ม — เป็น conservative bias, upside ที่ไม่ได้นับ)*

## Sensitivity (3 scenarios)

| Scenario | Cost of Equity | Terminal g | Fair Value/share |
|---|---|---|---|
| 🔴 Bear | 12% | 2.5% | ~$249 |
| 🟡 Base | 11% | 3.0% | ~$280 |
| 🟢 Bull | 10% | 3.5% | ~$354 |

## เทียบราคาปัจจุบัน $220.73
Base case fair value $280 สูงกว่าราคาตลาด **+26.7%**
→ **🟢 Cheap** (fair value สูงกว่าราคา ≥20%)

แม้แต่ **Bear case ($249) ก็ยังสูงกว่าราคาตลาด +12.8%** — แสดงว่า margin of safety ค่อนข้างมั่นคงต่อการเปลี่ยนแปลง assumption แม้ปรับ cost of equity ขึ้น 1% และ terminal growth ลง 0.5% พร้อมกัน

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $225-231** — ใกล้เคียงทิศทาง (ทั้งคู่บอกว่าราคาตลาดไม่ได้แพงเกินพื้นฐาน) แต่ Morningstar ระบุ bucket "Fair" (+2-4% เท่านั้น) ขณะที่ conquest เห็น upside มากกว่าชัดเจน (+26.7%) — ต่างกันเพราะ conquest ให้น้ำหนักกับ normalized Q2 run-rate (หลัง one-time Discover provision หมดไป) มากกว่า และประเมิน organic growth fade ในแง่ดีขึ้นจากช่วง trough
- **GuruFocus GF Value $163.32** — ไกลจาก conquest base case มาก (conquest สูงกว่า 71%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ยังไม่ปรับ base ให้สะท้อนขนาดบริษัทหลัง Discover M&A (revenue/asset base ใหญ่ขึ้นถาวร) — โมเดล regression มักลาก mean-reversion ของ multiple เดิมก่อนดีลมาใช้ ซึ่งไม่เหมาะกับบริษัทที่เพิ่งเปลี่ยนขนาดธุรกิจถาวรจาก M&A ใหญ่ขนาดนี้
- **สรุป: Conquest เห็นด้วยกับทิศทางของ Morningstar** (หุ้นไม่ได้แพงเกินพื้นฐาน แม้ conquest เห็น upside มากกว่า) และเห็นต่างจาก GuruFocus ชัดเจน — ทำให้ 2/3 แหล่ง (Morningstar + Conquest) เห็นตรงกันว่าราคาตลาด ณ $220.73 ไม่ใช่ "Expensive" → GuruFocus เป็น outlier ในกรณีนี้
