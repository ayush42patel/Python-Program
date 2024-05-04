import time
print("Start Execution : ",end="")
print(time.ctime())
import csv
f=open(r"C:\\Users\Lenovo\Desktop\student.csv",'w')
k=int(input("Enter till where/how many times:"))
stuwriter=csv.writer(f)
stuwriter.writerow(['Rollno','Name','Class','Math','Physics','Computer','Chemistry','English'])
for i in range(k):
    print("Student record",(i+1))
    Rollno=int(input("Enter rollno:"))
    Name=input("Enter name:")
    Class=int(input("Enter class:"))
    Math=int(input("Enter Math marks:"))
    Phy=int(input("Enter Physics marks:"))
    Comp=int(input("Enter Computer marks:"))
    Chem=int(input("Enter Chemisry marks:"))
    Eng=int(input("Enter English marks:"))
    sturec=[Rollno,Name,Class,Math,Phy,Comp,Chem,Eng]
    stuwriter.writerow(sturec)
f.close()
f=open(r"C:\\Users\Lenovo\Desktop\student.csv",'r',newline='\n')
d=csv.reader(f)
for j in d:
    print(j)
f.close()
print("Start Execution : ",end="")
print(time.ctime())
