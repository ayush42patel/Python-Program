import time
print("Start Execution : ",end="")
print(time.ctime())
e=int(input("Enter a no:"))
if e==1:
    s=0
    x=int(input("Enter a no:"))
    n=int(input("Enter till which power:"))
    for i in range(0,n+1):
        f=(x**n)/n
        s=s+f
        print("The sum of",i,"no are:",s)
elif e==2:
    s=0
    n=int(input("Enter till which power:"))
    x=int(input("Enter a no:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    l=fact
    for j in range(0,n+1):
        f=(x**n)/l
        s=s+f
        print("The sum of",j,"no are:",s)
else:
    print("end")
print("Stop Execution : ",end="")
print(time.ctime())
