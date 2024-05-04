def Push(h):
    h.append(Book[i])
Book=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
l=len(Book)
h=[]
top=None
while True:
    print('''Stack Operation
    1.Push
    2.End Program''')
    g=int(input("Enter 1/2:"))
    if g==1:
        for i in range(0,l):
            if Book[i]%2==0:
                Push(h)
        print(h)
    elif g==2:
        break
    else:
        print("Invalid choice.......")
