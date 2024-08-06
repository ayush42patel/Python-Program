def addition(a,b):
    s=a+b
    print("Sum:",s)

def subtraction(a,b):
        s=a-b
        print("Subtraction:",s)

def multiplication(a,b):
    s=a*b
    print("Multiplication:",s)

def division(a,b):
    s=a/b
    print("Division:",s)

def modulus(a,b):
    s=a//b
    print("Modulus:",s)

ch=int(input("Enter choice:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus\n")
a=int(input("Enter No 1:"))
b=int(input("Enter No 2:"))
if(ch==1):
    addition(a,b)
elif(ch==2):
    subtraction(a,b)
elif(ch==3):
    multiplication(a,b)
elif(ch==4):
    division(a,b)
elif(ch==5):
    modulus(a,b)
else:
    print("Invalid choice!")