def Exist(f):
    import os
    if not os.path.exists(f):
        return False
    else:
        return True
    
def writing():
    f=open("D:/File Handling files/First.text","w+")
    n=int(input("Enter how many Lines to input:"))
    for i in range(0,n):
        l=str(input(f"Enter Line {i+1}:"))
        f.write(l+"\n")
    print("Content in file:-\n")
    f.seek(0)
    print(f.read())          
    f.close()

def reading():
    f1=open("D:/File Handling files/First.text","r")
    print("Contents of file:-\n")
    f1.seek(0)
    print(f1.read())
    f1.close()

def Appending():
    f=open("D:/File Handling files/First.text","a+")
    print("Appending in file:=\n")
    no=int(input("Enter no of lines to append:"))
    for i in range(0,no):
        h=str(input(f"Enter Line {i+1}:"))
        f.write(h+"\n")
    f.seek(0)
    print("Content appended to file:-")
    print(f.read())

def Modifying():
    f=open("D:/File Handling files/First.text","r+")
    print("Modifying in the file:=\n")
    o=str(input("Enter old string to change:"))
    k=str(input("Enter new string to replace:"))
    g=f.read()
    if(o in g):
        u=g.replace(o,k)
        f.write(u)
        f.seek(0)
        print(f.read())
    else:
        print("String not found Error!!")

def Searching():
    f=open("D:/File Handling files/First.text","r+")
    print("Searching in the file:=\n")
    o=str(input("Enter string to search:"))
    g=f.read()
    if(o in g):
        print(o,"Found in the file")
    else:
        print(o,"not found in the file")

def Deleting_Line():
    f=open("D:/File Handling files/First.text","r+")
    print("Deleting Line:=\n")
    t=f.readlines()
    g=int(input("Enter Line to delete:"))
    if g<1 or g>len(t):
        print("Error!!")
    else:
        del t[g-1]
        f.seek(0)
        f.writelines(t)
        print("Line Deleted")
        print("Updated File")
        print(f.read())
    f.close()

def Deleting_File():
    import os
    print("Deleting File:=\n")
    f_name="D:/File Handling files/First.text"
    if(os.path.exists(f_name)):
        os.remove(f_name)
        print("File Deleted!")
    else:
        print("File does not exist.\n")

while True:
    f_name="D:/File Handling files/First.text"
    s=Exist(f_name)
    print("1.Writing\n2.Reading\n3.Appending\n4.Modifying\n5.Searching\n6.Deleting Line\n7.Deleting File\n8.Exit")
    g=int(input("Enter Choice:"))
    if(g==1):
        writing()
    elif(g==2):
        if(s==True):
            reading()
        else:
            print("Invalid File Does not exist\n")
        continue
    elif(g==3):
        if(s==True):
            Appending()
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==4):
        if(s==True):
            Modifying()
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==5):
        if(s==True):
            Searching()
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==6):
        if(s==True):
            Deleting_Line()
        else:
            print("Invalid file does not exist\n")
        continue
    elif(g==7):
        Deleting_File()
    elif(g==8):
        exit(0)
    else:
        print("Invalid Choice")
        continue