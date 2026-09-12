---
name: youtube-check
description: เช็คคลิปใหม่จากทุกช่อง YouTube ที่ track อยู่ (Tier 5b) รวดเดียว — ลงทุน Diary + The Diary Of A CEO + The Dam Investor + The Investor's Podcast ผ่าน YouTube "Ask" panel ทั้งหมด (ไม่ใช้ NotebookLM แล้ว)
---

# /youtube-check — Manual All-Channel YouTube Check

เช็คทั้ง 4 ช่องด้วยวิธีเดียวกันหมด — YouTube "Ask" (Gemini) panel ผ่าน Browser pane (login Google ครั้งเดียว ใช้ได้ทุกช่อง ไม่ต้องพึ่ง NotebookLM แล้ว — **2026-09-05 ตัด NotebookLM ออก** เพราะ auth คนละที่เก็บกับ Browser pane ทำให้ต้อง login แยก 2 จุดโดยไม่จำเป็น)

**2026-09-12: เปลี่ยนทุกช่องเป็นเช็คทุกคลิปใหม่ไม่กรอง ticker แล้ว** (เดิม The Dam Investor + The Investor's Podcast เช็คเฉพาะคลิปที่เกี่ยวกับ ticker ใน Holdings/Watchlist — ผู้ใช้อยากไล่ดูคลิปเก่าที่น่าสนใจด้วยแม้ไม่เกี่ยวกับพอร์ต) ทุกช่องใช้ RSS feed + state file แบบเดียวกันหมด:

| ช่อง | channel_id | state file | digest file |
|------|-----------|-----------|-------------|
| ลงทุน Diary | `UCELVTxN2RQM-JnKs6uG_5xg` | `.claude/state/longtoon-diary-last-seen.txt` | `youtube-digests/longtoon-diary.md` |
| The Diary Of A CEO | `UCGq-a57w-aPwyi3pW7XLiHw` | `.claude/state/diary-of-a-ceo-last-seen.txt` | `youtube-digests/diary-of-a-ceo.md` |
| The Dam Investor | `UC5pihKBMc4yDs9WufeGS9Ng` | `.claude/state/dam-investor-last-seen.txt` | `youtube-digests/dam-investor.md` |
| The Investor's Podcast | `UCBOkqyWxbp8jtcsvcHB7qog` | `.claude/state/investors-podcast-last-seen.txt` | `youtube-digests/investors-podcast.md` |

ทั้งหมดเป็น **ข้อมูลประกอบ/มุมมองเสริม ไม่ใช่ fact source** — ห้ามใช้แทน `/brief` หรือ 10-K/earnings/IR data ([[project-youtube-source-hierarchy]])

## ขั้นตอน (ทำซ้ำแบบเดียวกันทั้ง 4 ช่อง)

สำหรับแต่ละช่องในตารางด้านบน:

1. ดึง RSS feed: `curl -sL -A "Mozilla/5.0" "https://www.youtube.com/feeds/videos.xml?channel_id=[CHANNEL_ID]"` (ต้องใส่ user-agent ไม่งั้น 404) — parse videoId + title + published date
2. เทียบกับ state file ของช่องนั้น (videoId ล่าสุดที่ process แล้ว) — เอาทุกคลิปที่ใหม่กว่านั้น **ไม่กรองว่าเกี่ยวหุ้นหรือไม่ ไม่กรองว่าเกี่ยวพอร์ตหรือไม่**
   - **ถ้าไม่มีไฟล์ state (ช่องนี้ยังไม่เคย backfill)** → ให้ backfill ย้อนหลัง **3-6 เดือนล่าสุด** ของช่องนั้น (ไม่ใช่แค่ 5 คลิปล่าสุดแบบเดิม) — ทำแค่ครั้งเดียวตอนเริ่มใช้ช่องนี้ครั้งแรกเท่านั้น พอสร้าง state file แล้วรอบถัดไปกลับไปเช็คแค่คลิปใหม่ตามปกติ (ข้อ 2 ด้านบน)
3. สำหรับคลิปใหม่แต่ละคลิป — เปิดผ่าน Browser pane แล้วใช้ปุ่ม "Ask" (ดูขั้นตอนละเอียดในหัวข้อ "วิธีดึงเนื้อหาคลิป" ด้านล่าง) ถามสรุปประเด็นสำคัญเป็นภาษาไทย
4. บันทึกทุกคลิปลง digest file ของช่องนั้น (เพิ่มบนสุด ไม่ลบของเก่า):
   ```
   ## [วันที่ publish] — [ชื่อคลิป]
   [สรุป 3-4 ข้อจาก Ask panel]
   🔗 https://www.youtube.com/watch?v=[VIDEO_ID]
   ```
5. ถ้าคลิปไหนเกี่ยวกับ Ticker ใน Holdings/Watchlist ปัจจุบัน (เช็คจาก `portfolio.md`) → เพิ่ม note สั้นๆ ใน `portfolio.md` section `## 📺 YouTube Digest — [ชื่อช่อง]` ด้วย (เก็บแค่ 10 entry ล่าสุด) — ถ้าไม่เกี่ยวพอร์ตก็บันทึกแค่ใน digest file พอ ไม่ต้องยัดเข้า portfolio.md
6. อัปเดต state file ทับด้วย videoId ล่าสุด

ถ้าช่องไหนไม่มีคลิปใหม่ → ข้ามไปช่องถัดไป ไม่ต้อง commit ส่วนนั้น

## วิธีดึงเนื้อหาคลิป — YouTube "Ask" (Gemini) panel

ใช้วิธีเดียวกันทั้ง 4 ช่อง (รายละเอียดเต็มอยู่ใน Tier 5b ของ [augustus.md](../../agents/augustus.md)):

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

The Diary Of A CEO: [N คลิปใหม่ / ไม่มีคลิปใหม่]
  - [ชื่อคลิป] (ถ้าเกี่ยวหุ้นในพอร์ต ระบุ ticker)

The Dam Investor: [N คลิปใหม่ / ไม่มีคลิปใหม่]
  - [ชื่อคลิป] (ถ้าเกี่ยวหุ้นในพอร์ต ระบุ ticker)

The Investor's Podcast: [N คลิปใหม่ / ไม่มีคลิปใหม่]
  - [ชื่อคลิป] (ถ้าเกี่ยวหุ้นในพอร์ต ระบุ ticker)
```

## กฎ
- ห้ามแต่งข้อมูล — ถ้าหาไม่เจอจริงๆ บอกตรงๆ ว่าไม่เจอ ไม่ต้องยัดเยียด
- เนื้อหาจากทุกช่องเป็น**ความเห็นส่วนบุคคล ไม่ใช่ fact** — ไม่ใช่ trigger ซื้อ/ขายเอง ถ้าเจออะไรที่กระทบ thesis จริงจัง ให้แนะนำรัน `/brief [TICKER]` ต่อ
- ไม่ต้อง commit/push อัตโนมัติหลังรัน — ให้ user สั่งเองถ้าต้องการ (ต่างจาก scheduled task เดิมที่ auto-push)
