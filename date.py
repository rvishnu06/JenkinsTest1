from datetime import date
from datetime import time
from datetime import datetime


today = date.today()
print("todays date", today.day , today.month, today.year)

print("todays weekday # is:", today.weekday())
days = ["mon", "tue", 'wed', "thu", "fri", "sat"]
print ("whis is a:", days[today.weekday()])


today = datetime.now()
print ("the currrent dat and time", today)

