def multiply(matOne,matTwo,r,c):
    matThree = []
    for i in range(r):
        matThree.append([])
        for j in range(c):
            sum = 0
            for k in range(3):
                sum = sum + (matOne[i][k] * matTwo[k][j])
            matThree[i].append(sum)

    print("Multiplication Result of Two Given Matrix is:")
    for i in range(r):
        for j in range(c):
            print(matThree[i][j], end=" ")
        print()
def add(matOne,matTwo,r,c):
    matfour=[]
    for i in range(r):
        matfour.append([])
        for j in range(c):
            matfour[i].append(matOne[i][j]+matTwo[i][j])

    print("Addition of the two matrix:")
    for i in range(r):
        for j in range(c):
            print(matfour[i][j],end=" ")
        print()
            
r=int(input("Enter rows:"))
c=int(input("Enter column:"))
matOne = []
print("Enter Elements for First Matrix: ")
for i in range(r):
    matOne.append([])
    for j in range(c):
        num = int(input())
        matOne[i].append(num)

print("Matrix1=")
for i in range(r):
    for j in range(c):
        print(matOne[i][j],end=" ")
    print()

matTwo = []
print("Enter  Elements for Second Matrix: ")
for i in range(r):
    matTwo.append([])
    for j in range(c):
        num = int(input())
        matTwo[i].append(num)

print("Matrix 2=")
for i in range(r):
    for j in range(c):
        print(matTwo[i][j], end=" ")
    print()

ch=int(input("Enter choice:"))
if(ch==1):
    multiply(matOne,matTwo,r,c)
elif(ch==2):
    add(matOne,matTwo,r,c)
else:
    print("Invalid choice")
    exit(1)
