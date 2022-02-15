class Account:
	
	def __init__(self,own,dep,wit):
		self.own = own
		self.dep = dep
		self.wit = wit
		self.bal = 0
	
	def deposit(self,d):
		self.bal +=self.dep
		self.bal +=d

	def withdraw(self, w):
		if self.bal > self.wit:
			self.bal -=self.wit
			self.bal -=w
		else:
			print('You cannot withdraw money!!!')
			
			



	def show(self):
		print( self.own,'your balance is:',self.bal)
 

		

a = Account('Student',500,600)
a.deposit(1340)
a.withdraw(124)

a.show()



