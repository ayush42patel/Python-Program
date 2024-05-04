s=0
a=eval(input("Enter a list:"))
for i in range(1,len(a)):
    a.sort()
    s+=a[i]
print(s)
