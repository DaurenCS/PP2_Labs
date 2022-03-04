x = int(input())
a = []
def div(n):
	for i in range(1,n+1):
		if i%4==0 and i%3==0:
			yield i

s = div(x)

for i in s:
	print(i)