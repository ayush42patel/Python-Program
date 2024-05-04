def binsearch(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=int((low+high)/2)
        if key==a[mid]:
            return mid
        elif key<a[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        return -999
a=eval(input("Enter list:"))
key=int(input("Enter what you want to search:"))
res=binsearch(a,key)
if res>=0:
    print(key,"Found at index",res)
else:
    print("Sorry not found")
