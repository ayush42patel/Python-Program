n=int(input("Enter no of lines:"))
f=open("D://File Handling Files/A1.txt","w")
for i in range(0,n):
    s=str(input("Enter string:"))
    f.write(s)
f.close()

key=str(input("Enter string you want to count:"))
f=open("D://File Handling Files/A1.txt","r")
h=f.read()
c=h.count(key)
f.close()
print("The ",key," string occurred ",c," times")