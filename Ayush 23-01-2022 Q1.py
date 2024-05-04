def Push(l):
    n=int(input("Enter a no:"))
    l.append(n)
def Pop(l):
    if l==[]:
        print('Stack is Empty.....')
    else:
        j=l.pop()
        print("The item popped is:",j)
        top=len(l)-1
l=[]
top=None
while True:
    print('''Stack Operation
    1.Push
    2.Pop
    3.End Program''')
    g=int(input("Enter 1/2/3:"))
    if g==1:
        Push(l)
        print(l)
    elif g==2:
        item=Pop(l)
        print(l)
    elif g==3:
        break
    else:
        print("Invalid choice.......")
