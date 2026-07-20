---
name: daily-brief
description: อัปเดตพอร์ต + Top Pick + Watchlist ประจำวัน
---

# Daily Brief — Minimal System

## หลักการ
> "ข่าวที่ไม่เปลี่ยน Thesis ไม่ต้องใส่"

เป้าหมายคือ **ช่วยตัดสินใจ** ไม่ใช่รวบรวมข่าว

---

## Pre-flight (ทำก่อนเสมอ — < 30 วินาที)

```
☐ อ่าน portfolio.md — ห้ามใช้ memory
☐ อ่าน knowledge/INDEX.md (สรุป 1 บรรทัด/ticker) — เปิด knowledge/[TICKER].md เต็มเฉพาะตัวที่จำเป็น (ราคาเปลี่ยนแรง/มี earnings ใกล้/user ถามเจาะจง) ประหยัด token
☐ เช็ควันที่ — weekend แจ้ง "ตลาดปิด ราคา T-1"
☐ เช็ค .env มี OPENAI_API_KEY ไหม
```

## ⚠️ กฎราคาหุ้น — curl (Bash) เท่านั้น ห้าม WebFetch tool

**ห้ามใช้ WebSearch สำหรับราคา** — AI summary ของ WebSearch มักคืนราคาเก่าหรือผิดพลาด

**ห้ามใช้ WebFetch tool ดึงราคาจาก Yahoo Finance** — พบว่า WebFetch tool (ที่ผ่าน AI summarization) โดน Yahoo block/fail บ่อยมาก (2026-07-13/14) แต่ยิง `curl` ตรงจาก Bash กลับใช้ได้ปกติ 100% — สาเหตุคือ WebFetch tool proxy โดน rate-limit/block ไม่ใช่ API ตายจริง

ใช้ **Bash curl** ตรง Yahoo Finance API (ต้องใส่ User-Agent ไม่งั้นบาง endpoint อาจ reject):
```bash
curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://query1.finance.yahoo.com/v8/finance/chart/[TICKER]?interval=1d&range=1d"
```
Parse ค่า `meta.regularMarketPrice` จาก JSON output = ราคา real-time — fetch หลาย ticker พร้อมกันได้ด้วย loop เดียว:
```bash
for t in GWRE PLTR AVGO V SPGI; do
  echo "=== $t ==="
  curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "https://query1.finance.yahoo.com/v8/finance/chart/$t?interval=1d&range=1d" | grep -o '"regularMarketPrice":[0-9.]*'
done
```

**⚠️ ห้ามใช้วันที่จาก JSON/timestamp มาแปลงเอง** — Unix timestamp แปลงผิดบ่อย (เจอเคสจริง: ราคาถูกต้อง แต่บอกวันที่เป็น "May 2024" ทั้งที่จริงคือ Jul 2026)
→ **ใช้วันที่ปัจจุบันของระบบเสมอ** (วันที่รัน brief) ไม่ใช่วันที่จาก JSON/timestamp — ราคาที่ได้คือราคา ณ ตอนรันอยู่แล้ว ไม่ต้องพึ่งวันที่จาก API

**Fallback ถ้า curl โดน block ด้วย** (rare): ลอง `query2.finance.yahoo.com` แทน `query1` ก่อน ถ้ายัง fail ทั้งคู่ค่อย fallback ไป WebSearch ตามกฎเดิม (ราคาอาจ lag)

WebSearch ใช้ได้เฉพาะ: ค้นข่าว/catalyst เท่านั้น ห้ามใช้ดึงราคา

---

## Mode Detection

| Argument | Mode |
|----------|------|
| (ไม่มี) | Full Brief |
| `close` | Close Brief — สรุปปลายวัน |
| `topup [จำนวน]` | Top-up — แนะนำซื้อตัวไหน |
| `TICKER,...` | Spot Brief — วิเคราะห์ตัวที่ระบุ |

---

## Full Brief

### 1. ดึงข้อมูล (ทำพร้อมกัน)

**Holdings — fetch ราคาเฉพาะตัวที่เข้าเงื่อนไข:**
- มี earnings วันนี้ → WebSearch ข่าวเต็ม
- ราคาเปลี่ยน >3% → WebSearch หาสาเหตุ
- ที่เหลือ → fetch ราคาอย่างเดียว ไม่ search news

**⚠️ Dynamic TP Reset check — เฉพาะตัวที่มี earnings วันนี้ (GWRE/PLTR/AVGO เท่านั้น, ไม่ใช่ V):**
ถ้าวันนี้ตรงกับ "Re-evaluate เมื่อ" ของ ticker นั้นใน portfolio.md (earnings checkpoint) ให้เช็คตามกฎ "Dynamic TP Reset" ใน portfolio.md ก่อนตอบคำถามอื่น:
- Growth ยัง ≥30% YoY หรือ accelerating → reset TP1/TP2 ใหม่จากราคาวันนี้ (×1.5 / ×2.0) แล้วอัปเดต portfolio.md + knowledge/[TICKER].md
- Growth ชะลอแต่ยังผ่าน ≥30% → คง TP เดิม ไม่ต้องแก้ไฟล์
- ถ้า reset เกิดขึ้น → แจ้งใน output ด้วยบรรทัด "🔧 TP Reset: [TICKER] TP1/TP2 ใหม่ $X/$Y (จาก growth ยังผ่านเกณฑ์ ณ earnings วันนี้)"

**Market (WebSearch 1 ครั้ง):**
- S&P, NASDAQ, VIX, 10Y Yield

**Top Pick:**
- fetch ราคา + เช็ค entry zone เทียบ portfolio.md (เฉพาะตัวใน Watchlist ที่ผ่าน /brief แล้ว — ดู step 3)

**Market Scan (หาหุ้นใหม่ทั้งตลาด US ตรง growth style) — รันทุกเช้าคู่กับ Top Pick:**

ใช้ Finviz screener ผ่าน Bash curl (ทดสอบแล้วว่าใช้ได้โดยไม่ต้อง login/paywall — ต้องใส่ User-Agent) — **ดึง 2 หน้า (40 ตัว) เรียงตาม market cap มากไปน้อย** ห้ามปล่อย default sort (ตัวอักษร A-Z) เพราะจะได้ list ที่ bias ไปทางชื่อขึ้นต้นด้วย A-C ไม่สะท้อนหุ้นที่น่าสนใจจริง:
```bash
for r in "" "&r=21"; do
  curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36" "https://finviz.com/screener.ashx?v=111&f=cap_midover,fa_salesqoq_o30,geo_usa,sh_avgvol_o500,sh_price_o5&o=-marketcap${r}&ft=4"
done | grep -oE 'class="company-ticker" href="stock\?t=[A-Z.\-]+' | sed 's/.*t=//' | awk '!seen[$0]++'
```
**ห้ามใช้ `sort -u`** — จะทำให้ list กลับไปเรียงตัวอักษรทิ้ง market cap order ที่ตั้งใจไว้ ใช้ `awk '!seen[$0]++'` แทน (dedupe แต่รักษาลำดับเดิม)
Filter ที่ใช้: `cap_midover` (mkt cap ≥$2B กันหุ้นเล็ก/ผันผวนเกิน) + `fa_salesqoq_o30` (sales growth QoQ >30% — proxy ของ growth bar ≥30% YoY ใน portfolio.md) + `geo_usa` + `sh_avgvol_o500` (สภาพคล่องพอ) + `sh_price_o5` (กัน penny stock) + `o=-marketcap` (เรียง market cap มากไปน้อย — ได้หุ้นตัวใหญ่/รู้จักก่อน) — 20 ตัว/หน้า ดึง 2 หน้า (`r=21` = หน้า 2) รวม ~40 ตัว

**หลังได้ list ตัวเลือก:**
1. ตัดตัวที่อยู่ใน Holdings หรือ Watchlist (portfolio.md) ออก — ไม่ต้องเอามาเทียบซ้ำ
2. ตัดตัวที่เคย Avoid มาแล้วออกด้วย (เช็คจากชื่อไฟล์ `briefs/[TICKER]-*.md` ที่มีคำว่า "Avoid" ใน Layer 4 Action)
3. ตัวที่เหลือ = **New Candidates** — **ห้ามฟันธง Buy/Avoid ทันที** เพราะยังไม่ผ่าน 4-Layer analysis (Moat, Valuation, ฯลฯ) ของ `/brief` แค่ผ่านตัวกรอง growth เชิงปริมาณเท่านั้น
4. โชว์ New Candidates สูงสุด 5 ตัวใน output (**เรียงตาม market cap ที่ได้จาก screener แล้ว — เอาตัวแรกสุดของ list ที่เหลือหลังตัด**) พร้อมข้อความแนะนำให้รัน `/brief TICKER` ถ้าสนใจตัวไหน

**หมายเหตุ:** ขั้นนี้แค่ "ค้นพบ" ตัวใหม่ที่ผ่าน growth filter เชิงปริมาณ ไม่ได้แทนที่ 4-Layer analysis — Top Pick ยังคงเลือกจาก Watchlist ที่ผ่าน `/brief` แล้วเท่านั้น (ดู step 3) ตัวจาก Market Scan ต้องผ่าน `/brief` ก่อนถึงจะเข้า Watchlist และมีสิทธิ์เป็น Top Pick ได้

### 2. ตอบ 4 คำถามต่อ Holding ทุกตัว

```
[TICKER] $XXX [+X%]
├─ Thesis เปลี่ยนไหม?     ✅ No change / ⚠️ [อะไรเปลี่ยน]
├─ Valuation เปลี่ยนไหม?  ✅ Fair / ⚠️ Expensive / 🟢 Cheap
├─ Entry/Exit Zone?        ✅ ถืออยู่ (buffer X%) / 🚨 Kill ใกล้ / 🎯 TP1 ใกล้
└─ Action วันนี้           Hold / Watch / ⚠️ Review
```

**Conviction Score (0-10)** — คำนวณจาก 4 คำถามข้างบน ไม่ใช่ตัวเลขลอยๆ:
- Thesis: No change +3 / Improved +4 / Weakened +1
- Valuation: Cheap +3 / Fair +2 / Expensive +1
- Zone: buffer >10% หรือถือปกติ +2 / ใกล้ TP +2 / ใกล้ Kill +0
- Growth bar (revenue growth ≥30% YoY ตาม style ปัจจุบัน) ผ่าน +1 / ไม่ผ่าน +0

### 3. Top Pick

```
🏆 Top Pick: [TICKER]  (Conviction: X.X/10)
   ราคา: $XXX | Zone: $X–$X [✅ อยู่ใน zone / ⚠️ เกิน zone]
   เหตุผล: [1 ประโยค]
   ❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1]
   Action: Buy / Starter Position
```

**กฎ Top Pick (2026-07-20): ต้องเป็น Buy หรือ Starter เท่านั้น — ห้ามเป็น Watch/Avoid**

Top Pick เลือกจาก **Watchlist เท่านั้น** (ตัวที่ผ่าน `/brief` 4-Layer แล้ว) โดยใช้ **Layer 4 Action ล่าสุดจากไฟล์ `briefs/[TICKER]-[DATE].md` ล่าสุดของ ticker นั้น** เป็นตัวกรอง — ตัวที่เจอจาก Market Scan ยังไม่ผ่านการ vet เต็ม จะไม่ถูกเลือกจนกว่าจะรัน `/brief` แล้วเข้า Watchlist ก่อน

ทุกครั้งที่รัน Full Brief ให้เช็ค Action ล่าสุดของ Top Pick ปัจจุบันก่อนเสมอ (จากไฟล์ brief ล่าสุด ไม่ใช่ Watchlist table ที่อาจไม่ sync):
- ถ้ายังเป็น **Buy หรือ Starter** → คง Top Pick เดิม (หรืออัปเดตราคา/conviction)
- ถ้าเปลี่ยนเป็น **Watch หรือ Avoid** (ราคาแพงขึ้นจนเกิน zone, thesis อ่อนลง, หรือ /brief refresh ใหม่ปรับ Action ลง) → **เอาออกจาก Top Pick ทันที** แล้วหาตัวถัดไปใน Watchlist ที่ Action ล่าสุด = Buy/Starter มาแทน
- ถ้า**ไม่มี ticker ไหนใน Watchlist ที่เป็น Buy/Starter เลย** → ไม่ต้องมี Top Pick วันนี้ เขียนในสรุปว่า "🏆 Top Pick: ไม่มี — ไม่มี Watchlist ticker ที่ผ่านเกณฑ์ Buy/Starter ตอนนี้" และ **ต้องลบ Top Pick ออกจาก showcase/index.html ด้วย** (ดู step 5)

### 3b. Funding Source

หาว่า Holding ตัวไหนควรเป็นแหล่งเงินทุนสำหรับซื้อ Top Pick/Watchlist ตัวใหม่ — ใช้เกณฑ์ style เดิม ("⚠️ Holdings เดิม...ให้พิจารณาตอนมี TP/kill/earnings" ใน portfolio.md):

```
💰 Funding Source
   [TICKER] — Status: Funding Candidate
   จะขายเมื่อ: [เช็คลิสต์ — ระบุว่าผ่านข้อไหนแล้ว/ยังขาดข้อไหน]
     ☐ Top Pick ซ้ำ ≥3 Brief
     ☐ Bull ชนะ Bear (จาก /brief ล่าสุดของ Top Pick)
     ☐ Fact Check ผ่าน
     ☐ เข้า Entry Zone
```

ถ้าไม่มี Holding ไหนเข้าเกณฑ์ funding candidate (เช่น thesis ยังแข็งแรงและตรง growth style อยู่) → เขียน "ไม่มี — Holdings ทั้งหมดยังตรง style" แทน ไม่ต้อง force หา candidate

### 4. สรุปใน Chat

```
📊 [วันที่] — Daily Brief

🌍 ตลาด: S&P [+X%] | NASDAQ [+X%] | VIX [XX]

📌 Holdings:
   TICKER  $XXX [+X%] | ✅/⚠️/🚨 | [เหตุผล ถ้าเปลี่ยน]
   ...
   (ตัวที่ไม่เปลี่ยน Thesis → แสดงแค่ราคาและ ✅)

🏆 Top Pick: TICKER $XXX (Conviction: X.X/10)
   Action: [Buy/Starter/Watch] — [เหตุผล 1 ประโยค]
   ❓ ผิดได้ถ้า: [เหตุผลอันดับ 1]

💰 Funding Source: [TICKER — เงื่อนไขที่ผ่าน/ยังขาด] หรือ "ไม่มี"

📅 Earnings ใน 7 วัน: [ถ้ามี]
⚠️ ต้องทำวันนี้: [action เดียว หรือ "ไม่มี"]

🔮 Predictions for Today:
   1. [สิ่งที่คาดว่าจะเกิด — พร้อม trigger ที่จะ confirm/deny]
   2. [ถ้ามี]
   3. [ถ้ามี]

🔍 Fact Check & Confidence:
   [ข้อมูล/ข่าวสำคัญวันนี้] ★★★★★ Confirmed / ★★★☆☆ หลายแหล่งไม่ตรง / ★★☆☆☆ ยังเป็น Rumor
   ...
   Today's Confidence: XX% — [เหตุผลสั้นๆ อิงจาก fact check ข้างบน เช่น "✅ CPI ออกแล้ว ✅ ไม่มี Earnings ⚠️ ข่าว Iran ยังไม่นิ่ง"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 สรุป (Data vs Decision)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
สรุป Brief: [สิ่งที่สำคัญที่สุดวันนี้ — 1 ประโยค]
Fact Check: [อะไร confirmed แล้ว / อะไรยัง unconfirmed — 1 ประโยค]
Comment ระบบ: [thesis ตัวไหนเปลี่ยนหรือไม่ + ระบบควรทำอะไร] | Confidence XX% | Action: Do Nothing / [action เดียว]
🆕 Market Scan: [TICKER1, TICKER2, ...] (ยังไม่ผ่าน /brief — รัน `/brief TICKER` ถ้าสนใจ) หรือ "ไม่มีตัวใหม่วันนี้"

🎯 สิ่งที่จะทำให้เปลี่ยนใจ
   • [trigger 1 — เช่น earnings/event ที่รอผล]
   • [trigger 2]
   • [trigger 3 — เช่น "หุ้นใน Watchlist ลงเข้า Entry Zone"]
```

**หมายเหตุ:** Predictions section บังคับทุกครั้ง — Close Brief จะใช้ grade accuracy
**หมายเหตุ:** "สรุป (Data vs Decision)" + "🎯 สิ่งที่จะทำให้เปลี่ยนใจ" คือส่วนปิดท้ายเสมอ (ต่อกัน ไม่แยก section) — แยกข้อมูลออกจากการตัดสินใจ และบอกชัดว่าต้องรออะไรก่อนถึงจะพิจารณา action ใหม่ ให้อ่านแค่นี้แล้วรู้ทันทีว่าวันนี้ต้องทำอะไร/รออะไรอยู่ โดยไม่ต้องไล่อ่านทั้ง brief
**หมายเหตุ (2026-07-17):** Market Scan ต้องอยู่ตรงนี้เสมอ (ในบล็อกปิดท้ายติดกับ "สรุป Data vs Decision") ไม่ใช่แทรกกลาง brief — เหตุผล: ผู้ใช้อ่านแค่บล็อกปิดท้ายเป็นหลัก ถ้า Market Scan อยู่กลาง brief จะหลุดสายตาไปง่าย (เกิดเหตุการณ์จริง 2026-07-17 ที่ผู้ใช้ไม่เห็น candidates เพราะ section อยู่กลางไม่ใช่ท้าย)

### 5. Save + Push

```bash
git add portfolio.md showcase/index.html showcase/briefs.html
git commit -m "brief [วันที่]: [Top Pick] | [market 1 ประโยค]"
git push origin main
```

อัปเดต showcase/index.html ด้วย comment markers เดิม (แทนที่เฉพาะ content ระหว่าง markers) — รวมถึง `<!-- SUMMARY_START -->`/`<!-- SUMMARY_END -->` ที่ต้อง sync กับ "สรุป (Data vs Decision)" 3 บรรทัดในแชททุกครั้ง ห้ามลืม

**showcase/index.html scope (2026-07-17):** หน้านี้จบที่ Holdings section เท่านั้น (Header → What's Changed → Market → Zones → Analysis → Summary → Holdings) — ห้ามเพิ่ม Thesis Change Log, Company Briefs card, หรือ Watchlist/scout log กลับเข้ามา ข้อมูลพวกนี้อยู่ที่ portfolio.md / knowledge/[TICKER].md / briefs/[TICKER]-[DATE].md / showcase/briefs.html อยู่แล้ว

**หุ้นที่ขายแล้ว:** ลบการ์ดออกจาก Holdings section ใน showcase/index.html ทันทีที่ขาย (ไม่ต้องเก็บการ์ด "SOLD ✅" ไว้) — realized P&L ดูได้จาก portfolio.md และ knowledge/_sold/[TICKER].md อยู่แล้ว

**Top Pick ที่ไม่ใช่ Buy/Starter แล้ว (2026-07-20):** ทุกครั้งที่ Top Pick เปลี่ยน (ตัวเดิมหลุดจาก Buy/Starter, หรือเปลี่ยนไปตัวใหม่) ต้องอัปเดต showcase/index.html ให้ตรงทันที — ลบ/แก้ทุกจุดที่พูดถึง Top Pick เดิม:
- `<p>` บน Header (ส่วน "Top Pick: [TICKER] (...)")
- `<!-- WHATS_CHANGED_START -->` ถ้ามีพูดถึง Top Pick
- `<!-- SUMMARY_START -->` (บรรทัด Comment ระบบ ที่มักอ้างถึง Top Pick)
ถ้าไม่มี Top Pick ใหม่มาแทน (ไม่มี ticker ไหนใน Watchlist เป็น Buy/Starter เลย) → **ลบทุกการอ้างอิงถึง Top Pick ออกจากหน้านี้ทั้งหมด** ไม่ต้องเว้นว่างไว้เฉยๆ หรือเขียนว่า "ไม่มี Top Pick" ค้างอยู่ในหน้า pre-market — หน้านี้ควรมีแต่ข้อมูล Holdings/Market/Summary ที่เป็นปัจจุบันเท่านั้น

**เมื่อ daily-brief ทำ /brief ตัวไหน (เช่น Market Scan candidate, spot brief):** นอกจากบันทึก `briefs/[TICKER]-[DATE].md` ตามปกติแล้ว ให้เพิ่มการ์ดใน `showcase/briefs.html` ด้วย — ถ้ามี section ของวันนี้ (`<!-- YYYY-MM-DD -->`) อยู่แล้วให้เพิ่มการ์ดต่อท้าย `cards-grid` ของวันนั้น ถ้ายังไม่มีให้สร้าง section ใหม่ (คัดลอกโครงจาก section ล่าสุด) แล้ววางไว้บนสุด (ใหม่สุดอยู่บน) — ห้ามผสมหลายวันไว้การ์ดเดียวหรือย้อนกลับไปแก้การ์ดของวันเก่า

---

## Close Brief (`/daily-brief close`)

**เป้าหมาย:** ตรวจ prediction + เรียนรู้จากสิ่งที่ผิด + เตรียมพรุ่งนี้
**ไม่ใช่:** สรุปข่าวซ้ำ / เขียน Holdings ใหม่ทุกตัว / เขียน TP/Kill ซ้ำ

Search เฉพาะตัวที่เปลี่ยน >1% หรือมี after-hours news — ที่เหลือไม่ต้อง search

```
📊 Close — [วันที่]   🌍 ปิด: S&P [+X%] | NASDAQ [+X%] | VIX [XX]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔮 1. Prediction Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[copy Predictions จาก Morning Brief มา grade]

   Predicted → Reality → ✅/❌
   [prediction 1]  → [เกิดจริง?]  → ✅/❌
   [prediction 2]  → [เกิดจริง?]  → ✅/❌

   Accuracy: X/X ([%])
   ผิดเพราะ: [ถ้าผิด — 1 ประโยค อย่า justify แค่อธิบาย]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 2. What's Changed (vs Morning Brief)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[เขียนเฉพาะตัวที่เปลี่ยน >1% หรือมีข่าวใหม่]
   TICKER [+X%] — [เหตุผล 1 ประโยค]
   ...
   (ถ้าไม่มีอะไรเปลี่ยน → "No material changes")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧭 3. Thesis Check
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[เฉพาะตัวที่เปลี่ยน — ตัวที่ No Change ไม่ต้องเขียน]
   TICKER → Improved / No Change / Weakened — [เหตุผล ≤1 บรรทัด]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 4. Lessons Learned (≤3 ข้อ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   • [สิ่งที่ตลาดสอนวันนี้ — ไม่ใช่แค่ fact แต่คือ pattern]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 5. Tomorrow Watch (≤3 ข้อ)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   • [สิ่งที่ต้องดูพรุ่งนี้ — เฉพาะที่ actionable]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 6. สรุป (Data vs Decision)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
สรุป Brief: [สิ่งที่สำคัญที่สุดวันนี้ — 1 ประโยค]
Fact Check: [อะไร confirmed แล้ว / อะไรยัง unconfirmed — 1 ประโยค]
Comment ระบบ: [thesis ตัวไหนเปลี่ยนหรือไม่ + ระบบควรทำอะไร] | Confidence XX% | Action: Do Nothing / [action เดียว]

🎯 สิ่งที่จะทำให้เปลี่ยนใจ
   • [trigger 1]
   • [trigger 2]
   • [trigger 3]
```

**Token target:** 700–900 tokens | อ่านจบ 3 นาที

---

## Top-up Mode (`/daily-brief topup [จำนวน]`)

```
1. อ่าน portfolio.md (ไม่ต้อง search)
2. Fetch ราคา Holdings + Top Pick ทั้งหมด
3. คัดกรอง:
   - Size Up: Holdings ลง ≥8% + thesis ✅ + kill buffer >10%
   - เข้าใหม่: Watchlist ที่ราคาอยู่ใน entry zone
4. **Concentration Risk Check** (เฉพาะ Size Up ของ ticker ที่ถืออยู่แล้ว) — คำนวณ % ของพอร์ตรวมที่ ticker นั้นจะกลายเป็นหลัง top-up นี้ ถ้าเกิน 40% ให้เติม "⚠️ Concentration สูง — จะเป็น ~X% ของพอร์ต" ต่อท้ายคำแนะนำ (ไม่ใช่ Avoid อัตโนมัติ แค่เตือน เพราะ style นี้ยอมรับ concentration สูง)
5. ตอบ:
```

```
💰 Top-up แนะนำ — $[จำนวน]

[TICKER]  $XXX | [เหตุผล 1 ประโยค] | Action: [%] [⚠️ Concentration สูง ถ้าเข้าเงื่อนไข]
[TICKER]  $XXX | [เหตุผล 1 ประโยค] | Action: [%]

❓ Thesis ผิดได้ถ้า: [เหตุผลอันดับ 1 ของตัวที่แนะนำ]
```

ไม่ save ไฟล์ — ตอบใน chat อย่างเดียว

---

## Spot Brief (`/daily-brief TICKER`)

```
1. Fetch ราคา + WebSearch news 48 ชม.
2. ตรวจ 4 Layer (ถ้าตัวใหม่ — ดู company-brief SKILL)
3. ตอบ:
```

```
[TICKER] — [ชื่อบริษัท]
ราคา: $XXX | Moat: Wide/Narrow/None
Thesis: [2 ประโยค]
Action: 🟢 Buy / 🟡 Starter / 🟠 Watch / 🔴 Avoid
❓ ผิดได้ถ้า: [เหตุผลอันดับ 1]
```

---

## กฎ

- ข่าวที่ไม่เปลี่ยน Thesis → ไม่ใส่
- Search เฉพาะ: earnings วันนี้ หรือ ราคาเปลี่ยน >3%
- ตัวที่เงียบ → แสดงแค่ราคา + ✅
- ทุก recommendation ต้องมี "❓ Thesis ผิดได้ถ้า"
- ห้ามแต่งข้อมูล — ถ้าหาไม่ได้บอกตรงๆ
