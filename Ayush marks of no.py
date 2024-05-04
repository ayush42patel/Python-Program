n=int(input("Enter how many subject:"))
sum=0
for i in range(0,n):
    a=int(input("Enter marks:"))
    sum=sum+a
per=(sum/n)
if per>=90:
    print("The student has got above 90% i.e. A-GRADE:",per,"%")
elif per>=80:
    print("The student has got 80-90% i.e. B-GRADE:",per,"%")
elif per>=70:
    print("The student has got 70-80% i.e. C-GRADE:",per,"%")
elif per>=60:
    print("The student has got 70-60% i.e. D-GRADE:",per,"%")
else:
    print("The student has got below 60% i.e. E-GRADE:",per,"%")
