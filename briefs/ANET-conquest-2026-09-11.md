# 💰 Conquest DCF: ANET — 2026-09-11
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (FY2026E):** Revenue guided $12.6B (+40% YoY, ยืนยันโดย guidance บริษัท) × FCF margin 47% (= FY2025 actual FCF margin, FCF ~$4.3B / revenue ~$9.0B) = **$5.92B**
  - ใช้ FY2026 (guided, มี actual Q1+Q2 แล้ว, Q3 guided ~$3.3B, เหลือ Q4) เป็นปี base แทน FY2025 actual เพราะเป็นปีที่ตลาดกำลัง price-in อยู่ตอนนี้
- **Revenue growth fade (ปี 1-5, FY2027-FY2031):** เริ่มจาก guided growth ปัจจุบัน 40% (FY2026) → fade เป็น **35% → 28% → 20% → 14% → 8%**
  - เหตุผล fade: (1) TAM ที่บริษัทประกาศเอง ($70B ปี 2028, $105B ปี 2029) ยังน้อยกว่า market cap ปัจจุบัน (~$250B) แล้ว — ตลาด price การเติบโตที่สูงกว่า TAM ที่ระบุไว้เอง ต้องระมัดระวังไม่ต่อ growth สูงยาวเกินไป (2) Nvidia (Spectrum-X, NVLink) แซงขึ้นเป็นอันดับ 1 ใน data-center Ethernet switch revenue share แล้วใน Q1 2026 (21.5% vs Arista 20.7%, จากแค่ 4% เมื่อ Q1 2024) — เป็นสัญญาณ competitive pressure เชิงโครงสร้างที่น่าจะกดอัตราเติบโตเร็วกว่าที่ guidance ปัจจุบันบอกในปีถัดๆ ไป (3) mean-reversion ทั่วไปของธุรกิจ hardware ที่โตเร็วจาก capex supercycle — cycle การเร่งลงทุนระดับ hyperscaler มักมี plateau หลัง 3-5 ปี
- **Terminal growth rate: 3%** — สูงกว่า GDP มาตรฐาน (2%) เล็กน้อยเพราะมี Wide Moat จริง (EOS single-software-stack = switching cost สูง) ทำให้มีโอกาสรักษา pricing power/market share ได้ดีกว่าธุรกิจทั่วไป แต่ไม่ให้สูงกว่านี้เพราะ gross margin เริ่มมีแนวโน้มถูกกดดัน (63% ใน guidance ล่าสุด) และมี direct competitor (Nvidia) เข้ามาแย่ง segment หลักแล้ว
- **WACC ≈ 11.3%:**
  - Risk-free rate: 4.8% (ประมาณจาก 10Y UST ปัจจุบัน ซึ่งอยู่ในระดับสูงจากความตึงเครียด US-Iran ช่วงต้นเดือน ก.ย. 2026 — แตะ 4.92% เมื่อ 10 ก.ย., ใช้ระดับใกล้เคียง 4.8% เป็นตัวแทน ไม่ใช้จุดสูงสุดของวันที่มี event เฉพาะกิจ)
  - Beta: 1.3 (ประมาณ — high-growth networking hardware มักมี beta 1.2-1.4x, ไม่มีตัวเลขที่ยืนยันได้แน่ชัดจากแหล่งข้อมูลที่ให้มา จึงเป็นการประมาณจากลักษณะธุรกิจ ไม่ใช่ตัวเลขจริง)
  - Equity risk premium: 5% (มาตรฐานตลาด)
  - WACC = 4.8% + 1.3 × 5% = **11.3%**
  - บริษัท net-cash (ไม่มีหนี้, D/E 0%) จึงใช้ cost of equity ตรงๆ เป็น WACC โดยไม่ต้อง weight กับ cost of debt
- **Shares outstanding:** ~1.26B diluted (คำนวณจาก market cap $250B ÷ ราคา $199.08 ≈ 1.256B, ตรงกับตัวเลขที่ให้มา)
- **Net cash:** $12.4B, zero debt

## DCF Calculation

| ปี | Revenue ($B) | Growth | FCF margin | FCF ($B) | Discount factor @11.3% | PV FCF ($B) |
|---|---|---|---|---|---|---|
| Base (FY26E) | 12.60 | 40% (guided) | 47% | 5.92 | — | — |
| Y1 (FY27) | 17.01 | 35% | 46% | 7.83 | 0.8985 | 7.04 |
| Y2 (FY28) | 21.77 | 28% | 46% | 10.02 | 0.8073 | 8.09 |
| Y3 (FY29) | 26.13 | 20% | 45% | 11.76 | 0.7252 | 8.53 |
| Y4 (FY30) | 29.79 | 14% | 45% | 13.40 | 0.6516 | 8.73 |
| Y5 (FY31) | 32.17 | 8% | 45% | 14.48 | 0.5855 | 8.48 |

Sum PV of Stage-1 FCF (Y1-Y5) ≈ **$40.86B**

**Terminal Value** = FCF₅ × (1+g) ÷ (WACC−g) = 14.48 × 1.03 ÷ (0.113−0.03) = 14.91 ÷ 0.083 ≈ **$179.7B**
PV of Terminal Value = 179.7 × 0.5855 ≈ **$105.2B**

**Enterprise Value** = 40.86 + 105.2 ≈ **$146.1B**
**Equity Value** = EV + Net cash = 146.1 + 12.4 ≈ **$158.5B**
**Fair Value per share** = 158.5B ÷ 1.256B ≈ **$126.2**

## Sensitivity (3 scenarios)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| 🐻 Bear | 12.3% | 2.5% | **$109.1** |
| ⚖️ Base | 11.3% | 3.0% | **$126.2** |
| 🐂 Bull | 10.3% | 3.5% | **$150.8** |

## เทียบราคาปัจจุบัน $199.08

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($126.2) อยู่ **+57.8%** และสูงกว่าแม้แต่ Bull case ($150.8) อยู่ **+32.0%** ด้วย

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $230** — ไกลจาก conquest base case มาก (+82.3% สูงกว่า conquest) เพราะ Morningstar ให้เครดิต Wide Moat มากกว่า (น่าจะใช้ terminal growth/margin สูงกว่า และ fade growth ช้ากว่าที่ conquest ประเมิน) — โดยเฉพาะ conquest มองว่า Nvidia เข้ามาแข่งในตลาด data-center Ethernet switching อย่างจริงจังแล้ว (แซงเป็นอันดับ 1 ใน Q1 2026) ซึ่งกดดัน durability ของ moat ในกรอบเวลา 5 ปีข้างหน้าที่ Morningstar's framework อาจไม่ได้ปรับลดเร็วพอ
- **GuruFocus GF Value ~$161** — ใกล้กว่ามาก (+27.6% สูงกว่า conquest base case) ทั้งสองฝั่งเห็นตรงกันในทิศทางว่าตลาด price การเติบโตเกินพื้นฐานที่สมเหตุสมผล แม้ methodology จะต่างกันโดยสิ้นเชิง (GuruFocus ใช้ backward historical-multiple regression, conquest ใช้ forward DCF จาก raw fundamentals)
- **สรุป:** conquest เห็นด้วยกับ **GuruFocus (Significantly Overvalued)** มากกว่า Morningstar (Fair-ish ที่ $230) อย่างชัดเจน — ทำให้ตอนนี้มี 2 ใน 3 แหล่งอิสระ (GuruFocus + Conquest) ที่ตัดสินว่าราคา $199.08 แพงเกินพื้นฐาน โดย conquest ยังประเมินอนุรักษ์นิยมกว่า GuruFocus ด้วยซ้ำ (แม้แต่ bull case ของ conquest ที่ $150.8 ก็ยังต่ำกว่า GF Value $161) เหตุผลหลักที่ conquest มองต่างจาก Morningstar คือ TAM ที่บริษัทระบุเอง ($70-105B ปี 2028-29) ก็ยังน้อยกว่า market cap ปัจจุบันแล้ว และการที่ Nvidia แซงขึ้นเป็นผู้นำตลาด data-center switch เป็นความเสี่ยงเชิงโครงสร้างที่ conquest ให้น้ำหนักมากกว่าใน growth fade schedule
