def Push(s):
    n=input("Enter Student Name:")
    s.append(n)
def Pop(s):
    if s==[]:
        print("Stack is Empty.....")
    else:
        j=s.pop()
        print("The item popped is:",j)
        top=len(s)-1
s=['a','b']
top=None
while True:
    print('''Stack Operation
    1.Push
    2.Pop
    3.End Program''')
    g=int(input("Enter 1/2/3:"))
    if g==1:
        Push(s)
        print(s)
    elif g==2:
        item=Pop(s)
        print(s)
    elif g==3:
        break
    else:
        print("Invalid choice.......")
