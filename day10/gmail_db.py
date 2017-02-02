mport MySQLdb as m
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
if input==exit:
	db_cur.execute("exit")
elif re.search(create,input):
	if re.search(database,input):
		db_cur.execute(input)
	else:
		b_cur.execute(input)
elif input==select:
	b_cur.execute(input)

sql="select * from Emp_Data"
db_cur.execute(sql)
data=db_cur.fetchall()
data1=str(data)
