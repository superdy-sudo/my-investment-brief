---
name: company-brief
description: Research a public company and produce a structured investment brief. Trigger when the user asks for a brief, research, or analysis on a stock ticker or company name.
---

# Company Brief SOP

## Trigger
รัน skill นี้เมื่อ user ขอ brief, research, หรือ analysis ของหุ้นหรือบริษัท

## Steps
1. ระบุ TICKER และชื่อบริษัทจาก user input
2. รัน 3 agents พร้อมกันผ่าน Agent tool พร้อม `run_in_background: true` ทั้งหมด:
   - **keen** — อ่าน 10-K ใน sources/<TICKER>/ สกัด fundamentals, moat indicators, risk factors
   - **North** — อ่าน earnings transcript ใน sources/<TICKER>/ สรุป beat/miss, guidance, management tone
   - **augustus** — ใช้ WebSearch ค้นหา observable signals ล่าสุด: ข่าว, analyst ratings, insider activity
3. รอรับ output จากทั้ง 3 agents แล้ว compile เป็น brief ตาม Output format ด้านล่าง
4. ดึงตัวเลข Key Numbers (market cap, P/E, revenue TTM, gross margin) จาก output ของ keen และ augustus — ถ้าหาไม่พบให้เขียน "ไม่พบข้อมูล"
5. ระบุความเสี่ยง 2-3 ข้อจาก risk factors ของ keen + red flags ของ augustus
6. เขียน kill condition โดยอิง objective conditions จาก output ที่ได้
7. เขียน summary 1 ย่อหน้าในสไตล์ของ user (อ่านจาก CLAUDE.md)

## Output format
บันทึกเป็น briefs/[TICKER]-brief.md โดยใช้ structure นี้:

# [Company] ([TICKER]) — Brief

## Business
[2-3 ประโยค]

## Key Numbers
- Market Cap:
- P/E:
- Revenue (TTM):
- Gross Margin:

### 3. Latest earnings
3-5 bullets **Source:** อ่านทุกไฟล์ใน sources/<TICKER>/ ก่อนเขียน ถ้า folder ว่างหรือไม่มี เขียนตรงๆ: "ไม่มี earnings transcript ใน sources/<TICKER>/ skip section นี้หรือ user ใส่ source ก่อน" ห้ามแต่งตัวเลขจากความจำ ทุก bullet ในนี้ต้อง trace กลับไปที่ไฟล์ใน sources/ ได้ และระบุไฟล์ต้นทางใน parens ท้าย bullet เช่น (source: sources/AAPL/q1-2026-call.md)

## Risks
1.
2.
3.

## Kill Condition
ขายถ้า: [เงื่อนไข]

## Summary
[1 ย่อหน้า ในสไตล์ของ user]

## Checklist
- [ ] ตัวเลขทุกตัวมีแหล่งที่มา ไม่แต่งขึ้นเอง
- [ ] ถ้าหาข้อมูลไม่ได้ให้เขียน "ไม่พบข้อมูล" แทนการเดา
- [ ] Kill condition เป็น objective condition ไม่ใช่ความรู้สึก
