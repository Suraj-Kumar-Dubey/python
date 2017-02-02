inp1 = int(raw_input("enter first value"))
inp2 = int(raw_input("enter second value"))
inp3 = raw_input("enter the operation")
if inp3 == '+' :
	add = inp1 + inp2
	print add
elif inp3 == '-' :
	sub = inp1 - inp2
	print sub
elif inp3 == '*' :
	mul = (inp1 * inp2)
	print mul
else :
	div = inp1 / inp2
	print div
