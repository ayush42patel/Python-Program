import time
print("Start Execution : ",end="")
print(time.ctime())
min=max=0
sum=0
n=int(input("Enter from where :"))
k=int(input("Enter how many no(+ve):"))
for i in range(n,k):
    a=int(input("Enter a no(a):"))
    if max<a:
        max=a
    if min>a:
        min=a
    sum=sum+a
print("sum:",sum)
print("The greatest no is:",max)
print("The smallest no is:",min)
print("Stop Execution : ",end="")
print(time.ctime())
