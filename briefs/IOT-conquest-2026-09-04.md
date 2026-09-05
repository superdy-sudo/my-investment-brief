# 💰 Conquest DCF: IOT (Samsara Inc.) — 2026-09-04
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น)*

## Assumptions

**Base FCF (FY2027, current fiscal year — ending ~Jan 2027):**
- Full-year revenue guidance (post-Q2 beat): $2.043–2.047B → midpoint **$2,045M**
- FY2027 blended FCF margin: **12%** (Q2 actual 13%, แต่ management เตือนล่วงหน้าเรื่อง margin pressure จาก IoT device investment + supply-chain cost ใน H2 → เฉลี่ยทั้งปีลดลงเล็กน้อยจาก Q2)
- Base FCF ≈ **$245M**

**Stage 1 — 5-year growth fade (revenue YoY):**
| ปี | Growth | FCF margin |
|---|---|---|
| Y1 (FY28) | 25% | 11% |
| Y2 (FY29) | 22% | 13% |
| Y3 (FY30) | 18% | 16% |
| Y4 (FY31) | 15% | 20% |
| Y5 (FY32) | 12% | 24% |

เหตุผล fade: FY27 guide ปัจจุบันคือ 26% (actual Q2 ทำได้ 30% แต่ guide ทั้งปียัง conservative) — ปีที่ 1 เริ่มใกล้เคียง guide ปัจจุบันแล้วลดหลั่นตาม mean-reversion มาตรฐานของ SaaS/hardware-hybrid growth company เมื่อ revenue base ใหญ่ขึ้น (จาก $2.0B → $4.7B ใน 5 ปี, โต 2.3x) แม้ TAM ที่เหลือยังมหาศาล ($137B = ~67x revenue ปัจจุบัน) แต่ growth % ต้องลดลงตามกฎ large-number แม้ TAM จะรองรับได้

FCF margin trajectory: เริ่มกดดันปีแรกตามคำเตือนผู้บริหาร (device capex + supply chain) แล้วฟื้นตัวขึ้นเป็น mature-SaaS-like margin (~24% ปีที่ 5) ตาม operating leverage เมื่อ S&M/R&D ratio ลดลงเทียบ revenue — ยังคง**ต่ำกว่า** mature SaaS peer ทั่วไป (25-35%) เพื่อความระมัดระวัง เพราะ Samsara เป็น hardware+software hybrid ที่มี COGS สูงกว่า pure-software

**Terminal growth: 3%** — มาตรฐานผูก long-run GDP/inflation, ไม่ให้ premium เพิ่มแม้มี switching-cost moat ที่ยั่งยืน เพราะยังมีความเสี่ยงเชิงคุณภาพกำไร (ดูหัวข้อ SBC ด้านล่าง) ที่ทำให้ไม่อยากให้ terminal assumption เกินมาตรฐาน

**WACC ≈ 11.5%** (cost of equity ตรงๆ เพราะ net-cash):
- Risk-free rate (10Y UST, ก.ย. 2026): **4.78%**
- Beta (Yahoo Finance, 5Y monthly): **1.28**
- Equity risk premium: **5.0%** (มาตรฐานตลาด)
- Cost of equity = 4.78% + 1.28×5.0% = **11.18%**
- **+0.5% quality-of-earnings/governance premium** เพิ่มเข้าไปเป็น WACC ~11.7% ปัดเหลือ **11.5%** เพื่อสะท้อนความเสี่ยง SBC/dilution (ดูด้านล่าง) — ไม่ได้ subtract SBC ออกจาก FCF ตรงๆ (จะรุนแรงเกินไป เพราะ SBC ก็ซื้อ talent/retention จริง) แต่ใช้สองช่องทางแทน: (1) WACC premium เล็กน้อย (2) เพิ่ม share count ในอนาคตแทน dilution จริง

**SBC/Dilution treatment:** SBC ~19% ของ revenue + unrecognized SBC ค้าง ~$490M เป็นความเสี่ยงเชิงคุณภาพกำไรจริง — แทนที่จะ subtract SBC ออกจาก FCF ตรงๆ (ซึ่งจะทำให้ FCF ติดลบทันทีและรุนแรงเกินจริง เพราะ SBC ก็สร้างมูลค่าจริงผ่านการรักษาพนักงาน) เลือกใช้วิธี **เพิ่ม diluted share count ล่วงหน้า** แทน — สมมติ net dilution ~3%/ปี (หลัง buyback offset บางส่วน) ทบต้น 5 ปี: 582.7M × (1.03)^5 ≈ **675.5M หุ้น** ใช้เป็นตัวหารสำหรับ fair value per share วันนี้ (แทนที่จะใช้ 582.7M หุ้นปัจจุบันตรงๆ ซึ่งจะประเมินสูงเกินไป)

**Net cash:** $804M cash − $69M debt = **+$735M**

## DCF Calculation (Base Case, $M)

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| Revenue | 2,556 | 3,119 | 3,680 | 4,232 | 4,740 |
| FCF | 281 | 405 | 589 | 846 | 1,138 |
| PV @11.5% | 252 | 326 | 425 | 548 | 660 |

- Sum PV of Stage-1 FCF ≈ **$2,211M**
- Terminal value = FCF₅ × 1.03 / (0.115 − 0.03) ≈ **$13,785M**
- PV of terminal value ≈ **$8,000M**
- Enterprise Value ≈ **$10,210M**
- + Net cash $735M → Equity Value ≈ **$10,945M**
- ÷ 675.5M dilution-adjusted shares → **Fair Value ≈ $16.20/share**

## Fair Value

- Bear case (WACC 12.5%, terminal g 2.5%): **$13.84**
- **Base case: $16.20**
- Bull case (WACC 10.5%, terminal g 3.5%): **$19.58**

## เทียบราคาปัจจุบัน $44.15

🔴 **Expensive** — สูงกว่า Base case FV ประมาณ **+172%** (แม้เทียบกับ Bull case ($19.58) ราคาก็ยังสูงกว่า +126%)

ตลาดกำลัง price EV/Sales ~12x บน revenue ปัจจุบัน ในขณะที่ DCF อนุรักษ์นิยมนี้ implied EV/Sales เพียง ~5x — ช่องว่างสะท้อนว่าตลาดคาดหวัง growth/margin ที่สูงกว่าและยาวนานกว่าสมมติฐาน fade-to-12%-then-3%-terminal ที่ใช้ในโมเดลนี้มาก

## เทียบกับ Morningstar/GuruFocus

- Morningstar FV: ⚪ Unknown (ไม่มีตัวเลขยืนยันในตลาด)
- GuruFocus GF Value $57.42 (pre-earnings) — **ห่างไกลมาก** จาก conquest base case ($16.20 vs $57.42, ต่างกัน ~3.5x) เพราะ GF Value เป็น backward-looking historical-multiple regression ที่สะท้อน multiple ที่ตลาดเคยให้กับหุ้นกลุ่มนี้ในอดีต ไม่ได้ผูกกับ owner-earnings/DCF จริง และไม่ได้ปรับลดสำหรับความเสี่ยง SBC/dilution ที่ conquest ใส่เข้าไปตรงๆ
- **สรุป:** Conquest ไม่เห็นด้วยกับ GuruFocus อย่างมาก และเป็นมุมมองที่ **เข้มที่สุด (most conservative)** ในบรรดา 3 แหล่ง — ควรอ่านผลนี้เป็น "เพดานล่างสุดที่ยอมรับได้ถ้าไม่เชื่อ premium ใดๆ เลย" ไม่ใช่คำตัดสินสุดท้ายเดี่ยวๆ เพราะ DCF อ่อนไหวสูงต่อ terminal growth/WACC/margin-fade assumption และ conquest agent นี้มีแนวโน้มออกผล "Expensive" เป็นส่วนใหญ่จากธรรมชาติของ conservative WACC/terminal growth (ตามที่เคยสังเกตมาก่อนหน้านี้) — ควรใช้ประกอบกับ Layer 2 compounder checklist (5/5 confirmed) และ analyst price-target momentum ที่ยกขึ้นทั่วกระดานหลังงบ ไม่ใช่ใช้ conquest ตัดสินเดี่ยว
