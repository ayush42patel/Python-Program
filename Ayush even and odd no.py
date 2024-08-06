y=int(input("Enter 1/2:"))
x=int(input("Enter a no:"))
if y==1:
    for i in range(0,x,2):
        print("The Even no till are:",i)
elif y==2:
    for j in range(1,x+1,2):
        print("The Odd no till are:",j)
else:
    for l in range(0,x):
        print("The Natural no till are:",l)