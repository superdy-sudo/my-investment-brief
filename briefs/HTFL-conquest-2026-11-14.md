# 💰 Conquest DCF: HTFL (Heartflow) — 2026-11-14
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — **scenario-based: terminal FCF margin เป็น assumption ไม่ใช่ข้อเท็จจริง** ผลมีความไม่แน่นอนสูง*

ราคาอ้างอิง $49.46 (ปิด 2026-11-13) | shares 87.888M | net cash $253.0M (ไม่มีหนี้) | ข้อมูลจาก briefs/HTFL-2026-11-14.md (8-K/10-Q)

## ทำไมรอบนี้ทำได้ (ต่างจาก 10-20)
- Revenue base ชัดขึ้น: guidance FY2026 $262-264M (mid $263M), 9M $189.5M, Q3 +57% [8-K]
- margin trend มีฐานตัวเลข: non-GAAP op margin -24.0% -> -6.9% YoY, GM 83.6%
- **ข้อจำกัดที่ยังอยู่:** ไม่มี operating cash flow/capex ต้นทาง, ไม่มี FCF บวกในประวัติ -> ใช้ **revenue x FCF margin** แทน "Base FCF" และ terminal margin เป็นการกำหนดเอง (ดูเหตุผลด้านล่าง) ไม่ใช่ตัวเลขที่ verify ได้

## Assumptions
- **Base revenue (FY2026E):** $263M (guidance mid) | ปี 1-5 = FY2027-FY2031
- **Growth fade (base):** 38% -> 32% -> 26% -> 21% -> 16% (เหตุผล: Q3 โต 57%, guidance FY26 ~+49%; ไม่มี outlook 2027 จึงสมมติ decay ~15-20% สัมพัทธ์ต่อปีตาม mean-reversion ของธุรกิจโตเร็ว, ตลาด CCTA "underpenetrated" ตามบริษัทแต่ TAM $ ยังไม่ verify, คู่แข่ง CT vendors/AI + ความเสี่ยง reimbursement)
  - Bear: fade ต่ำกว่า base 5pt ทุกปี (33/27/21/16/11) | Bull: สูงกว่า base 4pt (42/36/30/25/20)
- **FCF margin path (assumption):**
  - Base: -2% -> 4% -> 10% -> 16% -> 22% (terminal 22%)
  - Bear: -4% -> 0% -> 5% -> 9% -> 12% (terminal 12%)
  - Bull: 0% -> 7% -> 15% -> 22% -> 28% (terminal 28%)
  - เหตุผล: GM ~83% ให้เพดาน margin สูงแบบ software/medtech; non-GAAP op margin -6.9% และแคบลง ~17pt/ปี; SBC ~10% ของ rev เป็นต้นทุนจริงที่ถ่วง FCF/ผู้ถือหุ้น จึงไม่ให้ terminal เกิน ~28% แม้ฝั่ง bull. **ตัวเลข terminal margin ไม่มีฐานประวัติ เป็นการประมาณของ agent**
- **Terminal growth:** base 3.0% (ธุรกิจ moat + ยังโตต่อ แต่ไม่เกิน nominal GDP ระยะยาวมากนัก), bear 2.5%, bull 3.5%
- **WACC:** base 12.6% = risk-free 5.13% (10Y, จาก daily brief 2026-11-13) + beta 1.5 x ERP 5.0% ; **beta 1.5 เป็นการประมาณ** (เพิ่ง IPO ไม่มีประวัติ beta ยาว; medtech/software โตเร็วขาดทุนปกติ ~1.3-1.7); net cash ไม่มีหนี้ -> ใช้ cost of equity ตรงๆ. Bear 13.6% / Bull 11.6% (+-1%)
- Net cash $253.0M, diluted shares ใช้ basic 87.888M (ไม่ได้ปรับ options/RSU dilution -> ถ้าปรับ FV จะต่ำลงอีกเล็กน้อย)

## DCF Calculation (Base, $M)
| ปี | Revenue | FCF margin | FCF |
|---|---|---|---|
| FY27 | 362.9 | -2% | -7.3 |
| FY28 | 479.1 | 4% | 19.2 |
| FY29 | 603.6 | 10% | 60.4 |
| FY30 | 730.4 | 16% | 116.9 |
| FY31 | 847.3 | 22% | 186.4 |

- PV FCF ปี 1-5 @12.6% = $226.6M
- Terminal value = 186.4 x 1.03 / (0.126 - 0.03) = $2,000M -> PV = $1,105M (**~83% ของ EV**)
- EV = $1,332M + net cash $253M = Equity $1,585M / 87.888M sh = **$18.0**

## Fair Value
| Case | WACC | g | Terminal margin | FV/share |
|---|---|---|---|---|
| Bear | 13.6% | 2.5% | 12% | **$8.4** |
| **Base** | 12.6% | 3.0% | 22% | **$18.0** |
| Bull | 11.6% | 3.5% | 28% | **$30.5** |

- Sensitivity เฉพาะ WACC/g (margin+growth base คงที่): $15.7 / $18.0 / $21.2
- **Caveat (bias):** โครง 2-stage 5 ปีตัด terminal ที่ปี 5 ขณะที่ยังโต 16-20% (ตอนนั้น g กระโดดลงเหลือ 3%) -> **ประเมินต่ำกว่าจริงสำหรับธุรกิจโตเร็ว**. เช็คด้วย fade 10 ปี (ปี 6-10 โตลง 13%->3%, margin ขึ้นถึง 28% base / 34% bull): Base ~$24.6, Bull ~$42.8 (ยังต่ำกว่า $49.46). เป็นการเช็คความไว ไม่ใช่ผลหลัก

## เทียบราคาปัจจุบัน $49.46
🔴 **Expensive** — ราคาสูงกว่า Base FV $18.0 ราว +175% (49.46/18.0 - 1); สูงกว่า Bull FV $30.5 ราว +62%; แม้ใช้ 10-yr bull ($42.8) ราคายังสูงกว่า ~+16%
- ราคานี้ต้องการ revenue โต + margin ระยะยาวเกิน bull ของเรา หรือ discount rate ต่ำกว่า ~11% — เป็นการ price in ความสำเร็จเต็มที่ (EV/Sales ~15.6x guidance)
- **ความเชื่อมั่นของ bucket: ปานกลาง** — ทิศทาง (แพงตาม DCF) ทนต่อ assumption ได้ค่อนข้างดี (bull ทุกตัวยังต่ำกว่าราคา) แต่ระดับ FV กว้างมาก ($8-31) เพราะ terminal margin/beta ไม่มีฐาน

## เทียบกับ Morningstar/GuruFocus
- Morningstar: Quantitative rating ถูก lock ⚪ | GuruFocus GF Value: ไม่พบ ⚪ | ไม่มี FV ภายนอกให้เทียบ (ไม่นำ analyst PT $68-70 มาเป็น FV ตามกฎ)
- **สรุป:** conquest ให้ภาพ Expensive; ผลไม่ใช่ข้อสรุปแน่นอนเพราะ terminal margin เป็น assumption — ควรอัปเดตเมื่อมี operating cash flow/capex ต้นทาง (10-Q cash flow statement) และ outlook 2027
