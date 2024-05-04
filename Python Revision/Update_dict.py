e=eval(input("Enter Dictionary:"))
m=str(input("Enter String key to change:"))
h=int(input("Enter Key:"))
if(m in e):
    print("Updated Dict")
    e[m]=h
    print(e)
else:
    print("changed dict")
    e[m]=h
    print(e)