import MySQLdb as m
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
print data
for row in data:
	print row['name']
	
