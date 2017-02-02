import sys
import smtplib
import getpass
host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username="yadav.pankit9894@gmail.com"
password=getpass.getpass()
server.login(username,password)
to=sys.argv[1]
sub=sys.argv[2]
mes=sys.argv[3]
f= open(sub,'r')
f1=f.read()
message="subject: %s\n\n %s" %(f1,mes)
server.sendmail(username,to,message)

