import time
print("Start Execution : ",end="")
print(time.ctime())
a=int(input("Enter a no:"))
b=int(input("Enter till which:"))
if b>0:
    for i in range(0,b+1):
        s=a**i
        print("The",a,"to the power",i,"is:",s)
elif b<0:
    b=-b
    for i in range(0,b+1):
        s=a**i
        print("The",a,"to the power",i,"is:",s)
print("Stop Execution : ",end="")
print(time.ctime())
