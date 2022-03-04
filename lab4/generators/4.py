x,b = map(int,input().split())

def sq(a,b):
	for i in range(a,b):
		yield i**2
s = sq(x,b)

for i in s:
	print(i)