r=int(input("Enter rows:"))
c=int(input("Enter Column:"))
for i in range(1,r+1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print("\n")