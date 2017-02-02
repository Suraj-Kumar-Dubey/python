rng = input("enter the range")
list = []
for i in range(rng) :
	x = input("enter the number")
	list.append(x)
print list
list.sort()
print list
print list[-2]
