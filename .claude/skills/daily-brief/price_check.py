"""ดึงราคา Yahoo (query1 + query2 cross-check) พร้อมตรวจว่า "วันของแท่งราคา" ตรงกับวันซื้อขายล่าสุดที่คาดไว้

ใช้: python price_check.py GWRE PLTR %5EGSPC ...
ผลลัพธ์: ticker | price | prev_close | pct | status

status:
  OK              วันของแท่งราคาตรงกับวันซื้อขายล่าสุดที่คาด และ query1/query2 ต่างกัน <=0.5%
  CHECK-DATE      วันของแท่งราคาไม่ตรง (อาจเป็นวันหยุดตลาด หรือข้อมูลค้าง) — ตรวจมือก่อนใช้
  CHECK-XSRC      query1 กับ query2 ต่างกัน >0.5% — ตรวจมือก่อนใช้
  FAIL            ดึงไม่ได้

กฎเดิมยังอยู่: วันที่จาก API ใช้ "ตรวจสอบ" เท่านั้น ห้ามคัดลอกไปเขียนใน brief — ใช้วันที่ระบบเสมอ
"""
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def fetch(host, ticker):
    url = f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=5d"
    out = subprocess.run(["curl", "-s", "-A", UA, url], capture_output=True, text=True, timeout=30).stdout
    d = json.loads(out)["chart"]["result"][0]
    closes = [c for c in d["indicators"]["quote"][0]["close"] if c]
    return d["meta"], closes


def expected_trading_date(gmtoffset):
    et = datetime.now(timezone.utc) + timedelta(seconds=gmtoffset)
    d = et.date()
    before_open = et.hour < 9 or (et.hour == 9 and et.minute < 30)
    if et.weekday() >= 5 or before_open:
        d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def main(tickers):
    sys.stdout.reconfigure(encoding="utf-8")
    for t in tickers:
        try:
            m1, c1 = fetch("query1", t)
            price = m1["regularMarketPrice"]
            off = m1.get("gmtoffset", -14400)
            bar = (datetime.fromtimestamp(m1["regularMarketTime"], timezone.utc) + timedelta(seconds=off)).date()
            status = "OK" if bar == expected_trading_date(off) else "CHECK-DATE"
            try:
                m2, _ = fetch("query2", t)
                if abs(m2["regularMarketPrice"] / price - 1) > 0.005:
                    status = "CHECK-XSRC"
            except Exception:
                status += "(query2-unavailable)"
            prev = c1[-2] if len(c1) > 1 else None
            pct = f"{(price / prev - 1) * 100:+.2f}%" if prev else "n/a"
            print(f"{t}\t{price}\t{round(prev, 3) if prev else 'n/a'}\t{pct}\t{status}")
        except Exception as e:
            print(f"{t}\tn/a\tn/a\tn/a\tFAIL({type(e).__name__})")


if __name__ == "__main__":
    main(sys.argv[1:])
