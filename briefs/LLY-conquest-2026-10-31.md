# 💰 Conquest DCF: LLY — 2026-10-31
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — อัปเดตหลัง Q3 2026 earnings (8-K 2026-10-29)*

## Assumptions
- **Base (2026) revenue: $91.5B** = midpoint guidance ใหม่ $91-92B (เดิม $85-87B) [หลัก: Lilly 8-K 2026-10-29]. หมายเหตุ: Q3 มี one-time ~$0.9B (ตัวเลขรอง) ไม่ได้ปรับออกจาก base
- **Base FCF margin 2026: ~13%** — ยกจาก baseline (TTM FCF $10.37B / revenue ~$80B) **ไม่ได้ refresh** เพราะ release 8-K ไม่มี cash-flow statement และยังไม่ได้ดึง 10-Q Q3 → **assumption/stale** (ใช้เพียงเป็นจุดเริ่ม; DCF จริงขึ้นกับ margin ปี 1-5)
- **Revenue growth fade (คงเดิมจาก baseline เพื่อแยกผลของ fundamentals):** ปี1 +30% → ปี2 +24% → ปี3 +18% → ปี4 +13% → ปี5 +9%
  เหตุผล: Q3 ไม่รวม one-time ≈ +33.5% YoY, volume +53% แต่ realized price -15% (ต่างประเทศ -29%) และ base ใหญ่ขึ้น, oral GLP-1 แข่งขันเข้มขึ้น, mean-reversion ของธุรกิจโตเร็ว
- **FCF margin expansion:** ปี1 15% → 18% → 21% → 23% → ปี5 25% (capex program ผลิต $18B+ เสร็จ ~2028, big-pharma ที่โตเต็มที่ 25-30%) — ไม่เปลี่ยนจาก baseline
- **Terminal growth: 3.0%** (Wide Moat + pipeline refresh แต่มี patent-cliff risk ระยะยาวของ tirzepatide) — ไม่เปลี่ยน
- **WACC ≈ 7.3%:** risk-free 4.929% (10Y Treasury ปิด 30 ต.ค. 2026 ตาม brief 2026-10-31) + beta 0.48 (ยกจาก baseline, Yahoo 5Y monthly — **stale ไม่ได้เช็คซ้ำ**) × ERP 5.0% = cost of equity 7.33%; debt weight ~3-4% → WACC ≈ 7.3%
  (baseline 7.0% ใช้ risk-free 4.68% — Rf ขึ้น ~25bp จึงดัน WACC ขึ้น)
- **Diluted shares: 893.4M** (Q3 2026 diluted weighted-average, 8-K 2026-10-29 [หลัก]; baseline 895M)
- **Net debt: ~$31B** — ยกจาก baseline (**ประมาณการ ไม่ใช่จาก filing; ไม่ได้ refresh Q3**); Q3 มี IPR&D $4.2B (AtaiBeckley, Curevo) ซึ่งอาจเพิ่ม net debt จริง → ความเสี่ยง FV จริงต่ำกว่าเล็กน้อย (~$5/หุ้นต่อ $4.2B)

## DCF Calculation (Base: WACC 7.3%, g 3.0%)
| ปี | Revenue | FCF margin | FCF | DF @7.3% | PV |
|----|---------|-----------|-----|----------|-----|
| 1 (2027) | $118.95B | 15% | $17.84B | 0.9320 | $16.63B |
| 2 (2028) | $147.50B | 18% | $26.55B | 0.8686 | $23.06B |
| 3 (2029) | $174.05B | 21% | $36.55B | 0.8095 | $29.59B |
| 4 (2030) | $196.68B | 23% | $45.24B | 0.7544 | $34.13B |
| 5 (2031) | $214.38B | 25% | $53.60B | 0.7031 | $37.69B |

- Sum PV Stage 1 = **$141.1B**
- Terminal Value = $53.60B × 1.03 / (0.073 − 0.03) = **$1,283.9B**; PV = **$902.7B**
- EV = $1,043.8B; Equity = EV − $31B = **$1,012.8B**
- **FV/share = $1,012.8B / 893.4M = $1,134**

## Fair Value (Sensitivity)
| Scenario | WACC | g | FV/share |
|---|---|---|---|
| Bear | 8.3% | 2.5% | **$830** |
| **Base** | **7.3%** | **3.0%** | **$1,134** |
| Bull | 6.3% | 3.5% | **$1,762** |
| อ้างอิง: base growth/margin ที่ WACC 7.0% (เทียบ baseline) | 7.0% | 3.0% | $1,226 |

(Terminal value ≈ 86% ของ EV → อ่อนไหวสูงต่อ WACC/g; range กว้างมาก = ความมั่นใจต่ำ-ปานกลาง)

## เทียบราคาปัจจุบัน $1,417.54
ราคาสูงกว่า Base FV $1,134 **+25.0%** → 🔴 **Expensive**
(ถ้าใช้ WACC 7.0% เท่า baseline → FV $1,226, ราคาสูงกว่า +15.6% → 🟡 Fair; bucket จึงอยู่ใกล้ขอบ 20% และขึ้นกับ Rf/WACC)

## เปลี่ยนจาก baseline 2026-08-28 ($1,147)
- Revenue base +6.4% ($86B → $91.5B) ดัน FV ขึ้น ≈ +$79 (ที่ WACC 7.0% → $1,226)
- Risk-free ขึ้น (4.68% → 4.929%) ดัน WACC 7.0% → 7.3% ลด FV ≈ -$92
- สุทธิ FV ต่ำกว่า baseline เล็กน้อย (-1%); ราคาตลาดขึ้น +20.5% ($1,176.10 → $1,417.54) จึงเปลี่ยน bucket Fair → Expensive
- ข้อจำกัด: FCF margin, net debt, beta ยังไม่ refresh จาก 10-Q Q3 — ผลควรอ่านเป็นกรอบ ไม่ใช่ตัวเลขเป๊ะ

## เทียบกับ Morningstar/GuruFocus (ตัวเลขจาก brief 2026-10-31 — ไม่ได้ใช้ในการคำนวณ)
- Morningstar $980 (stale, ก่อน Q3): conquest สูงกว่า ~16% — ทั้งคู่ forward-DCF; Morningstar ใช้ WACC/margin ระมัดระวังกว่า
- GuruFocus GF Value $1,593.50: conquest ต่ำกว่า ~29% — GF เป็น historical-multiple ไม่ fade growth
- **สรุป:** conquest ($1,134, 🔴) เอนไปทาง Morningstar (Expensive) — ราคา $1,417.54 ต้องการ WACC ต่ำกว่า/margin-growth สูงกว่า fade ที่ใช้ (Bull case WACC 6.3% ให้ $1,762) จึงจะสมเหตุผล; conquest มี bias conservative โดยธรรมชาติ (อ่านเป็น "มุมมองเข้มที่สุดในสาม")
