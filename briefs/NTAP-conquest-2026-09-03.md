# 💰 Conquest DCF: NTAP — 2026-09-03
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## หมายเหตุสำคัญ: ทำไมไม่ใช้ growth 30% ของ Q1 FY27
Q1 FY27 revenue โต +30% YoY แต่ตัวเลขนี้ถูกหนุนบางส่วนจาก 53-week fiscal quarter ("extra week" effect) + ดีล AI ที่อาจ lumpy ตาม brief. FY27 full-year **guidance** ($7.975-8.225B เทียบ FY26 $6.93B) implies โตแค่ ~15-19% YoY เท่านั้น — ไม่มีหลักฐานอิสระว่า 30% ยั่งยืน จึงใช้ **guided midpoint ~17%** เป็น growth anchor หลักของปีฐาน ตามกฎของ agent นี้

## Assumptions

**Base Year (FY27, ใช้ guidance เป็นฐาน ไม่ใช่ผลจริงที่ยังไม่ปิดปี):**
- Revenue FY27 (midpoint guidance): $8.10B (growth ~16.9% เทียบ FY26 $6.93B — สอดคล้องกับ guided range 15-19%)
- FCF margin: 19.8% (จาก Q1 FY27 actual) → Base FCF ≈ $1,603.8M

**Stage 1 — 5-year explicit forecast (FY28-FY32), growth fade:**
| ปี | Revenue growth | เหตุผล |
|---|---|---|
| ปี 1 (FY28) | 14% | ลงจาก guided 17% ของ FY27 — comp ยากขึ้นเมื่อไม่มี extra-week effect ช่วย, แต่ AI/all-flash demand ยังหนุนต่อ |
| ปี 2 (FY29) | 11% | AI data-infra tailwind เริ่ม normalize, แข่งขันจาก Dell/Pure/hyperscaler native storage เพิ่มขึ้น |
| ปี 3 (FY30) | 9% | mature storage market มักโต mid-to-high single digit นอกช่วง refresh cycle เร่งพิเศษ |
| ปี 4 (FY31) | 6% | mean-reversion เข้าใกล้ industry growth ของ enterprise storage ($157-170B market, โต low-to-mid single digit ระยะยาว) |
| ปี 5 (FY32) | 4% | ใกล้ terminal, เหลือ premium เล็กน้อยจาก switching-cost moat |

FCF margin ขยายแบบค่อยเป็นค่อยไปจาก 19.8% → 21.0% ตลอด 5 ปี (เหตุผล: operating margin ขยายตัว +610bps YoY ใน Q1 FY27 แล้ว, software/ONTAP mix ที่สูงขึ้นมัก scale ดีกว่า hardware — สมมติฐานระมัดระวัง ไม่ได้ extrapolate margin expansion เร็วเกินไป)

**Terminal growth: 3.0%** — สูงกว่า GDP เฉลี่ยเล็กน้อย เพราะ switching-cost moat (ONTAP lock-in) ทำให้ pricing power คงอยู่ระยะยาวได้ แต่ไม่สูงกว่านี้เพราะ storage hardware/software เป็น mature industry ที่แข่งขันสูง (Dell, Pure, HPE, hyperscaler native)

**WACC (cost of equity, ใช้ตรงเพราะ net-cash position):**
- Risk-free rate: 4.2% (10Y Treasury ปัจจุบัน โดยประมาณ)
- Equity risk premium: 5.0% (มาตรฐานตลาด)
- Beta: 1.1 (ประมาณ — storage/enterprise hardware มักมี beta ปานกลาง-สูงกว่าตลาดเล็กน้อยจากความอ่อนไหวต่อ IT capex cycle; ไม่ได้ดึงจาก data provider ตรงๆ ในรอบนี้ ระบุชัดว่าเป็นการประมาณ)
- WACC ≈ 4.2% + 1.1 × 5.0% = **9.5%**

**Shares outstanding:** ~196.4M (คำนวณจาก market cap ~$35.5B ÷ ราคา $180.77 ตามข้อมูลใน brief)
**Net cash:** ~$1.1B (จาก brief: cash+ST investments $3.6B − gross debt $2.5B)

## DCF Calculation (Base Case, WACC 9.5%, terminal g 3.0%)

| ปี | Revenue ($B) | FCF margin | FCF ($M) | Discount factor | PV FCF ($M) |
|---|---|---|---|---|---|
| FY28 (ปี1) | 9.234 | 20.0% | 1,846.8 | 0.9132 | 1,686.2 |
| FY29 (ปี2) | 10.250 | 20.3% | 2,080.7 | 0.8340 | 1,735.3 |
| FY30 (ปี3) | 11.172 | 20.6% | 2,301.4 | 0.7616 | 1,752.7 |
| FY31 (ปี4) | 11.842 | 20.8% | 2,463.3 | 0.6956 | 1,713.6 |
| FY32 (ปี5) | 12.316 | 21.0% | 2,586.4 | 0.6352 | 1,642.9 |

Sum PV FCF (ปี 1-5) = **$8,530.7M**

Terminal Value = FCF5 × (1+g) ÷ (WACC−g) = 2,586.4 × 1.03 ÷ (0.095−0.03) = **$40,984.6M**
PV Terminal Value = 40,984.6 × 0.6352 = **$26,041.4M**

Enterprise Value = 8,530.7 + 26,041.4 = **$34,572.1M**
+ Net cash $1,100M → Equity Value = **$35,672.1M**
÷ 196.4M shares → **Fair Value/share ≈ $181.6**

## Fair Value

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| Bear | 10.5% | 2.5% | **$150.3** |
| **Base** | **9.5%** | **3.0%** | **$181.6** |
| Bull | 8.5% | 3.5% | **$231.5** |

## เทียบราคาปัจจุบัน $180.77
🟡 **Fair** — ราคาปัจจุบันต่ำกว่า Base case FV เพียง ~0.5% (แทบเท่ากันพอดี) อยู่ใน ±20% ของ FV อย่างชัดเจน

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $175.69** — ใกล้กับ conquest base case มาก (ต่างกันแค่ ~3%) ทั้งสองวิธีมองว่าราคาปัจจุบัน "Fair" ไม่แพงไม่ถูก แม้ methodology จะต่างกัน (Morningstar เป็น forward-looking analyst DCF ผูก moat rating, conquest เป็น bottom-up DCF จาก raw guidance) แต่ผลลัพธ์บรรจบกันเพราะทั้งคู่ใช้ growth assumption ระดับ teens% (ไม่ใช้ 30% quarterly spike) เป็นฐาน
- **GuruFocus GF Value $120.44** — ห่างจาก conquest base case มาก (~$61 หรือ ~34% ต่ำกว่า) น่าจะเป็นเพราะ GF Value เป็น backward-looking historical-multiple regression ที่ยังอิง median multiple ของ NTAP ในอดีตตอนที่ตลาดยัง price หุ้นเป็น "mature slow-growth storage vendor" ก่อนที่ AI/all-flash tailwind และ operating margin expansion ปัจจุบันจะเกิดขึ้น — ไม่ได้ forward-looking พอที่จะจับ margin expansion (+610bps YoY) และ FCF quality ที่ดีขึ้น
- **สรุป:** Conquest DCF เห็นด้วยกับ **Morningstar** เป็นหลัก (ทั้งคู่ชี้ 🟡 Fair) และมองว่า GuruFocus underweight การเปลี่ยนแปลงเชิงบวกล่าสุดของธุรกิจ (margin expansion, AI-driven all-flash growth) เพราะเป็น backward-looking multiple ที่ยังไม่ปรับตามข้อมูลใหม่ — ข้อสรุป valuation: **🟡 Fair ที่ราคาปัจจุบัน $180.77** ไม่ใช่ Expensive ตามที่ GuruFocus บอก
