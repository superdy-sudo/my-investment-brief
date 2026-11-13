# 💰 Conquest DCF: NVDA — 2026-11-14
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — re-run จาก 2026-08-27 เพราะราคาเปลี่ยนมาก ($209.66 → $161.00) และ Rf เปลี่ยน (4.65% → 5.13%) ยังไม่มี Q3 FY27 actual จึงใช้ตัวเลขชุดเดิมจาก Q2 FY27 + Q3 guide $108B*

## Assumptions
- Base FCF: **$127B** (TTM FCF $126.9B, margin 41.9%, TTM revenue $302.9B — ตารางเดียวกับ conquest 08-27; Q2 FY27 FCF เดี่ยวต่ำ $21.3B จาก inventory/AR build จึงใช้ TTM เพื่อ normalize)
- Growth fade (FCF): ปี1 50% → ปี2 38% → ปี3 25% → ปี4 15% → ปี5 8% (**คงเดิมทั้งหมด** — ไม่มี Q3 actual ใหม่ ยึด Q3 guide $108B ±2% = +12.3% QoQ, +89% YoY; ปี1 ต่ำกว่า revenue growth เพราะ working-capital drag; ปี2-5 ลดหลั่นตาม mean-reversion ฐานใหญ่ + custom ASIC erosion + hyperscaler capex digestion)
- Terminal growth: **3.0%** (ผูก nominal GDP; ไม่ให้ premium เพิ่มเพราะ ASIC เป็นภัยเชิงโครงสร้างฝั่ง inference)
- WACC: **13.63%** = Rf 5.13% + beta 1.7 (ประมาณการเดิม ไม่มีข้อมูลใหม่ให้เปลี่ยน) × ERP 5.0% — cost of equity ล้วน เพราะ net cash
  - Rf: Yahoo ^TNX (curl ยืนยันแล้ว) regularMarketPrice 5.133% (Nov 13); brief ระบุ 5.127% intraday — ใช้ 5.13%
  - รอบก่อนคำนวณได้ 13.15% แล้วปัดเป็น 13.0%; รอบนี้ใช้ค่าไม่ปัด 13.63%
- Shares (diluted weighted avg Q2 FY27): 24.3B
- Net cash: +$66.0B (cash $22.44B + marketable debt $34.14B + equity securities $42.78B − debt $33.37B) — ยังไม่มีงบ Q3 ใหม่

## DCF Calculation ($B, WACC 13.63%, g 3.0%)
| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Growth | 50% | 38% | 25% | 15% | 8% |
| FCF | 190.5 | 262.9 | 328.6 | 377.9 | 408.1 |
| Discount factor | 0.880 | 0.774 | 0.682 | 0.600 | 0.528 |
| PV | 167.6 | 203.6 | 224.0 | 226.7 | 215.4 |

- Sum PV Stage-1 = $1,037.4B
- Terminal Value = 408.1 × 1.03 ÷ (0.1363 − 0.03) = $3,954.7B → PV = $2,087.6B
- EV = $3,124.9B | + net cash $66.0B → Equity Value = $3,190.9B
- **FV/หุ้น = $3,190.9B ÷ 24.3B = $131.3**

## ผลของการเปลี่ยน Rf (แยกชัด)
| ขั้น | WACC | FV/หุ้น |
|---|---|---|
| conquest 08-27 (Rf 4.65%, ปัดลง) | 13.00% | $140.1 (recompute ได้ $140.0) |
| Rf 4.65% ไม่ปัด | 13.15% | $137.9 (−$2.1 จากการไม่ปัด — ไม่ใช่ผลของ Rf) |
| **Rf 5.13% (+0.48pp)** | **13.63%** | **$131.3** (−$6.6 หรือ −4.8% จากผล Rf ล้วน) |
- รวมจาก $140.1 → $131.3 = −$8.8 (−6.3%) แบ่งเป็น: ผล Rf ล้วน −$6.6 + ผลการไม่ปัด WACC −$2.1
- Rf +0.48pp ดัน WACC +0.48pp (beta 1.7 ถูกคูณเฉพาะ ERP จึง pass-through 1:1) ความอ่อนไหว ~ −$13.6 ต่อ WACC +1pp
- ตัวแปรอื่น (growth fade, FCF base, net cash, shares) ไม่เปลี่ยน — ราคาตลาดไม่มีผลต่อ DCF

## Fair Value (Sensitivity)
| Scenario | WACC | Terminal g | FV/share |
|---|---|---|---|
| 🐻 Bear | 14.63% | 2.5% | **$116.0** |
| ⚪ Base | 13.63% | 3.0% | **$131.3** |
| 🐂 Bull | 12.63% | 3.5% | **$151.7** |

ปรับทีละตัว: WACC 12.63%/g3% = $145.7 | WACC 14.63%/g3% = $119.4 | g 2.5% = $127.1 | g 3.5% = $136.0 (growth ±0.5pp กระทบน้อยกว่า WACC ±1pp มาก)

## เทียบราคาปัจจุบัน $161.00 (Yahoo intraday 2026-11-13)
🔴 **Expensive** — ราคาสูงกว่า Base FV ($131.3) **+22.6%** (เฉียดเส้น 20% — ค่อนข้าง borderline) และสูงกว่า Bull ($151.7) อยู่ +6.1% ทุก scenario ยังต่ำกว่าราคา
- รอบ 08-27: ราคา $209.66 เหนือ Base +49.6% → รอบนี้ +22.6% ช่องว่างแคบลงเพราะราคาลง −23.2% ขณะที่ FV ลง −6.3% (จาก Rf)
- ราคา $161 ≈ FV ที่ WACC ราว 11.9% (ที่ g 3%) — เทียบเท่า implied cost of equity ที่ตลาดยอมรับต่ำกว่า conquest ~1.7pp

## เทียบกับ Morningstar/GuruFocus
ตามคำสั่ง ไม่ได้อ่านค่า FV ของแหล่งอื่นรอบนี้ ไม่นำมาเทียบ (ข้อสังเกตเชิงโครงสร้างเท่านั้น: conquest WACC 13.6% สูงกว่าที่ analyst forward-DCF มักใช้ จึงเป็น "เพดานความเข้มงวด" ไม่ใช่คำตัดสินเดี่ยว)

## ข้อจำกัด
- ยังไม่มี Q3 FY27 actual — ถ้า Q3 FCF/guide Q4 ต่างจากสมมติฐาน ให้ re-run
- Beta 1.7 เป็นประมาณการเดิม (ไม่ได้ดึงใหม่); WACC สูงมากจาก Rf 5.13% ที่เป็นระดับสูงใกล้ 52w high (5.364%)
- FCF ฐาน TTM ถูกกดจาก working-capital build; ถ้า normalize ได้เร็ว FV จะสูงกว่านี้
