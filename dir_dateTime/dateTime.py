

import datetime as dt

date = dt.date(2021,8,15)
today = dt.date.today()
year = today.year
day = today.day
weekday = today.weekday()
timedelta = dt.timedelta(days=20)
delta = today + timedelta
print(delta)

