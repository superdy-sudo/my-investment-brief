# 💰 Conquest DCF: ECG — 2026-10-08
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions
- Base FCF (normalized 2026E): ~$190M (~4.1% ของ revenue guide midpoint $4.6B). เหตุผล: FCF ดิบผันผวนตาม working capital (FY24 $128.8M/4.5%, FY25 $100.0M/2.7%, H1'26 $167.0M/7.4%) จึงไม่ใช้ H1'26 annualize. Bottom-up: EBITDA guide mid $417.5M - capex ~$95M - ภาษีเงินสด ~$85M (ประมาณ 25% ของ EBIT) - ดอกเบี้ย ~$18M - ลงทุน working capital ~$40M ≈ $180M; ปัดเป็น $190M (ประมาณการ ไม่ใช่ตัวเลขรายงาน)
- Growth fade (FCF, 2027-2031): 18% -> 13% -> 9% -> 6% -> 4%. เหตุผล: backlog $4.55B +53% รองรับปีแรก แต่ margin EBITDA 10.4% อยู่ระดับสูงของวัฏจักร, fixed-price risk, ธุรกิจรับเหมาไม่มี moat ชัด จึง fade เร็วเข้าสู่ระดับ GDP+
- Terminal growth: 3.0% (ขอบบนของช่วงปกติ เพราะ demand data center/utility ยาว แต่ไม่มี moat จึงไม่เกิน)
- WACC: 12.0% = cost of equity 12.3% (risk-free 10Y 5.30% [ตัวเลขจาก daily-brief 10-08] + beta 1.4 [ประมาณ ไม่ได้ดึงจริง: spin-off ใหม่ รับเหมา cyclical ผูก data center] x ERP 5.0%); หนี้น้อย (net leverage 0.3x) จึงถ่วงหนี้เล็กน้อย -> ~12.0%
- Diluted shares: 51.22M (10-Q Q2'26)
- Net debt: $120.1M (cash $157.4M, debt $274.5M, 30 มิ.ย. 2026)
- สมมติ discount ปี 2027 = t1 (ไม่ปรับ stub Q4'26)

## DCF Calculation (base, $M)
| ปี | FCF | DF @12% | PV |
|---|---|---|---|
| 2027 | 224.2 | 0.893 | 200.2 |
| 2028 | 253.3 | 0.797 | 201.9 |
| 2029 | 276.1 | 0.712 | 196.5 |
| 2030 | 292.7 | 0.636 | 186.0 |
| 2031 | 304.4 | 0.567 | 172.7 |

- PV Stage 1 = 957.3
- TV = 304.4 x 1.03 / (0.12 - 0.03) = 3,483.7 -> PV 1,976.6
- EV = 2,933.9 | Equity = 2,933.9 - 120.1 = 2,813.8 | / 51.22M = **$54.9**

## Fair Value
- Bear (WACC 13%, g 2.5%): $47.4
- **Base (WACC 12%, g 3.0%): $54.9**
- Bull (WACC 11%, g 3.5%): $65.5

## เทียบราคาปัจจุบัน $124.30
🔴 Expensive — ราคาสูงกว่า Base FV ~+126% (FV ต่ำกว่าราคา ~56%); แม้ Bull ($65.5) ราคายังสูงกว่า ~90%
ราคาปัจจุบันบอกเป็นนัยว่าตลาดคาด FCF โตสูง/ยาวกว่า fade นี้มาก หรือใช้ discount rate ต่ำกว่ามาก (reverse check: ต้อง FCF base/การเติบโตสูงกว่าสมมติฐานเท่าตัว) ผลไวต่อ base FCF: ถ้า normalized FCF = $250M (6% margin คงที่) FV base ≈ $72 ยังต่ำกว่าราคา

## เทียบกับ Morningstar/GuruFocus
- Morningstar FV: ไม่มี (quantitative เท่านั้น) / GuruFocus GF Value: N/A -> conquest เป็นแหล่งเดียว ไม่มีการเทียบ 2-ใน-3
- ความเชื่อมั่น: ปานกลาง-ต่ำ เพราะ beta เป็นการประมาณ และ base FCF เป็น normalized ประมาณการเอง
