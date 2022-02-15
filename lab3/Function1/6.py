n = input()
a = n.split(' ')

def rev(list):
	x = a.copy()
	x.reverse()
	a.append('->')
	for i in range(len(x)):
		a.append(x[i])
	for i in range(len(a)):
		print(a[i], end=' ')

rev(a)

