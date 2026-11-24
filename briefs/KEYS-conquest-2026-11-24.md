# 💰 Conquest DCF: KEYS — 2026-11-24
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — รอบใหม่หลังงบ Q4 FY26*

## Assumptions
- **Base FCF: $1,747M** (FY26 จริง จาก 8-K ex.99.1; FCF margin 24.4% = 1,747/7,157 คงที่ตลอด forecast — ไม่สมมติ operating leverage เพิ่ม)
- **Growth fade:** ปี1 (FY27) 22% → ปี2 17% → ปี3 13% → ปี4 9% → ปี5 6% → terminal 3%
  - เหตุผลปี1: guide Q1 FY27 $2.04-2.06B (midpoint +2.8% QoQ จาก Q4 $1.994B); ถ้า QoQ โต ~3% ต่อเนื่อง FY27 ≈ $8.57B ≈ +20% และ orders/book-to-bill ~1.14 หนุนเพิ่มเล็กน้อย → ใช้ 22% (ปรับขึ้นจากรอบ 08-20 ที่ใช้ 30% บน base ที่ประมาณต่ำกว่าจริง เพราะ Q4 run-rate โตแล้ว ปี1 จึงไม่ควรเป็น 30%)
  - ปี2-5: AI-capex supercycle เป็นวงจร, T&M TAM โตแค่ ~4.1% CAGR (brief 09-17/10-14) → mean-revert ลงใกล้ TAM + share gain ภายใน 5 ปี (สมมติฐานเดียวกับรอบ 08-20)
- **Terminal growth: 3%** (เหตุผลเดิม: Wide Moat switching cost + process power, secular driver 6G/defense/AI infra)
- **WACC: 11.7%** = risk-free 5.2% (10Y UST ปัจจุบัน ตามที่ผู้สั่งระบุ ~5.2%) + beta 1.3 (ประมาณ ค่ากลางเดิมจากรอบ 08-20) × ERP 5.0% = 11.7%
  - net cash +$407M เทียบ market cap ~$46B จึงใช้ cost of equity ตรงเป็น WACC
- **Shares:** 169.9M (Webull ตาม brief 11-24)
- **Net cash: +$407M** (cash $2,916M − debt $2,509M ณ 2026-10-31)

## DCF Calculation (Base, WACC 11.7%, g 3%)
| ปี | Growth | FCF ($B) | Discount Factor | PV ($B) |
|---|---|---|---|---|
| 1 | 22% | 2.131 | 1.117 | 1.908 |
| 2 | 17% | 2.494 | 1.248 | 1.999 |
| 3 | 13% | 2.818 | 1.394 | 2.022 |
| 4 | 9% | 3.071 | 1.557 | 1.973 |
| 5 | 6% | 3.256 | 1.739 | 1.872 |

- Sum PV Stage 1 = $9.77B
- Terminal Value = 3.256 × 1.03 ÷ (0.117 − 0.03) = $38.54B → PV = $22.17B
- EV = $31.95B; + net cash $0.407B → Equity $32.36B
- Fair Value/share = 32.36B ÷ 169.9M ≈ **$190**

## Fair Value (Sensitivity)
| Scenario | WACC | Terminal g | FV/share |
|---|---|---|---|
| Bear | 12.7% | 2.5% | $164 |
| **Base** | **11.7%** | **3.0%** | **$190** |
| Bull | 10.7% | 3.5% | $227 |

ตัวเปรียบ: รอบ 08-20 base $174 (WACC 11.1%) → รอบนี้ $190 เพิ่มขึ้นเพราะ base FCF จริงสูงกว่าที่ประมาณไว้ ($1.75B vs $1.33B) แม้ WACC สูงขึ้น 0.6pt จาก risk-free ที่สูงขึ้น และ growth ปี1 ลดลง

## เทียบราคาปัจจุบัน $270.97 (intraday 2026-11-24)
🔴 **Expensive** — ราคาสูงกว่า Base FV ($190) **+42.3%** (270.97/190.4 − 1); แม้ bull case $227 ราคายังสูงกว่า +19%

## เทียบกับ Morningstar/GuruFocus
- **Morningstar:** data conflict ($323 vs $151, ยืนยันไม่ได้ตาม brief 11-24) — $151 ใกล้ conquest มากกว่า, $323 ไกลมาก (สมมติ growth fade ช้ากว่า/moat premium)
- **GuruFocus GF Value $220.62** (ก่อนงบ อาจ stale) — ใกล้ conquest base (ต่างราว 16%) และอยู่ในช่วง bull-base ทิศทางเดียวกันคือ overvalued
- **สรุป:** conquest เห็นด้วยกับฝั่ง overvalued (GuruFocus + Morningstar $151 ถ้าถูก) — ความเห็น 🔴 ยังเหมือนเดิมแต่ช่องว่างแคบลงมาก (จาก +83.6% เหลือ +42%) เพราะราคาลง 15% จาก $319 และ FCF จริงสูงกว่าที่ประมาณ; DCF อ่อนไหวต่อ fade assumption มาก (ถ้า growth คงสูงกว่านี้ FV จะขยับขึ้น)
