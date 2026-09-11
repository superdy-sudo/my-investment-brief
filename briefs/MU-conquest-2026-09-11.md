# 💰 Conquest DCF: MU (Micron Technology) — 2026-09-11
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

- **Base FCF (Year 0, TTM FY2026 โดยประมาณ):** ~$49.0B
  - รวม Q1 FY2026 FCF $3.9B (ตัวจริง) + Q2 FY2026 FCF ประมาณ $6.9B (ประมาณจาก OCF $11.90B โดยใช้ FCF-conversion ระหว่างค่า Q1 (46%) กับ Q3 (69%) — **ตัวเลขนี้เป็นการประมาณ ไม่ใช่ตัวจริง เพราะไม่มี capex Q2 แยกให้**) + Q3 FY2026 FCF $17.562B (ตัวจริง) + Q4 FY2026 FCF ประมาณ $21.0B (ประมาณจาก revenue guidance กลาง $50B × FCF margin ~42% ตาม Q3 — **เป็นการประมาณจาก guidance ยังไม่ประกาศจริง**)
  - Base FCF นี้คือปีที่ peak ของ upcycle แล้ว ไม่ใช่ระดับที่ยั่งยืน

- **Growth fade (FCF, ไม่ใช่ revenue เฉยๆ — ผูก margin normalization เข้าไปในตัวเลขนี้เลย):**
  - ปี 1 (FY2027): **+15%** → $56.4B (HBM ยัง sold-out ถึงหลัง 2027 ตาม catalyst ที่ให้มา ดีมานด์ยังแกร่ง แต่เริ่มชะลอจากฐานที่สูงมาก)
  - ปี 2 (FY2028): **-5%** → $53.5B (คู่แข่ง Samsung/SK Hynix เริ่มเพิ่มกำลังผลิตตอบสนอง HBM4/AI demand ราคาเริ่มอ่อนตัว margin เริ่มบีบ)
  - ปี 3 (FY2029): **-25%** → $40.2B (จำลอง mid-cycle correction ตาม pattern วัฏจักร DRAM/NAND ที่เกิดซ้ำทุก upcycle — capacity ใหม่ทั่วอุตสาหกรรมเริ่ม online พร้อมกัน ราคาร่วง)
  - ปี 4 (FY2030): **-30%** → $28.1B (จำลอง trough/bust year แบบ FY2023 ที่เกิดขึ้นจริงมาแล้ว — แต่รุนแรงน้อยกว่าปี 2023 เพราะ AI structural demand เป็น floor บางส่วน)
  - ปี 5 (FY2031): **+10%** → $30.9B (เริ่มฟื้นตัวช่วงต้นวัฏจักรใหม่ margin กลับมา stabilize)
  - **เหตุผลของ fade schedule นี้:** โจทย์บังคับห้ามใช้ margin 84.9% ปัจจุบันเป็นค่าถาวร และ Micron มี track record วัฏจักร boom-bust ชัดเจนทุกรอบตั้งแต่กลางยุค 1990s (ล่าสุด FY2023: revenue -49%, GM ร่วงจาก 45.2% เป็น -9.1%, ขาดทุน $5.8B) จึงใส่ bust year (ปี 3-4) เข้าไปตรงๆ ใน stage 1 แทนที่จะ fade แบบ smooth monotonic ซึ่งจะประเมิน risk ของวัฏจักรต่ำเกินไป

- **Terminal growth: 2.5%** (ผูกกับ GDP/inflation ระยะยาว — ไม่ให้ premium สูงกว่านี้เพราะ Morningstar เองให้ rating "No Moat" คือธุรกิจ commodity ไม่มี pricing power ที่ยั่งยืน ต่างจากบริษัทมี moat ที่ใส่ terminal growth สูงกว่าได้)

- **WACC: 13.5%**
  - Risk-free rate: 4.85% (10Y Treasury, จาก daily brief ช่วง 2026-09-10/11 ที่เห็น yield 4.80-4.92%)
  - Beta: **1.7 (ประมาณ ไม่ใช่ตัวเลขจริงจาก data provider)** — semiconductor/memory cyclical มักมี beta สูงกว่าตลาดมากเพราะ earnings volatility รุนแรง (กำไร/ขาดทุนสลับขั้วทุกวัฏจักร)
  - Equity risk premium: 5% (มาตรฐาน)
  - Cost of equity = 4.85% + 1.7×5% = 13.35% ≈ ปัดเป็น **13.5%** (เพิ่ม premium เล็กน้อยจาก Very High Uncertainty ที่ Morningstar เองก็ให้ rating ไว้)
  - ใช้ cost of equity ตรงๆ เป็น WACC เพราะ MU เป็น net cash (~$23.75B net cash, debt แค่ ~$6.38B เทียบ market cap $1.1T แทบไม่มีนัยสำคัญ)

- **Shares outstanding:** ~1.129B (diluted)
- **Net cash:** ~$23.75B (cash $26.02B − debt ~$6.38B ตาม 10-Q ก.พ. 2026, ปรับด้วยตัวเลข debt ที่ต่ำกว่าเล็กน้อย ณ พ.ค. 2026)

## DCF Calculation

| ปี | FCF ($B) | Growth | Discount factor @13.5% | PV ($B) |
|---|---|---|---|---|
| Y0 (base) | 49.0 | — | — | — |
| Y1 (FY27) | 56.4 | +15% | 0.8811 | 49.65 |
| Y2 (FY28) | 53.5 | -5% | 0.7764 | 41.56 |
| Y3 (FY29) | 40.2 | -25% | 0.6841 | 27.46 |
| Y4 (FY30) | 28.1 | -30% | 0.6027 | 16.95 |
| Y5 (FY31) | 30.9 | +10% | 0.5310 | 16.42 |

- Sum PV Stage 1 = **$152.0B**
- Terminal Value (end of Y5) = FCF_Y5 × (1+g) ÷ (WACC−g) = 30.9 × 1.025 ÷ (0.135−0.025) = **$288.1B**
- PV of Terminal Value = 288.1 × 0.5310 = **$153.0B**
- **Enterprise Value = 152.0 + 153.0 = $305.0B**
- + Net cash $23.75B → **Equity Value = $328.8B**
- ÷ Shares outstanding 1.129B → **Fair Value = $291/share**

## Fair Value

- Bear case (WACC 14.5%, terminal g 2.0%): **$267/share**
- **Base case: $291/share**
- Bull case (WACC 12.5%, terminal g 3.0%): **$323/share**

**Fair Value (conquest DCF): $291/share** (range $267-$323)

## เทียบราคาปัจจุบัน $979.94

🔴 **Expensive** — ราคาสูงกว่า Base case FV **+237%**

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $850** — ห่างจาก conquest base case มาก ($850 vs $291, +192%) เพราะ Morningstar เป็น forward analyst DCF ที่ดูเหมือนไม่ได้บังคับใส่ bust-year ชัดเจนขนาดนี้ในโมเดล น่าจะให้ margin peak (84.9% GM) คงอยู่นานกว่า และ/หรือใช้ terminal growth/WACC ที่ผ่อนกว่า แม้ตัวเองจะให้ rating "No Moat, Very High Uncertainty" ก็ตาม — ดูเป็นความขัดแย้งภายในของ Morningstar เอง (rating บอกว่าไม่มี moat แต่ FV กลับ assume ความยั่งยืนของกำไรสูง)
- **GuruFocus GF Value $627.48** — ใกล้ conquest base case กว่า Morningstar แต่ยังห่างพอสมควร ($627 vs $291, +115%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่อิง P/E, P/FCF เฉลี่ยย้อนหลังของ MU เอง ซึ่งรวมทั้งปี boom และปี bust ในอดีตไว้ด้วย จึงมี mean-reversion อยู่ในตัวอยู่แล้ว แต่ยังไม่ได้ตัดกำไร peak ปัจจุบันออกแรงเท่า DCF ที่จำลอง bust year ตรงๆ
- **สรุป:** Conquest DCF เป็นมุมมองที่ bearish ที่สุดในสามแหล่ง ไม่ได้เอนไปทาง Morningstar หรือ GuruFocus ฝั่งใดฝั่งหนึ่ง แต่ตัดสินใจอิสระว่าราคาปัจจุบัน $979.94 แพงเกินจริงมาก เพราะตลาดกำลัง price-in ว่า margin ระดับ peak (GM 84.9%) จะอยู่ต่อเนื่องยาวนาน ทั้งที่ประวัติศาสตร์ 30 ปีของอุตสาหกรรม DRAM/NAND ไม่เคยเกิดขึ้นแบบนั้น — นี่คือความเห็นอิสระที่ไม่ได้ "เข้าข้าง" forward-methodology (Morningstar) หรือ backward-methodology (GuruFocus) เพียงแต่บังเอิญอยู่ต่ำกว่าทั้งคู่มากเพราะให้น้ำหนักกับความเสี่ยงวัฏจักรมากกว่า

## หมายเหตุความไม่แน่นอน
- Base FCF (Q2 และ Q4 FY2026) เป็นตัวเลขประมาณจาก guidance/conversion ratio ไม่ใช่ตัวจริงทั้งหมด — ถ้า Q4 earnings จริง (30 ก.ย. 2026) ต่างจาก guidance มาก ควรคำนวณใหม่
- Beta 1.7 เป็นค่าประมาณจาก sector-level cyclicality ไม่ใช่ตัวเลขจาก data provider โดยตรง
- โมเดลนี้ตั้งใจใส่ bust-year (ปี 3-4) เข้าไปตรงๆ ตาม track record วัฏจักรของอุตสาหกรรม ถ้า AI-memory demand เปลี่ยนโครงสร้างอุตสาหกรรมจริง (ไม่ boom-bust แบบเดิมอีกต่อไป) Fair Value นี้จะต่ำเกินไป — เป็นความเสี่ยงหลักของสมมติฐานนี้ที่ควรจับตา
