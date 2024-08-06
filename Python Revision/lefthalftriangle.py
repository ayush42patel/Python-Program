r=int(input("Enter row:"))
c=int(input("Enter column:"))
for i in range(1,r+1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
for i in range(1,r+1):
    for j in range(r,i,-1):
        print("*",end=" ")
    print("\n")