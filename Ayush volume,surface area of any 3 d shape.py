print('''
|------------------MENU----------------------|
|                                            |
|                1.cube                      |
|                2.cuboid                    |
|                3.cone                      |
|                4.solidcylinder             |
|                5.hollowcylinder            |
|                6.solidsphere               |
|                7.hollowsphere              | 
|                8.hemisphere                |
|                                            |
|-----------------THE END--------------------|''')
m=int(input("Enter 1-8:"))
pie=22/7
l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
h=int(input("Enter height:"))
r=int(input("Enter radius:"))
if m==1:
    v=l*b*h
    lsa=4*l^2
    tsa=6*l^2
    print("The Volume of cube:",v)
    print("The Lateral surface area of cube:",lsa)
    print("The Total surface area of cube:",tsa)
elif m==2:
    v=l*b*h
    lsa=2*h*(l+b)
    tsa=2*(l*b+b*h+h*l)
    print("The Volume of cuboid:",v)
    print("The Lateral surface area of cuboid:",lsa)
    print("The Total surface area of cuboid:",tsa)
elif m==3:
    l=int(input("Enter slantheight:"))
    v=1/3*pie*(r^2)*h
    csa=pie*r*l
    tsa=(pie*r*l)+(pie*r^2)
    print("The Volume of cone:",v)
    print("The Curved surface area of cone:",csa)
    print("The Total surface area of cone:",tsa)
elif m==4:
    v=pie*(r^2)*h
    csa=2*pie*r*h
    tsa=2*pie*r*(h+r)
    print("The Volume of solid cylinder:",v)
    print("The curved surface area of solid cylinder:",csa)
    print("The Total surface area of solid cylinder :",tsa)
elif m==5:
    R=int(input("Enter radius2:"))
    v=pie*(r^2-R^2)*h
    csa=2*pie*r*h+2*pie*R*h
    tsa=2*pie*(r+R)*(h+r+R)
    print("The Volume of hollow cylinder:",v)
    print("The curved surface area of hollow cylinder:",csa)
    print("The Total surface area of hollow cylinder :",tsa)
elif m==6:
    v=4/3*pie*r^3
    csa=4*pie*r^2
    tsa=4*pie*r^2
    print("The Volume of solid Sphere:",v)
    print("The curved surface area of solid Sphere:",csa)
    print("The Total surface area of solid Sphere:",tsa)
elif m==7:
    R=int(input("Enter radius2:"))
    v=4/3*pie*(R^3-r^3)
    csa=4*pie*(R^2-r^2)
    tsa=4*pie*(R^2-r^2)
    print("The Volume of hollow sphere:",v)
    print("The curved surface area of hollow sphere:",csa)
    print("The Total surface area of hollow sphere :",tsa)
elif m==8:
    v=2*pie*(r^2)
    csa=3*pie*(r^2)
    tsa=2/3*pie*(r^3)
    print("The Volume of hemisphere:",v)
    print("The curved surface area of hemisphere:",csa)
    print("The Total surface area of hemisphere :",tsa)
