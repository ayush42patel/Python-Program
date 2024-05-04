import time
print("Start Execution : ",end="")
print(time.ctime())
import pickle as p
print("-----------------MENU---------------")
print('''1.Rollno.
2.Name.
3.Address.
4.Class.
5.Section.
6.Marks.''')
print('---------------THE END--------------')
n=input("Enter what you want to search?:")
m=input("Enter the preffered:")
e=input("Enter value you want to correct:")
stu={}
found=False
f=open(r"C://Users/Lenovo/Desktop/Abc.dat",'rb+')
try:
    while True:
        r=f.tell()
        stu=p.load(f)
        if n=="Marks" or n=="Rollno" or n=="Class":
            if stu[n]==m:
                stu[n]=e
                f.seek(r)
                p.dump(stu,f)
                print(stu)
                found=True
        else:
            if stu[n]==m:
                stu[n]=e
                f.seek(r)
                p.dump(stu,f)
                print(stu)
                found=True
except EOFError:
    if found==False:
        print("No record")
    else:
        print("success")
f.close()
print("Stop Execution : ",end="")
print(time.ctime())
