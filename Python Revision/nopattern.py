r=int(input("Enter row:"))
c=int(input("Enter column:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")