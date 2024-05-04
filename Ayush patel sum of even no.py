import time
print("Start Execution : ",end="")
print(time.ctime())
s=0
d=0
f=0
a=int(input("Enter a no:"))
for i in range(0,a+1,2):
    s=s+i
print("Sum of",a,"even no is:",s)
for k in range(1,a+1,2):
    d=d+k
print("Sum of",a,"odd no is:",d)
for j in range(0,a+1):
    f=f+j
print("Sum of",a,"natural no is:",f)
print("Stop Execution : ",end="")
print(time.ctime())
