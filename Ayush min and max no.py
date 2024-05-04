import time
print("Start Execution : ",end="")
print(time.ctime())
max=0
min=0
a=int(input("Enter a how many no(a):"))
for i in range(0,a):
    f=int(input("Enter value of f:"))
    if min>f:
        min=f
for i in range(0,a):
    g=int(input("Enter value of g:"))
    if max<g:
        max=g
print("The Largest no is:",max)
print("The Smallest no is:",min)
print("Stop Execution : ",end="")
print(time.ctime())
