# 💰 Conquest DCF: TSM (ADR) — 2026-10-20
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น) — รันใหม่หลังงบ Q3 2026 (ออก 2026-10-15)*

## Data Sources
- Raw fundamentals หลังงบ: briefs/TSM-2026-10-20.md + TSMC 3Q26 Management Report / Presentation (investor.tsmc.com, WebSearch 2026-10-20; ตัวเลขบริษัทเอง ยังไม่ cross-check แหล่งที่ 2)
- Q3'26: Revenue US$46.72B (+41.2% YoY); OCF NT$919.77B; Capex NT$443.21B (~US$13.8B); FCF NT$476.56B ≈ US$14.9B (อัตรา 31.98 NT$/US$ จาก 1,494.24/46.72)
- Q3'25 (ฐานเทียบ): OCF NT$426.83B, Capex NT$287.45B (แปลงด้วยอัตราประมาณ ~30 NT$/US$ = **ประมาณ** → OCF ~US$14.2B, Capex ~US$9.6B)
- Interest-bearing debt ณ 30 ก.ย. 2026: NT$1,031.58B ≈ US$32.3B (แปลงที่ 31.98 — ประมาณ; Q2 เดิมใช้ $33.59B)
- Cash & marketable securities ~US$126B (brief 10-20)
- Shares: 5.186B ADR-equivalent (carried จากรอบ 08-17; ไม่ได้ re-verify)
- Beta 1.35 (carried จากรอบ 08-17, ประมาณจาก CNBC/GuruFocus/Macroaxis; ไม่ได้ re-verify)
- Risk-free 10Y = 5.125% (Yahoo ^TNX 2026-10-20 ตามที่ผู้สั่งงานระบุ)
- ห้ามใช้ FV ของ Morningstar/GuruFocus ในการคำนวณ

## LTM ใหม่ (สอบกลับแบบ roll-forward: LTM Q2'26 + Q3'26 − Q3'25)
| รายการ | LTM Q2'26 (08-17) | + Q3'26 | − Q3'25 | LTM Q3'26 |
|---|---|---|---|---|
| Revenue | $130.0B | 46.72 | ~33.1 (Q3'25 ≈ $33.1B, อนุมานจากตัวเลข LTM $143.6B ที่ผู้สั่งงานให้) | **~$143.6B** |
| OCF | $82.28B | 28.76 (919.77/31.98) | ~14.2 | **~$96.8B** |
| Capex | $46.57B | 13.8 | ~9.6 | **~$50.8B** |
| FCF | $35.71B | 14.9 | ~4.6 | **~$46.0B** (margin ~32%) |

หมายเหตุ: ตัวเลข LTM เป็นการประมาณ (การแปลง FX ของ Q3'25 และ revenue Q3'25 ไม่ได้ดึงจาก filing โดยตรง) ความคลาดเคลื่อนคาดไม่เกิน ±$2B และไม่กระทบ DCF มาก เพราะ DCF ใช้ forward revenue เป็นฐาน

## Assumptions

### Net cash
Cash $126B − debt $32.3B = **+$93.7B** (เดิม +$76.99B)

### Revenue (เปลี่ยนวิธีฐานปีที่ 1)
รอบ 08-17 ใช้ LTM × (1+growth) ซึ่งตอนนี้ **ต่ำกว่า run-rate จริงมาก** (Q4 guide midpoint $53.3B ×4 = $213B vs LTM $143.6B) จึงตั้งปีที่ 1 = NTM (Q4'26–Q3'27) โดยตรง:
- Q4'26 = $53.3B (guide midpoint $52.3-54.3B)
- Q1-Q3'27 โต +4% QoQ (ช้ากว่า +14-16% QoQ ล่าสุด; ผู้บริหารยัง "demand higher than supply" แต่ capacity constraint) → 55.4 / 57.6 / 59.9
- **ปี 1 ≈ $225B** (+57% เทียบ LTM เป็นผลจากการ catch-up ของ LTM ที่ล้าหลัง ไม่ใช่ growth จริงรายปี)

| ปี | Growth | Revenue ($B) | เหตุผล |
|---|---|---|---|
| 1 | NTM | 225.0 | ดูด้านบน |
| 2 | 25% | 281.3 | เท่าเดิมรอบ 08-17: hyperscaler capex เริ่ม normalize, N2/A14 ramp ยังหนุน |
| 3 | 18% | 331.9 | คู่แข่ง (Samsung/Intel) ไล่ตาม; mean reversion |
| 4 | 12% | 371.7 | ยังสูงกว่า pre-AI baseline เพราะ AI structural |
| 5 | 8% | 401.4 | ใกล้ terminal |

### FCF margin
| ปี | Margin | เหตุผล |
|---|---|---|
| 1-3 | 31% | LTM/Q3 จริง ~32%; CFO ระบุ capex 2026-2028 "significantly higher" จึงไม่ใส่ margin expansion; overseas fab dilution ขยายเป็น 3-4pt กด GM |
| 4 | 32% | capex intensity เริ่มลดเมื่อ buildout ผ่านจุดสูงสุด |
| 5 | 32% | เดิมรอบ 08-17 คาด 31% ในปี 5 — ปรับขึ้นเล็กน้อยตามหลักฐาน margin จริง แต่ **ไม่** ไปถึง 34-35% เพราะ capex ยังหนัก |

### Terminal growth 3.0% (คงเดิม — Wide Moat, share 72.5% foundry; ไม่ปรับเพื่อไม่ให้ผลเปลี่ยนจากการเปลี่ยน assumption หลายตัวพร้อมกัน)

### WACC 11.9%
Cost of equity = 5.125% + 1.35 × 5.0% = 5.125% + 6.75% = 11.875% → **11.9%** (net cash → ใช้ cost of equity ตรงๆ) (เดิม 11.5% เพราะ rf 4.69%)

## DCF Calculation (Base: WACC 11.9%, g 3.0%)
| ปี | Revenue | FCF margin | FCF ($B) | PV @11.9% ($B) |
|---|---|---|---|---|
| 1 | 225.0 | 31% | 69.8 | 62.3 |
| 2 | 281.3 | 31% | 87.2 | 69.6 |
| 3 | 331.9 | 31% | 102.9 | 73.4 |
| 4 | 371.7 | 32% | 118.9 | 75.9 |
| 5 | 401.4 | 32% | 128.4 | 73.2 |

- Sum PV Stage 1 = **$354.5B**
- TV = 128.4 × 1.03 ÷ (0.119 − 0.03) = **$1,486.5B**; PV(TV) = **$847.3B** (~70% ของ EV)
- EV = $1,201.8B; + net cash $93.7B = Equity **$1,295.5B**; ÷ 5.186B = **$249.8**

## Fair Value
| Scenario | WACC | g | FV/share |
|---|---|---|---|
| Bear | 12.9% | 2.5% | **$217.7** |
| **Base** | **11.9%** | **3.0%** | **$249.8** |
| Bull | 10.9% | 3.5% | **$294.9** |

## เทียบราคาปัจจุบัน $427.555
🔴 **Expensive** — ราคาสูงกว่า Base FV ($249.8) **+71.2%**; สูงกว่า Bull ($294.9) +45.0% (ราคา = Base × 1.71 ; Base ต่ำกว่าราคา ~41.6%)

## ที่มาของการเปลี่ยนจากรอบ 08-17 ($192.3 → $249.8, +30%)
- ปัจจัยบวก: ฐานรายได้ปี 1 สูงขึ้นมาก ($171.6B → $225B), FCF margin จริง ~32% (สูงกว่าที่สมมติ 27-31%), net cash +$16.7B
- ปัจจัยลบ: WACC สูงขึ้น 11.5% → 11.9% จาก rf 4.69% → 5.125%
- Bull ยังต่ำกว่าราคา แปลว่าราคาปัจจุบันต้องการ WACC ต่ำกว่านี้มาก และ/หรือ growth ยาวกว่า fade 5 ปีนี้มาก (ไม่ได้คำนวณจุดคุ้มทุนแน่นอน)

## ข้อจำกัด
- DCF ไวต่อ WACC (±1% ≈ ±13-18%) และ TV ~70% ของ EV; ปี 1 NTM เป็น judgment ของ QoQ +4%
- Beta, shares ไม่ได้ re-verify; FX/Q3'25 เป็นค่าประมาณ
- เป็นมุมมองที่ conservative: ไม่ได้ใส่ AI accelerator CAGR mid-to-high 50s% ที่ผู้บริหารพูด ถ้า growth ปี 2-3 สูงกว่า fade นี้ FV จะสูงขึ้น (เช่น ปี 2 +35% / ปี 3 +25% แทน 25%/18% จะยกฐานรายได้ปี 5 ~+14%)
