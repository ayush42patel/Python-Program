def push(c):
    j=int(input("Enter a no:"))
    c.append(j)
def pop(c):
    if c==[]:
        print("Underflow")
    else:
        m=c.pop()
        print("The item popped is:",m)
def display(c):
    if c==[]:
        print("STACK IS EMPTY")
    else:
        top=len(c)-1
        print(c[top],"<==top")
        for i in range(top-1,-1,-1):
            print(c[i])
c=[]
top=None
while True:
    print('''Stack opertations
          1.Push
          2.Pop
          3.Display
          4.End Program''')
    h=int(input("Enter 1/2/3/4:"))
    if h==1:
        push(c)
        print(c)
    elif h==2:
        pop(c)
    elif h==3:
        display(c)
    elif h==4:
        break
    else:
        print("Invalid value entered")
