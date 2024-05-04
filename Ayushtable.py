import time
s=time.time()
print("Start Execution : ",end="")
print(time.ctime())
a=int(input("Whose table you want:"))
b=int(input("Till which no you want the table:"))
for i in range(1,b+1):
    j=a*i
    print("The Table of",a,"*",i,"is:",j)
print("Total time:",s)
print("Stop Execution : ",end="")
print(time.ctime())
