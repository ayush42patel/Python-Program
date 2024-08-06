r=int(input("Enter rows:"))
nu=1
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print(nu,end=" ")
#         nu=nu+1
#     print("\n")

for i in range(1,r+1):
    for j in range(r,i,-1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(nu,end=" ")
        nu=nu+1
    print("\n")