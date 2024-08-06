r=int(input("Enter no of Rows:"))
c=int(input("Enter no of columns:"))
for i in range(0,r+1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print("\n")
