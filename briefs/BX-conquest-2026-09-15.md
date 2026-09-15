# 💰 Conquest DCF: BX (Blackstone) — 2026-09-15
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จาก Morningstar/GuruFocus)*

## Assumptions

- **Base cash flow: $7.6B** — ใช้ Distributable Earnings (DE) annualized จาก H1'26 ($1.8B Q1 + $2.0B Q2 = $3.8B × 2) **แทน GAAP OCF-based FCF ($4.43B TTM)** เหตุผล: สำหรับ alternative asset manager แบบ BX, DE คือ metric มาตรฐานอุตสาหกรรมที่สะท้อน cash จริงที่ available ให้ shareholder (fee income + realized performance fees + net investment income หัก non-cash items) — GAAP OCF ของบริษัทกลุ่มนี้ผันผวนจาก timing ของ consolidated fund flows ซึ่งไม่ใช่ owner-earnings ที่แท้จริง การใช้ FCF ต่ำกว่าจะ understate มูลค่าของ asset-light fee business
- **Growth fade (Year 1-5): 22% → 18% → 14% → 10% → 7%** — เริ่มจาก DE growth ปัจจุบัน (+25-26% YoY) ลดหลั่นลงเพราะ (1) BCRED redemption gate ที่ 5% ต่อเนื่อง 2 ไตรมาสเป็น near-term drag ต่อ fundraising ใน private-credit channel, (2) FRE growth เริ่มชะลอตัวเล็กน้อยแล้ว (Q1 +23% → Q2 +22%), (3) mean-reversion ปกติเมื่อ AUM base ใหญ่ขึ้น แต่ยังคง premium เหนือ terminal เพราะ secular tailwind alts AUM industry-wide ($1.35T → $32T คาดปี 2030)
- **Terminal growth: 3%** — สูงกว่า GDP เล็กน้อย เพราะ BX เป็น #1 alternative asset manager ที่มี switching-cost moat (LP lock-up หลายปี) และ AUM ยังเป็น <5% ของตลาดโลก ให้ runway ยาว แต่ไม่ให้สูงกว่านี้เพราะ moat เป็น Narrow (house view) ไม่ใช่ Wide และมีการแข่งขันจาก KKR/Apollo/Ares ในพื้นที่เดียวกัน
- **WACC: 11%** = Risk-free 10Y Treasury ~4.3% (ประมาณจากช่วง Sep 2026 ที่ yield แกว่งใกล้ 5.0% ช่วง risk-off แล้วย่อลงมา) + Beta 1.35 (ประมาณ — alternative asset manager มี earnings sensitivity สูงกว่าตลาดจาก fundraising cycle + carried interest ผันผวนตามตลาดทุน, ไม่ใช่ beta จริงจาก terminal) × ERP 5% = 4.3% + 6.75% ≈ 11% — ไม่ปรับ weighted cost of debt เพราะ net debt เล็กมาก ($7B) เทียบ market cap ($156B), ใช้ cost of equity ตรงๆ ได้
- Shares outstanding: 1.227B
- Net debt: $7.07B (corporate level)

## DCF Calculation (Base case)

| Year | Growth | FCF (DE-based, $B) | Discount factor @11% | PV ($B) |
|---|---|---|---|---|
| 0 (base) | — | 7.600 | — | — |
| 1 | 22% | 9.272 | 0.901 | 8.35 |
| 2 | 18% | 10.941 | 0.812 | 8.88 |
| 3 | 14% | 12.473 | 0.731 | 9.12 |
| 4 | 10% | 13.720 | 0.659 | 9.04 |
| 5 | 7% | 14.680 | 0.594 | 8.71 |

Sum PV of Stage-1 FCF ≈ **$44.1B**

Terminal Value = FCF5 × (1+3%) / (11%−3%) = 14.68 × 1.03 / 0.08 ≈ **$189.0B**
PV of Terminal Value = 189.0 × 0.594 ≈ **$112.2B**

Enterprise Value ≈ 44.1 + 112.2 = **$156.3B**
Equity Value = EV − Net Debt = 156.3 − 7.07 ≈ **$149.3B**
**Fair Value/share = 149.3B / 1.227B ≈ $121.7**

## Fair Value (Sensitivity)

| Scenario | WACC | Terminal g | FV/share |
|---|---|---|---|
| 🐻 Bear | 12% | 2.5% | **$102.5** |
| ⚖️ **Base** | **11%** | **3%** | **$121.7** |
| 🐂 Bull | 10% | 3.5% | **$149.5** |

## เทียบราคาปัจจุบัน $127.12

🟡 **Fair** — ราคาปัจจุบันสูงกว่า Base case FV ($121.7) อยู่ **+4.5%** ซึ่งอยู่ในกรอบ ±20% ของ base case (ช่วง $97.4–$146.0) → ตลาดให้ราคาที่ใกล้เคียง intrinsic value ตาม assumption ของ conquest ไม่ถูกไม่แพงชัดเจน

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $140** — ใกล้กว่า conquest base case ($121.7) เทียบกับ GuruFocus (ห่างจาก conquest ~15%) — Morningstar อาจใช้ terminal growth/WACC ใกล้เคียง base-to-bull ของเรา (WACC ต่ำกว่า 11% เล็กน้อย หรือให้เครดิต Wide-moat premium ที่ house view เราไม่ให้เพราะมองเป็น Narrow Moat)
- **GuruFocus GF Value $199.58** — ห่างจาก conquest base case มาก (+64%) และเกินแม้แต่ bull case ของเรา ($149.5) — เพราะ GF Value เป็น backward-looking historical-multiple regression ที่สะท้อนช่วงที่ BX เทรดที่ premium multiple สูงกว่านี้มาก (ก่อน BCRED stress) ไม่ได้ปรับลดสำหรับ growth ที่ชะลอลงต่ำกว่า 30% หรือ overhang จาก redemption gate ที่ยังไม่คลี่คลาย
- **สรุป: Conquest เห็นด้วยกับ Morningstar มากกว่า GuruFocus อย่างชัดเจน** — DCF อิสระที่คำนวณจาก raw fundamentals (DE growth ที่ชะลอตัว + BCRED overhang ที่ยังไม่จบ) ให้ผลใกล้เคียง Morningstar ($121.7 vs $140, ห่างกัน ~13%) ในขณะที่ GuruFocus ดูเหมือนจะ overstate value จาก historical multiple ที่ไม่ทันปรับกับ fundamental ปัจจุบัน → **2 ใน 3 แหล่ง (Morningstar + Conquest) เห็นตรงกันว่า valuation อยู่โซน Fair-to-slightly-expensive ไม่ใช่ deep undervalued แบบที่ GuruFocus บอก**
