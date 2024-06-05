a=int(input("Enter age of ram:"))
b=int(input("Enter age of Shyam:"))
c=int(input("Enter age of Ajay:"))
lst=[a,b,c]
m=min(lst)
if(m==a):
    print("Ram is the youngest")
elif(m==b):
    print("Shyam is the youngest")
else:
    print("Ajay is the youngest")