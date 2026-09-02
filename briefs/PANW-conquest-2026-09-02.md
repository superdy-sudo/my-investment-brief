# 💰 Conquest DCF: PANW — 2026-09-02
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (FY2026, ปีงบล่าสุดที่ปิดแล้ว):**
- Revenue FY2026 ≈ $11.41B — คำนวณย้อนจาก FY2027 guidance midpoint $14.15B ÷ (1+24%) เพราะบริษัท guide FY2027 โต ~24% YoY จาก FY2026
- FCF margin FY2026 (guided) 37.5% → Base FCF ≈ $4.28B

**Growth fade (Stage 1, ปีที่ 1-5):**
| ปี | Revenue growth | เหตุผล |
|---|---|---|
| 1 (FY2027) | 24% | ตัวเลข guidance จริงของบริษัท ($14.10-14.20B) ไม่ใช่ประมาณเอง |
| 2 | 21% | ยังได้แรงหนุนจาก RPO +34% YoY (backlog มองเห็นล่วงหน้า) และ NGS ARR +63% YoY ที่ยังเร่งตัว — ลดจากปีก่อนแบบค่อยเป็นค่อยไปเพราะ platformization ยังมี momentum แข็ง |
| 3 | 18% | เริ่มเข้าสู่ mean-reversion ปกติของ SaaS/cybersecurity ขนาดใหญ่ที่ revenue base โตข้ามหลัก $17-20B แล้ว |
| 4 | 14% | คู่แข่ง (CrowdStrike, Fortinet, Microsoft Security, Zscaler) เริ่มกัดส่วนแบ่งตลาดใน segment ที่ platformization ยังไม่ lock-in เต็มที่ |
| 5 | 10% | เข้าใกล้ terminal, TAM claim ของบริษัทเอง ($360B, ~1.2x mkt cap) แคบกว่าที่จะ sustain growth สูงระยะยาว (ดู Layer 2 item 2 ใน brief หลัก — data conflict ยังไม่ resolve) |

**Terminal growth: 3%** — ผูกกับ long-run nominal GDP/inflation มาตรฐาน ไม่ยกสูงกว่านี้แม้มี Wide Moat เพราะ TAM ที่บริษัทยืนยันเองยังแคบ (ไม่ใช่ moat ที่ยืนยันได้ว่า pricing power จะขยาย TAM ได้ไม่จำกัด)

**FCF margin trajectory:** ขยายจาก 37.5% (Y1) → 39.5% (Y5) จาก operating leverage ปกติของ SaaS ที่ scale ขึ้น (สอดคล้องกับ TTM 38.5% ปัจจุบันที่ใกล้เพดานบนแล้ว)

**WACC: 10.5%**
- Risk-free rate: 4.80% (10Y Treasury, 2026-09-02 — ตรงกับที่ brief พูดถึง bond yield พุ่งเป็นปัจจัย macro risk-off)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด)
- Beta: ~1.15 (ประมาณ — แหล่งข้อมูลกระจายมาก: CNBC 0.91, TradingView/MarketChameleon 1.46 ใช้ค่ากลางเนื่องจากหุ้นผันผวนสูงระยะสั้น เช่น -7.75% วันนี้ แต่ cash-heavy balance sheet ลดความเสี่ยง systematic บางส่วน)
- WACC = 4.80% + 1.15 × 5.0% = 10.55% ≈ **10.5%** — ใช้ cost of equity ตรงๆ เพราะบริษัทอยู่ใน net-cash position (net cash ~$0.98B, interest coverage ~532x)

**Shares outstanding:** ~815M (diluted, จาก brief)
**Net cash:** ~$0.98B (cash+ST investments $3.11B − total debt $2.13B)

## DCF Calculation

| ปี | Revenue ($B) | Growth | FCF margin | FCF ($B) | Discount factor @10.5% | PV FCF ($B) |
|---|---|---|---|---|---|---|
| Y1 (FY27) | 14.15 | 24% | 37.5% | 5.31 | 0.9050 | 4.80 |
| Y2 | 17.12 | 21% | 38.0% | 6.51 | 0.8189 | 5.33 |
| Y3 | 20.20 | 18% | 38.5% | 7.78 | 0.7411 | 5.76 |
| Y4 | 23.03 | 14% | 39.0% | 8.98 | 0.6706 | 6.02 |
| Y5 | 25.33 | 10% | 39.5% | 10.00 | 0.6068 | 6.07 |

Sum of PV(FCF Y1-Y5) ≈ **$27.98B**

Terminal Value (end of Y5) = $10.00B × 1.03 ÷ (0.105 − 0.03) = **$137.33B**
PV of Terminal Value = $137.33B × 0.6068 = **$83.34B**

**Enterprise Value = $27.98B + $83.34B = $111.32B**
+ Net cash $0.98B
**Equity Value ≈ $112.30B**

÷ 815M diluted shares = **Fair Value ≈ $138/share**

## Fair Value

- Bear case (WACC 11.5%, terminal g 2.5%): **$115.70**
- **Base case: $137.80**
- Bull case (WACC 9.5%, terminal g 3.5%): **$171.00**

## เทียบราคาปัจจุบัน $334.02

🔴 **Expensive** — ราคาสูงกว่า Base case FV ถึง **+142.5%** (ต้องร่วงลง ~59% เพื่อกลับเข้า Base case FV, หรือ ~48% เพื่อถึง Bull case FV) — เป็นสถานะ Expensive ที่ชัดเจนที่สุดในบรรดาสามแหล่งข้อมูล

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $285** — ไกลจาก conquest base case มาก (conquest ต่ำกว่า MS ถึง -51.6%) เหตุผลที่ต่างกัน: MS เป็น forward-DCF ของนักวิเคราะห์ที่ผูกกับ Wide Moat rating น่าจะให้ terminal growth หรือ competitive-advantage period ยาวกว่าที่ conquest ใช้ (conquest ยึด TAM claim ของบริษัทเอง $360B ที่ยังแคบเป็นเพดานไม่ให้ยก terminal growth สูง) และอาจใช้ WACC ต่ำกว่าเพราะเชื่อมั่นใน moat มากกว่า
- **GuruFocus GF Value $214.72** — ใกล้กว่า MS แต่ conquest ก็ยังต่ำกว่า GF อีก -35.8% เหตุผล: GF เป็น backward-looking historical-multiple regression ที่ยังอิง multiple ในอดีตของ PANW เอง (ซึ่งช่วงหลังตลาดให้ premium สูงกว่าที่ fundamentals bottom-up จะ justify) ขณะที่ conquest DCF ยึด raw growth-fade + WACC มาตรฐานล้วนๆ ไม่มี multiple ในอดีตมาถ่วง
- **สรุป:** Conquest เห็นด้วยกับทิศทาง "Expensive" ของ GuruFocus มากกว่า Morningstar (แม้ตัวเลขจะต่ำกว่า GF เองอีก) — ทำให้เสียงแตก 2 (GuruFocus + Conquest) ต่อ 1 (Morningstar) เอียงไปทาง **Expensive** เป็นข้อสรุป — สอดคล้องกับ pattern ที่เคยสังเกตว่า conquest DCF มักให้ผล Expensive เป็นส่วนใหญ่ (ควรอ่านเป็น "มุมมองที่เข้มที่สุดในสามแหล่ง" ไม่ใช่คำตัดสินสุดท้ายเพียงอย่างเดียว — ดู feedback-conquest-bias-toward-expensive ในความจำ)

Sources: [10-Year Treasury Yield](https://tradingeconomics.com/united-states/government-bond-yield), [PANW Beta - GuruFocus](https://www.gurufocus.com/term/beta/PANW/Beta/Palo%20Alto%20Networks), [PANW Beta - TradingView](https://www.tradingview.com/symbols/NASDAQ-PANW/)
