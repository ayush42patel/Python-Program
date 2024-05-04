import time
print("Start Execution : ",end="")
print(time.ctime())
x=int(input("Enter a no:"))
if x==1:
    p=int(input("Enter Printciple:"))
    r=int(input("Enter Rate:"))
    t=int(input("Enter time:"))
    s=r/100
    si=p*s*t
    print("The simple interest is:",si)
    A=p*(1+r*t)
    print("The Amount is:",A)
elif x==2:
    p=int(input("Enter Printciple:"))
    r=int(input("Enter Rate:"))
    t=int(input("Enter time:"))
    n=int(input("Enter no of times:"))
    for i in range(0,n):
        d=n*t
    c=(1+r/n)**d
    print("The compound interest is:",c)
    A=p*(1+r/n)*d
    print("The Amount is:",A)
print("Stop Execution : ",end="")
print(time.ctime())
