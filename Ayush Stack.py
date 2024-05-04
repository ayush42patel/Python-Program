def Push(Book):
    name=input("Enter:")
    Book.append(name)
def Pop(Book):
    if Book==[]:
        print("Stack is Empty....")
    else:
        j=Book.pop()
        print("The item popped is:",j)
        top=len(Book)-1
def Display(Book):
    if Book==[]:
        print("Stack is Empty....")
    else:
        top=len(Book)-1
        print(Book[top],'<-top')
        for i in range(top-1,-1,-1):
            print(Book[i])
Book=[]
top=None
while True:
    print('''Stack Operation
    1.Push
    2.Pop
    3.Display
    4.End Program''')
    g=int(input("Enter 1/2/3/4:"))
    if g==1:
        Push(Book)
    elif g==2:
        item=Pop(Book)
    elif g==3:
        Display(Book)
    elif g==4:
        break
    else:
        print("Invalid choice.......")
