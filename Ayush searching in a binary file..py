import time
print("Start Execution : ",end="")
print(time.ctime())
import pickle
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
stu={}
found=False
print("Searching in file")
f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","rb")
try:
    while True:
        stu=pickle.load(f)
        if n =="Rollno" or n=="Marks" or n=='Class':
            g=int(m)
            if stu[n]==g:
                print(stu)
                found=True
        else:
            if stu[n]==m:
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
