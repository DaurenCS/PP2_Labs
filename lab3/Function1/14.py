from itertools import permutations
def has_33(nums):
	if len(nums) == 3:
		return True 
	else:
		return False

def pal(n):
	arr1=[]
	
	for i in range(len(n)):
		arr1.append(n[i])
	arr2 = arr1.copy()
	arr2.reverse()

	if arr1 == arr2:
		return True
	else:
		return False

def histogram(list):
	for i in range(len(list)):
		for j in range(list[i]):
			print('*',end='')
		print(end='\n')

perm = list()

while True:
	n = list(map(int,input().split()))
	if has_33(n) == True and pal(n) :
		perm = permutations(n)
		break
	else:
		print('Try again it is not Palindrom')
for i in perm:
	histogram(list(i))