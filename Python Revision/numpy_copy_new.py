import numpy as np
w=eval(input("Enter the list:"))
a=np.array(w)
x=a.view()
a[0]=7

print(a)
print(x)