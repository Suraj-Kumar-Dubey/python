import MySQLdb as m
import sys
import smtplib
import getpass
host='localhost'
username='root'
password='ids123'
database='Employee'
db_con=m.connect(host,username,password,database)
#db_cur=db_con.cursor()
db_cur=db_con.cursor(m.cursors.DictCursor)
sql="select * from Emp_Data"
db_cur.execute(sql)
data=db_cur.fetchall()
data1=str(data)


host="smtp.gmail.com"
port=587
server=smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
username="surajdubey302.sd@gmail.com"
password=getpass.getpass()
server.login(username,password)
to=sys.argv[1]
table_name=sys.argv[2]
#message="subject: %s\n\n %s" %(table_name,data)
message="subject: {}\n\n {}".format(table_name,data1)
server.sendmail(username,to,message)
