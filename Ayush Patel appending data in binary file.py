import pickle
stu={}
print("-----------------MENU---------------")
print('''1.Rollno.
2.Name.
3.Address.
4.Class.
5.Section.
6.Marks.''')
print('---------------THE END--------------')
f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","ab")
x=int(input("How many students?"))
for i in range(0,x):
    rno=int(input("Enter rno:"))
    name=input('Enter name:')
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
    pickle.dump(stu,f)
f.close()
emp={}
f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","rb")
try:
    while True:
        emp=pickle.load(f)
        print(emp)
except EOFError:
    f.close()
