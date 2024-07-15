a=int(input("Enter a no:"))
m=0
for k in range(2,a):
    if(a%k==0):
        m=m+1
        break
if(m==1):
    print("Factor Found ",a,"is not a prime no")
else:
    print(a,"is prime no")