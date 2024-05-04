import time
print("Start Execution : ",end="")
print(time.ctime())
import pickle as p
'''stu={}
f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","wb")
j=int(input("Enter how many times:"))
for x in range(0,j):
    rno=int(input("Enter rno:"))
    name=input("Enter Name:")
    add=input("Enter address:")
    cl=int(input("Enter class:"))
    sec=input("Enter section:")
    Marks=(input("Enter a no:"))
    stu['Rollno']=rno
    stu['Name']=name
    stu['Address']=add
    stu['Class']=cl
    stu['Section']=sec
    stu['Marks']=Marks
    p.dump(stu,f)
f.close()'''
emp={}
f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","rb")
try:
    while True:
        emp=p.load(f)
        print(emp)
except EOFError:
    f.close()
print("Stop Execution : ",end="")
print(time.ctime())
