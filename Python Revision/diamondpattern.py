r=int(input("Enter row:"))
c=int(input("Enter column:"))
for i in range(1,r+1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print("\n")
for i in range(r-1,0,-1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print("\n")
