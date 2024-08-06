r=int(input("Enter row:"))
c=int(input("Enter column:"))
for i in range(0,r):
    for j in range(r,i,-1):
        print(j,end=" ")
    print("\n")