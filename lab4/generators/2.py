x = int(input())

def even(n):
	for i in range(n):
		if i%2 == 0:
			yield i
print(list(even(x)))