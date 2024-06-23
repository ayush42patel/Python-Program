import matplotlib
import matplotlib.pyplot as p
import numpy as n

e=eval(input("Enter x coordinate:"))
h=eval(input("Enter y coordinate:"))
a=n.array(e)
b=n.array(h)

# matplotlib.pyplot.plot(a,b,"o-",ms=5,mec='black',mfc='yellow')
# p.plot(b,color="pink")
p.plot(a,linestyle='dotted')
p.plot(b)
p.show()