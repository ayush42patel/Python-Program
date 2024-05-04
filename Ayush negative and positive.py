import time
print("Start Execution : ",end="")
print(time.ctime())
n=int(input("Enter a no:"))
if n>0:
    print("The no is positive:",n)
elif n<0:
    print("The no is negative:",n)
elif n==0:
    print("The no is:",n)
print("Stop Execution : ",end="")
print(time.ctime())
