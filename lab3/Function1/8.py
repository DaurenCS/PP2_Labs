def spy_game(nums):
	arr7 = []
	arr0 = []
	for i in range(len(nums)):
		if nums[i] == 7:
			arr7.append(i)
		if nums[i] == 0:
			arr0.append(i)

	cont=0
	for i in range(len(arr0)):
		if max(arr7) > arr0[i]:
			cont+=1
	if cont >=2:
		print('True')
	else:
		print('False')


	
		
			


	
	
spy_game([1,2,7,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 