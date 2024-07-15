num=int(input("Enter num:"))
w=num
rev=0
while w>0:
    dig=w%10
    rev=rev*10+dig
    w=w//10
if num==rev:
    print(num,"is a Pallindrome")
else:
    print(num,"is not a Pallindrome")