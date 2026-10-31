# Conquest: PB (Prosperity Bancshares) - 2026-10-31
*Independent check, ใช้เฉพาะ raw fundamentals ใน briefs/PB-2026-10-31.md (ราคา $71.98)*

## ผล: คำนวณ point-estimate Fair Value ไม่ได้ (ไม่ฝืน)

เหตุผล:
1. **ไม่มี cost of equity input ในไฟล์** - ไม่มี risk-free, beta, ERP. Bank valuation (excess return / Gordon) อ่อนไหวต่อ r มาก ถ้าเดา r ผลคือ "FV" ที่เป็นแค่ผลของ r ที่เดา
2. **ไม่มี TBV/share และ period-end shares** (brief ระบุ ⚪ เอง) ROATCE ให้มาแต่ tangible equity ไม่มี
3. **Earnings ไม่สะอาด** - Q3 มี merger cost $69.7M, accretion $11.6M, Stellar เข้ามาเต็มไตรมาสแรก (ปิด 1 ก.ค.) ไม่มี organic growth, ไม่มี NIM/accretion guidance
4. Morningstar FV ไม่มี (brief ⚪)

## สิ่งที่คำนวณได้จากไฟล์ (reverse valuation แทน forward FV)
- Diluted shares Q3 ≈ 141.5M / 1.18 = 119.9M (คำนวณเอง, weighted ไม่ใช่ period-end)
- BVPS รวม goodwill ≈ $9.760B / 119.9M ≈ $81.4 -> P/B ≈ 0.88 (ตรงกับ Webull 0.88) ไม่ใช่ TBV
- ROE บน period-end equity: adjusted 200.8M x4 / 9.760B ≈ 8.2%; GAAP 141.5M x4 / 9.760B ≈ 5.8% (period-end equity > avg equity จึงต่ำกว่าจริงเล็กน้อย)
- Dividend run-rate $0.64 x4 = $2.56 -> payout ≈ 38% ของ adj EPS annualized ($6.68)
- Reverse (P/B = (ROE-g)/(r-g), ROE 8.2%, g 3% สมมติเพื่อดูเท่านั้น): ราคา $71.98 สื่อ r ≈ 8.9% ถ้า r จริง 8% -> ~$85, 9% -> ~$70, 10% -> ~$60 (FV ผันผวน +/-$12 ต่อ 1% ของ r)

## สรุป
- FV: N/A | Bucket: ไม่ตัดสิน (ไม่ใช่ Cheap/Fair/Expensive)
- ที่ $71.98 ตลาดสื่อ implied cost of equity ~9% บน adjusted ROE 8.2% - ไม่ถูก/แพงชัดเจน
- ไม่ควรใช้เป็นเสียงที่ 3 ใน 2-ใน-3 สำหรับ PB จนกว่าจะมี TBV, period-end shares, และ Q4 ที่ไม่มี merger noise (earnings ~ปลาย ม.ค. 2027)
- GuruFocus implied ~$83-84 (brief) ไม่สามารถยืนยัน/โต้แย้งได้จาก conquest นี้
