---
name: narrative-drift
description: เทียบ 10-K ย้อนหลังหลายปีของ holding เทียบคำพูดผู้บริหาร (guidance/strategy) กับสิ่งที่เกิดขึ้นจริง หา Red Flag
---

# /narrative-drift [TICKER] — Management Narrative Drift Check

ไอเดียจากคลิป "ผมใช้ CLAUDE COWORK ยังไงบ้าง?" ของช่องลงทุน Diary (ดู [[project-youtube-notebooklm-digest]]) — เทียบ 10-K ย้อนหลังหลายปีดูว่าสิ่งที่ผู้บริหารเคยพูดไว้ (guidance, strategy, promises) ตรงกับที่ทำได้จริงไหม หรือมีการเปลี่ยน narrative แบบเงียบๆ (red flag)

## Input
```
/narrative-drift AVGO           ← ตัวเดียว
/narrative-drift GWRE PLTR V    ← หลายตัว (spawn agent แยกพร้อมกัน)
```

## Pre-flight

```
☐ เช็คว่า sources/[TICKER]/ มีไฟล์ 10-k-*.htm อย่างน้อย 2 ปี — ถ้าไม่ครบ บอกตรงๆ ว่าข้อมูลไม่พอ ห้ามวิเคราะห์จากความจำ
```

## ขั้นตอน (ต่อ 1 ticker)

### 1. แปลง HTML เป็น text

10-K ที่ดึงจาก SEC EDGAR เป็น inline XBRL HTML ขนาดใหญ่ (2-4MB) อ่านตรงๆ เปลืองมาก ให้แปลงเป็น plain text ก่อน:

```bash
for f in sources/[TICKER]/10-k-*.htm; do
  node .claude/skills/narrative-drift/strip-html.js "$f" "${f%.htm}.txt"
done
```

### 2. Spawn agent วิเคราะห์ (subagent_type: general-purpose)

Spawn 1 agent ต่อ 1 ticker (parallel ถ้าหลาย ticker) พร้อม prompt ที่บอกให้:

1. อ่านไฟล์ `sources/[TICKER]/10-k-*.txt` **ทุกปีที่มี** เรียงจากเก่าสุดไปใหม่สุด
2. จากแต่ละปี สกัด:
   - **Item 1A (Risk Factors):** risk ใหม่ที่เพิ่งปรากฏปีนี้ / risk ที่หายไปจากปีก่อน
   - **Item 7 (MD&A):** guidance, strategic priorities, การอธิบายผลประกอบการ, คำมั่นสัญญาต่อนักลงทุน (เช่น "we plan to...", "we expect...", "our strategy is...")
3. **เทียบข้ามปี** หา:
   - Guidance/promise ปีก่อน ที่ปีถัดมาไม่พูดถึงอีกเลย (เงียบหาย) หรือพูดตรงข้าม
   - Strategic priority ที่เปลี่ยนทิศทางกะทันหันโดยไม่มีคำอธิบายเหตุผลชัดเจน
   - Risk factor ใหม่ที่ปรากฏขึ้นแบบไม่มีปี่มีขลุ่ย (อาจเป็นสัญญาณปัญหาที่เพิ่งเกิด)
   - ภาษาที่ soften ลง (เช่น จาก "we will" → "we intend to" → หายไปเลย)
4. **ห้ามแต่งข้อมูล** — ทุก flag ต้อง quote ประโยคจริง + ระบุปีที่มา (เช่น "10-K FY2023 กับ FY2024") ถ้าไม่เจอความขัดแย้งอะไรเลย ให้บอกตรงๆ ว่า "ไม่พบ narrative drift ที่มีนัยสำคัญ" ห้ามยัดเยียดหา flag ที่ไม่มีจริง
5. Return: list ของ flag (ถ้ามี) แต่ละอันมี [ปีที่เปรียบเทียบ] + [คำพูดเดิม] → [สิ่งที่เกิดขึ้น/คำพูดใหม่] + [ทำไมถึงน่าสงสัย]

รันแบบ `run_in_background: false` เพราะต้องรอผลมาเขียนไฟล์ต่อ

### 3. บันทึกผลลง Knowledge Base

เพิ่ม section ใหม่ใน `knowledge/[TICKER].md` (ต่อท้ายไฟล์ ถ้ายังไม่มี section นี้):

```markdown
## Narrative Drift Check ([วันที่])
[ถ้าไม่พบอะไร]: ✅ เทียบ 10-K [ปีเริ่ม]–[ปีล่าสุด] แล้ว ไม่พบ narrative drift ที่มีนัยสำคัญ

[ถ้าพบ]:
🚩 **[หัวข้อสั้น]** ([ปี A] vs [ปี B])
> "[คำพูดเดิมจาก 10-K ปี A]"
→ [สิ่งที่เกิดขึ้นจริง/คำพูดใหม่ใน 10-K ปี B]
เหตุผลที่น่าสงสัย: [1 ประโยค]
```

**ถ้ามี flag ที่ร้ายแรง** (guidance กลับด้านชัดเจน หรือ risk factor ใหม่ที่กระทบ thesis หลัก) → เพิ่มบรรทัดใน `portfolio.md` ใต้ Thesis Change Log ของ ticker นั้นด้วย พร้อม tag `🚩 Narrative Drift`

### 4. Output ใน Chat

```
📋 Narrative Drift — [TICKER] ([ปีเริ่ม]–[ปีล่าสุด], N ปี)

[ถ้าไม่พบ]: ✅ ไม่พบความขัดแย้งที่มีนัยสำคัญระหว่างคำพูดผู้บริหารกับผลที่เกิดขึ้นจริง

[ถ้าพบ — เรียงตามความร้ายแรง]:
🚩 [หัวข้อ] — [ปี A] vs [ปี B]
   "[quote]" → [สิ่งที่เกิดขึ้นจริง]
```

## กฎ

- ห้ามแต่งหรือเดา quote จาก 10-K — ทุก quote ต้องมาจากไฟล์จริงใน `sources/[TICKER]/` เท่านั้น
- ถ้าไฟล์ 10-K มีแค่ปีเดียวหรือไม่มีเลย → บอกตรงๆ ว่าข้อมูลไม่พอ ไม่ทำการวิเคราะห์
- ไม่ใช่ trigger ขาย/ซื้อทันที — เป็นข้อมูลประกอบให้ระวังเพิ่มเติมเท่านั้น ถ้าร้ายแรงจริงให้ user ไปตัดสินใจต่อผ่าน `/brief` อีกที
- ถ้าพบ flag ระดับสูง (guidance กลับด้านชัดเจนกระทบ thesis หลัก) ให้แนะนำให้รัน `/brief [TICKER]` ซ้ำเพื่อประเมิน thesis ใหม่
