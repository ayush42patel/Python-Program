import time
print("Start Execution : ",end="")
print(time.ctime())
num=int(input("Enter num:"))
wnum=num
rev=0
while wnum>0:
    dig=wnum%10
    rev=rev*10+dig
    wnum=wnum//10
if num==rev:
    print(num,"is a Pallindrome")
else:
    print(num,"is not a Pallindrome")
print("Stop Execution : ",end="")
print(time.ctime())
