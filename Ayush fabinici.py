import time
print("Start Execution : ",end="")
print(time.ctime())
a=int(input("Enter the terms:"))
f=0
s=1
if a<=0:
    print("The requested series is",f)
else:
    print(f,",",s)
    for x in range(2,a):
        next=f+s                           
        print(f,"+",s,"=",next)
        f=s
        s=next
print("Stop Execution : ",end="")
print(time.ctime())
