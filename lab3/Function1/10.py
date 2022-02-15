n = list(map(int,input().split()))

def unique(list):
	arr=[]
	for i in n :
		if i not in arr:
			arr.append(i)
	print(arr)
unique(n)