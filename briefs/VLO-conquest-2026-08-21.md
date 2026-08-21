# 💰 Conquest DCF: VLO — 2026-08-21
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF normalization — จุดสำคัญที่สุดของโมเดลนี้:**
Q2 2026 OCF $5.6B/ไตรมาส คือ **peak-cycle earnings** จาก crack spread ที่พุ่ง +91% YoY ($12.35→$23.62/bbl) ในขณะที่ throughput แทบไม่ขยับ (~3.0mm bpd ทั้งสองไตรมาส) — ห้าม annualize ตัวเลขนี้ตรงๆ (จะได้ ~$22B/ปี ซึ่งเกินจริงมาก) เพราะ margin ระดับนี้เกิดจาก Middle East/Hormuz supply stress ที่เป็นเหตุการณ์ชั่วคราวตามประวัติศาสตร์ (Katrina, 2008, 2022 ก็ mean-revert เร็ว)

วิธี normalize: ใช้ Q2 2025 (net income $714M, margin $12.35/bbl) เป็น proxy ของสภาวะ "ปกติ/mid-cycle" (อยู่ในกรอบ crack spread ปกติ $10-20/bbl ตามที่ระบุใน Bear case) เทียบกับ Q2 2026 ที่เป็น peak แล้วสร้าง fade path ที่ยอมให้ margin สูงคงอยู่บางส่วนในปีที่ 1-2 (geopolitical tension อาจยังไม่คลี่คลายทันที ตาม Bull case #1) ก่อน converge กลับสู่ mid-cycle ในปีที่ 3-5

- **Year 1 FCF: $6.5B** — margin ยังสูงบางส่วน (geopolitical stress ยังไม่คลี่คลายทันที)
- **Year 2 FCF: $5.0B** — เริ่ม fade
- **Year 3 FCF: $4.0B** — converge เข้าใกล้ mid-cycle
- **Year 4 FCF: $3.8B** — mid-cycle stable (ใกล้เคียง Q2'25 annualized ~$2.9B แต่ปรับขึ้นเล็กน้อยเผื่อ optimization capex เล็กๆ เช่น St. Charles FCC upgrade ที่ช่วย margin/bbl ระยะยาว)
- **Year 5 FCF: $3.8B** — flat (mature/declining industry, ไม่มี volume growth engine — renewable diesel expansion ถูก pause)

**Terminal growth: 1.5%** — ต่ำกว่ามาตรฐาน 2-3% โดยตั้งใจ เพราะ refining เป็นอุตสาหกรรม mature/declining ในสหรัฐฯ (ไม่มีโรงกลั่นใหม่มาหลายสิบปี, EV adoption กัดกร่อน gasoline demand ระยะยาว) — Narrow Moat เท่านั้น ไม่มี pricing power ที่ยั่งยืนพอจะ justify terminal growth ระดับ GDP เต็มที่

**WACC: 9.5%**
- Risk-free rate: 4.3% (10Y UST ปัจจุบัน)
- Beta: ~1.1 (ประมาณ — refiner หุ้น cyclical/commodity มี volatility สูงกว่าตลาดปานกลาง ไม่มีตัวเลข beta ที่แม่นยำจาก source เดียว จึงใช้ค่าประมาณตามลักษณะธุรกิจ)
- ERP: 5%
- Cost of equity ≈ 4.3% + 1.1×5% = 9.8% — ปรับลงเล็กน้อยเป็น 9.5% เพื่อสะท้อน weighted cost of debt (net debt-to-cap เพียง 11%, debt cost ต่ำกว่า equity cost มาก, interest coverage 7.8x)

**Shares outstanding: ~297M**
**Net debt: -$1.2B** (cash $7.9B − debt $9.1B → net cash เล็กน้อย, ใกล้ neutral)

## DCF Calculation (Base Case, WACC 9.5%, terminal g 1.5%)

| Year | FCF | Discount Factor | PV |
|---|---|---|---|
| 1 | $6.5B | 0.913 | $5.94B |
| 2 | $5.0B | 0.834 | $4.17B |
| 3 | $4.0B | 0.762 | $3.05B |
| 4 | $3.8B | 0.696 | $2.64B |
| 5 | $3.8B | 0.635 | $2.41B |

Sum PV of FCF (Yr1-5) = **$18.21B**

Terminal Value = FCF5 × (1+g) / (WACC−g) = $3.8B × 1.015 / (0.095−0.015) = **$48.2B**
PV of Terminal Value = $48.2B × 0.635 = **$30.62B**

Enterprise Value = $18.21B + $30.62B = **$48.83B**
Equity Value = EV + cash − debt = $48.83B + $7.9B − $9.1B = **$47.63B**

**Fair Value per share = $47.63B / 297M shares = ~$160**

## Fair Value

- Bear case (WACC 10.5%, terminal g 1.0%): **~$139**
- **Base case: ~$160**
- Bull case (WACC 8.5%, terminal g 2.0%): **~$192**

## เทียบราคาปัจจุบัน $346.37

🔴 **Expensive** — ราคาสูงกว่า Base case FV ($160) ถึง **+117%** — และสูงกว่าแม้แต่ Bull case ($192) ถึง +80% ตลาดกำลัง price-in ว่า margin ระดับ peak-cycle ($23.62/bbl) จะคงอยู่ต่อเนื่องระยะยาว ซึ่งขัดกับ pattern ทางประวัติศาสตร์ของ crack spread cycle

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $268** — ไกลจาก conquest base case ($160) มาก (+68%) เพราะ Morningstar เป็น forward-DCF ที่น่าจะ smooth/extrapolate margin ปัจจุบันเข้าไปในโมเดลมากกว่าที่ conquest ยอมให้ (conquest fade เข้า mid-cycle เร็วและแรงกว่า โดยตั้งสมมติฐานว่า peak margin เป็นปรากฏการณ์ชั่วคราวจาก geopolitical stress ไม่ใช่ new-normal)
- **GuruFocus GF Value $148** — ใกล้เคียง conquest base case ($160) มาก (ต่างกันเพียง ~8%) เพราะทั้งคู่เป็นวิธี backward-looking/mean-reverting ที่ไม่ extrapolate peak-cycle earnings ไปอนาคต — regression บน historical multiple (GuruFocus) กับ 2-stage DCF ที่ fade margin กลับ mid-cycle (conquest) ให้ผลลัพธ์ทิศทางเดียวกันโดยบังเอิญ (คนละวิธีคิด แต่ premise เดียวกันคือ "อย่าเชื่อ peak earnings")
- **สรุป:** Conquest เห็นด้วยกับฝั่ง **GuruFocus (backward-looking) มากกว่า Morningstar (forward-looking)** อย่างชัดเจน เพราะจุดต่างหลักคือสมมติฐานเรื่อง crack-spread persistence — conquest เชื่อว่า margin ปัจจุบันเป็น cyclical spike ที่ mean-revert เร็ว ไม่ใช่ structural shift แบบที่ forward-DCF ของ Morningstar ดูเหมือนจะ assume ไว้ ผลคือ **3/3 แหล่งเห็นตรงกันทิศทาง Expensive** (แม้ตัวเลขต่างกัน) — ยืนยัน Avoid call ของ Layer 1/2/3 อย่างมั่นคง
