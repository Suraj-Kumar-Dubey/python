import re
inp = raw_input("Enter the Input String")
#op = ('\w',inp)
op1=re.findall('\d+\w+',inp)
print op1
