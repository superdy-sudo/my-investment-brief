# 🧪 Quant Lab — Sandbox ทดลอง (ไม่ใช่ระบบตัดสินใจ)

> ⚠️ **ไฟล์นี้ห้ามใช้ตัดสินใจ Avoid/Buy/Watchlist เด็ดขาด** — `/brief` และ `/daily-brief` ห้ามอ้างอิงไฟล์นี้ในการให้ Action ใดๆ ทั้งสิ้น
>
> จุดประสงค์: เก็บไอเดีย/ผลทดลองแนวคิด quant (เช่น Statistical Arbitrage, pair trading, correlation/cointegration) ไว้ฝึกความเข้าใจเฉยๆ — เป็นคนละ philosophy กับพอร์ตหลัก (directional/concentrated/long-only, ดู [portfolio.md](portfolio.md)) ไม่ควรผสมสองกลยุทธ์เข้าด้วยกันเพราะ time horizon และ position sizing ขัดกัน

---

## หลักการที่ใช้อ้างอิง (จากคลิป ดร.พศิน — Stat Arb)

1. **Correlation คือด่านแรก ไม่ใช่ตัวชี้ขาด** — แค่บอกว่าราคาสองตัวเคลื่อนไปทางเดียวกัน
2. **Cointegration คือตัวชี้ขาดจริง** — spread ระหว่างสองตัวต้องมี mean ที่นิ่งพอจะคาดการณ์การกลับตัวได้ (mean-reversion)
3. **Cointegration แตก = stop loss ทันที** — สัญญาณว่าความสัมพันธ์เชิงโครงสร้างหายไปแล้ว (regime break) ห้ามฝืนถือต่อ
4. **OU Process** ช่วยประมาณรอบเวลาที่ราคาจะกลับตัว
5. **Position Sizing ด้วย Standard Deviation** — ผันผวนสูง → ลด size ลง
6. **Market Neutral / Non-directional** — ไม่สนทิศทางตลาดรวม ต่างจากพอร์ตหลักที่เป็น directional

---

## 📋 Pair Ideas ที่น่าลองเช็ค (ยังไม่ได้ทดสอบจริง)

### EPD vs ET — Energy Midstream MLP
- ทั้งคู่โดน `/brief` Avoid วันเดียวกัน (2026-08-22) ด้วยเหตุผลคล้ายกัน (commodity-price mirage, sector เดียวกัน) — ดู [briefs/EPD-2026-08-22.md](briefs/EPD-2026-08-22.md), [briefs/ET-2026-08-22.md](briefs/ET-2026-08-22.md)
- น่าสนใจเพราะ business model ใกล้เคียงกันมาก (midstream pipeline/NGL) — correlation น่าจะสูงโดยธรรมชาติ
- **ยังไม่ได้เช็ค:** correlation coefficient, cointegration test (เช่น Engle-Granger หรือ Johansen), historical spread behavior
- **สถานะ:** 💡 ไอเดียเฉยๆ ยังไม่ได้ทดสอบ

---

## 📝 Log การทดลอง

### [2026-08-23] — EPD vs ET (2 ปีย้อนหลัง, daily adjusted close, N=501)

- **Price level correlation:** 0.9121 (สูงมาก)
- **Daily return correlation:** 0.6549 (ปานกลาง — ต่ำกว่า price correlation ตามคาด เพราะ level correlation มักถูก inflate จาก trend ร่วมของทั้ง sector)
- **Cointegration (Engle-Granger test):** test statistic -1.95, **p-value 0.5522** ❌ — ไม่ผ่าน (ต้อง p<0.05 ถึงจะสรุปว่า cointegrated) critical values ที่ 1%/5%/10% คือ -3.92/-3.35/-3.05 ห่างจาก test statistic มาก
- **Hedge ratio (OLS, EPD = a + b·ET):** b=2.0456, a=-3.2122, R²=0.8319
- **Spread stationarity (ADF test บน spread):** ADF stat -1.95, **p-value 0.3088** ❌ — residual spread ไม่ stationary ยืนยันผล cointegration ข้างต้น
- **Spread ปัจจุบัน:** -5.3364 (เทียบ full-sample mean -3.2122, std 1.5893) → Z-score เต็มช่วง = -1.34
- **Rolling window (ดูว่า spread หลุด mean ระยะสั้นแค่ไหน):**
  | Window | Mean | Std | Current Z |
  |---|---|---|---|
  | 6mo | -2.05 | 1.12 | **-2.94** |
  | 3mo | -2.77 | 1.04 | **-2.48** |
  | 1mo | -3.79 | 0.99 | -1.56 |

**สรุป: ⚪ ไม่ผ่านเกณฑ์ cointegration — ยังไม่ควรเทรดเป็น pair แม้ correlation จะดูสูง**

เหตุผล: นี่คือเคสคลาสสิกที่ ดร.พศิน เตือนไว้พอดี — correlation 0.91 (price level) ดูสวยมาก แต่พอทดสอบ cointegration จริงด้วย Engle-Granger กลับไม่ผ่าน (p=0.55, ควรน้อยกว่า 0.05) ADF บน spread residual ก็ยืนยันว่า spread**ไม่ใช่ stationary process** — แปลว่าไม่มีหลักฐานทางสถิติว่า spread ระหว่าง EPD-ET จะ "กลับเข้าหา mean" จริง มันอาจแค่ trend ไปเรื่อยๆ ตาม sector fundamentals ที่ต่างกันทีละนิด (leverage, capital allocation quality ที่ /brief เจอว่าต่างกันจริง — ET มี "Poor" capital allocation rating จาก Morningstar ส่วน EPD ไม่มีปัญหานี้)

แม้ Z-score ระยะสั้น (6mo: -2.94, 3mo: -2.48) จะดูเหมือน "หลุด mean ไปไกลมาก น่าจะกลับ" — **ถ้าไม่มี cointegration รองรับ การเทรดตาม Z-score แบบนี้คือการเดิมพันว่ามันจะกลับ ไม่ใช่มี anchor ทางสถิติจริง** ตรงกับกฎที่ตั้งไว้ในไฟล์นี้พอดี (cointegration แตก/ไม่ผ่าน = ไม่เทรด ไม่ใช่แค่ตอน position เปิดอยู่แล้วเท่านั้น)

**ถ้าอยากลองต่อ:** อาจต้องหา pair ที่ business model เหมือนกันกว่านี้ (เช่น pure-play pipeline ที่ leverage/quality ใกล้กันจริงๆ ไม่ใช่แค่ sector เดียวกัน) หรือลอง window สั้นลง (1 ปี) เผื่อ regime เปลี่ยนในช่วงกลางของ 2-year sample ทำให้ full-period test ไม่ผ่านทั้งที่ sub-period อาจ cointegrated — ยังไม่ได้ทดสอบ

### Template
```
### [YYYY-MM-DD] — [Pair A] vs [Pair B]
- Correlation: [ค่า, ช่วงเวลาที่คำนวณ]
- Cointegration: [ผ่าน/ไม่ผ่าน + test ที่ใช้]
- Spread behavior: [mean, std, ครั้งล่าสุดที่ revert]
- สรุป: [น่าเทรดไหม + เหตุผล]
```

---

## กฎของไฟล์นี้

- อัปเดตได้อิสระ ไม่ต้อง sync กับ portfolio.md
- ไม่ต้อง commit พร้อมกับ daily-brief/brief runs — commit แยกต่างหากได้
- ถ้าจะเอาไอเดียจากที่นี่ไปทดลองจริงด้วยเงิน ต้องแยกเป็นการตัดสินใจใหม่ ไม่ใช่ auto-apply จากไฟล์นี้
