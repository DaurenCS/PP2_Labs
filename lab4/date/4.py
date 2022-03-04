import datetime 
y,m,d = map(int,input().split())
y1,m1,d1 = map(int, input().split())
x = datetime.datetime(y,m,d)
x1 = datetime.datetime(y1,m1,d1)

print(abs(x1-x).days*86400, "sec")