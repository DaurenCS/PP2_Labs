h=int(input())
l=int(input())

def Solve(numh,numl):
	y = int(((4*numh)-numl)/2)
	x = int(numh - y) 
	print (f'rabbits: {y} , chicken: {x}' )
Solve(h,l)