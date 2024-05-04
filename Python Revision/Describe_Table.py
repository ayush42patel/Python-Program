import mysql.connector as a
import Display_mysql as h
mydb=a.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="graduation"
)
m=mydb.cursor()
s2="DESCRIBE college;"
m.execute(s2)

print("Table Description:\n")
print("|Field|Type|Null|Key|Default|Extra|")
desc=m.fetchall()
for de in desc:
    print(de)

m.close()
mydb.close()