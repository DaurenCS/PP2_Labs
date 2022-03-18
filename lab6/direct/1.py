import os
path = 'C:/Users/ASus/Desktop/KBTU/pp2 labs/lab5'


for item in os.listdir(path):
	if os.path.isdir(os.path.join(path, item)):
		print(f'dir: {item}')
		for item in os.listdir(os.path.join(path, item)):
			if os.path.exists(item):
				print('---', item)
			else:
				continue

			
	elif os.path.isfile(os.path.join(path, item)):
		print(f'file: {item}')
	else:
		print(f'other: {item}')

