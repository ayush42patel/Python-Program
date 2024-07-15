print('''
|~~~~~~~~~~~~~~~~~~~~~~~MENU OF BINARY FILES~~~~~~~~~~~~~~~~~~~~~~~~|
|                                                                   |
|                 1.Writing and Reading binary files.               |
|                 2.Correcting values in binary files.              |
|                 3.Searching values in binary files.               |
|                 4.Appending data in binary files.                 |
|                                                                   |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THE END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
''')
x=int(input("Enter 1-4:"))
if x==1:
    import pickle as p
    print('''Writing and Reading binary files.
             1. Write
             2. Read''')
    a=int(input('Enter 1 or 2:'))
    if a==1:
        stu={}
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
        f.close()
    elif a==2:
        emp={}
        f=open(r"C:\\Users\Lenovo\Desktop\ABC.dat","rb")
        try:
            while True:
                emp=p.load(f)
                print(emp)
        except EOFError:
            f.close()
elif x==2:
    import pickle as p
    print('Correcting values in binary files.')
    print('''
    |-----------------MENU---------------|
    |             1.Rollno.              |
    |             2.Name.                |
    |             3.Address.             |
    |             4.Class.               |
    |             5.Section.             |
    |             6.Marks.               |
    |---------------THE END--------------|
    ''')
    n=input("Enter what you want to correct:")
    m=input("Enter the previous value:")
    e=input("Enter correct value:")
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
elif x==3:
    import pickle
    print('Searching values in binary files.')
    print('''
    |-----------------MENU---------------|
    |              1.Rollno.             |
    |              2.Name.               |
    |              3.Address.            |
    |              4.Class.              |
    |              5.Section.            |
    |              6.Marks.              |
    |---------------THE END--------------|
    ''')
    n=input("Enter what you want to search?:")
    m=input("Enter the value:")
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
elif x==4:
    import pickle
    print('Appending values in binary files.')
    stu={}
    print('''
    |-----------------MENU---------------|
    |              1.Rollno.             |
    |              2.Name.               |
    |              3.Address.            |
    |              4.Class.              |
    |              5.Section.            |
    |              6.Marks.              |
    |---------------THE END--------------|
    ''')
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
    x=x+1