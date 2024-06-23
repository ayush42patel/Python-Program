import numpy as np
import matplotlib.pyplot as mp
a=eval(input("Enter X coordinate:"))
b=eval(input("Enter Y coordinate:"))

x=np.array(a)
y=np.array(b)

mp.bar(x,y)
mp.show()