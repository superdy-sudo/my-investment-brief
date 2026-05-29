ค้นหาข้อมูลหุ้น $ARGUMENTS และสร้างรายงานสั้นๆ ประกอบด้วย:

- ชื่อบริษัทและ ticker
- ธุรกิจหลักคืออะไร (2-3 ประโยค)
- ตัวเลขสำคัญ: market cap, P/E, revenue ล่าสุด
- Latest earnings: ผลประกอบการล่าสุดเป็นยังไง
- ความเสี่ยงหลัก 2-3 ข้อ
- สรุป 1 ย่อหน้า

บันทึกผลลัพธ์เป็นไฟล์ briefs/[TICKER]-brief.md

## อัปเดต showcase/index.html

หลังเขียน brief เสร็จ ให้เพิ่ม card ของหุ้นตัวนั้นเข้าไปใน showcase/index.html ด้วย โดย:

1. เพิ่ม section ใหม่ (ถ้ายังไม่มี section ของวันนี้) หรือเพิ่ม card เข้า section วันนี้
2. Card ต้องมี section "🏢 บริษัทนี้ทำอะไร?" เสมอ — เขียนเป็นภาษาคน 3-4 บรรทัด
3. ใส่ metrics สำคัญ (market cap, revenue, key metric)
4. ใส่ thesis/summary สั้นๆ ใน trend div
5. badge ใช้ class `badge-scout`
6. อัปเดต Tier List ตามความเหมาะสม (ถ้ายังไม่มี ticker นี้ใน tier ใดเลย ให้ใส่ B ก่อนเป็น default)
7. อัปเดต header `<p>` ให้แสดงวันที่และ ticker ล่าสุดที่ brief
