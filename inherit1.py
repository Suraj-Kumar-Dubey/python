class Shape:
	def __init__(self):
		print "Shape"
	l=5
	b=6
class Rectangle(Shape):
	print l
	print b
	def __init__(self,l,b):
		self.l=l
		self.b=b
		self.__c = self.l+self.b

obj1=Rectangle(1,2)
print obj1._Rectangle__c
