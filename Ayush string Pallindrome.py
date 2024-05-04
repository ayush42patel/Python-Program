import time
print("Start Execution : ",end="")
print(time.ctime())
s=input("Enter a value:")
l=len(s)
rev=-1
for a in range(l):
    if s[a]==s[rev]:
        a+=1
        rev-=1
    else:
        print(s,"is not a pallindrome")
        break
else:
    print(s,"is a pallindrome")
print("Stop Execution : ",end="")
print(time.ctime())
