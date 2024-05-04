import mysql.connector as a
mydb=a.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="graduation"
)
m=mydb.cursor()
sql="SELECT * FROM college;"
m.execute(sql)

f=m.fetchall()
for de in f:
    print(de)
m.close()
mydb.close()