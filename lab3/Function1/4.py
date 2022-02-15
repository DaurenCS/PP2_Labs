n = list(map(int, input().split()))

def prime(list):
	arr=[]
	
	for i in range(len(list)):
		cont=0
		for j in range(1,int(list[i]**0.5)+1):
			if list[i] == 1:
				continue

			if list[i] % j == 0:
				cont +=1

		if cont==1:
			arr.append(list[i])
	
	print(arr)
				
			

				
	
prime(n)

