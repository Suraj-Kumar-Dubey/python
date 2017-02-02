class area_rec:
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def area(self):
		c=(self.a*self.b)
		d=2*self.a+2*self.b
		print c
		print d
	def __add__(self,other):
		return Area_rec(self.a+other.b,self.b+other.a)
#e = area_rec(10,20)
#e.area()
#ob1=area_rec(2,3)
#ob2=area_rec(4,5)
#print ob1+ob2
#print ob2.b
