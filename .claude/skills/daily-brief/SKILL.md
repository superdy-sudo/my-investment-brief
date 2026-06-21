---
name: daily-brief
description: อัปเดตพอร์ต + Top Pick + Watchlist ประจำวัน
---

# Daily Brief Skill

## Trigger
- `/daily-brief` — รัน pipeline ปกติทั้งหมด (pre-market / ระหว่างวัน)
- `/daily-brief TICKER1,TICKER2,...` — รัน daily-brief ปกติ **+ brief หุ้นที่ระบุด้วย** (ถ้า daily-brief วันนั้นรันไปแล้ว ดูแค่หุ้นที่ระบุ)
- `/daily-brief topup` — Top-up Mode: แนะนำว่าควรซื้อตัวไหน + สัดส่วน % ที่ควรแบ่ง
- `/daily-brief close` — Close Mode: สรุปผลปิดตลาด + เปรียบเทียบกับที่ brief ทำนายตอนเช้า

---

## Step 0: อ่าน config + Mode Detection

**Mode Detection (ทำก่อนสุด):**

ถ้า argument = `close`:
- → **Close Mode** — ดู Step 0D ด้านล่าง

ถ้า argument = `topup` หรือ `topup [จำนวน]`:
- → **Top-up Mode** — ดู Step 0C ด้านล่าง

ถ้ามี argument (เช่น `/daily-brief SPACEX,V,SYK`):
1. เช็คว่าวันนี้รัน daily-brief ไปแล้วหรือยัง → ดูจากไฟล์ `briefs/market-overview-<YYYY-MM-DD>.md` หรือ Holdings brief ล่าสุด
2. **ถ้ายังไม่ได้รันวันนี้** → รัน **Full Brief Mode ปกติทุก Step ก่อน** แล้วต่อด้วย Spot Brief ของ ticker ที่ระบุ
3. **ถ้ารันไปแล้ววันนี้** → ข้าม Full Brief, รัน **Spot Brief เฉพาะ ticker ที่ระบุ** (Step 0B) แล้วจบ
- ไม่ต้องเช็ควันในสัปดาห์ — ทำได้ทุกวันรวมวันหยุด

ถ้าไม่มี argument:
- → **Full Brief Mode** — รัน pipeline ปกติทุก step
- วันเสาร์-อาทิตย์: ตลาดปิด แต่ **ยังรัน** ได้ — อาจมีข่าวสำคัญ
  - แจ้ง: "⚠️ วันหยุด — ตลาดปิด ราคาเป็น T-1 แต่ข่าวอาจมีใหม่"
  - ดำเนินต่อตามปกติ ไม่หยุด

จากนั้น:
- อ่าน `CLAUDE.md` → investment style
- อ่าน `portfolio.md` → Holdings, Kill Conditions, Top Pick ปัจจุบัน, Watchlist

---

## Step 0D: Close Mode (`/daily-brief close`)

> **Daily Brief ฉบับหลังตลาดปิด** — ค้นข้อมูลจากแหล่งเดียวกับ Full Mode แต่เน้นสิ่งที่เกิดขึ้น **ระหว่างวันและหลังปิด** + เปรียบเทียบกับที่คาดไว้เช้า

---

### C1: อ่าน baseline เช้า (ถ้ามี)

อ่านไฟล์ (ถ้ามี):
- `briefs/market-overview-<YYYY-MM-DD>.md` → sector call + macro prediction เช้า
- `briefs/<TICKER>-update-<YYYY-MM-DD>.md` ของแต่ละ Holdings → thesis status เช้า

ถ้าไม่มีไฟล์เช้า → รัน close-only ไม่มี comparison section

---

### C2: ดึงราคาปิด + After-Hours (dispatch augustus — ทำพร้อมกัน)

**Holdings ทุกตัว** (WebFetch Yahoo Finance):
- ราคาปิด + % วันนี้
- After-hours price + % (ถ้ามี)
- Volume วันนี้ vs average (สูง = แรงขาย/ซื้อมีความหมาย)

**Market Indices:**
- S&P 500, NASDAQ, Dow, VIX, 10Y Yield
- Sector performance วันนี้ — เน้น Financials + Technology (sector ที่ Holdings อยู่)

---

### C3: ค้น News หลังปิดตลาด (WebSearch — ทำพร้อมกัน)

สำหรับแต่ละ Holding ที่ขยับ ±1%+ วันนี้ → WebSearch:
- `[TICKER] news today after market close 2026`
- `[TICKER] stock analysis [date] 2026`

สำหรับ Holdings ที่ **diverge จากตลาด** (ตลาดขึ้นแต่ตัวนั้นลง หรือกลับกัน) → WebSearch เพิ่ม:
- `[TICKER] analyst downgrade upgrade today`
- `[TICKER] institutional filing SEC today`

**Market News:**
- `S&P 500 recap today [date] 2026` → สาเหตุที่ตลาดขึ้น/ลง
- `after hours movers stocks today 2026` → หุ้นอื่นที่ขยับหลังปิด (อาจกระทบ Holdings พรุ่งนี้)

---

### C4: Kill + TP Check (เหมือน Step 1B)

เช็คราคาปิดกับ Kill Zone และ TP ทุกตัว:
- Kill buffer < 5% → 🚨
- ราคาปิด ≥ TP1 → 🎯 Alert trim 30%
- After-hours ขยับมาก → แจ้งด้วย

---

### C5: เปรียบเทียบ Prediction vs จริง

เฉพาะถ้ามีไฟล์เช้า:

| ด้าน | คาดเช้า | จริงปิด | ถูก/ผิด |
|------|---------|---------|---------|
| Market direction | [จาก market-overview] | S&P จริง | ✅/❌ |
| Sector call | [คาด] | [จริง] | ✅/❌ |
| Holdings thesis | ✅/⚠️/🚨 แต่ละตัว | ราคาสอดคล้อง? | ✅/❌ |
| Kill/TP alert | [คาด] | [trigger จริงไหม] | ✅ true / ❌ false |

---

### C6: สรุปใน chat

```
📊 Close Brief — [วันที่]

🌍 ตลาดปิด:
   S&P [+X%] | NASDAQ [+X%] | VIX [XX] | Financials [+X%]
   สาเหตุหลัก: [1 ประโยคจาก news]

📌 Holdings:
   SPGI  $XXX [+X%] vol[Xx avg] AH:$XXX | thesis ✅/⚠️/🚨 | [เหตุผลถ้าผิดปกติ]
   CME   $XXX [+X%] vol[Xx avg] AH:$XXX | 🚨 Kill buffer X%
   MA    $XXX [+X%] vol[Xx avg] AH:$XXX | thesis ✅
   V     $XXX [+X%] vol[Xx avg] AH:$XXX | thesis ✅
   GWRE  $XXX [+X%] vol[Xx avg] AH:$XXX | thesis ✅/⚠️

🎯 Prediction Accuracy: X/Y ถูก (X%)
   ✅ ถูก: [รายการ]
   ❌ ผิด: [รายการ + สาเหตุจาก news]

📰 News สำคัญหลังปิด:
   [TICKER]: [ข่าวที่อาจกระทบพรุ่งนี้]
   After-hours movers: [หุ้นที่ขยับผิดปกติ — อาจกระทบ sector พรุ่งนี้]

📋 พรุ่งนี้ดูอะไร:
   1. [ประเด็นหลัก]
   2. [ประเด็นรอง]
```

**7. Save ทั้ง 2 ที่:**
- `briefs/close-<YYYY-MM-DD>.md` — archive
- `showcase/close.html` — อัปเดต comment markers ตามนี้:

| Section | Markers |
|---------|---------|
| วันที่ + เวลา | `<!-- CLOSE_DATE_START -->` … `<!-- CLOSE_DATE_END -->` |
| Ticker tape | `<!-- TAPE_START -->` … `<!-- TAPE_END -->` |
| Indices + สรุปตลาด | `<!-- INDICES_START -->` … `<!-- INDICES_END -->` (รวม MARKET_SUMMARY) |
| Holdings table | `<!-- HOLDINGS_START -->` … `<!-- HOLDINGS_END -->` |
| After-Hours | `<!-- AH_START -->` … `<!-- AH_END -->` |
| Prediction accuracy | `<!-- ACCURACY_START -->` … `<!-- ACCURACY_END -->` |
| News | `<!-- NEWS_START -->` … `<!-- NEWS_END -->` |
| Tomorrow watch | `<!-- TOMORROW_START -->` … `<!-- TOMORROW_END -->` |
| Footer | `<!-- FOOTER_START -->` … `<!-- FOOTER_END -->` |

**วิธีอัปเดต:** แทนที่เฉพาะ content ระหว่าง markers — อย่าแตะ markers เอง

---

## Step 0B: Spot Brief Mode (ใช้เฉพาะเมื่อมี argument)

---

## Step 0C: Top-up Mode (`/daily-brief topup [จำนวน]`)

> **ประหยัด token สูงสุด** — ไม่รัน pipeline ใดๆ ใช้ข้อมูลที่มีอยู่แล้ว + WebFetch ราคาเดียว

**ขั้นตอน (ทั้งหมดทำใน 1 round):**

1. **อ่าน `portfolio.md`** (local — ไม่ใช้ token search)
   - ดึง entry zone ของทุกตัวใน Watchlist
   - ดึง Top Pick ปัจจุบัน + thesis สั้น + earnings ที่รออยู่

2. **WebFetch ราคาเดียว** — Yahoo Finance Watchlist summary:
   - `https://finance.yahoo.com/quote/V` (Top Pick ก่อน)
   - ถ้า Top Pick เกิน zone → fetch ตัวถัดไปใน Watchlist เรียงตาม priority
   - **หยุดทันทีที่เจอตัวที่อยู่ใน zone** — ไม่ต้อง fetch ทุกตัว

3. **ตอบใน chat ทันที** (ไม่ save ไฟล์ ไม่อัปเดต showcase):
   ```
   💰 Top-up แนะนำ:

   🟢 [TICKER] — 100% (ซื้อได้เลย)
      ราคา $XXX | zone $XXX–$XXX ✅ | buffer เหลือ X%
      thesis: [ดึงจาก portfolio.md]
      ระวัง: [earnings ถ้ามี]

   — หรือถ้ามีหลายตัวในโซนพร้อมกัน —

   🟢 [TICKER A] — 60% | zone ✅ buffer X%
   🟢 [TICKER B] — 40% | zone ✅ buffer X%
   เหตุผลแบ่ง: [A moat แข็งกว่า / B buffer เยอะกว่า / ฯลฯ]

   ❌ ยังไม่เหมาะ: SYK $312 (เกิน zone $295 อยู่ 5.8%), V $323 (ในzone แต่ Recurring)
   ```

   **หลักการแบ่ง %:**
   - มีตัวเดียวในโซน → 100%
   - มีหลายตัว → ให้ % มากกว่ากับตัวที่ buffer เหลือมากกว่า (ถูกกว่าในโซน) หรือ moat กว้างกว่า

> **หลักการ:** ใช้ข้อมูลจาก daily-brief ล่าสุดที่รันไปแล้ว — ไม่ค้นซ้ำ fetch แค่ราคาปัจจุบัน 1-2 ตัว

---

## Step 1: Update Holdings + Kill Check + Earnings Calendar

> ข้าม Step 1, 2, 3 ทั้งหมด — วิเคราะห์เฉพาะ ticker ที่ระบุ

สำหรับแต่ละ ticker ใน argument:

**1. ดึงข้อมูล (dispatch augustus Mode B + C พร้อมกัน):**
- ราคาปัจจุบันจาก Yahoo Finance
- news 48 ชม. ล่าสุด
- analyst rating / target
- ถ้าเป็น ticker ใหม่ที่ไม่อยู่ใน portfolio.md → ดึง 10-K + moat analysis ด้วย (Mode B เต็ม)
- ถ้าอยู่ใน Holdings/Watchlist แล้ว → Mode C (news + price update)

**2. สรุปแต่ละตัว:**
```
[TICKER] — [ชื่อบริษัท]
ราคา: $XXX ([+X%] วันนี้)
Moat: [Wide/Narrow/None] | Sector: [X]
thesis สั้น: [2-3 ประโยค]
action: 🟢/🟡/🔴 [เหตุผล]
entry zone: $XXX หรือ "ยังไม่กำหนด"
```

**3. save:** `briefs/spot-<TICKERS>-<YYYY-MM-DD>.md`

**4. ถามว่าอยากเพิ่มเข้า Watchlist ไหม** — ถ้าใช่ → อัปเดต portfolio.md

---

## Step 1: Update Holdings + Kill Check + Earnings Calendar

### 1A: Update Holdings (ทำก่อนเสมอ)

dispatch augustus พร้อมกันทุกตัวใน Holdings (run_in_background: true)

หาข้อมูลแต่ละตัว:
- ราคาปัจจุบัน → P&L %
- news 24-48 ชม.
- analyst rating เปลี่ยนไหม
- thesis ยังใช้ได้ไหม → ✅ / ⚠️ / ❌

save `briefs/<TICKER>-update-<YYYY-MM-DD>.md`
อัปเดต showcase Holdings section

### 1B: Target & Kill Check (ทำทันทีหลัง update)

**Target Check ก่อน:**
อ่าน Target & Exit Plan จาก `portfolio.md` → เช็คราคาปัจจุบันกับ TP1 / TP2 ของแต่ละตัว

| สถานะ | ทำอะไร |
|-------|--------|
| ราคา ≥ TP1 | 🎯 **TP1 Alert** — ถึงเวลา trim 30% แล้ว |
| ราคา ≥ TP2 | 🎯🎯 **TP2 Alert** — thesis realized พิจารณาขายทั้งหมด |
| ใกล้ TP1 (ภายใน 5%) | ⚡ แจ้ง "ใกล้ TP1 อีก X% เท่านั้น" |

แสดงใน summary Step 6:
```
🎯 Target Status:
   SPCX $201 | TP1 $220 (ห่างอีก 9.0%) | TP2 $250
   SPGI $433 | TP1 $520 (ห่างอีก 20.1%) | TP2 $580
   ...
```

**Kill Condition Check ถัดไป:**

อ่าน Kill Conditions จาก `portfolio.md` → เช็คว่าเงื่อนไขใดถูก trigger ไหม

| สถานะ | ทำอะไร |
|-------|--------|
| ไม่มี kill condition ถูก trigger | ✅ ถือต่อ — ดำเนิน brief ปกติ |
| kill condition ถูก trigger บางส่วน | ⚠️ เพิ่ม alert ใน card พร้อมระบุว่า condition ไหนถูก trigger |
| kill condition หลักถูก trigger | 🚨 พิจารณาขาย — ระบุชัดใน card + แจ้งใน summary |

> kill condition ไม่ได้สั่งขายอัตโนมัติ — แค่ alert ให้รู้ว่าถึงเวลา re-evaluate

### 1C: Earnings Calendar (ทำพร้อมกับ 1A)

WebSearch สำหรับทุกตัวใน Holdings + Watchlist:
- `TICKER earnings date Q[X] 2026`
- เช็คว่ามีใครออก earnings **ใน 14 วันข้างหน้า** ไหม

**ถ้ามี → เพิ่ม Earnings Alert ใน card:**
```
📅 EARNINGS ALERT: รายงาน [วันที่] (~X วันข้างหน้า)
   ดูอะไร: [revenue guidance / EPS / margin / volume data]
   ถ้า beat → [คาดว่าจะเกิดอะไร]
   ถ้า miss → [kill condition เปิดใช้งานไหม]
```

**แจ้งใน summary Step 6 ด้วยเสมอ**

### 1D: Market Overview (ทำพร้อมกับ 1A — run_in_background: true)

WebSearch หาข้อมูลตลาดโดยรวมวันนี้:

**Indices:**
- `S&P 500 today performance` → ปิดที่เท่าไหร่ เปลี่ยน % เท่าไหร่
- `NASDAQ composite today` → tech sector เป็นยังไง
- `Dow Jones today` → blue chip sentiment

**Macro Signals:**
- `VIX index today` → ถ้า >20 = ตลาดกลัว / <15 = สงบ
- `10-year treasury yield today` → ถ้าขึ้นเร็ว = กดดัน growth stocks
- `USD index DXY today` → ถ้าแข็ง = กดดัน emerging + commodities

**Sector Performance:**
- `S&P 500 sector performance today` → sector ไหนนำ/ตาม
- เช็คเฉพาะ sector ที่ Holdings อยู่: Financials, Technology

**Key Macro Events (ถ้ามี):**
- `Fed meeting FOMC today 2026` → มีประชุมไหม / มีแถลงไหม
- `CPI PPI jobs report today 2026` → economic data release

**ประเมินสภาพตลาด:**
| สัญญาณ | ความหมายต่อพอร์ตเรา |
|--------|-------------------|
| ตลาดลง + VIX สูง | Holdings ลงเพราะ market risk ไม่ใช่ thesis พัง |
| Financials sector ร่วง | SPGI/CME/MA อาจลงตาม — เช็ค sector-specific news |
| Rate สูงขึ้นเร็ว | CME ได้ประโยชน์ (volume สูงขึ้น) |
| Rate ลด | MA/SPGI ได้ประโยชน์ (activity เพิ่ม) |

> 📝 Updated 2026-06-21: Holdings diverge จาก market Jun 18 (ตลาด +1.08% แต่ทุกตัวลง) — เพิ่ม divergence check
**Holdings Divergence Check (เพิ่มใหม่):**
ถ้า S&P วันนี้ขึ้น แต่ Holdings ของเรา **ทุกตัว** ลง → flag เป็น ⚠️ Stock-Specific Risk:
- ค้นหา news เฉพาะตัวทันที (CEO change / analyst downgrade / sector rotation)
- ระบุในสรุปว่า "Holdings diverge จากตลาด — ตรวจ stock-specific news แล้ว: [เหตุผล]"
- ห้ามสรุปว่า "market-wide" ถ้า S&P บวกแต่ Holdings ลบ

save `briefs/market-overview-<YYYY-MM-DD>.md`

---

## Step 2: หา Top Pick ทุกวัน (Fresh Search เสมอ)

> **หลักการใหม่:** ทุกวันทำ fresh search จริงๆ — ผลอาจเป็นตัวเดิมก็ได้ แต่ต้องผ่านกระบวนการทุกครั้ง ห้าม brief ซ้ำโดยไม่ re-evaluate

### ขั้นตอน (ห้ามข้าม):

**1. ดึง Top Pick เก่าจาก portfolio.md**
- ย้ายเข้า Watchlist อัตโนมัติทันที (ถ้ายังไม่อยู่ใน Watchlist)
- อัปเดต portfolio.md → ล้าง Top Pick เก่าออก

**2. รวม candidate pool**
- เริ่มจาก Watchlist ปัจจุบัน (SYK, COST, AMZN, LLY, SNPS, NVDA ฯลฯ)
- เพิ่มจาก Morningstar Wide Moat list: `WebSearch: morningstar wide moat focus index holdings 2026`
- Cross-check กับ Quality Fund 13F: Fundsmith / Polen / Akre ถืออะไรอยู่

**3. Hard Filter (ตัดออกถ้าไม่ผ่าน):**
- ❌ ไม่ใช่ US stock (NYSE/NASDAQ)
- ❌ Market cap < $2B
- ❌ Revenue ลด YoY
- ❌ D/E > 3x โดยไม่มีเหตุผล
- ❌ อยู่ใน Holdings แล้ว (ซื้อไปแล้ว = ไม่ใช่ Top Pick)

**4. Valuation check ด้วย GuruFocus**
- เลือกตัวที่ trading ใกล้หรือต่ำกว่า fair value มากที่สุด
- Tier S/A ก่อน → Tier B ถ้าไม่มีตัวดีกว่า

**5. เลือก 1 ตัวที่ดีที่สุดวันนี้**
- ถ้าผลออกมาเป็นตัวเดิม (เช่น SYK) = โอเค แต่ต้องระบุว่า "SYK ชนะการเปรียบเทียบวันนี้เพราะ [เหตุผล]"
- ถ้ามีตัวใหม่ดีกว่า = เปลี่ยน Top Pick

**5A. Repeated Top Pick Check (ทำก่อน 5B)**

นับว่า ticker นี้เป็น Top Pick ติดต่อกันกี่วันแล้ว (ดูจาก portfolio.md history):

| ติดต่อกัน | ทำอะไร |
|-----------|--------|
| 1–2 วัน | ปกติ — แสดงผลตามปกติ |
| 3–4 วัน | ⚠️ เพิ่ม note "Top Pick ซ้ำ X วัน — ยังไม่ซื้อเพราะรออะไร?" |
| **5+ วัน** | **→ Demote เข้า Watchlist อัตโนมัติ** ติด tag `⭐ Recurring` |
|  | → หา Top Pick ตัวใหม่จาก candidate pool แทน |
|  | → แจ้ง: "[TICKER] ถูก demote — เป็น Top Pick 5+ วันแต่ยังไม่ซื้อ ย้ายเข้า Watchlist (⭐ Recurring)" |

> **เหตุผล:** ถ้าตัวเดิมเป็น Top Pick หลายวันแต่ผู้ใช้ยังไม่ซื้อ = มีเหตุผลบางอย่าง ระบบควรหาตัวเลือกถัดไปให้ดู ส่วนตัวเดิมยังอยู่ใน Watchlist ไม่ได้หายไป

**5B. Entry Zone Check (ทำทันทีหลังเลือกได้)**
- ดูราคาปัจจุบัน vs entry zone ที่กำหนดไว้
- ถ้าราคา **เกิน entry zone** → ตัวนั้น **ไม่ใช่ Top Pick actionable**
  - ย้ายเข้า Watchlist พร้อม note "รอ pull back กลับสู่ [entry zone]"
  - อัปเดต portfolio.md → Top Pick = "ไม่มี (รอตัวที่ราคาเหมาะสม)"
  - ค้นหา candidate ตัวถัดไปจาก pool (กลับไปข้อ 4)
- ถ้าราคา **อยู่ใน entry zone หรือต่ำกว่า** → ดำเนินต่อปกติ

> **หลักการ:** Top Pick คือ "ซื้อได้เลยถ้าอยากเข้า" — ถ้าราคาเกิน zone ไปแล้ว มันคือ Watchlist ไม่ใช่ Top Pick

dispatch keen + North + augustus วิเคราะห์ตัวที่ชนะ
save `briefs/<TICKER>-<YYYY-MM-DD>.md`
อัปเดต `portfolio.md` → บันทึก Top Pick ใหม่

---

## Step 3: Update Watchlist

อ่าน Watchlist จาก `portfolio.md`

**สำหรับแต่ละตัวใน Watchlist:**
- ถ้ามีการขยับ ±3%+ หรือ news สำคัญ → augustus อัปเดตสั้นๆ
- ถ้าเงียบ → ข้ามไป ไม่ต้อง brief

**Auto-drop rule:**
- ถ้าตัวไหนเงียบมา 14 วันติด (ไม่มี news สำคัญ + ราคาไม่ขยับ) → ลบออกจาก Watchlist อัตโนมัติ
- แจ้งใน summary ว่า "ลบ TICKER ออก — เงียบ 14 วัน"

**Watchlist max 10 ตัว**
- Top Pick ทุกตัว (เก่าและใหม่) → อยู่ใน Watchlist เสมอ อัตโนมัติ
- ถ้า list เต็ม (10 ตัว) → ลบตัวที่เงียบนานที่สุดก่อน แล้วค่อยเพิ่ม

---

## Step 4: Bull vs Bear Debate (Gemini)

หลัง brief Top Pick เสร็จ → dispatch bear agent (run_in_background: true)
- bear อ่าน brief → เรียก Gemini API → หา bear case
- save `briefs/<TICKER>-bear-<YYYY-MM-DD>.md`
- save `briefs/<TICKER>-debate-<YYYY-MM-DD>.md`

> 📝 Updated 2026-06-21: Gemini API ไม่พร้อม 2 ครั้งติดกัน (GWRE + MDLZ) — เพิ่ม fallback rule
**Gemini API Fallback:**
- ถ้า Gemini unavailable → ใช้ Claude วิเคราะห์ bear case แทน
- บันทึกใน debate file ว่า `Bear: Claude (Gemini unavailable)` ชัดเจน
- ผล debate ที่ใช้ Claude แทน Gemini → ลด confidence: Bull ชนะ → Tier A (ไม่ใช่ S)

ถ้า Top Pick ซ้ำตัวเดิม → ข้ามขั้นตอนนี้ได้ (debate เดิมยังใช้ได้)

### ผล Debate → ตัดสินใจต่อ (สำคัญมาก)

| ผล | ทำอะไร |
|----|--------|
| Bull ชนะ | คง Top Pick ตัวเดิม — Tier S หรือ A |
| Tie | คง Top Pick ตัวเดิม แต่เพิ่ม ⚠️ warning ใน card |
| **Bear ชนะ** | **ยกเลิก Top Pick ตัวนี้ทันที → กลับไป Step 2B หาตัวใหม่** |

> **หลักการ:** ถ้า bear ชนะ = ตัวนั้นมีจุดอ่อนชัดเจน ไม่ควรแนะนำต่อ ต้องหาตัวที่ bull case แข็งแกร่งกว่า

---

## Step 5: อัปเดต showcase/index.html

Layout:
1. **🏆 Tier List** — ทุกตัวที่เคย brief (S/A/B/C)
2. **📌 Holdings** — SPGI, CME, MA + P&L
3. **🏆 Top Pick วันนี้** — 1 card เด่น พร้อม debate verdict
4. **👁 Watchlist** — เฉพาะตัวที่มีความเคลื่อนไหว
5. **📅 Scout Calendar** — brief เต็มเรียงตามวัน

**Card ทุกใบต้องมี ACTION VERDICT ที่บนสุดเสมอ — นี่คือสิ่งสำคัญที่สุด:**

```
🟢 เข้าได้เลย
   เหตุผล: [1-2 ประโยค ระบุว่าทำไมตอนนี้ถึงเหมาะ]
   เงื่อนไข: [ซื้อที่ราคาไหน หรือจำนวนเท่าไหร่]

🟡 รอก่อน
   รออะไร: [ระบุ catalyst หรือเงื่อนไขที่ต้องรอ เช่น "รอ earnings Q2", "รอราคาลงถึง $X"]
   ดูอีกครั้ง: [วันที่หรือ event ที่จะ re-evaluate]

🔴 หลีกเลี่ยง
   เหตุผล: [ระบุชัดว่าทำไม — valuation แพง / thesis พัง / leverage สูง]
```

Holdings ใช้:
```
✅ ถือต่อ — [เหตุผล 1 ประโยค]
⚠️ ระวัง — [สิ่งที่ต้องติดตาม]
🚨 พิจารณาขาย — [เหตุผล + kill condition ที่ถูก trigger]
```

**Card ทุกใบต้องมี section "🏢 บริษัทนี้ทำอะไร?" เสมอ:**
- เขียนเป็น "ภาษาคน" — อธิบายเหมือนคุยกับเพื่อนที่ไม่รู้เรื่องหุ้น
- ต้องตอบ 3 ข้อ: (1) ทำธุรกิจอะไร (2) เงินมาจากไหน (3) ทำไมคนเปลี่ยนไปใช้เจ้าอื่นได้ยาก
- ห้ามใช้ศัพท์เทคนิคโดยไม่อธิบาย
- ความยาว 3-4 บรรทัด อ่านจบใน 20 วินาที

**Tier List อัปเดต:**
- S = Bull ชนะ + moat แข็ง + valuation fair
- A = ดีแต่รอ หรือ valuation stretched
- B = มีข้อกังวล หรือ bear ชนะ
- C = ไม่ตรง style

---

## Step 6: สรุปใน chat

```
🌍 ตลาดวันนี้:
   S&P 500 [+X%] | NASDAQ [+X%] | Dow [+X%]
   VIX: XX (สงบ/ระวัง/กลัว) | 10Y Yield: X.XX%
   Financials sector: [+X%] | สภาพ: [1 ประโยค]

📌 Holdings:
   SPGI $XXX [+X%] | Kill $350.87 (buffer X%) | ✅/⚠️/🚨
   CME  $XXX [+X%] | Kill $246.51 (buffer X%) | ✅/⚠️/🚨
   MA   $XXX [+X%] | Kill $420.41 (buffer X%) | ✅/⚠️/🚨
   context: ลง/ขึ้นเพราะ [market-wide / sector / stock-specific]
   🚨 Kill Alert: [ถ้ามี]

🏆 Top Pick: TICKER (ซ้ำ / ใหม่)
   entry zone: $XXX–$XXX | ราคาปัจจุบัน: $XXX [อยู่ใน zone ✅ / เกิน zone ⚠️]
   thesis: [เหตุผล 1 ประโยค]
   debate: Bull ชนะ / Bear ชนะ / Tie

📊 Zone Summary (ทุกตัว):
   Ticker | ราคา | Entry Zone | Kill Zone | สถานะ
   SPGI   | $XXX | ถือแล้ว   | $350.87   | ✅/⚠️
   CME    | $XXX | ถือแล้ว   | $246.51   | ✅/⚠️
   MA     | $XXX | ถือแล้ว   | $420.41   | ✅/⚠️
   V      | $XXX | $310-330  | —         | 🟡/🟢
   SYK    | $XXX | <$295     | —         | 🟡/🟢
   LLY    | $XXX | รอ pullback| —        | 🟡
   SNPS   | $XXX | รอ Q3     | —         | 🟡
   COST   | $XXX | ยังไม่กำหนด| —        | 🟡

📅 Earnings ใน 14 วัน:
   [TICKER] — [วันที่] (~X วัน) | ดูอะไร: [ประเด็นหลัก]
   (ถ้าไม่มี → "ไม่มี earnings ใน 14 วันข้างหน้า")

👁 Watchlist: X ตัว (Y ตัวมีการขยับ, Z ตัวถูก drop)

🌐 Showcase: อัปเดตแล้ว
```

---

## Rules

- ห้ามแต่งข้อมูล ถ้าไม่พบให้บอกตรงๆ
- augustus ห้ามทำนายตลาด รายงานเฉพาะ observable signals
- brief ซ้ำได้ถ้าตัวเดิมยังดี ไม่ต้องหาใหม่เพื่อความแปลกใหม่
- save ทุกอย่างลงไฟล์เสมอ ไม่ทิ้งไว้แค่ใน chat
