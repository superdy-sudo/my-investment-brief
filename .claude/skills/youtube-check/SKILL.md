---
name: youtube-check
description: เช็คคลิปใหม่จากทุกช่อง YouTube ที่ track อยู่ (Tier 5b) รวดเดียว — ลงทุน Diary + The Dam Investor + The Investor's Podcast ผ่าน YouTube "Ask" panel ทั้งหมด (ไม่ใช้ NotebookLM แล้ว)
---

# /youtube-check — Manual All-Channel YouTube Check

เช็คทั้ง 3 ช่องด้วยวิธีเดียวกันหมด — YouTube "Ask" (Gemini) panel ผ่าน Browser pane (login Google ครั้งเดียว ใช้ได้ทุกช่อง ไม่ต้องพึ่ง NotebookLM แล้ว — **2026-09-05 ตัด NotebookLM ออก** เพราะ auth คนละที่เก็บกับ Browser pane ทำให้ต้อง login แยก 2 จุดโดยไม่จำเป็น):
1. **ลงทุน Diary** — เช็ค**ทุกคลิปใหม่ไม่กรอง** (ผู้ใช้ติดตามทั้งสาย AI/automation ด้วย ไม่ใช่แค่การลงทุน)
2. **The Dam Investor + The Investor's Podcast** — ค้นหาเฉพาะคลิปที่เกี่ยวกับ ticker ใน Holdings/Watchlist ปัจจุบัน

ทั้งหมดเป็น **ข้อมูลประกอบ/มุมมองเสริม ไม่ใช่ fact source** — ห้ามใช้แทน `/brief` หรือ 10-K/earnings/IR data ([[project-youtube-source-hierarchy]])

## ขั้นตอน

### 1. ลงทุน Diary — เช็คคลิปใหม่ทุกคลิป

1. ดึง RSS feed: `curl -sL -A "Mozilla/5.0" "https://www.youtube.com/feeds/videos.xml?channel_id=UCELVTxN2RQM-JnKs6uG_5xg"` (ต้องใส่ user-agent ไม่งั้น 404) — parse videoId + title + published date
2. เทียบกับ state file `.claude/state/longtoon-diary-last-seen.txt` (videoId ล่าสุดที่ process แล้ว) — เอาทุกคลิปที่ใหม่กว่านั้น ไม่กรองว่าเกี่ยวหุ้นหรือไม่ (ถ้าไม่มีไฟล์ state → ใช้แค่ 5 คลิปล่าสุด กันย้อนหลังท่วม)
3. สำหรับคลิปใหม่แต่ละคลิป — เปิดผ่าน Browser pane แล้วใช้ปุ่ม "Ask" (ดูขั้นตอนละเอียดในหัวข้อ "วิธีดึงเนื้อหาคลิป" ด้านล่าง) ถามสรุปประเด็นสำคัญเป็นภาษาไทย
4. บันทึกทุกคลิปลง `youtube-digests/longtoon-diary.md` (เพิ่มบนสุด ไม่ลบของเก่า):
   ```
   ## [วันที่ publish] — [ชื่อคลิป]
   [สรุป 3-4 ข้อจาก Ask panel]
   🔗 https://www.youtube.com/watch?v=[VIDEO_ID]
   ```
5. ถ้าคลิปไหนเกี่ยวกับ Ticker ใน Holdings/Watchlist ปัจจุบัน (เช็คจาก `portfolio.md`) → เพิ่ม note สั้นๆ ใน `portfolio.md` section `## 📺 YouTube Digest — ลงทุน Diary` ด้วย (เก็บแค่ 10 entry ล่าสุด)
6. อัปเดต state file ทับด้วย videoId ล่าสุด

ถ้าไม่มีคลิปใหม่ → ข้ามไปข้อ 2 เลย ไม่ต้อง commit ส่วนนี้

### 2. The Dam Investor + The Investor's Podcast — เช็คเฉพาะ ticker ที่ถืออยู่/สนใจ

อ่านรายชื่อ ticker ปัจจุบันจาก `portfolio.md` (section `## Holdings` + `## Watchlist`)

สำหรับ **แต่ละ ticker ใน Holdings** (conviction สูงสุด เช็คทุกตัว) และ **ticker ใน Watchlist ที่ยัง Provisional/รอ catalyst** (ข้าม ticker ที่ Watch เฉยๆ ไม่มีอะไรเปลี่ยนแปลงถ้าเวลาจำกัด):

1. WebSearch: `The Dam Investor youtube [TICKER] 2026` และ `The Investor's Podcast youtube [TICKER] 2026`
2. ถ้าเจอคลิปที่เกี่ยวกับ ticker นั้นโดยตรงและโพสต์ใหม่ (เทียบวันที่ล่าสุดที่เคยดึงจาก `knowledge/[TICKER].md` หรือ `briefs/` ถ้ามี) → เปิดผ่าน Browser pane แล้วใช้ปุ่ม "Ask" (ดูขั้นตอนละเอียดด้านล่าง) เพื่อสรุปเนื้อหา
3. ถ้าไม่เจอคลิปใหม่ที่เกี่ยวข้อง → ข้าม ไม่ต้องฝืนหา

**บันทึกผล:** เพิ่ม section สั้นๆ ต่อท้าย `knowledge/[TICKER].md` (ถ้ามีคลิปที่เกี่ยวข้องจริง):
```markdown
## YouTube Update ([วันที่])
🎥 **[ชื่อช่อง]** — "[ชื่อคลิป]" ([วันที่โพสต์])
[สรุปมุมมองที่เกี่ยวกับ thesis ticker นี้]
🔗 [URL]
```
ระบุกำกับเสมอว่า "[ช่อง] มองว่า..." แยกจาก fact จริง — ห้ามปนกับตัวเลขจาก Tier 1-4

## วิธีดึงเนื้อหาคลิป — YouTube "Ask" (Gemini) panel

ใช้วิธีเดียวกันทั้ง 3 ช่อง (รายละเอียดเต็มอยู่ใน Tier 5b ของ [augustus.md](../../agents/augustus.md)):

1. **ต้อง login Google account ในหน้า Browser pane ก่อนเสมอ** — ถ้ายังไม่ login ให้ขอ user login เอง (ห้ามกรอกรหัสผ่านแทน) session จะจำ cookie ไว้จนกว่าจะหมดอายุ
2. `navigate` ไปที่ URL คลิป
3. หาปุ่ม "Ask" ใต้วิดีโอ (ข้าง Save/Share) แล้วคลิกเปิด panel "Ask about this video"
4. พิมพ์คำถามในช่อง `Ask a question...` เช่น "สรุปวิดีโอนี้อย่างละเอียด แบ่งเป็นหัวข้อ ครอบคลุมทุกประเด็นสำคัญที่พูดถึง ห้ามย่อสั้นเกินไป"
5. **ปุ่ม Send เป็น custom element** plain click มักไม่ติด — ถ้ากดแล้วข้อความยังค้าง ใช้ `javascript_tool` dispatch synthetic pointer event:
   ```js
   const btn = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-label')==='Send');
   const r = btn.getBoundingClientRect();
   ['pointerdown','mousedown','pointerup','mouseup','click'].forEach(t =>
     btn.dispatchEvent(new MouseEvent(t, {bubbles:true, cancelable:true, clientX:r.left+r.width/2, clientY:r.top+r.height/2, view:window})));
   ```
6. รอ 5-6 วินาที แล้วอ่านด้วย `get_page_text` (คำตอบพร้อม timestamp เช่น `(5:05 - 7:17)`)
7. ถามต่อเนื่องได้ในช่องเดิม

**Fallback** ถ้าไม่มีปุ่ม "Ask" ขึ้น (ยังไม่ login/ฟีเจอร์ไม่เปิด) → `yt-dlp --write-auto-sub --skip-download --sub-lang th` ดึง auto-caption แทน (มีในเครื่องแล้ว) — คุณภาพรองลงมา สะกดเพี้ยนได้ ต้องอ่านตีความเอาความหมาย

## Output ใน Chat

สรุปสั้นๆ ต่อช่อง:
```
📺 YouTube Check — [วันที่]

ลงทุน Diary: [N คลิปใหม่ / ไม่มีคลิปใหม่]
  - [ชื่อคลิป] (ถ้าเกี่ยวหุ้นในพอร์ต ระบุ ticker)

The Dam Investor: [ticker ที่เจอคลิปใหม่ / ไม่เจอคลิปที่เกี่ยวข้อง]
The Investor's Podcast: [ticker ที่เจอคลิปใหม่ / ไม่เจอคลิปที่เกี่ยวข้อง]
```

## กฎ
- ห้ามแต่งข้อมูล — ถ้าหาไม่เจอจริงๆ บอกตรงๆ ว่าไม่เจอ ไม่ต้องยัดเยียด
- เนื้อหาจากทุกช่องเป็น**ความเห็นส่วนบุคคล ไม่ใช่ fact** — ไม่ใช่ trigger ซื้อ/ขายเอง ถ้าเจออะไรที่กระทบ thesis จริงจัง ให้แนะนำรัน `/brief [TICKER]` ต่อ
- ไม่ต้อง commit/push อัตโนมัติหลังรัน — ให้ user สั่งเองถ้าต้องการ (ต่างจาก scheduled task เดิมที่ auto-push)
