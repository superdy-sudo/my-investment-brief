# 💰 Conquest DCF: BAM — 2026-09-04
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Cash-flow proxy ที่เลือก
ใช้ **Distributable Earnings (DE) per share** แทน FCF มาตรฐาน — DE คือ cash ที่ actually จ่ายได้ให้ผู้ถือหุ้น (fee income หลัง corporate cost/tax + realized carry) เป็น proxy ที่ levered-to-equity แล้ว จึงคิดลดด้วย **cost of equity** ตรงๆ (ไม่ต้องทำ WACC แบบ EV แล้วลบหนี้ทีหลัง) — FRE ถูกใช้แค่ cross-check เพราะเป็นรายได้ recurring pre-corporate-cost เท่านั้น ไม่ใช่ cash flow เต็มที่ถึงมือผู้ถือหุ้น

## Assumptions
- **Base DE/share (LTM):** $1.75 (LTM DE $2.8B ÷ ~1,600M diluted shares, +12% YoY LTM; Q2 2026 เดี่ยว DE $0.44/share +15% YoY — โมเมนตัมล่าสุดเร่งกว่าค่าเฉลี่ย LTM)
- **Growth fade (ปี 1-5):** ปี1 15% → ปี2 12% → ปี3 9% → ปี4 6% → ปี5 4%
  เหตุผล: (1) เริ่มจาก run-rate ล่าสุด (Q2 +15% YoY) ไม่ใช่ peak FRE growth (19-20%) เพราะ DE volatile กว่าและรวม realized-carry cyclicality; (2) AUM base ใหญ่ขึ้นเรื่อยๆ ($1.18T) ทำให้ % growth เพิ่มยากขึ้นตามกฎ large-number; (3) ผู้บริหารเองพูดว่าปี 2027 "robust แต่ probably not" ทำสถิติใหม่เท่าปี 2026 — สัญญาณ deceleration ชัดเจนจากปากบริษัท; (4) คู่แข่ง megafund (Blackstone, KKR, Apollo) แย่ง deal flow มากขึ้นเรื่อยๆ กด margin ระยะยาว
- **Terminal growth:** 3% (ผูกกับ long-run GDP+inflation มาตรฐาน — ไม่ใช้ premium สูงกว่าแม้ moat จะกว้าง เพราะ DE มี cyclical component จาก realized carry ที่ไม่ควรสมมติว่าโตเกิน GDP ตลอดไป)
- **Discount rate (cost of equity):** 11.25% = risk-free 4.75% (10Y UST, ก.ย. 2026) + beta 1.3 (**ประมาณ** — หา beta เฉพาะของ BAM ไม่เจอชัดเจนจากแหล่งที่ WebSearch ได้ ใช้ค่ากลางเทียบเคียงกลุ่ม alt-asset-manager เช่น BX/KKR/APO ซึ่งอยู่ราว 1.3-1.5 แต่ BAM มี recurring-fee mix สูงกว่าคู่แข่งบางตัวจึงใช้ขอบล่างของกลุ่ม) × ERP 5% (มาตรฐานตลาด)
- **Shares outstanding:** ~1,620M diluted (คำนวณจาก LTM DE $2.8B ÷ $1.75/share, สอดคล้องกับ market cap $81.5B ÷ $50.29)
- **Net debt:** ~$1.4B (cash $1.5B ณ 30 มิ.ย. 2026 vs total debt $2.9B) ≈ -$0.86/share — ผลกระทบเล็กน้อย (~3% ของมูลค่ารวม) เพราะ DE per-share เป็น levered metric อยู่แล้ว

## DCF Calculation (Base case)
| ปี | Growth | DE/share | PV factor @11.25% | PV |
|---|---|---|---|---|
| 1 | 15% | $2.01 | 0.899 | $1.81 |
| 2 | 12% | $2.25 | 0.808 | $1.82 |
| 3 | 9% | $2.46 | 0.726 | $1.79 |
| 4 | 6% | $2.60 | 0.653 | $1.70 |
| 5 | 4% | $2.71 | 0.587 | $1.59 |

- Sum PV of Stage-1 cash flows: **$8.71/share**
- Terminal value (ปี5 × 1.03 ÷ (0.1125−0.03)): $33.81 → PV = **$19.85/share**
- Equity value/share (ก่อนปรับ net debt): $28.55
- ปรับ net debt (-$0.86/share): **$27.69/share**

## Fair Value
- Bear case (WACC 12.25%, terminal g 2.5%): **$23.6**
- **Base case: $27.7**
- Bull case (WACC 10.25%, terminal g 3.5%): **$33.6**

## เทียบราคาปัจจุบัน $50.29
🔴 **Expensive** — ราคาสูงกว่า Base case FV +81.6% (สูงกว่าแม้แต่ Bull case ($33.6) ก็ยัง +49.7%)

## เทียบกับ Morningstar/GuruFocus
- **Morningstar FV $28** — ใกล้กับ conquest base case ($27.7) มาก (ต่างกัน <2%) แม้จะคำนวณจากคนละวิธี/คนละตัวเลขตั้งต้น สะท้อนว่า forward-DCF ที่ใช้ discount rate ระดับ double-digit (สอดคล้องกับความเสี่ยง earnings ที่ผูกกับ capital markets cycle) ให้ผลใกล้เคียงกัน
- **GuruFocus GF Value $55-59** — ไกลจาก conquest base case มาก (+~100%) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่ extrapolate multiple ที่ตลาดเคย pay ให้ BAM/asset managers ในอดีต (ช่วงดอกเบี้ยต่ำกว่านี้) มาปรับใช้กับรายได้ปัจจุบัน — ไม่ได้ปรับ discount rate ตามระดับดอกเบี้ยปัจจุบัน (10Y UST ~4.75%) เหมือนวิธี DCF
- **สรุป:** Conquest เห็นด้วยกับ Morningstar อย่างชัดเจน (ทั้งสองใช้ forward cash-flow discounting ที่ sensitive กับ discount rate ปัจจุบัน) และขัดแย้งกับ GuruFocus ซึ่งไม่ได้ปรับ multiple ตามภาวะดอกเบี้ยปัจจุบัน — 2 ใน 3 แหล่ง (Morningstar + Conquest อิสระ) เห็นตรงกันว่า **Expensive**

⚠️ **หมายเหตุความน่าเชื่อถือ:** ผลลัพธ์ conquest DCF ของ ticker ต่างๆ ที่ผ่านมามักเอนไปทาง "Expensive" เป็นส่วนใหญ่ (10/11 ครั้งก่อนหน้า) เพราะ methodology นี้ (WACC/terminal growth แบบ conservative) มี bias เชิงระบบไปทาง valuation เข้มกว่าตลาดโดยธรรมชาติ — ควรอ่านผลนี้เป็น "มุมมองที่เข้มที่สุดในบรรดา 3 แหล่ง" ไม่ใช่คำตัดสินสุดท้ายเพียงลำพัง แต่การที่ Morningstar (คนละ methodology, คนละทีมคำนวณ) ลงมาที่ตัวเลขใกล้เคียงกันมาก ($28 vs $27.7) ให้น้ำหนักเพิ่มกับฝั่ง Expensive ในเคสนี้
