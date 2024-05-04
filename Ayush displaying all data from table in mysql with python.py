import mysql.connector as c
mydb =c.connect(
    host = "localhost",
    user = "root",
    password = "ayushpatel",
    database='abc')
print(mydb)
'''g=mydb.cursor()
sq=DESCRIBE STUDENT;
A=g.execute(sq)
print(A)
for i in r:
    print(i)
    print('\n')'''

