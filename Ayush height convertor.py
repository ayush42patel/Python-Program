n=int(input("Enter a 1,2 or 3:"))
if n==1:
    h=float(input("Enter a height:"))
    d=h*12
    print("The height in inches is:",d)
    r=d*2.54
    print("The height in centimeter is:",r) 
elif n==2:
    x=float(input("Enter a height:"))
    e=x/2.54
    print("The height in inches is:",e)
    f=e/12
    print("The height in foot:",f)
elif n==3:
    r=float(input("Enter a height:"))
    a=r/12
    print("The height in foot:",a)
    s=r*2.54
    print("The height in centimeter is:",s)
