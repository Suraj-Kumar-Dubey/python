class Test:
	def __init__(self,a):
		self.a=a
		print "object created"
		print a
	def __str__(self):
		return str(self.a)
	def __del__(self):
		print "object removed"
	def sqr(self):
		return self.a**2
	def prime(self):
		#num = int(input("Enter the how many numbers you want to print"))
		print '2'
		count = 1
		for i in range(3,100):
    			flag = 1
    			for j in range(2,i):
        			if (i % j == 0):
            				flag = 0
    			if (flag == 1):
        			print i
        			count = count +1
    			if (self.a == count):
        			break
	def __add__(self,other):
		return self.a+other.a
	def __sub__(self,other):
		return self.a-other.a
	def __mul__(self,other):
		 return self.a*other.a
	def __init(self,a,b,c....)
a = Test(10)#creating 1st object
print a
print a.sqr()
print "10 prime numbers are"
a.prime()
b = Test(20)
print a+b
print a-b
print a*b
print c
#del a

