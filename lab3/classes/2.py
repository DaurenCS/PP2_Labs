n=int(input())
class Shape:
	area=0
	def ar(self):
		print(self.area)
class Square(Shape):
	def __init__(self,lengh):
		
		self.lengh=lengh
		self.area=pow(lengh,2)
a= Square(n)
a.ar()



