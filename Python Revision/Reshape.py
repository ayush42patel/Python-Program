import numpy as np
e=eval(input("Enter the list:"))
arr=np.array([e])
new=arr.reshape(2,3)
print(new)