import mysql.connector as a
mydb=a.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="graduation"
)
m=mydb.cursor()
sql='''CREATE TABLE College
       (Sno integer NOT NULL,
        Univ_Roll_No integer PRIMARY KEY NOT NULL,
        NAME char(50) NOT NULL,
        Course char(30) NOT NULL,
        Branch char(30) NOT NULL,
        Semester integer NOT NULL);'''
m.execute(sql)
mydb.commit()
mydb.close()