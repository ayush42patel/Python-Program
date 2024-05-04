import csv
print('''
|~~~~~~~~~~~~~~~~~MENU OF CSV~~~~~~~~~~~~~~~~~~~|
|                                               |
|               1.writing mode                  |
|               2.reading mode                  |
|               3.appending mode                |
|               4.correcting values             |
|               5.searching values              |
|                                               |
|~~~~~~~~~~~~~~~~~~~THE END~~~~~~~~~~~~~~~~~~~~~|''')
x=int(input('Enter 1-5:'))
if x==1:
    print('Writting in the csv file')
    f=open('Student.csv','w')
    m=csv.writer(f)
    g=int(input('how many students:'))
    m.writerow(['Rollno','Name','Class','Marks'])
    for i in range(0,g):
        print('Student record',(i+1))
        sch=int(input("Enter Scholar no:"))
        rol=int(input('Enter rollno:'))
        name=input("Enter Name:")
        cl=int(input("Enter class:"))
        mark=int(input("Enter marks:"))
        sturec=[sch,rol,name,cl,mark]
        m.writerow(sturec)
    f.close()
elif x==2:
    print('Reading the csv File')
    f=open('Student.csv','r',newline='\n')
    e=csv.reader(f)
    for i in e:
        print(i)
elif x==3:
    print('Appending  values in the csv file')
    f=open('student.csv','a',newline='\n')
    m=csv.writer(f)
    g=int(input('how many more students:'))
    for i in range(0,g):
        print('Student record',(i+1))
        sch=int(input("Enter Scholar no:"))
        rol=int(input('Enter rollno:'))
        name=input("Enter Name:")
        cl=int(input("Enter class:"))
        mark=int(input("Enter marks:"))
        sturec=[sch,rol,name,cl,mark]
        m.writerow(sturec)
    f.close()
    f=open('Student.csv','r',newline='\n')
    e=csv.reader(f)
    for i in e:
        print(i)
elif x==4:
    print("Correcting values in the csv File")
    f=open('Student.csv','r',newline='\n')
    e=csv.reader(f)