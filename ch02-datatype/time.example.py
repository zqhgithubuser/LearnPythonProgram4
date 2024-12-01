import calendar as cal
import time
from datetime import date, datetime, timedelta, timezone
import pytz

print("**************************************************")
# datetime.date
today = date.today()  # 2024-11-27
print(today)
print(today.ctime())
print(today.isoformat())
print(today.weekday())  # 2
print(cal.day_name[today.weekday()])  # Wednesday
print(today.day, today.month, today.year)
print(today.timetuple())

print("**************************************************")
# time
print(time.ctime())  # Wed Nov 27 16:05:05 2024
print(time.daylight)
print(time.gmtime())
print(time.gmtime(0))
print(time.localtime())
print(time.time())

print("**************************************************")
# datetime.datetime
now = datetime.now()  # 2024-11-27 16:05:05.616238
print(now)
# utcnow = datetime.utcnow()
# print(utcnow)
print(now.date())
print(now.day, now.month, now.year)
print(now.time())
print(now.microsecond, now.second, now.minute, now.hour)
print(now.ctime())
print(now.isoformat())
print(now.tzinfo)
print(now.weekday())

print("**************************************************")
# datetime.timedelta
f_bday = datetime(1975, 12, 29, 12, 50, tzinfo=pytz.timezone("Asia/Shanghai"))
h_bday = datetime(1981, 10, 7, 15, 30, 50, tzinfo=timezone(timedelta(hours=2)))
diff = h_bday - f_bday
print(type(diff))
print(diff.days)
print(diff.total_seconds())
print(today + timedelta(days=49))
print(now + timedelta(weeks=7))
