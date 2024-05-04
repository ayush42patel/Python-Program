import random
a=int(input("Enter a no from where(a):"))
b=int(input("Enter no till where(b):"))
g=random.randint(a,b)
f=int(input("You want how many chances:"))
for i in range(0,f):
    i=int(input("Enter a no (a,b):"))
    if g==i:
         print("YOU ARE VERY LUCKY:) ,The no is:",i)
         break
else:
         print("YOU ARE NOT LUCKY:( ,The no is:",g)

