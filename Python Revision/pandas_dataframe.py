import pandas as p

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'City':["Delhi","Lucknow","Mumbai"]
}

myvar = p.DataFrame(mydataset)
print(myvar)
