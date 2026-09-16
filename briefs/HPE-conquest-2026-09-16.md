# 💰 Conquest DCF: HPE — 2026-09-16
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- **Base FCF (Year 0, ~FY2026 run-rate):** $3.99B (TTM ต้นทาง, source: stockanalysis.com) — แต่ใช้ FY2027 company FCF guidance ≥$5B เป็น anchor ปีที่ 1 แทนการต่อ growth rate เอง เพราะบริษัทให้ guidance ตรงมาแล้วและสอดคล้องกับ margin expansion จาก Juniper synergy ที่กำลังเกิดขึ้นจริง
- **Growth fade (revenue, ใช้ผลักดัน FCF ปีต่อๆ ไปจาก anchor ปี 1):**
  - ปี 1 (FY27): 15% (จุดกลาง guided 13-17%)
  - ปี 2 (FY28): 11%
  - ปี 3 (FY29): 8% (ลู่เข้าใกล้ organic growth ex-Juniper ที่บริษัทเปิดเผยเอง ~7% ต้นปี FY26)
  - ปี 4 (FY30): 5.5%
  - ปี 5 (FY31): 3.5%
  - **เหตุผล:** ธุรกิจหลักเป็น "No-Moat" hardware OEM ตาม Morningstar (commodity margin ปกติ 6-8%) — headline growth 34% ปี FY26 เกือบทั้งหมดมาจาก Juniper M&A consolidation ไม่ใช่ organic (บริษัทเปิดเผยเอง organic ex-Juniper ~7%) และ guidance FY27 เองก็ชี้ว่ากำลังชะลอเหลือ 13-17% ทันทีที่ Juniper anniversary — ไม่มีเหตุผลให้ extrapolate growth สูงต่อเนื่อง ต้อง fade เร็วกว่าธุรกิจมี moat ปกติ เพราะไม่มี pricing power ป้องกัน margin/growth จากคู่แข่ง Dell/Cisco/Supermicro
- **Terminal growth:** 2.0% (ต่ำกว่าค่ากลาง 2-3% เล็กน้อย เพราะไม่มี moat ที่ยั่งยืน — คอมโมดิตี้ฮาร์ดแวร์ระยะยาวมักโตช้ากว่า GDP nominal เนื่องจากแรงกดดัน price/unit ต่อเนื่อง)
- **WACC: 10.5%**
  - Risk-free rate: 10Y Treasury = **5.01%** (2026-09-15, พุ่งแตะสูงสุดตั้งแต่ 2007 จากแรงกดดัน FOMC/เงินเฟ้อสัปดาห์นี้ — source: tradingeconomics.com, cnbc.com)
  - Beta: **~1.4** (ประมาณ, เฉลี่ยจาก CNBC 1.39 และ StockAnalysis 1.45 — ตัวเลขจากบางแหล่งกระจายกว้าง 0.87-1.63 จึงใช้ค่าเฉลี่ยกลุ่มหลักเป็นการประมาณ)
  - Equity Risk Premium: 5.0% (มาตรฐาน)
  - Cost of equity = 5.01% + 1.4×5.0% ≈ 12.0%
  - Cost of debt (pretax) ≈ 5.5% (ประมาณจาก rate environment ปัจจุบัน, interest coverage 10.87x แข็งแรง) → after-tax (21%) ≈ 4.35%
  - Weight: Equity 84% (market cap $73.8B), Debt 16% (net debt $14.0B, EV $87.8B)
  - WACC = 0.84×12.0% + 0.16×4.35% ≈ **10.5%**
- Shares outstanding: 1.32B
- Net debt: $14.0B

## DCF Calculation (Base case: WACC 10.5%, terminal growth 2.0%)

| ปี | Growth | FCF ($B) | Discount factor | PV ($B) |
|---|---|---|---|---|
| FY27 (Y1) | 15% (guided) | 5.00 (company guidance) | 0.905 | 4.53 |
| FY28 (Y2) | 11% | 5.55 | 0.819 | 4.55 |
| FY29 (Y3) | 8% | 5.99 | 0.741 | 4.44 |
| FY30 (Y4) | 5.5% | 6.32 | 0.671 | 4.24 |
| FY31 (Y5) | 3.5% | 6.54 | 0.607 | 3.97 |

- Sum PV Stage 1 = **$21.72B**
- Terminal Value (ปี 5) = 6.54 × 1.02 / (0.105 − 0.02) = **$78.48B**
- PV of Terminal Value = 78.48 × 0.607 = **$47.65B**
- **Enterprise Value = 21.72 + 47.65 = $69.37B**
- Equity Value = EV − Net Debt = 69.37 − 14.0 = **$55.37B**
- **Fair Value/share = 55.37B ÷ 1.32B = $41.95**

## Fair Value (Sensitivity: WACC ±1%, terminal growth ±0.5%)
- Bear case (WACC 11.5%, g 1.5%): **$34.61**
- **Base case (WACC 10.5%, g 2.0%): $41.95**
- Bull case (WACC 9.5%, g 2.5%): **$52.38**

## เทียบราคาปัจจุบัน $55.88
🔴 **Expensive** — ราคาสูงกว่า Base case FV ($41.95) อยู่ **+33.2%** (>20% threshold)
หมายเหตุ: แม้ใช้ **Bull case** ($52.38, WACC ต่ำสุด + terminal growth สูงสุดในช่วง sensitivity) ราคาตลาด $55.88 ก็ยังสูงกว่าอยู่ +6.7% — แปลว่าแม้มองในแง่ดีที่สุดในกรอบ sensitivity นี้ ราคาก็ยัง priced-in เกินกว่าที่ fundamentals รองรับ

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $64** — ไกลจาก conquest base case มาก (conquest ต่ำกว่า 34%) เพราะ Morningstar เป็น forward-DCF ที่ (สันนิษฐาน) ยังให้น้ำหนักกับ headline growth 34-37% และ AI/Cloud margin expansion (7%→17%) มากกว่า ไม่ได้ fade เร็วเท่า conquest ที่ยึดตาม guidance FY27 ชะลอ + No-Moat label ของ Morningstar เอง (แปลกที่ Morningstar ให้ FV สูงทั้งที่ตัวเองเรียก HPE ว่า "No-Moat") และอาจใช้ WACC ต่ำกว่าเพราะไม่ได้ปรับตาม 10Y yield ที่พุ่งแตะ 5% สัปดาห์นี้
- **GuruFocus GF Value $27.74** — ใกล้เชิงทิศทาง (ทั้งคู่บอก Expensive) แต่ conquest ($41.95) สูงกว่า GuruFocus เกือบเท่าตัว เพราะ GF Value เป็น backward-looking historical-multiple regression ที่น่าจะโดนกดจากช่วงที่ HPE เทรดที่ multiple ต่ำมาหลายปี (ก่อน AI/Juniper) ไม่ได้ให้เครดิตกับ FCF guidance FY27 ≥$5B และ deleveraging ที่เกิดขึ้นจริง
- **สรุป:** Conquest เห็นด้วยกับทิศทาง **GuruFocus (Expensive)** มากกว่า Morningstar (Fair) — แม้ตัวเลขจะไม่ตรงกันเป๊ะ (conquest อยู่กึ่งกลางระหว่างสองแหล่งในเชิงตัวเงิน แต่ผลลัพธ์ bucket ตรงกับ GuruFocus) เหตุผลหลักคือ **risk-free rate ที่พุ่งแตะ 5.01% สัปดาห์นี้ (สูงสุดตั้งแต่ 2007) ดัน WACC ขึ้นมาที่ ~10.5%** ซึ่งกดมูลค่าปัจจุบันของ terminal value ลงมาก บวกกับการปฏิเสธที่จะ extrapolate headline growth 34% ที่ไม่ใช่ organic ต่อ — ผลคือ **2 ใน 3 แหล่ง (GuruFocus + Conquest) เห็นตรงกันว่า Expensive** → ยืนยัน Action = Avoid ที่ Layer 1/2 สรุปไว้แล้วจาก moat/growth quality
