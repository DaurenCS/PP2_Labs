n = input()


def pal(n):
	arr1=[]
	
	for i in range(len(n)):
		arr1.append(n[i])
	arr2 = arr1.copy()
	arr2.reverse()

	if arr1 == arr2:
		print('Is Palindrome')
	else:
		print('Is not Palindrome')

pal(n)

