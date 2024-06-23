import matplotlib.pyplot as mp
import numpy as np
a=eval(input("Enter x coordinate:"))
b=eval(input("Enter Label:"))
my=eval(input("Enter explode:"))

x=np.array(a)
mp.pie(x,labels=b,explode=my,startangle=0)
mp.show()