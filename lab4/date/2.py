import datetime 
x = datetime.date.today()
x1 = datetime.timedelta(days = 1)
print('tomorrow:', x + x1)
print('today:',x)
print('yesterday:', x - x1)