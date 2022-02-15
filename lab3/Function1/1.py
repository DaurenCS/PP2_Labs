n = list(map(int,input().split()))

def toUn(list):
	for i in range(len(list)):
		list[i] *=28.3495231
	print(list)
toUn(n)

