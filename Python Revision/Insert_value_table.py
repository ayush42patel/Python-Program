import mysql.connector as a
mydb=a.connect(
    host="localhost",
    user="root",
    password="ayush",
    database="graduation"
)
m=mydb.cursor()
sq="INSERT INTO college (Sno, Univ_Roll_No, NAME, Course, Branch, Semester) VALUES (%s, %s, %s, %s, %s, %s)"

n=int(input("Enter no of students:"))
def data():
    sno = int(input("Enter Sno: "))
    roll_no = int(input("Enter Univ Roll No: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    branch = input("Enter Branch: ")
    sem = int(input("Enter Semester: "))
    return (sno,roll_no,name,course,branch,sem)
while True:
    s_data=data()
    m.execute(sq,s_data)
    h=str(input("Want more input:"))
    if(h.lower()!="yes"):
        break
mydb.commit()
print("Values inserted successfully.")

m.close()
mydb.close()