# Weekly Review — Pre vs Post Market Accuracy
## สัปดาห์ Jun 15–20, 2026 | force mode ⚠️

---

## 📊 Pre vs Post Market Accuracy (ข้อมูลที่มี)

> Close Mode เริ่มใช้ Jun 18 เป็นวันแรก — มีข้อมูล pair เพียง 1 วัน

### Jun 18: Pre-market (market-overview-2026-06-18.md) vs Close (close-2026-06-18.md)

| ด้านที่คาด | คาดเช้า | จริงปิด | ถูก/ผิด |
|-----------|---------|---------|---------|
| S&P direction | +0.72% (futures) | **+1.08%** | ✅ ถูก |
| NASDAQ direction | +1.38% (futures) | **+1.91%** | ✅ ถูก |
| Financials sector | defensive (ดีสุดเมื่อวาน) | Holdings ทุกตัวลง ⚠️ | ❌ ผิด |
| Holdings follow market | คาดว่า recover ตาม | SPGI -1.70%, CME -2.44%, V -0.95%, MA -0.65%, GWRE -2.98% | ❌ ผิด |
| CME kill zone | ⚠️ ใกล้ kill | **BREACHED $246.38 < $246.51** | ✅ True Positive |

**Pre vs Post accuracy Jun 18: 3/5 (60%)**

### ปัญหาที่เจอ: Holdings Diverge จากตลาด
- S&P +1.08% แต่ Holdings ทุกตัวลง
- เหตุผลที่ระบบไม่ได้คาด: CEO CME ลาออก (Jun 17) + GWRE insider sell (Jun 15-16)
- ระบบ brief เช้ามีข้อมูล CEO CME ใน portfolio.md แต่ไม่ได้ escalate เป็น "จะกดราคาแม้ตลาดขึ้น"

---

## 🏆 Top Pick Accuracy (Jun 15–20)

| Ticker | แนะนำวันที่ | Entry Zone | ราคาจริง | ผล |
|--------|-----------|------------|----------|----|
| ไม่มี (SYK เกิน zone) | Jun 15–16 | < $295 | $307.94 | ✅ ถูกที่ไม่แนะนำ |
| GWRE | Jun 18 | $105–$120 | ซื้อ $107.76 | ✅ zone ถูก |
| MDLZ | Jun 19–20 | $55–$63 | $60.12 | ✅ zone ถูก |

**Zone call accuracy: 3/3 (100%)**

---

## 📌 Holdings Thesis Accuracy (Jun 15–20)

| Ticker | Status Call | เหตุการณ์จริง | ถูก? |
|--------|-------------|--------------|------|
| CME ⚠️ | Hold + Kill Watch | Kill BREACHED Jun 18 close | ✅ True Positive |
| SPGI ✅ | Intact | MBGL on track, ราคาลงจาก market | ✅ ถูก |
| V ✅ | ซื้อ Jun 15 | +1.31% vs buy ✅ | ✅ ถูก |
| MA ✅ | Intact | -0.97% vs buy (minor) | ✅ ถูก |
| SPCX | ขาย Jun 17 | Realized +12.29% | ✅ ถูก |
| GWRE ⚠️ | Watch + CEO insider sell | ราคา -2.98% Jun 18 (volume 3.9x) | ✅ ถูก |

**Holdings thesis accuracy: 6/6 (100%)**

---

## 🌍 Market Overview Accuracy (Jun 12–20)

| วัน | Sector/Direction Call | จริง | ถูก? |
|-----|----------------------|------|------|
| Jun 15 | Risk-On จาก Iran deal | S&P +1.65% Jun 16 | ✅ |
| Jun 16 | FOMC hawkish → ตลาดดิ่ง | S&P -1.21% Jun 17 | ✅ |
| Jun 16 | Warsh ยกเลิก Dot Plot | ไม่เกิด — เก็บไว้ | ❌ minor |
| Jun 18 | Pre-market recover | S&P +1.08% | ✅ |
| Jun 18 | Holdings follow Financials sector | Holdings ทุกตัวลงสวนทาง | ❌ |
| Jun 20 | Financials นำ week | XLF strong | ✅ |

**Market direction accuracy: 4/5 (80%) | Holdings prediction: 0/1 (0%) วัน Jun 18**

---

## 🔧 SKILL.md Updates (force mode)

### 1. Gemini API Fallback (เพิ่มแล้ว ✅)
- เหตุผล: Gemini unavailable 2 ครั้ง (GWRE + MDLZ debate)
- การเปลี่ยน: เพิ่ม fallback rule — ใช้ Claude แทน + บันทึกชัดเจน + ลด confidence Tier A (ไม่ใช่ S)

### 2. Holdings Divergence Check (เพิ่มแล้ว ✅)
- เหตุผล: Jun 18 ตลาด +1.08% แต่ Holdings ทุกตัวลง — ระบบไม่ได้ flag
- การเปลี่ยน: ถ้า S&P ขึ้นแต่ Holdings ทุกตัวลง → ค้น stock-specific news ทันที + ห้ามสรุปว่า "market-wide"

### Pattern ที่ track ต่อ (ยังไม่ update)
| Pattern | ครั้ง | Threshold |
|---------|-------|-----------|
| Kill alert true positive | 1 | 3 |
| Entry zone ถูก | 3 | ✅ ระบบดีแล้ว |

---

## 🔍 ข้อจำกัดของ Review นี้

⚠️ Close Mode เพิ่งเริ่มวันนี้ (Jun 18) — มีข้อมูล pair เพียง 1 วัน
- Pre vs post accuracy 60% มาจาก 1 วันเท่านั้น → อาจเป็น noise
- สัปดาห์หน้าจะมีข้อมูล pair 5 วัน (จ-ศ) → review ครั้งถัดไปจะแม่นยำกว่ามาก
- ควร re-evaluate pattern อีกครั้งใน weekly-review Jun 28

---

## 📅 สิ่งที่ต้องติดตามสัปดาห์หน้า (Jun 22–27)

1. **CME** — ราคาปิด $246.38 < kill $246.51 → ตัดสินใจ: ขาย / partial / ถือถึง Jul 22
2. **SPGI MBGL WI Trading** — Jun 26 เริ่มซื้อขาย → มักเป็น catalyst ราคาขึ้น
3. **Pre vs Post accuracy** — สัปดาห์แรกที่มี close mode ครบวัน → จับตา divergence pattern
4. **GWRE volume** — 3.9x avg วันที่ซื้อ เป็น institutional exit หรือ normal volatility?
5. **Gemini API** — ถ้าใช้ Claude แทน Gemini ต้องบันทึก "Claude (Gemini unavailable)" ชัดเจน

---

*สร้างโดย /weekly-review force | Jun 21, 2026 | อัปเดต SKILL.md: 2 rules*
