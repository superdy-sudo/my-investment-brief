# My First Project — US Stock Research System

## Project Purpose
ระบบวิจัยและติดตามหุ้น US สำหรับนักลงทุนระยะยาว (Naphat, Bangkok)
- วิเคราะห์หุ้นแบบ Moat-focused ตาม style ของ Buffett / Fundsmith
- อัปเดต Holdings (SPGI, CME, MA) และ Watchlist ทุกวันอัตโนมัติ
- หา Top Pick รายวัน → เถียงกับ Gemini (Bull vs Bear debate)
- แสดงผลใน showcase: https://capable-rabanadas-bd7540.netlify.app/

## Agent System
- **augustus** — WebSearch + ราคาหุ้นจาก Yahoo Finance + วิเคราะห์ข้อมูล
- **keen** — อ่าน 10-K SEC filing → fundamentals
- **bear** — เรียก Gemini API → หา bear case โต้แย้ง bull thesis
- **Skills:** /daily-brief (รัน pipeline ทั้งหมด), /company-brief

## File Structure
- `portfolio.md` — Holdings (shares, buy price), Kill Conditions, Watchlist
- `briefs/` — brief ทุกไฟล์เรียงตามวัน
- `sources/` — SEC filings, earnings data
- `showcase/index.html` — หน้าเว็บแสดงผล

## How I work
- ตอบเป็นภาษาไทยเสมอ
- ถ้าไม่แน่ใจให้ถามก่อนทำ
- บันทึกผลลัพธ์ลงในไฟล์เสมอ อย่าแค่แสดงใน chat
- ราคาหุ้น → ดึงจาก Yahoo Finance (finance.yahoo.com/quote/TICKER) เสมอ ห้ามเดา

## My investing style
- นักลงทุนระยะกลาง-ยาว (1-3 ปี) ไม่ใช่ trader
- สนใจบริษัทที่มี moat ชัดเจน และ management น่าเชื่อถือ
- เน้น downside protection ก่อน upside
- ไม่ชอบบริษัทที่ leverage สูงโดยไม่จำเป็น
- ถ้า valuation แพงเกินไป บอกตรงๆ อย่าเกลี้ยกล่อม
- ใช้ Morningstar Wide Moat + Quality Fund 13F เป็น primary screener

## Screener criteria
- **Sector:** ทุก sector (Tech, Healthcare, Consumer, Energy, Financials ฯลฯ)
- **Market cap:** Large cap ($10B+) และ Mid cap ($2B-$10B)
- **Valuation:** ไม่มี P/E limit แต่ต้องอธิบายได้ว่า premium สมเหตุสมผลกับ moat/growth
- **Geography:** US only (NYSE, NASDAQ)

## Current Holdings (ดูรายละเอียดใน portfolio.md)
- SPGI — S&P Global | 0.1816941 shares | buy avg $412.79 (2 lots: 0.1463022 @ $410.11 + 0.0353919 @ $423.26)
- CME — CME Group | 0.1204786 shares | buy $290.01
- MA — Mastercard | 0.0504650 shares | buy $494.60

## Rules
- ห้ามแต่งตัวเลข — ทุก claim ต้องมี source + วันที่
- ห้ามทำนายราคา ห้าม buy/sell recommendation
- Kill condition trigger → แสดง 🚨 alert เสมอ (ไม่ขายอัตโนมัติ)
