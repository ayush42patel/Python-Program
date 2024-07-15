import pandas as p

h=eval(input("Enter dictionaries:"))
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2],
#   'City':["Delhi","Lucknow","Mumbai"]
# }

myvar = p.DataFrame(h)
print(myvar)
