number = int(input("Enter the input Range : "))
arr=[]
for i in range(2,number):
	arr.append(i)

is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )

print(list(filter(is_prime,arr)))