# 💰 Conquest DCF: TSM — 2026-08-17
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Data Sources
- Base fundamentals: จาก briefs/TSM-2026-08-17.md (revenue growth trend, FCF, margin, balance sheet)
- Diluted ADR shares outstanding: **5,186M shares (~5.186B)** — WebSearch ยืนยัน (Q1 2026 diluted average, GuruFocus)
- Beta: **1.35 (ประมาณ, ค่าเฉลี่ยจากหลายแหล่ง)** — CNBC 1.39, GuruFocus 1.38, Macroaxis 1.27 → ใช้ค่ากลาง ~1.35
- Risk-free rate (10Y Treasury): **4.69%** — WebSearch ณ 17 ส.ค. 2026 (TradingEconomics)
- ห้ามใช้ fair value สำเร็จรูปจากเว็บใดๆ — ทุกตัวเลขด้านล่างคำนวณเองจาก raw fundamentals

## Assumptions

### Base numbers
- Base Revenue (LTM ประมาณ): **$130.0B** — สอบกลับจาก Base FCF $35.71B ÷ FCF margin กลาง ~27.5% (จากช่วง 25-30% ในไฟล์ brief) ≈ $129.9B → ปัดเป็น $130.0B
- Base FCF (LTM): **$35.71B** (Operating Cash Flow $82.28B − Capex $46.57B) — ตรงกับไฟล์ brief
- Diluted shares: 5.186B ADR-equivalent
- Net cash: **+$76.99B** (cash $110.58B − debt $33.59B)

### Revenue growth fade (ปีที่ 1-5)
| ปี | Growth | เหตุผล |
|---|---|---|
| ปัจจุบัน (FY26 guidance) | ~40%+ | AI/HPC demand surge, Q2 2026 +36% YoY, guidance ปรับขึ้นเป็น "slightly above 40%" |
| ปี 1 | 32% | เริ่ม fade จาก peak — ยังอยู่ใน AI capex supercycle แต่ไม่ยั่งยืนที่ 40%+ ตลอดไปเพราะ capacity constraint แม้ capex $60-64B/ปี |
| ปี 2 | 25% | Hyperscaler capex growth เริ่ม normalize, TSM ยังได้ share gain จาก 2nm ramp |
| ปี 3 | 18% | เข้าใกล้ mean-reversion, คู่แข่ง (Samsung Foundry, Intel Foundry) เริ่มไล่ตามใน leading-edge บางส่วน |
| ปี 4 | 12% | โตช้าลงต่อเนื่อง แต่ยังสูงกว่า historical pre-AI baseline (~15-23%) เพราะ AI demand เป็น structural ไม่ใช่ cyclical ล้วน |
| ปี 5 | 8% | เข้าใกล้ terminal growth, สะท้อน mature high-single-digit growth ของผู้นำตลาดที่มี moat กว้างแต่ industry โต slower |

เหตุผลรวม: กฎ mean-reversion ของธุรกิจโตเร็ว — ไม่มีบริษัทไหนรักษา 40%+ growth ได้ตลอด 5 ปีแม้จะมี wide moat เพราะฐาน revenue ใหญ่ขึ้นทุกปี (denominator effect) และการแข่งขัน/capacity constraint จะเข้ามาแทรกในที่สุด

### FCF margin expansion (ปีที่ 1-5)
| ปี | FCF margin | เหตุผล |
|---|---|---|
| Base | 27.5% | กลางช่วง 25-30% ที่ระบุใน brief |
| ปี 1 | 27% | Capex ยังสูง ($60-64B guidance FY26) จากการขยาย Arizona เป็น 8 fabs — กด margin ต่อเนื่องช่วงแรก |
| ปี 2 | 28% | เริ่มเห็น operating leverage บางส่วน |
| ปี 3 | 29% | Capex/revenue ratio เริ่มลดลงเมื่อ fab ใหม่ทยอย online |
| ปี 4 | 30% | Arizona buildout ใกล้เสร็จเฟสหลัก, capex intensity ลดลง |
| ปี 5 | 31% | Margin กลับสู่ระดับ TSM ในอดีตช่วง non-peak capex cycle (historically TSM เคยทำ FCF margin 30-35% ได้ในปีที่ capex ไม่ peak) |

เหตุผล: capex ปัจจุบันสูงผิดปกติเพราะการขยาย Arizona แบบเร่งรัด (8 fabs) พร้อม node transition 2nm/1.4nm พร้อมกัน — เมื่อ fab ใหม่ทยอยแล้วเสร็จ capex/revenue ratio ควรค่อยๆ ลดลง ทำให้ FCF margin ขยายตัว (ไม่ใช่คงที่ตายตัว)

### Terminal growth rate: 3.0%
สูงกว่ามาตรฐาน 2% เล็กน้อย เพราะ TSM มี Wide Moat ที่ยั่งยืนจริง (Process Power + Scale Economies, market share >90% ใน leading-edge) และ pricing power ต่อเนื่องจากการเป็นผู้ผลิต foundry รายเดียวที่ทำ leading-edge node ได้ในสเกลใหญ่ — justify terminal growth สูงกว่า GDP nominal เล็กน้อย

### WACC: 11.5%
- Risk-free rate: 4.69% (10Y Treasury, 17 ส.ค. 2026)
- Equity Risk Premium: 5.0% (มาตรฐานตลาด กลางช่วง 4-6%)
- Beta: 1.35 (ประมาณจากค่าเฉลี่ยหลายแหล่ง — ดู Data Sources)
- Cost of Equity = 4.69% + 1.35 × 5.0% = 4.69% + 6.75% = **11.44%** → ปัดเป็น 11.5%
- TSM เป็น net-cash position ($76.99B net cash) จึงใช้ cost of equity ตรงๆ เป็น WACC โดยไม่ต้อง weight กับ cost of debt (หนี้น้อยมากเทียบ market cap และ cash สำรอง)

## DCF Calculation (Base Case: WACC 11.5%, Terminal g 3.0%)

| ปี | Revenue ($B) | FCF margin | FCF ($B) | Discount factor (1.115^n) | PV ($B) |
|---|---|---|---|---|---|
| 0 (base) | 130.0 | 27.5% | 35.71 | — | — |
| 1 | 171.6 | 27% | 46.3 | 1.115 | 41.52 |
| 2 | 214.5 | 28% | 60.1 | 1.243 | 48.34 |
| 3 | 253.1 | 29% | 73.4 | 1.386 | 52.95 |
| 4 | 283.5 | 30% | 85.1 | 1.546 | 55.06 |
| 5 | 306.2 | 31% | 94.9 | 1.723 | 55.06 |

**Sum PV of Stage 1 FCF = $252.9B**

Terminal Value (ปีที่ 5) = FCF₅ × (1+g) ÷ (WACC−g) = 94.9 × 1.03 ÷ (0.115−0.03) = 97.75 ÷ 0.085 = **$1,150.0B**
PV of Terminal Value = 1,150.0 ÷ 1.723 = **$667.3B**

**Enterprise Value = 252.9 + 667.3 = $920.2B**
**+ Net Cash $76.99B = Equity Value $997.2B**
**÷ 5.186B diluted ADR shares = Fair Value ≈ $192.3/share**

## Fair Value (Sensitivity)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| Bear | 12.5% | 2.5% | **$166.4** |
| **Base** | **11.5%** | **3.0%** | **$192.3** |
| Bull | 10.5% | 3.5% | **$229.3** |

## เทียบราคาปัจจุบัน $434.00

🔴 **Expensive** — ราคาปัจจุบันสูงกว่า Base case FV ($192.3) ถึง **+125.7%** และยังสูงกว่า Bull case ($229.3) ถึง +89.3%

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $534** — ไกลจาก conquest base case มาก ($192.3 vs $534, ต่างกัน ~64%) เพราะ Morningstar เป็น forward-analyst DCF ที่ผูกกับ Wide Moat rating โดยตรง มักใช้ WACC ต่ำกว่า (สะท้อนความมั่นใจสูงใน moat durability) และ/หรือสมมติ growth fade ที่ช้ากว่านี้มาก (คง growth สูงไว้นานกว่า 5 ปี หรือ terminal growth สูงกว่า 3%)
- **GuruFocus GF Value ~$315-320** — ใกล้กว่า Morningstar แต่ยังห่างจาก conquest base case พอสมควร (~40% ต่ำกว่า GF) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่อิง valuation multiple เฉลี่ยในอดีตของ TSM คูณกับ fundamental ปัจจุบัน — ไม่ได้ทำ explicit fade ของ growth สูงปัจจุบันแบบ DCF ตรงๆ จึงยังสูงกว่า conquest ที่ discount cash flow ปีที่ 3-5 ลงมาชัดเจนกว่า
- **สรุป:** Conquest เห็นด้วยกับทิศทางของ GuruFocus มากกว่า Morningstar (ทั้งคู่มองว่าราคาปัจจุบันแพงกว่าที่ fundamental รองรับ) แต่ conquest **conservative กว่า GuruFocus เองด้วย** ตัวแปรที่กำหนดผลต่างมากที่สุดคือ **WACC** — ถ้าใช้ WACC ต่ำกว่านี้ (เช่น 9-10% ซึ่งบางนักวิเคราะห์ใช้กับ mega-cap wide-moat compounder ที่มีความเสี่ยงต่ำกว่าค่าเฉลี่ยตลาด) fair value จะขยับขึ้นมาใกล้ช่วง GuruFocus ได้มาก — ผู้อ่านควรตีความ conquest base case ว่าเป็น "ขอบล่างที่ conservative" ไม่ใช่ตัวเลขสมบูรณ์แบบ เพราะ DCF ไวต่อ WACC assumption สูงมาก (ดู sensitivity: WACC ±1% เปลี่ยน FV ได้ ±19-20%)
