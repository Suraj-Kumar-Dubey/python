import MySQLdb as m
import sys
import smtplib
import getpass
host='localhost'
username='root'
password='infoblox'
database='ASM'
db_con=m.connect(host,username,password,database)
#db_cur=db_con.cursor()
db_cur=db_con.cursor(m.cursors.DictCursor)
sql="select * from Ankit"
db_cur.execute(sql)
data=db_cur.fetchall()


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
data=sys.argv[2]
message="subject: %s\n\n %s" %(data,mes)
server.sendmail(username,to,message)

