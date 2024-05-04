import time
print("Start Execution : ",end="")
print(time.ctime())
n=int(input("Enter rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        p=i*j
        if p<10:
            print(" ",p," ",end=" ")
        else:
            print(p," ",end=" ")
    print()
print("Stop Execution : ",end="")
print(time.ctime())
