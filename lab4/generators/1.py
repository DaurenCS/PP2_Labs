x = int(input())

def square(n):
	for i in range(n):
		yield i**2
		
print(list(square(x)))