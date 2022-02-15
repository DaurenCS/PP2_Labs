from itertools import permutations
n = input()
def per(str):
	perm = permutations(n)

	for i in list(perm):
		print(i)
per(n)

