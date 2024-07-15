f=open("D://File Handling Files/A.txt","w")
n=int(input("Enter how many lines:"))
for i in range(1,n+1):
    a=str(input(f"Enter string {i}:"))
    f.write(a)
    f.write("\n")
f.close()

f1=open("D://File Handling Files/A.txt","r")
j=int(input("Enter line no to copy:"))
s=f1.readlines()
f1.close()

if(1<=j<=len(s)):
    li=s[j-1]
else:
    print("Invalid line no")

f2=open("D://File Handling Files/B.txt","w")
f2.write(li)
f2.close()

f2=open("D://File Handling Files/B.txt","r")
print(f2.read())
f2.close()