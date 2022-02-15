class Shape:
	s=0
	def area(self):
		print(self.s)
class Rectangle(Shape):

	def __init__(self,l,w):
		self.lengh = l
		self.widgh = w
		self.s = self.lengh*self.widgh
n=int(input())
b=int(input())
a=Rectangle(n,b)
a.area()


