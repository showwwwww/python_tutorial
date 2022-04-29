# import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%D %H:%M:%S'))

import datetime
print(datetime.datetime.now())
newTime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newTime)

one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print(new_date + one_day)
