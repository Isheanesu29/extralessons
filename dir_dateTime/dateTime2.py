

import datetime as dt
import pytz as pz

date1 = dt.datetime(2021,7,27,12,30,45,tzinfo=pz.utc)

date2 = dt.datetime.now(tz=pz.utc)

# for x in pz.all_timezones:
  #  print(x)

date3 = date2.astimezone(pz.timezone('Europe/Stockholm'))

iSo_format = dt.datetime.now()
 
stringDate = "04 July, 2021"
date4 = dt.datetime.strptime(stringDate,"%d %B, %Y")

print(date4)

