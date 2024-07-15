a=int(input("Enter no from where:"))
b=int(input("Enter no till where:"))
for i in range(a,b+1):
    for k in range(2,i):
        if i%k==0:
            g=i/k
            print("Found a factor(",k,")for",i)
            break
    else:
            print(i,"is a Prime Number")