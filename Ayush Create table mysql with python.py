import mysql.connector as c
mydb =c.connect(
    host = "localhost",
    user = "root",
    password = "ayushpatel",
    database='abc')
g=mydb.cursor()
sql='''CREATE TABLE r_c_12
       (Sno integer NOT NULL,
        Schono integer PRIMARY KEY NOT NULL,
        Name char(50) NOT NULL,
        Class integer NOT NULL,
        Sec char(20) NOT NULL,
        Gender char(20) NOT NULL,
        Boardrollno integer NOT NULL,
        Center_No integer NOT NULL,
        School_No integer NOT NULL,
        DOB DATE NOT NULL,
        Father_Name char(100) NOT NULL,
        Mother_No char(100) NOT NULL,
        Mob_No integer NOT NULL,
        Stream char(100) NOT NULL,
        English int NOT NULL,
        Physics/Accounts/History int NOT NULL,
        Scholarship char(10) NOT NULL,
        Only_Child char(10) NOT NULL,
        Minority char(10) NOT NULL,
        Percentage integer NOT NULL);'''
g.execute(sql)
mydb.commit()
mydb.close()
