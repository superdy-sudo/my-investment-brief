# Weekly Review Skill

## Trigger
- `/weekly-review` — รีวิวสัปดาห์ที่ผ่านมา + อัปเดต SKILL.md ถ้ามี pattern ชัด
- `/weekly-review force` — บังคับ update แม้ข้อมูลน้อยกว่า 3 วัน

---

## Step 0: Mode Detection

ถ้ามี argument `force`:
- ข้ามเกณฑ์ minimum data (3+ วัน) — update ได้แม้มีข้อมูลแค่ 1-2 วัน
- แจ้งใน output ว่า "⚠️ Force mode — ข้อมูลน้อย อาจเป็น noise"

ถ้าไม่มี argument:
- ใช้เกณฑ์ปกติ — ต้องมีข้อมูลจาก 3+ วันขึ้นไปถึงจะ update SKILL.md

---

## Step 1: อ่าน Skill ปัจจุบัน

อ่านไฟล์: `C:\Users\Admin\Desktop\my-first-project\.claude\skills\daily-brief\SKILL.md`

จำ rules ปัจจุบันไว้ก่อนเพื่อเปรียบเทียบหลัง review

---

## Step 2: รวบรวมหลักฐานสัปดาห์นี้

อ่านไฟล์ทั้งหมดใน `C:\Users\Admin\Desktop\my-first-project\briefs\` ที่สร้างใน 7 วันล่าสุด:
- `*-update-YYYY-MM-DD.md` — Holdings updates (pre-market / เช้า)
- `close-YYYY-MM-DD.md` — Close summaries (หลังปิดตลาด)
- `spot-*-YYYY-MM-DD.md` — Spot briefs
- `market-overview-YYYY-MM-DD.md` — Market overviews
- `TICKER-YYYY-MM-DD.md` — Top Pick briefs
- `*-debate-YYYY-MM-DD.md` — Bull/Bear debates

**Pair เช้า–ปิด (ทำทุกวันที่มีไฟล์ทั้งคู่):**
สำหรับแต่ละวันที่มีทั้ง `*-update-DD.md` และ `close-DD.md`:
- ดึง thesis status เช้า vs ราคาจริงปิด
- บันทึก accuracy: ✅ ถูก | ❌ ผิดทิศ | ⚠️ ถูกบางส่วน

อ่าน `C:\Users\Admin\Desktop\my-first-project\portfolio.md` เพื่อดู:
- Realized gains/losses (ขายตัวไหนไป ได้/เสียเท่าไหร่)
- Holdings P&L ปัจจุบัน vs thesis status
- Top Pick ที่แนะนำใน 7 วันที่ผ่านมา

**ถ้าไม่มีไฟล์ brief เลยใน 7 วัน:**
- แจ้ง "ไม่มีข้อมูลเพียงพอสำหรับ review" แล้วหยุด (เว้นแต่ force mode)

---

## Step 3: วิเคราะห์ผล

### 3A: Top Pick Accuracy
สำหรับแต่ละ Top Pick ที่แนะนำสัปดาห์นี้:
- Entry zone ที่กำหนดไว้ — ราคาจริงเข้า zone ไหม?
- Thesis ที่ให้ไว้ — ยังถูกต้องปลายสัปดาห์ไหม?
- Bull/Bear debate verdict — ผลออกมาถูกทิศทางไหม?

ให้คะแนน: ✅ ถูก | ⚠️ บางส่วน | ❌ ผิด

### 3B: Holdings Thesis Check
- Thesis status call (✅/⚠️/🚨) แต่ละตัว — ตรงกับราคาจริงที่เกิดขึ้นไหม?
- Kill alert ที่ trigger — false positive หรือ true positive?
- TP alert (ถ้ามี) — ราคาถึงจริงไหม?

### 3C: Pre vs Post Market Accuracy
สำหรับแต่ละวันที่มีทั้ง brief เช้า + close file:

| วัน | คาดเช้า | จริงปิด | ถูก? |
|-----|---------|---------|------|
| จันทร์ | Financials +X% | จริง +Y% | ✅/❌ |
| ... | ... | ... | ... |

- นับ accuracy รายวัน → คำนวณ % สัปดาห์
- หาว่า sector call หรือ Holdings thesis call ผิดบ่อยกว่า

### 3D: Market Overview Accuracy
- Sector call (Financials, Tech) — ถูกทิศทางกี่วัน?
- VIX interpretation — ตลาดเป็นไปตามที่ประเมินไหม?
- Rate/Yield call — กระทบ Holdings ตามที่คาดไหม?

---

## Step 4: หา Pattern ที่ควร Update

**อัปเดต SKILL.md เฉพาะเมื่อ:**
- Pattern เกิดซ้ำ 3+ ครั้ง (หรือ 3+ วัน) — ไม่ใช่ noise รายวัน
- Force mode: ลด threshold เหลือ 1+ ครั้ง

**ตัวอย่าง pattern ที่อัปเดตได้:**
- Entry zone แคบเกินไป 3 ครั้ง → ขยาย zone threshold
- Top Pick ซ้ำตัวเดิม 3+ สัปดาห์แต่ราคาไม่เข้า → เพิ่ม auto-drop rule
- Kill alert ที่ trigger แต่ราคา recover ทุกครั้ง → ปรับ buffer threshold
- Sector call ผิดเมื่อ VIX ต่ำกว่า 15 → เพิ่ม caveat

**ห้ามอัปเดตถ้า:**
- ข้อมูล 1-2 วัน (เว้นแต่ force mode)
- ตลาดผิดปกติ (earnings week ทุกตัว, macro shock ใหญ่)
- การเปลี่ยนทำให้ skill ซับซ้อนขึ้นโดยไม่ได้ประโยชน์ชัดเจน

---

## Step 5: อัปเดต SKILL.md (ถ้ามี)

แก้ไข `C:\Users\Admin\Desktop\my-first-project\.claude\skills\daily-brief\SKILL.md`

**format การเพิ่ม comment:**
```
> 📝 Updated YYYY-MM-DD: [เหตุผลจากข้อมูลสัปดาห์นี้]
```

เพิ่ม comment ก่อน rule ที่เปลี่ยน — แก้เฉพาะจุด ไม่ rewrite section ทั้งหมด

---

## Step 6: เขียน Weekly Review File

บันทึกผลไปที่: `C:\Users\Admin\Desktop\my-first-project\briefs\weekly-review-YYYY-MM-DD.md`

```markdown
# Weekly Brief Review — สัปดาห์สิ้นสุด [วันที่]

## Top Pick Performance
| Ticker | วันที่แนะนำ | Entry Zone | ราคาจริง | ผล |
|--------|------------|------------|----------|-----|
| ...    | ...        | ...        | ...      | ✅/⚠️/❌ |

**accuracy: X/Y (X%) | mode: [ปกติ/force]**

## Holdings Thesis Accuracy
| Ticker | Status Call | ราคาจริง | ถูก/ผิด |
|--------|-------------|----------|---------|
...

## Market Overview
- Sector calls ถูก X/Y วัน
- VIX interpretation: [ถูก/ผิด/ไม่สามารถตัดสินได้]

## SKILL.md Updates
[รายการที่เปลี่ยน — หรือ "ไม่มีการเปลี่ยนแปลง: [เหตุผล]"]

## สิ่งที่ต้องติดตามสัปดาห์หน้า
1. [ประเด็นสำคัญ 1]
2. [ประเด็นสำคัญ 2]
```

---

## Rules

- ห้ามแต่งข้อมูล — ถ้าไม่มีไฟล์ brief บอกตรงๆ
- ห้าม update SKILL.md จาก noise — ต้องมี pattern ชัด
- update ต้องเป็น surgical — แก้เฉพาะ rule ที่มีหลักฐาน ไม่ rewrite ทั้ง section
- ถ้า force mode ให้แจ้งเตือนทุกครั้งที่ output ว่า "⚠️ Force mode"
