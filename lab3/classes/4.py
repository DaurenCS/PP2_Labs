class Point:
	x = y = 0
	def __init__(self,x,y):
		self.x = x
		self.y = y
	
	def move(self,x,y):
		self.x +=x
		self.y +=y


	def show(self):
		return f'{self.x} {self.y}'

	def dist(self):
		return float(pow((self.x)**2+(self.y)**2, 0.5))
	

p= Point(2,2)
p.move(1,1)
print(p.show())
print(p.dist())
