# 💰 Conquest DCF: ASML — 2026-08-17
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (Year 0, TTM):** $13.46B (USD-converted TTM FCF จาก brief ต้นทาง; อิง FY2025 FCF €11.08B บน revenue €32.7B, FCF margin ~34%)
- **Growth fade (FCF growth, ปี 1-5):**
  - ปี1: 27% → ปี2: 20% → ปี3: 15% → ปี4: 10% → ปี5: 6%
  - เหตุผล: จุดเริ่ม fade ตั้งจาก FY2026 guided revenue growth ~34.6% (สูงสุดในรอบหลายปี จาก AI/HBM capex supercycle + High-NA EUV ramp) แต่ TTM base ที่ใช้เริ่มต้นได้ดูดซับ momentum ปัจจุบันไปบางส่วนแล้ว จึงตั้งปี1 ต่ำกว่า guidance เล็กน้อยที่ 27% แล้วลดหลั่นเร็วลงมาที่ 6% ในปี5 — สะท้อน mean-reversion ทั่วไปของ semiconductor capex cycle (WFE spending มีประวัติ boom-bust แม้ ASML จะเป็น sole EUV supplier ก็ยังผูกกับ capex cycle ของลูกค้า TSMC/Samsung/Intel/SK Hynix) และไม่มี company-specific เหตุผลให้เชื่อว่า growth 30%+ จะคงอยู่ได้ 5 ปีเต็มโดยไม่มี digestion period
- **Terminal growth rate: 3%** —ผูกกับ long-run GDP/inflation มาตรฐาน ไม่ได้ให้ premium สูงกว่านี้แม้จะมี wide moat เพราะ demand ระยะยาวยังผูกกับวงจร capex ของอุตสาหกรรม semiconductor ซึ่งมีความเป็น cyclical มากกว่าธุรกิจ subscription/consumer staple ทั่วไปที่มักได้ terminal growth สูงกว่า
- **WACC: 11.5%**
  - Risk-free rate: 4.68% (US 10Y Treasury yield, 2026-08-17, จาก WebSearch)
  - Equity risk premium: 5.0% (มาตรฐานตลาด, จุดกึ่งกลางของช่วง 4-6%)
  - Beta: 1.39 (จาก financecharts.com, พฤษภาคม 2026, ตามที่ระบุใน brief ต้นทาง)
  - WACC ≈ Cost of Equity = 4.68% + 1.39 × 5.0% = 11.63% → ปัดเป็น 11.5%; ใช้ cost of equity ตรงๆ เพราะ ASML เป็น net-cash position (net cash ~€5.3B, Debt/EBITDA 0.21x) ไม่ต้อง weighted กับ cost of debt
- **Shares outstanding:** 386M diluted (weighted-average, Q1 2026)
- **Net cash:** €5.3B × EUR/USD 1.157 = ~$6.13B (ตามอัตราแลกเปลี่ยนที่ใช้ใน brief ต้นทาง)

## DCF Calculation

| Year | Growth | FCF ($B) | Discount Factor @11.5% | PV ($B) |
|------|--------|----------|------------------------|---------|
| 0 (TTM) | - | 13.46 | - | - |
| 1 | 27% | 17.09 | 0.8969 | 15.33 |
| 2 | 20% | 20.51 | 0.8044 | 16.50 |
| 3 | 15% | 23.58 | 0.7215 | 17.02 |
| 4 | 10% | 25.94 | 0.6470 | 16.79 |
| 5 | 6% | 27.50 | 0.5802 | 15.96 |

- Sum of PV (Stage 1 FCF, ปี1-5): **$81.59B**
- Terminal Value (ปี5+) = FCF5 × (1+g) / (WACC − g) = 27.50 × 1.03 / (0.115 − 0.03) = **$333.22B**
- PV of Terminal Value = 333.22 × 0.5802 = **$193.35B**
- **Enterprise Value = 81.59 + 193.35 = $274.94B**
- + Net cash $6.13B → **Equity Value = $281.07B**
- ÷ 386M diluted shares → **Fair Value per share ≈ $728**

## Fair Value

- Bear case (WACC 12.5%, terminal g 2.5%): **$627**
- **Base case (WACC 11.5%, terminal g 3%): $728**
- Bull case (WACC 10.5%, terminal g 3.5%): **$873**

## เทียบราคาปัจจุบัน $1,883.47

🔴 **Expensive** — สูงกว่า Base case FV ($728) ประมาณ **+159%**, สูงกว่าแม้แต่ Bull case ($873) ถึง +116%

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV EUR 1,800 (~$2,083):** ไกลจาก conquest base case มาก (conquest ต่ำกว่า Morningstar ~65%) — เป็นเพราะ Morningstar เป็น forward analyst DCF ที่ผูกกับ moat rating น่าจะสมมติให้ growth สูง (ใกล้เคียง guided 30%+) คงอยู่ยาวนานกว่า 5 ปีมาก และ/หรือใช้ discount rate ต่ำกว่าที่สะท้อนความเชื่อว่า wide-moat monopoly ทำให้ cash flow มีความแน่นอนสูงเหมือนธุรกิจ non-cyclical — ในขณะที่ conquest ให้ growth fade เร็วกว่าและใช้ WACC ที่สะท้อน cyclical risk ของ semiconductor capex ผ่าน beta 1.39 ที่สูงกว่าตลาดทั่วไป
- **GuruFocus GF Value $1,196.15:** ใกล้กว่า Morningstar แต่ conquest base case ยังต่ำกว่า GuruFocus อีก ~39% — GF Value เป็น backward-looking historical-multiple regression ที่ยังคงอิง multiple ในอดีตของ ASML เองซึ่งถูก re-rate สูงขึ้นเรื่อยๆ จาก optimism หลายปีที่ผ่านมา ในขณะที่ conquest DCF สร้างจาก raw cash flow ล้วนๆ โดยไม่อิง multiple ในอดีตเลย ทำให้ penalize ราคาปัจจุบันหนักกว่า เพราะราคาที่ ~54x TTM FCF ต้องการ growth ที่สูงต่อเนื่องยาวนานกว่าที่ DCF นี้ยอมให้
- **สรุป:** Conquest เห็นด้วยกับทิศทางของ GuruFocus ว่าหุ้น**แพง** (ไม่ใช่ Fair แบบ Morningstar) แต่ conquest มองว่าแพงกว่าที่ GuruFocus ประเมินไว้อีกมาก — ผลนี้ทำให้ 2 ใน 3 แหล่ง (GuruFocus + Conquest) เห็นตรงกันว่าราคาปัจจุบัน **Expensive** ชัดเจน โดย Morningstar เป็นเสียงข้างน้อยที่มองว่า Fair — ทำลาย tie ที่ค้างไว้จากความขัดแย้งเดิมได้ ไปในทิศทาง Expensive
