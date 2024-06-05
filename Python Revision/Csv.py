import csv 
import os
def exist(f):
    if not os.path.exists(f):
        return False
    else:
        return True

def writing(f):
    f=open("D:/File Handling Files/Marks.csv","w")
    writer = csv.writer(f)
    n = int(input('How many students: '))
    writer.writerow(['Rollno', 'Name', 'Course', 'Semester', 'Math', 'English', 'Science', 'SST', 'Comp', 'Hindi'])
    for i in range(n):
        print(f"Student record {i+1}")
        Rollno=int(input("Enter Rollno:"))
        Name=str(input("Enter Name:"))
        course=str(input("Enter Course:"))
        semester=int(input("Enter Semester:"))
        math=int(input("Enter Math Marks:"))
        english=int(input("Enter English marks:"))
        science = int(input('Enter Science marks: '))
        sst = int(input('Enter SST marks: '))
        comp = int(input('Enter Comp marks: '))
        hindi = int(input('Enter Hindi marks: '))
        writer.writerow([Rollno, Name, course, semester, math, english, science, sst, comp, hindi])
    f.close()
    print("data added to csv")
        
def reading(f):
    f=open("D:/File Handling Files/Marks.csv","r")
    

def appending(f):
    print()

def modifying(f):
    print()

def searching(f):
    print()

def deleting_Line(f):
    print()

def deleting_file(f):
    print()

while True:
    f_name="D:/File Handling files/Marks.csv"
    s=exist(f_name)
    print("1.Writing\n2.Reading\n3.Appending\n4.Modifying\n5.Searching\n6.Deleting Line\n7.Deleting File\n8.Exit")
    g=int(input("Enter Choice:"))
    if(g==1):
        writing(f_name)
    elif(g==2):
        if(s==True):
            reading(f_name)
        else:
            print("Invalid File Does not exist\n")
        continue
    elif(g==3):
        if(s==True):
            appending(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==4):
        if(s==True):
            modifying(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==5):
        if(s==True):
            searching(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==6):
        if(s==True):
            deleting_Line(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==7):
        deleting_file(f_name)
    elif(g==8):
        exit(0)
    else:
        print("Invalid Choice")
        continue