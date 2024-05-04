import time
print("Start Execution : ",end="")
print(time.ctime())
min=0
max=0
a=int(input("Enter value of a:"))
for i in range(0,a):
    list=eval(input("Enter a no:"))
    if max<list[i]:
        max=list[i]
for i in range(0,a):
    if min>list[i]:
        min=list[i]
print("The max no is:",max)
print("The min no is:",min)  
print("Stop Execution : ",end="")
print(time.ctime())
