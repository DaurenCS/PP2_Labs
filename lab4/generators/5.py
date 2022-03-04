x = int(input())

def fun(n):
	for i in range(n,0,-1):
		yield i
s = fun(x)

for i in s:
 print(i) 
