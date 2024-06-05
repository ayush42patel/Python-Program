import statistics as s
import numpy as m
n=eval(input("Enter List:"))
print("Statistics->")
print("Mean:",s.mean(n))
print("Median:",s.median(n))
print("Mode:",s.mode(n))
print("Numpy->")
print("Mean:",m.mean(n))
print("Median:",m.median(n))
