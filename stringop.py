import sys
import re
fr = 
#os.mkdir('ankit')
#list =[]
fr = open("fr",'r')
sent = fr.read()
list = sent.split("\n")
##print sent
for x in list:
	y=x.split(" ")
	try:
		print y[1]
	except:
		pass

#for i in 10:
fr.close()

