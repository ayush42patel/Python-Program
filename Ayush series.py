import time
print("Start Execution : ",end="")
print(time.ctime())
n=int(input("Enter a no:"))
for i in range(0,n+1):
    h=(n)*(n+1)*(2*n+1)
    d=h//6
print("The sum of square of no till",n,"is:",d)
print("Stop Execution : ",end="")
print(time.ctime())
