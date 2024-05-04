import time
print("Start Execution : ",end="")
print(time.ctime())
s=0
l=eval(input("Enter a list1:"))
m=eval(input("Enter a list2:"))
n=[]
for x in range(len(l)):
    s=l[x]+m[x]
    n.append(s)
print(n)
print("Stop Execution : ",end="")
print(time.ctime())
