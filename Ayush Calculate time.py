import time
print("Start Execution : ",end="")
print(time.ctime())
t=int(input("Enter how many days:"))
d=t*24#hour
print("The Hour in",t,"days are:",d)
f=d*60#minutes
print("The minutes in",t,"days are:",f)
r=f*60#second
print("The seconds in",t,"days are:",r)
print("Stop Execution : ",end="")
print(time.ctime())
