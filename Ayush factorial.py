import time
print("Start Execution : ",end="")
print(time.ctime())
num=int(input("Enter a no:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    print("The factorial of",i,"is:",fact)
print("The factorial of",num,"is:",fact)
print("Stop Execution : ",end="")
print(time.ctime())
