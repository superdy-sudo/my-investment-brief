---
name: system-audit
description: ตรวจสอบทั้งระบบ daily-brief/showcase — หา bug, sync ข้อมูล, แก้ไขเอง, รายงานสิ่งที่เจอ/แก้ (manual — auto schedule ถูกปิดแล้ว 2026-09-06)
---

# /system-audit — Manual System Audit

คุณคือระบบ audit ตัวเองของ daily-brief/showcase สำหรับพอร์ตหุ้น US ของ Naphat ที่ `C:\Users\Admin\OneDrive\my-first-project\` — **เดิมรันอัตโนมัติทุกวันอาทิตย์ ปิด auto schedule แล้ว 2026-09-06 เปลี่ยนเป็นสั่งรันมือผ่าน `/system-audit` แทน**

**เป้าหมาย:** หา bug/ความไม่สอดคล้องทั้งระบบ → แก้ไขที่แก้ได้ทันที → รายงานทุกอย่างที่เจอและที่แก้ให้ชัดเจน (ไม่ใช่แค่รายงานเฉยๆ — ต้องลงมือแก้ด้วย)

## ขั้นตอนตรวจสอบ

### 1. Data Consistency — เทียบ 3 ไฟล์
อ่าน `portfolio.md`, `showcase/index.html`, `showcase/close.html`
- เช็คว่าราคา/P&L ของทุก ticker ใน Holdings ตรงกันทั้ง 3 ไฟล์ไหม
- **ถ้าไม่ตรง** → ใช้ `portfolio.md` เป็น source of truth เสมอ แก้ showcase ให้ตรง แล้ว commit
- เช็ควันที่ "Updated:" ในแต่ละไฟล์ว่าใกล้เคียงกันไหม (ห่างกันเกิน 3 วัน = ผิดปกติ)

### 2. Orphan Ticker Check
สแกน `showcase/index.html` และ `showcase/close.html` หา ticker ที่:
- ปรากฏเป็น "Holdings" หรือ "Top Pick" ที่ active แต่ **ไม่อยู่ใน portfolio.md Holdings ปัจจุบันแล้ว** (แปลว่าขายไปแล้วแต่ card ยังค้าง)
- **ถ้าเจอ** → ลบ/แก้ card นั้นออกทันที (เหมือนเคส CME/MA/MDLZ ที่เจอมาก่อน) แล้ว commit

### 3. Automation Health Check
- รัน `git log --oneline -20` ใน `C:\Users\Admin\OneDrive\my-first-project` เช็คว่ามี commit จากการ brief/daily-brief ในช่วง 7 วันที่ผ่านมากี่ครั้ง (ทุก skill เป็น manual หมดแล้ว 2026-09-06 — ไม่มีอะไรควรรันเองอัตโนมัติอีก ถ้าเจอ commit ที่ timestamp ดูเหมือนมาจาก cron ให้ flag ว่าอาจมี schedule หลงเหลือที่ลืมปิด)
- เช็ค `mcp__scheduled-tasks__list_scheduled_tasks` ว่าทุก task ยัง `enabled: false` ตามที่ตั้งใจไว้หรือมีตัวไหนถูกเปิดกลับมาโดยไม่ได้ตั้งใจ

### 4. Scheduled Task Registry Check
เรียก `mcp__scheduled-tasks__list_scheduled_tasks` เช็คสถานะทุก task (`daily-brief-premarket`, `daily-brief-close`, `system-audit` เดิม, `brief-as-weekly`) — **ทั้งหมดควร `enabled: false` แล้ว** (เปลี่ยนเป็น manual 2026-09-06) ถ้าเจอตัวไหน `enabled: true` โดยไม่มีเหตุผล → flag ในรายงาน (ไม่ต้อง auto-disable เอง เผื่อผู้ใช้ตั้งใจเปิดกลับมาเอง)

### 5. Skill File Regression Check
อ่าน `.claude/skills/brief/SKILL.md`, `.claude/skills/daily-brief/SKILL.md`
เช็คว่ากฎสำคัญที่เคยแก้ไปยังอยู่ครบไหม:
- ใช้ Bash curl ตรงจาก Yahoo Finance (`query1.finance.yahoo.com/v8/finance/chart/[TICKER]`) ไม่ใช่ WebFetch/WebSearch สำหรับราคาปัจจุบัน — WebFetch โดน Yahoo block บ่อย (แก้ 2026-09-06: เดิม SKILL.md นี้เขียนผิดว่า "ใช้ WebFetch ไม่ใช่ WebSearch" ซึ่งสวนทางกับกฎจริงใน `brief/SKILL.md` เจอตอนรัน audit รอบแรก)
- ห้ามใช้วันที่จาก WebFetch/WebSearch summary
- ระบบสถานะ 4 แบบ (✅/❌/⚠️/⚪) ใน /brief
- กฎค้นซ้ำก่อนสรุป Unknown
- **ถ้ามี after-hours move แรงหลังงบ → ต้อง verify ราคาปิดตลาดจริงกับแหล่งภายนอกก่อนคำนวณ TAM/valuation** (เพิ่ม 2026-09-05 หลังเจอเคส IOT ใช้ after-hours peak ผิด)
- ถ้ากฎไหนหายไป (ถูกแก้ทับโดยไม่ตั้งใจ) → แจ้งในรายงาน ไม่ต้อง auto-restore เอง (เผื่อเป็นการแก้ไขที่ตั้งใจ)

## Commit (เฉพาะข้อ 1-2 ที่แก้ได้จริง)
```bash
cd "C:\Users\Admin\OneDrive\my-first-project"
git add portfolio.md showcase/index.html showcase/close.html
git commit -m "system-audit [YYYY-MM-DD]: [สรุปสิ่งที่แก้]"
git push origin main
```

## Output ในแชท — รายงานเสมอ (ไม่ต้อง terse แบบ daily-brief)

```
🔍 System Audit — [วันที่]

✅ แก้ไขแล้ว (auto-fix):
   [รายการที่แก้ พร้อมเหตุผลสั้นๆ — หรือ "ไม่มี" ถ้าไม่เจออะไร]

⚠️ พบแต่แก้เองไม่ได้ — ต้องตรวจสอบด้วยมือ:
   [Automation gap / scheduled task เปิดกลับมาโดยไม่ตั้งใจ / skill file regression — หรือ "ไม่มี"]

📊 สรุป: [X ไฟล์ sync ตรงกัน / Y orphan ticker ที่เจอ+ลบ / Z commit ใน 7 วัน]
```

ห้ามแต่งข้อมูล — ถ้าตรวจไม่ได้บางจุด (เช่น tool ไม่พร้อม) ให้บอกตรงๆ ว่าข้ามจุดไหนไป
