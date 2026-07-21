---
name: brief
description: วิเคราะห์หุ้นรายตัว — 4 Layer + Bull/Bear + บันทึก showcase และ briefs/
---

# /brief [TICKER ...] — Company Brief

## 🎯 Investment Style: Aggressive Growth — Target 100%/ปี

พอร์ตนี้เปลี่ยนจาก quality-compounder แบบกระจายเป็น **aggressive growth แบบ concentrate** (2026-07-14) — เป้าหมายผลตอบแทน 100%/ปี ไม่ใช่ 15-20%/ปีแบบเดิม
- **Growth bar สูงขึ้น:** เกณฑ์ revenue growth ใน Layer 2 ยกจาก ≥15% → **≥30% YoY หรือ accelerating**
- **Concentration:** โน้มเอียงไปทาง position ใหญ่ในตัวที่ conviction สูงสุด แทนกระจายเท่าๆ กันหลายตัว — ตัวที่ growth ช้ากว่า (defensive/quality แบบเดิม) ควร flag ว่าอาจไม่ match style ใหม่แล้ว แม้ thesis จะยังไม่พัง
- **Kill zone คงเดิมที่ -15%** จากราคาซื้อ — ไม่ขยายแม้หุ้น growth จะผันผวนกว่า (risk control ยังเข้มเท่าเดิม)
- Time horizon สั้นลง — re-evaluate ทุกไตรมาส ไม่รอ 2-5 ปีแบบเดิม

## Input
```
/brief AAPL              ← ตัวเดียว
/brief NVDA PLTR SYK     ← หลายตัวพร้อมกัน
```

---

## Multi-Ticker Mode (2+ tickers)

ถ้า arguments มีมากกว่า 1 ticker:

1. **spawn agent แยกต่อ 1 ticker พร้อมกันทุกตัว** (parallel) — อย่ารอทีละตัว
2. แต่ละ agent ทำ Step 1–4 (ดึงข้อมูล + วิเคราะห์) ของตัวเอง
3. รอทุก agent เสร็จ แล้วรวม output ใน chat ต่อกัน
4. Save ทุก brief file + inject ทุก card เข้า showcase พร้อมกัน
5. **commit ครั้งเดียว** รวมทุก ticker

```
git commit -m "brief [TICKER1] [TICKER2] ... [DATE]: [สรุปสั้น]"
```

---

## Pre-flight

```
☐ อ่าน portfolio.md — เช็คว่า TICKER อยู่ใน Holdings หรือ Watchlist
☐ ห้ามแต่งข้อมูล — ถ้าหาไม่ได้เขียน "ไม่พบข้อมูล"
```

---

## ⚠️ สถานะข้อมูล — 4 แบบ (ห้ามใช้ ❌ พร่ำเพรื่อ)

ทุกข้อใน Layer 1 และ Layer 2 ต้องให้สถานะ 1 ใน 4 แบบนี้เท่านั้น — **ห้ามใช้ ❌ แทน "หาไม่เจอ"**

| สัญลักษณ์ | ความหมาย | เมื่อไหร่ใช้ |
|---|---|---|
| ✅ | ผ่าน (Confirmed Pass) | มีข้อมูลยืนยันชัดเจนว่าเข้าเกณฑ์ |
| ❌ | ไม่ผ่าน (Confirmed Fail) | มีข้อมูลยืนยันชัดเจนว่า**ไม่**เข้าเกณฑ์ — ต้องมีตัวเลข/หลักฐานอ้างอิงเสมอ |
| ⚠️ | Data Conflict | หาข้อมูลมาได้ แต่แหล่งขัดแย้งกันเอง (เช่น ราคาจาก 2 แหล่งไม่ตรงกัน, ADR ratio ไม่ชัด) |
| ⚪ | Unknown | ค้นแล้วแต่หาไม่เจอเลย ไม่มีข้อมูลจะยืนยันหรือปฏิเสธ |

**ทำไมต้องแยก:** "หาไม่เจอ" กับ "รู้ว่าไม่ผ่าน" คือคนละเรื่องกัน ระบบเดิมที่บังคับ ✅/❌ แบบ binary ทำให้ default ไปทาง ❌ เวลาไม่มีข้อมูล ซึ่งเอนเอียงไปทาง Avoid โดยไม่มีหลักฐานจริงรองรับ — ไม่เป็นมืออาชีพ

### ⚠️ ห้ามสรุป ⚪ Unknown จาก WebSearch แค่รอบเดียว

**เจอเคสจริง (MU brief):** ค้นด้วย query กว้าง "Micron Morningstar fair value moat rating" → สรุปผิดว่า "ไม่พบ/อยู่หลัง paywall" ทั้งที่ข้อมูลมีอยู่จริงในบทความฟรี — พอค้นซ้ำด้วย query เจาะจง "Micron Morningstar 'No Moat' fair value" กลับเจอทันที

**สาเหตุ:** (1) query กว้างเกินไปมักโดนหน้า paywall แทนบทความข่าวฟรีที่มีคำตอบฝังอยู่ (2) AI ที่สรุปผล WebSearch พลาดข้อมูลที่ฝังอยู่ในประโยคแบบ adjective (เช่น "no-moat Micron") ไม่ใช่ field ชัดๆ

**กฎบังคับ:** สำหรับข้อมูลสำคัญที่จะกลายเป็น Layer 1/Layer 3 (**Moat rating, Fair Value**) — ถ้า WebSearch รอบแรกบอกว่า "ไม่พบ" หรือ "อยู่หลัง paywall" **ห้ามสรุปเป็น ⚪ Unknown ทันที** ต้องค้นซ้ำอย่างน้อย 1 ครั้งด้วย query ที่เจาะจงกว่าเดิมก่อนเสมอ เช่น:
- รอบแรก (กว้าง): `"[TICKER] Morningstar fair value moat rating"`
- รอบสอง (เจาะจง) ถ้ารอบแรกไม่เจอ: `"[TICKER] Morningstar 'No Moat' OR 'Wide Moat' OR 'Narrow Moat' fair value"` หรือ `"[TICKER] Morningstar economic moat rating [ปีปัจจุบัน]"`

ถ้าค้นซ้ำแล้วยังไม่เจอจริงๆ ถึงจะสรุป ⚪ Unknown ได้

---

## ขั้นตอน (ต่อ 1 ticker)

### 1. ดึงข้อมูล (WebSearch พร้อมกัน)

**ราคา — ใช้ Bash curl ไม่ใช่ WebSearch:** (WebFetch tool โดน Yahoo block บ่อย แต่ curl ตรงจาก Bash ใช้ได้ปกติ)
```bash
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://query1.finance.yahoo.com/v8/finance/chart/[TICKER]?interval=1d&range=1d"
```
Parse `meta.regularMarketPrice` — ถ้า curl fail ค่อย fallback ไป WebSearch (ราคาอาจ lag)

```
☐ ราคาปัจจุบัน + % change
☐ Revenue, EPS, FCF margin (2 ปีล่าสุด)
☐ Net Debt/EBITDA + Interest coverage
☐ Morningstar Fair Value + Moat Rating หรือ GuruFocus GF Value — ค้นซ้ำด้วย query เจาะจงถ้ารอบแรกไม่เจอ (ดูกฎด้านบน)
☐ ข่าว/catalyst สำคัญ 30 วันล่าสุด
☐ Short interest + insider activity (ถ้ามี) — ดูกฎ materiality filter ด้านล่างก่อนนำไปใช้ใน Bear Case
☐ Guru Holdings — เช็คว่ามีกองทุน quality-investing ชื่อดังถืออยู่ไหม (Fundsmith, Berkshire/Buffett, Terry Smith, Nomad, Baillie Gifford ฯลฯ) + สัดส่วนในพอร์ตเขา + เพิ่ม/ลดสถานะล่าสุด — ใช้ query เช่น `"[TICKER] Fundsmith holding"`, `"[TICKER] 13F Berkshire"`, `"[TICKER] guru stock picks"`
☐ YouTube Digest (ลงทุน Diary) — grep `youtube-digests/longtoon-diary.md` หา TICKER/ชื่อบริษัท ถ้าเจอ entry ที่เกี่ยวข้อง ใส่เป็นข้อมูลประกอบใน Bull/Bear (ระบุว่ามาจาก YouTube digest ไม่ใช่ primary source) ถ้าไม่เจอ ข้ามเงียบๆ ไม่ต้องเขียนว่า "ไม่พบ"
```

**กฎการใช้ YouTube Digest:** เป็น**ข้อมูลประกอบเท่านั้น** ห้ามใช้เป็นหลักฐานเดี่ยวเพื่อให้ ✅/❌ ใน Layer 1/2 หรือเป็นเหตุผลหลักใน Layer 4 Action — ใช้ได้แค่เสริมน้ำหนัก Bull/Bear case ที่มีเหตุผลเชิงธุรกิจ/ตัวเลขรองรับอยู่แล้ว

**วิธีใช้ Guru Holdings ใน Layer 2:** ถ้าพบว่ากองทุน quality-investing ชื่อดังถือ/เพิ่มสถานะ → เป็นหลักฐานสนับสนุนข้อ 4 (Competitive advantage ยั่งยืน) หรือข้อ 1 (โตได้ 5-10 ปี) ได้ — แต่ **ไม่ใช่เหตุผลเดี่ยวพอจะให้ ✅** ต้องมีเหตุผลเชิงธุรกิจประกอบด้วยเสมอ ถ้าหาไม่เจอเลย → ⚪ Unknown (ไม่ใช่ ❌)

### ⚠️ Insider Selling — ต้องผ่าน materiality filter ก่อนนับเป็น Bear Case

Insider selling มีหลายแบบ ไม่ใช่ทุกแบบคือสัญญาณลบ: 10b5-1 plan (ตั้งเวลาล่วงหน้าตามกฎหมาย), tax payment, diversification ส่วนตัว, emergency liquidity — เหล่านี้เป็นเรื่องปกติและไม่ควรให้น้ำหนักเท่ากับการขายที่ผิดปกติ

**ให้น้ำหนักสูง (นับเป็น Bear Case point) เฉพาะเมื่อเข้าเงื่อนไขครบทั้ง 3 ข้อ:**
1. ผู้บริหารระดับสูงหลายคน (เช่น CEO + CFO) ขายพร้อมกันในช่วงเวลาใกล้กัน
2. สัดส่วนที่ขายมากเมื่อเทียบกับสัดส่วนถือครองเดิม (ไม่ใช่แค่มูลค่า absolute สูงเพราะราคาหุ้นแพง)
3. ไม่มีคำอธิบายที่ชัดเจนว่าเป็น routine 10b5-1 / tax / diversification ที่ตั้งไว้ล่วงหน้า

**ถ้าไม่ครบ 3 ข้อ** (เช่น เป็นแค่ 10b5-1 plan ปกติของคนเดียว) → ใส่ไว้เป็นข้อมูลประกอบใน Management (Layer 1) แบบ factual เฉยๆ **ห้ามยกเป็น Bear Case หลัก**

---

### 2. วิเคราะห์ 4 Layer

**Layer 1: Quality Filter** — หยุดทันทีเฉพาะเมื่อมีข้อที่เป็น **❌ (Confirmed Fail)** อย่างน้อย 1 ข้อ
ถ้ามีแต่ ⚠️/⚪ (ไม่มี ❌ เลย) → **ผ่านต่อไป Layer 2 ได้** แต่ต้องติด flag "ข้อมูลไม่ครบ" ไว้ในสรุปด้วย

```
☐ Wide Moat — ใช้กรอบ "7 Powers" (Hamilton Helmer) ระบุว่าเข้าข้อไหนบ้าง ห้ามตอบกว้างๆ แค่ Wide/Narrow/No Moat:
    1. Scale Economies — ต้นทุนต่อหน่วยลดลงเมื่อใหญ่ขึ้น คู่แข่งเล็กสู้ไม่ได้
    2. Network Economies — มูลค่าเพิ่มขึ้นเมื่อผู้ใช้เพิ่มขึ้น (เช่น payment network, marketplace)
    3. Counter-Positioning — โมเดลธุรกิจใหม่ที่ incumbent เลียนแบบไม่ได้เพราะจะทำร้ายธุรกิจเดิมตัวเอง
    4. Switching Costs — ต้นทุน/เวลาย้ายออกสูง (เช่น implementation หลายปี, data lock-in)
    5. Branding — แบรนด์ทำให้ตั้งราคาสูงกว่า/ขายง่ายกว่าคู่แข่งที่คุณภาพเท่ากัน
    6. Cornered Resource — ครอบครอง asset/IP/license ที่คนอื่นเข้าถึงไม่ได้
    7. Process Power — กระบวนการภายในที่สั่งสมมานาน คู่แข่งลอกไม่ได้แม้รู้วิธี
   ระบุ 1-2 ข้อที่เข้าเกณฑ์ชัดเจนที่สุดพร้อมหลักฐาน — ถ้าไม่เข้าข้อไหนเลย = No Moat (❌ ถ้าเป็น commodity/cyclical business ชัดเจน)
☐ Management ดี — capital allocation + ไม่ dilute เกิน
☐ Balance Sheet แข็ง — Net Debt/EBITDA < 3x
☐ FCF margin >10% หรือ trend ขาขึ้น
☐ Interest coverage > 5x
```

**Layer 2: Compounder Filter** — นับคะแนนจาก ✅ เท่านั้น (ต้อง ≥4/5 ถึงผ่าน), ❌ นับเป็นลบ, ส่วน ⚠️/⚪ **ไม่นับทั้งสองฝั่ง** แต่ต้องแสดงในผลลัพธ์เสมอ

```
1. โตได้อีก 5–10 ปีไหม?
2. TAM ใหญ่กว่า market cap ≥5x ไหม?
3. Revenue growth ≥30% YoY หรือ accelerating? (ยกจาก ≥15% เดิม — ตาม aggressive growth style เป้า 100%/ปี)
4. Competitive advantage ยั่งยืนอีก 10 ปี?
5. บริษัทนี้มีโอกาสเป็นผู้นำอุตสาหกรรมต่อเนื่องอีก 10 ปีหรือไม่? (ตอบจาก market share trend, R&D moat, competitive positioning — ไม่ใช่การคาดเดา)
```

**ข้อยกเว้น TAM (Dominant Incumbent Exception) — 2026-07-19:** กฎ "TAM ≥5x" ออกแบบมาเช็คว่าหุ้น**โตเร็ว**ยังมีที่วิ่งอีกไหม แต่ใช้ผิดกับบริษัทที่ผูกขาดตลาดตัวเองอยู่แล้ว (เช่น TSM, ASML) เพราะ market cap ตัวเองก็ใหญ่จนหา TAM ที่ใหญ่กว่า 5 เท่าแทบเป็นไปไม่ได้ ทั้งที่ธุรกิจคุณภาพดีมาก

ถ้าเข้าเงื่อนไข**ครบทั้ง 3 ข้อ**นี้ → ข้อ 2 (TAM) ให้เป็น **⚠️ แทน ❌** (ไม่นับเป็นลบ แต่ต้องแสดงเหตุผลเสมอว่าเข้าเกณฑ์ exception):
1. Layer 1 Wide Moat ✅ มาจาก **Cornered Resource, Process Power, หรือ Scale Economies** (ไม่ใช่ Branding/Switching Cost เพียงอย่างเดียว — เพราะ exception นี้เจาะจงบริษัทที่ผูกขาด supply-side ไม่ใช่แค่ lock-in ลูกค้า)
2. Market share ในตลาดหลัก ≥40-50% (มีตัวเลข/หลักฐานยืนยัน ไม่ใช่กะเอา)
3. ROIC สูงต่อเนื่องหลายปี หรือ FCF margin >25% (หลักฐานว่า pricing power จริง ไม่ใช่แค่ market cap ใหญ่)

ถ้าไม่ครบ 3 ข้อ → ใช้กฎเดิม (TAM ไม่ถึง 5x = ❌ ตามปกติ)

**กฎ caveat:** ถ้ามีข้อที่เป็น ⚠️ หรือ ⚪ รวมกัน ≥2 ข้อ จาก 5 ข้อ → Layer 4 Action **ห้ามฟันธงมั่นใจเต็มร้อย** ต้องเขียนกำกับว่า "Provisional — ข้อมูลไม่ครบ X ข้อ" และแนะนำว่าต้องหาข้อมูลอะไรเพิ่มถึงจะฟันธงได้ชัดกว่านี้

**Layer 3: Valuation**

```
🟢 Cheap     — ต่ำกว่า fair value ≥20%
🟡 Fair      — ±20% ของ fair value
🔴 Expensive — เกิน fair value >20%
```

**⚠️ ถ้าแหล่ง Fair Value ขัดแย้งกันมาก (เช่น GuruFocus vs Simply Wall St vs analyst consensus ต่างกัน >30-40%)** — **ห้าม**เลือกตัวเลขจากแหล่งเดียวมาฟันธงเป็น Cheap/Fair/Expensive แบบมั่นใจ ให้สรุปเป็น:

```
⚠️ Valuation Inconclusive — แหล่งขัดแย้งกัน ($X จาก [แหล่ง A] vs $Y จาก [แหล่ง B])
```

และให้ Layer 4 Action โน้มเอียงไปทาง Provisional/Watch แทนการฟันธง Buy หรือ Avoid ด้วยเหตุผลด้าน valuation เพียงอย่างเดียว (ยังใช้เหตุผลจาก Layer 1/2 ฟันธงได้ตามปกติ)

**Layer 4: Action**

```
🟢 Buy              — Cheap + ≥4/5 confirmed + thesis แข็ง
🔵 Starter Position — Fair + ≥4/5 confirmed + catalyst ชัด
🟠 Watch            — ดีแต่ราคา Expensive หรือรอ catalyst
🔴 Avoid            — มีข้อ ❌ confirmed ใน Layer 1 หรือ <4/5 confirmed ใน Layer 2
```

**ถ้ามี ⚠️/⚪ รวม ≥2 ข้อ** (จาก Layer 1+2 ทั้งหมด) → เติม "(Provisional)" ต่อท้าย Action เสมอ ไม่ว่าผลจะออกมาเป็นอะไร — สื่อว่ายังฟันธงได้ไม่เต็มที่เพราะข้อมูลไม่ครบ

---

### 2.5 Independent Second Opinion — เฉพาะเมื่อ Action = Buy หรือ Starter

**เหตุผล:** ก่อนจะเอาเงินจริงเข้าไปตาม /brief เดียวของ Claude ควรมีมุมมองอิสระเช็คไขว้ก่อน กันจุดบอด/bias — ถ้า Action = Watch/Avoid ไม่ต้องทำขั้นนี้ (ไม่คุ้มเวลา)

**หมายเหตุ 2026-07-14:** เดิมออกแบบให้ยิง OpenAI/Gemini API ตรง แต่ทั้ง 2 key ใน `.env` ไม่มี quota ใช้งาน (billing ไม่ได้เปิด) ผู้ใช้ให้ใช้ Claude ล้วนๆ ทั้งระบบแทน — และ agent `bear` (`.claude/agents/bear.md`) ทำหน้าที่ตรงนี้อยู่แล้ว (devil's advocate, Claude-only) เลย**ใช้ agent เดิมแทนที่จะสร้าง logic ซ้ำ**

**วิธี:** agent `bear` ต้องอ่านไฟล์ `briefs/[TICKER]-[DATE].md` ก่อนถึงจะทำงานได้ — ดังนั้นให้ **save brief file (ตาม step 6 format) ไปก่อนตั้งแต่ตรงนี้เลย** (ยังไม่ต้อง update showcase/portfolio.md ก็ได้ รอทำพร้อมกันตอนท้าย) แล้วเรียก agent `bear` ผ่าน Agent tool (`subagent_type: bear`) ให้อ่านไฟล์ที่เพิ่ง save แล้วทำ bear case + debate ตามหน้าที่ของมัน (จะ save ไฟล์ `briefs/[TICKER]-bear-[DATE].md` และ `briefs/[TICKER]-debate-[DATE].md` เพิ่มเอง) — รันแบบ synchronous (`run_in_background: false`) เพราะต้องรอผล verdict มาใส่ใน output ของ step 4 ต่อ

### 2.5b Quality Gate — เฉพาะเมื่อ Action = Buy หรือ Starter (2026-07-20)

**เหตุผล:** ก่อนเงินจริงจะเข้า ควรมีคนเช็คว่าตัวเลข/สถานะ ✅❌⚠️⚪ ที่เขียนไว้ถูกต้อง สอดคล้องกันเอง และตรงตามกฎของ skill นี้จริงไหม — เป็นคนละมุมกับ `bear` (ที่เช็ค investment thesis) Quality Gate เช็คแค่ความถูกต้องเชิงข้อเท็จจริง/ตรรกะ

**วิธี:** หลังบันทึก brief file แล้ว (ไม่ต้องรอ bear เสร็จก่อน — รันพร้อมกันได้) เรียก agent `vera` ผ่าน Agent tool (`subagent_type: vera`) ให้อ่านไฟล์ `briefs/[TICKER]-[DATE].md` แล้วตรวจสอบตาม 5 หมวดของมัน (Math, สถานะ ✅❌⚠️⚪, Layer 2 scoring, Action ตรงกฎไหม, Insider selling/YouTube digest ใช้ถูกกฎไหม) — รันแบบ synchronous เพราะถ้าเจอปัญหาต้องแก้ก่อนส่ง output จริง

**ถ้า Vera เจอปัญหา 🔴 สูง** → แก้ไฟล์ brief ให้ถูกก่อน แล้วค่อยไปต่อ step ถัดไป (อย่าปล่อยผ่าน)
**ถ้าเจอแค่ 🟡/⚪** → แก้ถ้าทำได้ง่าย ถ้าไม่กระทบ Action/ตัวเลขหลัก ข้ามไปได้แต่ควรบันทึกไว้
**ถ้า PASS** → ไปต่อได้เลย ไม่ต้องพูดถึงใน output

**นำผลไปใส่ใน Output** เป็น section ใหม่ `🔍 Second Opinion (Bear/Devil's Advocate)` — สรุป verdict จาก debate file สั้นๆ (Bull ชนะ/Bear ชนะ/Tie) — ถ้า Bear ชนะหรือ Tie → เติม "(⚠️ Second opinion flagged)" ต่อท้าย Layer 4 Action ด้วย ไม่ต้องเปลี่ยน Action เอง แค่ flag ให้ user เห็นก่อนตัดสินใจ

### 2.6 Concentration Risk Check — เฉพาะเมื่อ Action = Buy หรือ Starter และ TICKER อยู่ใน Holdings อยู่แล้ว (size-up)

พอร์ตนี้ใช้ style **concentrate ในตัว conviction สูงสุด** (ดู portfolio.md Investment Style) — concentrate ได้ แต่ต้องรู้ตัวว่ากระจุกแค่ไหน:

1. อ่านมูลค่ารวมพอร์ต + มูลค่าปัจจุบันของ TICKER นี้จาก portfolio.md Holdings table
2. คำนวณ % ของพอร์ตที่ TICKER นี้จะกลายเป็นถ้า buy ตามคำแนะนำ (คร่าวๆ พอ ไม่ต้องเป๊ะ)
3. ถ้าจะทำให้ตัวเดียวเกิน **40% ของพอร์ตรวม** → เติมคำเตือนสั้นๆ ต่อท้าย Action: "⚠️ Concentration สูง — จะเป็น ~X% ของพอร์ต" (ไม่ใช่ Avoid อัตโนมัติ แค่เตือนให้รู้ตัว เพราะ style นี้ยอมรับ concentration สูงอยู่แล้ว)
4. ถ้าต่ำกว่า 40% → ไม่ต้องพูดถึงเรื่องนี้เลย (ไม่ต้องเขียนว่า "concentration ok" ให้ยืดเยื้อ)

---

### 3. Bull/Bear Case

**Bull Case** — เหตุผล 3 ข้อที่ทำให้ราคาขึ้น 50–100% ใน 3–5 ปี
**Bear Case** — เหตุผล 3 ข้อที่ทำให้ thesis พังหรือราคาร่วงหนัก

จบด้วย: **"❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1 — 1 ประโยค]"**

---

### 4. Output ใน Chat

```
📋 [TICKER] — [ชื่อบริษัท]  [วันที่]
[sector tag] | [moat type]

💰 ราคา: $XXX [+X%] | Fair Value: $XXX | [🟢 Cheap / 🟡 Fair / 🔴 Expensive]
👤 Guru Holdings: [รายชื่อกองทุน + สัดส่วน หรือ "ไม่พบข้อมูล"]

━━ Layer 1: Quality ━━
Wide Moat    ✅/❌/⚠️/⚪ — [7 Powers ข้อที่เข้า เช่น "Switching Costs + Scale Economies" + เหตุผล + แหล่งอ้างอิงถ้า ❌]
Management   ✅/❌/⚠️/⚪ — [เหตุผล]
Balance Sheet✅/❌/⚠️/⚪ — Net Debt/EBITDA [X.Xx หรือ "ไม่พบข้อมูล"]
FCF          ✅/❌/⚠️/⚪ — [margin หรือ trend หรือ "ไม่พบข้อมูล"]
Debt         ✅/❌/⚠️/⚪ — Interest coverage [Xx หรือ "ไม่พบข้อมูล"]
→ ผล: ✅ ผ่าน / ❌ หยุด (ระบุข้อที่ ❌ จริง) — ถ้ามีแต่ ⚠️/⚪ ให้เขียน "ผ่านแบบมีข้อมูลไม่ครบ"

━━ Layer 2: Compounder (X/5 confirmed, Y ⚠️/⚪) ━━
1. โตได้ 5–10 ปี?    ✅/❌/⚠️/⚪ — [เหตุผล]
2. TAM ≥5x mkt cap?  ✅/❌/⚠️/⚪ — [ตัวเลข หรือ "ไม่พบข้อมูล"]
3. Growth ≥15%?      ✅/❌/⚠️/⚪ — [ตัวเลข]
4. Moat ยั่งยืน?     ✅/❌/⚠️/⚪ — [เหตุผล]
5. เสียดายไม่ซื้อ?   ✅/❌/⚠️/⚪ — [เหตุผล]

━━ Layer 3: Valuation ━━
Fair Value: $XXX (แหล่ง: Morningstar/GuruFocus)
ส่วนต่าง: [−X% Cheap / +X% Expensive]

━━ Layer 4: Action ━━
[🟢 Buy / 🔵 Starter / 🟠 Watch / 🔴 Avoid] [+ "(Provisional — ข้อมูลไม่ครบ)" ถ้ามี ⚠️/⚪ ≥2 ข้อ] [+ "(⚠️ Second opinion flagged)" ถ้า agent อิสระไม่เห็นด้วย]
[เหตุผล ≤2 บรรทัด — ถ้า Provisional ระบุด้วยว่าต้องหาข้อมูลอะไรเพิ่มถึงจะฟันธงชัดกว่านี้]

━━ 🔍 Second Opinion (Bear/Devil's Advocate) ━━ (เฉพาะ Buy/Starter)
[verdict จาก agent bear สั้นๆ — Bull ชนะ/Bear ชนะ/Tie + เหตุผล 1 ประโยค + ความเสี่ยงอันดับ 1 ที่ bear เจอ]

━━ Bull / Bear ━━
🐂 Bull: [ข้อ 1] / [ข้อ 2] / [ข้อ 3]
🐻 Bear: [ข้อ 1] / [ข้อ 2] / [ข้อ 3]

❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1]
🚨 ขายถ้า: [observable event — 1 ประโยค]
```

---

### 5. Auto-Watchlist

**ถ้า Action = Buy / Starter / Watch → เพิ่มเข้า portfolio.md Watchlist อัตโนมัติ**
**ถ้า Action = Avoid → ไม่เพิ่ม**

ตรวจก่อน:
- ถ้า TICKER **ไม่มีใน Watchlist** → append row ใหม่
- ถ้า TICKER **มีอยู่แล้ว** → update row เดิม (ราคา + เหตุผล)
- ถ้า TICKER **อยู่ใน Holdings แล้ว** → ข้าม (ไม่ต้อง add watchlist)

Format row:
```
| **[TICKER]** | [moat type] — [thesis killer สั้น] — /brief [DATE] | [entry zone จาก valuation] | **$[price]** ([DATE]) |
```

ตัวอย่าง:
```
| **NVDA** | Narrow Moat AI compute — /brief Jun 26 | รอ $182–190 | **$211** (Jun 26) — เกิน zone |
```

---

### 6. Save ไฟล์

**บันทึก** `briefs/[TICKER]-[YYYY-MM-DD].md` — ใช้ output format เดิม

**อัปเดต showcase/briefs.html** (ไม่ใช่ index.html — index.html ถูกตัด scope ไปแล้ว 2026-07-17 เหลือแค่ Header→Summary→Holdings ห้ามเพิ่ม brief card กลับเข้าไป — ดู `feedback-showcase-scope-trimmed` memory)

briefs.html คือ archive แยกตามวันจริง (section ต่อวัน ใหม่สุดอยู่บนสุด ใต้ `<div class="container">`):

หากมี section `<!-- [DATE] -->` ของวันนี้อยู่แล้ว → เพิ่ม card เข้าไปใน `.cards-grid` นั้น
หากยังไม่มี → สร้าง section ใหม่ต่อจาก `<div class="container">` (บนสุด ก่อน section ของวันก่อนหน้า):

```html
<!-- [YYYY-MM-DD] -->
<div class="section">
  <div class="day-section-header">
    <div class="day-label">[YYYY-MM-DD]</div>
    <div class="day-note">[บริบทสั้นๆ ว่าทำไมสแกน/บรีฟตัวนี้]</div>
  </div>
  <div class="cards-grid">

    <div class="card">
      <div class="card-header">
        <div><div class="ticker">[TICKER]</div><div class="company-name">[ชื่อบริษัท]</div></div>
        <span class="badge badge-[avoid/watch/starter/buy]">[Avoid/Watch/Starter/Buy]</span>
      </div>
      <div class="sector-tag">[sector] — [moat type]</div>
      <div class="price-line">$[XXX] [+X%] | FV [...] — [🟢/🟡/🔴/⚠️ Inconclusive]</div>
      <div class="action-box action-[avoid/watch/starter/buy]">
        [สรุป Layer 1 + Layer 2 ผลลัพธ์ + เหตุผลหลัก ≤2-3 บรรทัด]
      </div>
      <div class="wrong-line"><strong>❓ ผิดได้ถ้า:</strong> [เหตุผลอันดับ 1]</div>
    </div>

  </div>
</div>

<hr class="divider">
```

**badge/action class mapping:** Buy → `badge-buy`/`action-buy`, Starter → `badge-starter`/`action-starter`, Watch → `badge-watch`/`action-watch`, Avoid → `badge-avoid`/`action-avoid`

ถ้า TICKER อยู่ใน **Holdings** อยู่แล้ว (ไม่ใช่ scout ใหม่) → เพิ่ม `<div class="hold-flag">⚠️ นี่คือ HOLDING ปัจจุบัน — ผลนี้คือสัญญาณให้พิจารณาขาย</div>` ก่อน action-box ถ้า Action = Avoid

### 6.5 Knowledge Base Atomize (2026-07-20) — เฉพาะเมื่อ TICKER อยู่ใน Holdings/Watchlist และ thesis เปลี่ยนจากครั้งก่อน

**เมื่อไหร่เรียก:** ถ้า TICKER นี้เคยมี `knowledge/[TICKER].md` อยู่แล้ว (คืออยู่ใน Holdings) และผล `/brief` รอบนี้ทำให้ Action หรือ Layer 1/2 status เปลี่ยนจากที่บันทึกไว้ล่าสุด — เรียก agent `indy` (`subagent_type: indy`) ให้อ่าน brief ที่เพิ่ง save แล้วเขียน atom entry ใหม่เข้า `knowledge/[TICKER].md` + sync `knowledge/INDEX.md` (รันแบบ background ได้ ไม่ต้องรอผล เพราะไม่กระทบ output หลักของ brief)

**ถ้าเป็น ticker ใหม่ที่เพิ่งเข้า Watchlist ครั้งแรก** (ไม่เคยมี `knowledge/[TICKER].md` มาก่อน) → ไม่ต้องเรียก indy ยังไม่จำเป็นต้องมี Knowledge Base แยกจนกว่าจะกลายเป็น Holdings จริง (Watchlist entry ใน portfolio.md เพียงพอแล้ว)

จากนั้น push:
```bash
git add briefs/ showcase/briefs.html portfolio.md knowledge/
git commit -m "brief [TICKER] [DATE]: [action] | [valuation] | [thesis killer สั้น]"
git push origin main
```

---

## กฎ

- **ห้ามใช้ ❌ แทน "หาข้อมูลไม่เจอ" เด็ดขาด** — ❌ ต้องมีหลักฐาน/ตัวเลขยืนยันเสมอว่าไม่ผ่านเกณฑ์จริง ถ้าแค่หาไม่เจอ → ⚪ Unknown ถ้าแหล่งขัดแย้งกัน → ⚠️ Data Conflict
- Layer 1 หยุดทันทีเฉพาะเมื่อมี ❌ confirmed อย่างน้อย 1 ข้อ (ไม่ใช่ ⚠️/⚪)
- Layer 2 นับคะแนนจาก ✅ เท่านั้น — ⚠️/⚪ ไม่นับทั้งขึ้นทั้งลง แต่ต้องแสดงในผลลัพธ์
- ถ้า ⚠️/⚪ รวม ≥2 ข้อ → ติด "(Provisional)" ที่ Action เสมอ + บอกว่าต้องหาอะไรเพิ่ม
- Thesis killer ต้องเป็น 1 ข้อเท่านั้น
- Bull/Bear แต่ละข้อต้องเป็น observable fact ไม่ใช่ wish
- Action ต้องชัด 1 คำ (+ Provisional tag ถ้าเข้าเงื่อนไข) — ห้ามกำกวม
- ถ้า Fair Value จากหลายแหล่งขัดแย้งกันมาก (>30-40%) → Layer 3 ต้องเขียน "Valuation Inconclusive" ห้ามฟันธง % จากแหล่งเดียว
- Insider selling นับเป็น Bear Case ได้เฉพาะเมื่อผ่าน materiality filter ครบ 3 ข้อ (ผู้บริหารหลายคนขายพร้อมกัน + สัดส่วนมาก + ไม่มีคำอธิบายเป็น routine) — ถ้าไม่ครบให้ใส่แค่ factual note ใน Management ไม่ใช่ Bear Case
