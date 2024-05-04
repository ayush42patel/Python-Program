import time
print("Start Execution : ",end="")
print(time.ctime())
j=int(input("Enter 1 or 2:"))
degree=u"\N{DEGREE SIGN}"
import math
if j==1:
    n=int(input("Enter a no:"))
    pie=22/7
    r=(180/pie)*n
    print("The value in radian is:",r)
elif j==2:
    e=float(input("Enter a no:"))
    pie=22/7
    t=(pie/180)*e
    print("The value in degree is:",t,degree)
else:
    print("error")
print("Stop Execution : ",end="")
print(time.ctime())
