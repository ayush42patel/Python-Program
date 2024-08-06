r=int(input("Enter rows:"))
c=int(input("Enter columns:"))
for i in range(r,0,-1):
    for j in range(r-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print("\n")