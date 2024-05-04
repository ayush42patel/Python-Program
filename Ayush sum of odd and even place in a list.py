import time
print("Start Execution : ",end="")
print(time.ctime())
y=float(input("Enter a y:"))
x=eval(input("Enter a no:"))
length=len(x)
sum=0
A=0
if y==1:
    for i in range(0,length,2):
        sum+=x[i]
        print("The sum of no of",i,"th place is:",sum)
elif y==2:
    for k in range(1,length,2):
        A+=x[k]
        print("The sum of no of",k,"th place is:",A)
print("Stop Execution : ",end="")
print(time.ctime())
