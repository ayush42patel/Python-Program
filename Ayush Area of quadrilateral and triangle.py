import time
print("Start Execution : ",end="")
print(time.ctime())
import math
print("-------------------MENU------------------------------")
print('''if x==1,Triangle
if x==2 then,
         1.Square/Rhombus
         2.Rectangle/Parallelogram
         3.Kite
         4.Any Quadrilateral''')
print("----------------------THE END------------------------")
x=int(input("Enter 1or2:"))
if x==1:
    w=int(input("enter 1or2:"))
    if w==1:
        side1=int(input("Enter side1:"))
        side2=int(input("Enter side2:"))
        side3=int(input("Enter side3:"))
        s=(side1+side2+side3)/2
        k=(s*(s-side1)*(s-side2)*(s-side3))
        Area=math.sqrt(k)
        print("Area of triangle by Heron's formula is:",Area)
    elif w==2:
        h=int(input("Enter height:"))
        p=int(input("Enter perpendicular:"))
        b=int(input("Enter base:"))
        Area=1/2*h*b
        "h**2"=="p**2"+"b**2"
        print("Area of Triangle by general method is:",Area)
elif x==2:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    c=int(input("Enter c:"))
    d=int(input("Enter d:"))
    if a==b==c==d:
        Area=a**2
        p=a+b+c+d
        l=int(input("Enter angle between them :"))
        if l==90:
            print("The Area of square:",Area)
            print("The Perimeter of square:",p)
        else:
            d1=int(input("Enter diagonal 1:"))
            d2=int(input("Enter diagonal 2:"))
            area=1/2*d1*d2
            print("Perimeter of rhombus:",p)
            print("Area of Rhombus:",area)
    elif a==c and b==d:
        h=int(input("Enter height:"))
        Area=h*b
        p=a+b+c+d
        l=int(input("Enter angle between them :"))
        if l!=90:
            print("The Area of Parellelogram:",Area)
            print("The Perimeter of Parallelogram:",p)
        else:
            print("The Area of Rectangle:",Area)
            print("The Perimeter of Rectangle:",p)
    elif a==b and c==d or a==d and b==c:
        d1=int(input("Enter diagonal 1:"))
        d2=int(input("Enter diagonal 2:"))
        area=(d1*d2)*2
        p=(2*a)+(2*c)
        print("The Area of kite:",area)
        print("The Perimeter of kite:",p)
    elif a!=b!=c!=d:
        d1=int(input("Enter diagonal 1:"))
        d2=int(input("Enter diagonal 2:"))
        h1=int(input("The perpendicular length drawn from vertices1:"))
        h2=int(input("The perpendicular length drawn from vertices2:"))
        area=1/2*(d1*(h1+h2))
        p=(a*b)+(b*c)+(c*d)+(d*a)
        print("The Area of quadrilateral is:",area)
        print("The Perimeter of quadrilateral is:",p)
print("Stop Execution : ",end="")
print(time.ctime())
