import mysql.connector as c
mydb =c.connect(
    host = "localhost",
    user = "root",
    password = "ayushpatel",
    database='abc')
g=mydb.cursor()
sq='''INSERT INTO statinary(I_code,I_Name,Qty,Price) VALUES('2','Pen','2500','12500');'''
g.execute(sq)
mydb.commit()
mydb.close()
