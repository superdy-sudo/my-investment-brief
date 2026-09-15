# 💰 Conquest DCF: STRL (Sterling Infrastructure) — 2026-09-15
*Independent bottom-up 2-stage DCF (Claude-only, ไม่อิงตัวเลข fair value จากแหล่งอื่น — คำนวณเองจาก raw fundamentals ในไฟล์ brief + WebSearch เฉพาะ beta/risk-free rate)*

## Assumptions

**Base FCF (FY2026, Year 0): ~$520M**
ที่มา: H1 2026 actual FCF = OCF $328M − capex $70M = $258M → annualize แบบตรงไปตรงมาที่สุด (H1 × 2 = $516M ≈ $520M) แทนที่จะเดา H2 seasonality/acceleration ที่ไม่มีหลักฐานชัดรองรับ (rule: ห้ามเดาแบบไม่มีฐาน) — **หมายเหตุ:** วิธีนี้น่าจะ conservative กว่าความจริง เพราะ E-Infra ramp และ backlog conversion กำลังเร่งตัวเข้า H2 มากกว่า H1 (Transportation segment กำลังหดตัวลง ขณะ E-Infra โตแรงขึ้นเรื่อยๆ) แต่เลือกใช้ตัวเลข actual ที่ verify ได้แทนการประมาณ H2 ที่ไม่มีฐานข้อมูลรองรับ

**Revenue growth fade (Year 1-5, ปี FY2027-2031):**
| ปี | Growth |
|---|---|
| Y1 (FY2027) | 30% |
| Y2 (FY2028) | 20% |
| Y3 (FY2029) | 13% |
| Y4 (FY2030) | 10% |
| Y5 (FY2031) | 8% |

เหตุผล fade: FY2026 guidance growth +63.7% YoY (midpoint) เร่งตัวจาก backlog conversion ($4.3B signed, 2x YoY) แต่ backlog นี้ให้ visibility จริงแค่ ~1-1.5 ปี (signed backlog $4.3B ≈ ~1x ของ FY2026 guidance revenue, combined $5.6B ≈ ~1.4x) ไม่ใช่ multi-year locked-in recurring contract — เป็น construction backlog ที่ต้อง re-book ต่อเนื่องทุกปี ธุรกิจนี้ concentration สูงขึ้นเรื่อยๆ ใน hyperscaler/semiconductor capex cycle เดียว (E-Infra ~70% ของรายได้ ขณะ Transportation -20% YoY) ซึ่งเป็น cyclical capex ไม่ใช่ recurring revenue — ถ้า AI capex cycle ชะลอ growth จะ mean-revert กลับสู่ historical construction industry range (high-single-digit ถึง low-teens) ค่อนข้างเร็ว ตาม fade นี้ Year 5 เหลือ 8% ใกล้เคียง terminal และยังสูงกว่า FY2025 pre-AI-boom growth rate (+17.69%) เล็กน้อยเพื่อสะท้อนว่า mix ที่ดีขึ้น (E-Infra margin สูงกว่า) ยังช่วยหนุนได้บ้าง

**Terminal growth rate: 2.5%**
ผูกกับ long-run GDP + inflation blend มาตรฐาน — ไม่ใช้ terminal growth สูงกว่านี้ เพราะ STRL ไม่ใช่ธุรกิจที่มี durable pricing power ที่พิสูจน์แล้วเต็มรอบ (Layer 2 ข้อ 4-5 ยังเป็น ⚠️ Uncertain — คู่แข่งใหญ่กว่า Quanta/MasTec/EMCOR ยังอยู่ในตลาดเดียวกัน) เป็นธุรกิจ construction/engineering แบบ project-based ไม่ใช่ subscription — terminal growth สูงกว่า GDP ไม่มีหลักฐานรองรับ

**WACC: 11.5%**
- Risk-free rate: 10Y Treasury yield = 5.02% (2026-09-15, สูงสุดตั้งแต่ปี 2007 จาก oil surge + inflation + Fed rate-hike expectation) [WebSearch]
- Equity Risk Premium: 4.5% (กลางช่วงมาตรฐานตลาด 4-6%)
- Beta: 1.44 (5-year, Zacks) [WebSearch] — สอดคล้องกับความผันผวนสูงของหุ้น (ราคาร่วง -19.2% ใน 1 เดือนที่ผ่านมา)
- WACC ≈ Cost of Equity = 5.02% + 1.44 × 4.5% = **11.50%** — ใช้ cost of equity ตรงๆ ไม่ weighted กับ cost of debt เพราะบริษัทเป็น net-cash ($181M) ตามกฎมาตรฐาน

**Shares outstanding diluted:** ~30.6M (จาก market cap $14.28B ÷ price $465.995)
**Net cash:** $181M (cash $464M − debt $284M)

## DCF Calculation (Base Case)

| ปี | Revenue ($B) | FCF ($M) | Discount Factor @11.5% | PV FCF ($M) |
|---|---|---|---|---|
| Y0 (FY26) | 4.075 | 520 | — | — |
| Y1 (FY27) | 5.298 | 676.0 | 0.8969 | 606.3 |
| Y2 (FY28) | 6.357 | 811.2 | 0.8044 | 652.6 |
| Y3 (FY29) | 7.183 | 916.7 | 0.7215 | 661.5 |
| Y4 (FY30) | 7.902 | 1,008.4 | 0.6470 | 652.4 |
| Y5 (FY31) | 8.534 | 1,089.1 | 0.5802 | 631.9 |

Sum PV of Stage-1 FCF = **$3,204.7M**

Terminal Value = FCF₅ × (1+g) / (WACC−g) = 1,089.1 × 1.025 / (0.115−0.025) = **$12,403.3M**
PV of Terminal Value = 12,403.3 × 0.5802 = **$7,196.9M**

Enterprise Value = 3,204.7 + 7,196.9 = **$10,401.6M**
+ Net cash $181M → Equity Value = **$10,582.6M**
÷ 30.6M diluted shares = **Fair Value ≈ $345.8/share**

## Sensitivity (3 Scenarios — ปรับ WACC ±1% / terminal g ±0.5%, FCF forecast คงเดิม)

| Scenario | WACC | Terminal g | Fair Value/share |
|---|---|---|---|
| 🐻 Bear | 12.5% | 2.0% | **$299.7** |
| ⚖️ **Base** | **11.5%** | **2.5%** | **$345.8** |
| 🐂 Bull | 10.5% | 3.0% | **$410.1** |

## เทียบราคาปัจจุบัน $465.995

🔴 **Expensive** — สูงกว่า Base case FV ($345.8) **+34.8%** และสูงกว่าแม้กระทั่ง Bull case ($410.1) **+13.6%**
ราคาปัจจุบันต่ำกว่า Bear case เพียง... ไม่ใช่ ราคาสูงกว่า Bear case ด้วยซ้ำ (+55.5%) — กล่าวคือ ราคาตลาดวันนี้อยู่ *เหนือ* ทั้ง 3 สถานการณ์ที่คำนวณจาก fundamentals และ assumption ที่มีเหตุผลรองรับ ต้องใช้ assumption ที่ aggressive กว่า Bull case ของผม (เช่น WACC ต่ำกว่า 10.5% มาก หรือ growth fade ช้ากว่านี้มาก หรือ terminal growth สูงกว่า 3% อย่างมีนัยสำคัญ) จึงจะ justify ราคาปัจจุบันได้

## เทียบกับ Morningstar/GuruFocus

- **Morningstar FV $918.67** — ห่างจาก conquest base case มาก (+165.7%) และห่างจากแม้แต่ conquest bull case (+124.0%) ตัวเลขนี้ implies การเติบโตต่อเนื่องสูงกว่า fade schedule ของผมมาก (revenue growth assumption ของ Morningstar เพิ่งปรับขึ้นเป็น 21.02% — ถ้าคงระดับนั้นยาวนานกว่า 5 ปีที่ผมสมมติ Terminal Value จะพองตัวมาก) บวกกับใช้ future P/E 29.15x ซึ่งเป็นวิธี relative-multiple ไม่ใช่ DCF-mechanics ล้วนๆ แบบผม — ผมมองว่า assumption ของ Morningstar ไม่ conservative พอเมื่อพิจารณาว่า backlog ให้ visibility จริงแค่ ~1-1.5 ปี ไม่ใช่ multi-year recurring contract และ concentration risk เข้าสู่ hyperscaler/semiconductor customer base เดียวเพิ่มขึ้นเรื่อยๆ (Transportation -20% YoY)

- **GuruFocus GF Value $290.20** — ใกล้กับ conquest **Bear case** ($299.7) มากที่สุด (ห่างกันแค่ +3.3%) และห่างจาก Base case ของผม -16.1% (ต่ำกว่า) วิธี historical-multiple regression ของ GuruFocus (backward-looking) โดยธรรมชาติจะ "ลงโทษ" การเติบโตที่เพิ่งเร่งตัวขึ้นใหม่ (มองว่าไม่ยั่งยืน) ซึ่งใกล้เคียงกับ assumption แบบ fade-fast ของผมใน bear case มากกว่า base case

- **สรุป:** Conquest DCF อิสระเห็นด้วยกับฝั่ง **GuruFocus (ฝั่งอนุรักษ์นิยม)** มากกว่า Morningstar อย่างชัดเจน — แม้ base case ของผม ($345.8) จะสูงกว่า GuruFocus ($290.20) อยู่บ้าง แต่ทั้งคู่อยู่ในเซนติเมนต์เดียวกัน (backward/mean-reversion-leaning) ตรงข้ามกับ Morningstar ที่ต้อง assume การเติบโตแบบ hypergrowth ต่อเนื่องยาวนานกว่าที่ backlog visibility จริงจะรองรับได้ **นัยสำคัญ: 2 ใน 3 แหล่งอิสระ (GuruFocus + Conquest) ชี้ไปทาง fair value ต่ำกว่าราคาตลาดปัจจุบัน ($465.995) อย่างมีนัยสำคัญ ขณะ Morningstar เป็น outlier ด้านสูง** → ควรตีความ valuation ของ STRL ไปทาง 🔴 **Expensive** มากกว่า 🟢 Cheap ที่ Morningstar อย่างเดียวชี้ไว้ก่อนหน้านี้

## ข้อจำกัดที่ควรระบุ (Limitations)
1. Base FCF ($520M) มาจาก H1 2026 actual × 2 (ไม่ปรับ H2 seasonality/acceleration) — อาจ conservative เกินจริงถ้า E-Infra ramp เร่งแรงใน H2 ตามที่ guidance บอกเป็นนัย ถ้า Base FCF สูงกว่านี้ (เช่น $600M) Fair Value ทุก scenario จะขยับขึ้นตามสัดส่วน (~15%) ซึ่งจะทำให้ Base case ใกล้เคียง current price มากขึ้น (แต่ยังต่ำกว่า)
2. Beta 1.44 มาจาก 5-year historical (Zacks) ซึ่งรวมช่วงก่อนที่ STRL จะกลายเป็น "AI infrastructure play" เต็มตัว — beta ปัจจุบันอาจสูงกว่านี้เนื่องจากหุ้นผันผวนแรงขึ้นมากในปีที่ผ่านมา (ถ้า beta สูงกว่านี้ WACC จะสูงขึ้น → Fair Value จะยิ่งต่ำลงกว่าที่คำนวณ)
3. FCF assumed เติบโตในอัตราเดียวกับ revenue (constant margin ~14.4%) ไม่ได้ model margin expansion จาก operating leverage/mix shift ไปทาง E-Infra แยกต่างหาก — ถ้า margin ขยายตัวจริงตามที่ adj EBITDA margin โชว์ (22%, +150bps YoY) Fair Value อาจสูงกว่าที่คำนวณเล็กน้อย
