# 💰 Conquest DCF: MPWR (Monolithic Power Systems) — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — refresh หลังงบ Q3 2026 เทียบรอบ 2026-09-17 (base $427.16)*

## Assumptions

**Base FCF (TTM Sep 2026, ประมาณการบางส่วน):**
- TTM OCF = TTM Jun-26 $822.34M (brief 09-17) + Q3'26 $289.9M (8-K Ex.99.1) − Q3'25 $239.3M (8-K Ex.99.1) = **$872.94M**
- Capex: Q3'26 capex ยังไม่พบ (8-K ไม่มี cash flow statement, 10-Q Q3 หาไม่เจอจากการค้นหา) → **[ประมาณ]** ใช้ TTM capex เดิม $236.80M (brief 09-17) ถ้า Q3 capex จริงสูงกว่า FCF จะต่ำกว่านี้
- TTM FCF ≈ 872.94 − 236.80 = **$636.1M [ประมาณ]**
- TTM Revenue = 3,273.0 (จาก brief 09-17: 4,582.2/1.40) + 1,202.4 − Q3'25 (1,202.4/1.631 = 737.2) = **$3,738.2M** → FCF margin ≈ 17.0% [ประมาณ]

**Revenue growth fade (YoY เทียบ TTM ฐาน $3,738M):**
| ปี | Growth | Revenue ($M) | FCF margin | FCF ($M) |
|---|---|---|---|---|
| Y1 | 60% | 5,981.1 | 18% | 1,076.6 |
| Y2 | 35% | 8,074.5 | 20% | 1,614.9 |
| Y3 | 22% | 9,850.9 | 23% | 2,265.7 |
| Y4 | 14% | 11,230.0 | 25% | 2,807.5 |
| Y5 | 8% | 12,128.4 | 27% | 3,274.7 |

เหตุผล growth: Q3 +63.1% YoY (เร่งจาก +47.6%), Q4 guide กลาง $1,350M (+12.3% QoQ) → run-rate รายปีของ Q4 ≈ $5.4B ดังนั้น NTM revenue ~$6.0B (+60% เหนือ TTM $3.74B) สมเหตุสมผล ปรับขึ้นจาก 40% รอบก่อน เพราะ guidance/ผลจริงแรงกว่า แล้ว fade เร็วขึ้นเป็น 8% ปี 5: comp base ของ Enterprise Data ($506.7M, +164.6%) ใหญ่ขึ้น, SAM ที่บริษัทระบุ ~$34B (brief 09-17) — Y5 revenue $12.1B = ~36% ของ SAM ปัจจุบัน (รอบก่อน ~26%) ซึ่งเป็นสมมติฐานที่ aggressive มากอยู่แล้ว, คู่แข่ง (TI, Renesas, Vicor) และ in-house power silicon ของ hyperscaler

เหตุผล margin: FCF margin ฟื้นจาก ~17% ไป 27% เท่ารอบก่อน (กึ่งกลางระหว่าง trough กับค่าเฉลี่ย 3 ปี ~28.3% จาก brief 09-17) เพราะ capex cycle (GlobalFoundries partnership) ยังหนัก; OCF margin Q3 24.1% ดีขึ้นจาก 23.2% แต่ FCF จริงรอ 10-Q

**Terminal growth:** 3.0% (เท่าเดิม — SAM จำกัด, power IC market โต ~6.8% CAGR ตาม brief 09-17)

**WACC: 12.43%** = Rf 4.93% (10Y Treasury 4.929% ใน daily brief 2026-10-31) + beta 1.5 [ประมาณ ค่ากลางของ 1.48–2.08 ตาม brief 09-17] × ERP 5.0%. ใช้ cost of equity ตรง (ไม่มีหนี้กู้)

**Shares:** 49.1M (Q4 guide 48.9–49.3M [หลัก]) | **Net cash:** $1,091.2M (cash+ST inv, ไม่มีหนี้ใน release [หลัก]) — รอบก่อนใช้ $1.23B

## DCF Calculation (WACC 12.43%, g 3.0%)
| ปี | FCF ($M) | PV ($M) |
|---|---|---|
| Y1 | 1,076.6 | 957.6 |
| Y2 | 1,614.9 | 1,277.6 |
| Y3 | 2,265.7 | 1,594.3 |
| Y4 | 2,807.5 | 1,757.1 |
| Y5 | 3,274.7 | 1,822.9 |

- Sum PV Stage 1 = **$7,409.3M**
- TV = 3,274.7 × 1.03 ÷ (0.1243 − 0.03) = **$35,767.9M** → PV TV = **$19,910.5M** (72.9% ของ EV)
- EV = **$27,319.9M** + net cash $1,091.2M = Equity **$28,411.1M**
- ÷ 49.1M shares = **$578.64**

## Fair Value
| Scenario | WACC | g | FV/share |
|---|---|---|---|
| 🐻 Bear | 13.43% | 2.5% | **$501.88** |
| ⚖️ **Base** | **12.43%** | **3.0%** | **$578.64** |
| 🐂 Bull | 11.43% | 3.5% | **$684.34** |

## เทียบราคาปัจจุบัน $1,211.63 (ปิด 2026-10-30)
🔴 **Expensive** — ราคาสูงกว่า Base FV **+109.4%**; สูงกว่า Bull case ด้วย (+77.1%). ราคาตลาด mkt cap $59.5B ≈ 2.1x equity value ของ base

## เทียบรอบ 2026-09-17 (base $427.16, ราคา $1,165.70)
- Base FV **+35.5%** ($427.16 → $578.64) ขับเคลื่อนโดย: (1) revenue base/growth สูงขึ้นมาก (Y5 revenue $12.1B vs $8.7B; Y1 growth 60% vs 40%) จากงบ Q3 ที่เร่งขึ้นและ guide Q4 แรง, (2) base FCF $636M (ประมาณ) vs $586M, (3) WACC ลดเล็กน้อย 12.5% → 12.43% (Rf 5.0% → 4.93%)
- ฉุดลงเล็กน้อย: net cash ลดจาก $1.23B เป็น $1.09B (buyback $453M ใน Q3)
- Bucket ไม่เปลี่ยน: 🔴 Expensive เหมือนเดิม; premium ของราคาเหนือ base ลดจาก +172.9% เป็น +109.4% (ราคาลง -8.2% จาก 10-14 + FV ขึ้น)
- Sanity: แม้ใช้ FCF margin 27% ตั้งแต่ปี 1 หรือ growth สูงกว่านี้ ก็ยากจะถึง $1,211 โดยไม่ลด WACC ลงมาก → ตลาด price-in AI datacenter growth ยาวกว่า/ใหญ่กว่า SAM ที่บริษัทระบุ

## ข้อจำกัด
- Q3'26 capex/FCF จริงยังไม่มี (รอ 10-Q) — base FCF เป็นการประมาณ
- Beta 1.5 เป็นค่าประมาณ; FV ไวต่อ WACC (±1% ≈ -13%/+18%)
- ไม่ได้อ้าง Morningstar/GuruFocus รอบนี้ (ไม่มีตัวเลขใหม่ใน brief 10-31)
