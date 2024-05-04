import pickle as p
def Exist(f):
    import os
    if not os.path.exists(f):
        return False
    else:
        return True
    
def writing(f):
    f=open("D:/File Handling Files/Binary.dat","wb")
    d=int(input("Enter no of lines:"))
    for i in range(0,d):
        e=input(f"Enter Line {i+1}:")
        p.dump(e,f)
    f.close()

    f=open("D:/File Handling Files/Binary.dat","rb")
    print("~~~~~~~~~~~~~~Content in file~~~~~~~~~~~~~~~\n")
    try:
        while True:
            r=p.load(f)
            print(r)
    except EOFError:
        f.close()

def reading(f):
    f=open("D:/File Handling Files/Binary.dat","rb")
    print("~~~~~~~~~~~~~~Content in file~~~~~~~~~~~~~~~\n")
    f.seek(0)
    try:
        while True:
            r=p.load(f)
            print(r)
    except EOFError:
        f.close()

def Appending(f):
    f=open("D:/File Handling files/Binary.dat","ab+")
    print("~~~~~~~~~~~~~Appending in file~~~~~~~~~~~~~~\n")
    no=int(input("Enter no of lines to append:"))
    for i in range(0,no):
        e=input(f"Enter Line {i+1}:")
        p.dump(e,f)
    f.seek(0)
    try:
        while True:
            r=p.load(f)
            print(r)
    except EOFError:
        f.close()

def Modifying(f):
    old=str(input("Enter old string:"))
    new=str(input("Enter new string:"))
    f=open("D://File Handling files/Binary.dat","rb+")
    m=False
    try:
        while True:
            pos = f.tell()
            r = p.load(f)
            if old in r:
                r = r.replace(old,new)
                f.seek(pos)
                p.dump(r, f)
                m=True
    except EOFError:
        pass
    finally:
        f.close()
    if(m==False):
        print("String do not exist so file cannot be modified.\n")
    
    f1=open("D://File Handling files/Binary.dat","rb")
    print("~~~~~~~~~~~~~~Content in file~~~~~~~~~~~~~~~\n")
    f1.seek(0)
    try:
        while True:
            r=p.load(f1)
            print(r)
    except EOFError:
        f1.close()

def Searching(f):
    f=open("D:/File Handling files/Binary.dat","rb+")
    print("~~~~~~~~~~~Searching in the file~~~~~~~~~~~~\n")
    fo=False
    f.seek(0)
    key=str(input("Enter string to search:"))
    try:
        while True:
            r=p.load(f)
            if(key in r):
                print("The ",key," found in the file")
                fo=True
    except EOFError:
        f.close()
    if(fo!=True):
        print("String ",key," not found in file")

def Deleting_Line(f,t):
    import os
    try:
        temp_f = f + ".tmp"
        with open(f, "rb") as input_f, open(temp_f, "wb") as output_f:
            try:
                cl = 1
                while True:
                    if cl != t:
                        en = p.load(input_f)
                        p.dump(en, output_f)
                    else:
                        p.load(input_f)
                    cl += 1
            except EOFError:
                pass
        
        os.remove(f)
        os.rename(temp_f, f)

        with open(f, "rb") as f1:
            print("~~~~~~~~~~~~~~Content in file~~~~~~~~~~~~~~~\n")
            f1.seek(0)
            try:
                while True:
                    r = p.load(f1)
                    print(r)
            except EOFError:
                pass
            
    except Exception as e:
        print(f"An error occurred: {e}")

def Deleting_File(f):
    import os
    if os.path.exists(f):
        os.remove(f)
        print("File deleted.")
    else:
        print("File does not exist.")

while True:
    f_name="D:/File Handling files/Binary.dat"
    s=Exist(f_name)
    print("\n1.Writing\n2.Reading\n3.Appending\n4.Modifying\n5.Searching\n6.Deleting Line\n7.Deleting File\n8.Exit")
    ch=int(input("Enter choice:"))
    if(ch==1):
        writing(f_name)
    elif(ch==2):
        if(s==True):
            reading(f_name)
        else:
            print("Invalid File Does not exist\n")
        continue
    elif(ch==3):
        if(s==True):
            Appending(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(ch==4):
        if(s==True):
            Modifying(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(ch==5):
        if(s==True):
            Searching(f_name)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(ch==6):
        if(s==True):
            t=int(input("Enter Line no:"))
            Deleting_Line(f_name,t)
        else:
            print("Invalid file does not exist\n")
        continue
    elif(ch==7):
        Deleting_File(f_name)
    elif(ch==8):
        exit(0)
    else:
        print("Invalid Choice")
        continue
