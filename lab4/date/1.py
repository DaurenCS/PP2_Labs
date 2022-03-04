import datetime

n = int(input())

x = datetime.date.today() 
x1 = datetime.timedelta(days=n)

print(x-x1)
