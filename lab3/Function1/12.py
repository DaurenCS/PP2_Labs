def histogram(list):
	for i in range(len(list)):
		for j in range(list[i]):
			print('*',end='')
		print(end='\n')
histogram([4, 9, 7])