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

*(ยังไม่มี entry — เพิ่มทีละรายการเมื่อทดสอบจริง ตาม template ด้านล่าง)*

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
