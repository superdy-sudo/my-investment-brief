# 💰 Conquest DCF: ANET — 2026-08-19
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (FY2026E):** Revenue guided $12.6B × FCF margin 47% (FY2025 actual FCF margin, ~$4.3B FCF / ~$9.0B revenue) = **$5.92B**
  - ใช้ FY2026 (guided, เกือบปิดปีแล้ว — Q1+Q2 actual รายงานแล้ว, Q3 guided, เหลือ Q4) เป็นปี base แทน FY2025 actual เพราะ FY2026 คือปีที่ market กำลัง price-in อยู่ตอนนี้
- **Revenue growth fade (ปี 1-5, FY2027-FY2031):** เริ่มจาก guided growth ปัจจุบัน 40% (FY2026) → fade ลงเป็น **35% → 28% → 20% → 14% → 8%**
  - เหตุผล fade: (1) TAM broadest estimate ~$200B ยังน้อยกว่า market cap ปัจจุบัน $245B แล้ว แปลว่าตลาดกำลัง price การเติบโตเกิน TAM ที่ระบุไว้ไปมาก ต้องระมัดระวัง (2) Nvidia เข้ามาแข่งอย่างจริงจังและกลายเป็น #1 vendor ใน data-center Ethernet switching ไปแล้วใน Q1 2026 (segment revenue ของ Nvidia +193% YoY) — เป็นสัญญาณ competitive pressure ที่จะกดอัตราเติบโตของ ANET ลงเร็วกว่าที่ guidance บอกในปีถัดๆ ไป (3) mean-reversion ทั่วไปของธุรกิจ hardware/semi ที่โตเร็วจาก AI capex cycle — cycle capex ระดับ hyperscaler มักมี plateau หลัง 3-5 ปีของการเร่งลงทุน
- **Terminal growth rate: 3%** — สูงกว่า GDP มาตรฐาน (2%) เล็กน้อยเพราะมี Wide Moat จริง (EOS single software stack = switching cost สูง, process power) ทำให้น่าจะรักษา pricing power และ market share ได้ดีกว่าธุรกิจทั่วไปในระยะยาว แต่ไม่ใช้สูงกว่านี้เพราะ gross margin กำลังลดลงแล้ว (63.4% จาก 65.6% YoY) ซึ่งเป็นสัญญาณว่า moat ไม่ได้แข็งพอจะกันการแข่งขันด้าน pricing ได้ 100%
- **WACC ≈ 11%:**
  - Risk-free rate: 4.3% (ประมาณจาก 10Y UST ระดับปัจจุบัน)
  - Beta: 1.3 (ประมาณ — high-growth semiconductor/networking hardware มักมี beta 1.2-1.4x, ไม่มีตัวเลขที่หาได้แน่ชัดในไฟล์ brief ต้นทาง จึงใช้ค่าประมาณจากลักษณะธุรกิจ)
  - Equity risk premium: 5% (มาตรฐานตลาด)
  - WACC = 4.3% + 1.3 × 5% = 10.8% → ปัดเป็น 11%
  - บริษัท net-cash (ไม่มีหนี้) จึงใช้ cost of equity ตรงๆ เป็น WACC โดยไม่ต้อง weight กับ cost of debt
- **Shares outstanding:** ~1.26B (diluted, จาก market cap $245B ÷ ราคา $189.51 ≈ 1.29B แต่ใช้ตัวเลข shares outstanding ที่ระบุในไฟล์ต้นทาง 1.26B)
- **Net cash:** $12.35B, zero debt

## DCF Calculation

| ปี | Revenue ($B) | Growth | FCF margin | FCF ($B) | Discount factor @11% | PV FCF ($B) |
|---|---|---|---|---|---|---|
| Base (FY26E) | 12.60 | 40% (guided) | 47% | 5.92 | — | — |
| Y1 (FY27) | 17.01 | 35% | 46% | 7.83 | 0.9009 | 7.05 |
| Y2 (FY28) | 21.77 | 28% | 46% | 10.02 | 0.8116 | 8.13 |
| Y3 (FY29) | 26.13 | 20% | 45% | 11.76 | 0.7312 | 8.60 |
| Y4 (FY30) | 29.79 | 14% | 45% | 13.40 | 0.6587 | 8.83 |
| Y5 (FY31) | 32.17 | 8% | 45% | 14.48 | 0.5935 | 8.59 |

Sum PV of Stage-1 FCF (Y1-Y5) ≈ **$41.2B**

**Terminal Value** = FCF₅ × (1+g) ÷ (WACC−g) = 14.48 × 1.03 ÷ (0.11−0.03) = 14.91 ÷ 0.08 ≈ **$186.4B**
PV of Terminal Value = 186.4 × 0.5935 ≈ **$110.6B**

**Enterprise Value** = 41.2 + 110.6 ≈ **$151.8B**
**Equity Value** = EV + Net cash = 151.8 + 12.35 ≈ **$164.2B**
**Fair Value per share** = 164.2B ÷ 1.26B ≈ **$130.3**

## Sensitivity (3 scenarios)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| 🐻 Bear | 12% | 2.5% | **$111.9** |
| ⚖️ Base | 11% | 3.0% | **$130.3** |
| 🐂 Bull | 10% | 3.5% | **$157.1** |

## เทียบราคาปัจจุบัน $189.51

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($130.3) อยู่ **+45.4%** และสูงกว่าแม้แต่ Bull case ($157.1) อยู่ +20.6% ด้วย

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $230** — ไกลจาก conquest base case มาก (+76.5% สูงกว่า) เพราะ Morningstar ให้เครดิต Wide Moat มากกว่านี้ (น่าจะใช้ terminal growth/margin ที่สูงกว่า และอาจไม่ fade growth ลงเร็วเท่าที่ conquest ประเมิน — โดยเฉพาะ conquest มองว่า Nvidia เข้ามาแข่งในตลาด data-center Ethernet switching อย่างจริงจังแล้ว ซึ่งกดดัน durability ของ moat ระยะกลาง)
- **GuruFocus GF Value $142.75** — ใกล้กว่ามาก (+9.6% สูงกว่า conquest base case) ทั้งสองฝั่งเห็นตรงกันว่าตลาดกำลัง price การเติบโตเกินพื้นฐานที่สมเหตุสมผล แม้ methodology จะต่างกัน (GuruFocus ใช้ backward historical-multiple regression, conquest ใช้ forward DCF จาก raw fundamentals)
- **สรุป:** conquest เห็นด้วยกับ **GuruFocus (Expensive)** มากกว่า Morningstar (Fair) อย่างชัดเจน — ทำให้ตอนนี้มี 2 ใน 3 แหล่งอิสระ (GuruFocus + Conquest) ที่ตัดสินว่าราคา $189.51 แพงเกินพื้นฐาน แม้ conquest จะประเมินต่ำกว่า GuruFocus อีกด้วยซ้ำ (bear case ของ conquest ที่ $111.9 ยังต่ำกว่า GF Value) เหตุผลหลักที่ conquest มองต่างจาก Morningstar คือ TAM ที่ระบุเอง ($200B broadest estimate) ก็ยังน้อยกว่า market cap ปัจจุบันแล้ว และการเข้ามาแข่งของ Nvidia เป็นความเสี่ยงเชิงโครงสร้างที่ Morningstar's Wide Moat framework อาจไม่ได้ปรับลดเร็วพอ
