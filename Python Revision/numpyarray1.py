import numpy as np
ar=np.array([1,2,3,4,5,6])# 1 d
r=np.array([[1,2,3],[4,5,6]]) #2 d
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
e=np.array([1,2,3,4],ndmin=5)

print(e)
print(ar)
print(r)
print(d.ndim) # No of Dimensions 
print(type(ar))
print(type(r))