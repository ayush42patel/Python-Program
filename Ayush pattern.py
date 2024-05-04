import time
print("Start Execution : ",end="")
print(time.ctime())
print('''
|------------------------------------------------------MENU------------------------------------------------------|
|                                                                                                                |
|                            1.#Pattern 1(Simple triangle)                                                       |
|                            2.#Pattern 2(Inverted Pyramid of numbers)                                           |
|                            3.#Pattern 3(Half pyramid)                                                          |
|                            4.#Pattern 4(Inverted pyramid of descending order)                                  |
|                            5.#Pattern 5(Inverted Pyramid of same digit)                                        |
|                            6.#Pattern 6(reverse pyramid of no)                                                 |  
|                            7.#Pattern 7(Inverted half pyramid)                                                 |
|                            8.#Pattern 8(Pyramid of natural no)                                                 |
|                            9.#Pattern 9(Unique Pyramid Pattern of Digits)                                      |
|                            10.#Pattern 10(Connected Inverted Pyramid Pattern of Numbers)                       |
|                            11.#Pattern 11(Even Number Pyramid Pattern)                                         |
|                            12.#Pattern 12(Pyramid of Horizontal Tables)                                        |
|                            13.#Pattern 13(Pyramid Pattern of Alternate Numbers)                                |
|                            14.#Pattern 14( Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers)        |
|                            15.#Pattern 15(Equilateral Triangle with Stars (Asterisk Symbol))                   |
|                            16.#Pattern 16(Downward Triangle Pattern of Stars)                                  |
|                            17.#Pattern 17(Pyramid Pattern of Stars)                                            |
|                            18.#Pattern 18(Right Start Pattern Program)                                         |
|                            19.#Pattern 19(Left Start Pattern Program)                                          |
|                            20.#Pattern 20(Hourglass Pattern Program)                                           |
|                            21.#Pattern 21(Left Half-Pyramid Pattern Program)                                   |
|                            22.#Pattern 22(Downward Half-Pyramid Pattern Program)                               |
|                            23.#Pattern 23(Diamond Shaped Pattern Program1)                                     |
|                            24.#Pattern 24(Diamond Star Pattern Program2)                                       |
|                            25.#Pattern 25(1,212)                                                               |
|                            26.#Pattern 26(Half-Pyramid Pattern With Numbers)                                   |
|                            27.#Pattern 27(Diamond Pattern With Numbers)                                        |
|                            28.#Pattern 28(Descending Order Pattern Program)                                    |
|                            29.#Pattern 29(Binary Numbers Pattern Program)                                      |
|                            30.#Pattern 30(Right Alphabetical Triangle)                                         |
|                            31.#Pattern 31(Square)                                                              |
|                            32.#Pattern 32(Rectangle)                                                           |
|                            33.#Pattern 33(Right alphabet)                                                      |
|                            34.#Pattern 34(Hollow straight triangle)                                            |
|                                                                                                                |
|--------------------------------------------------THE END-------------------------------------------------------|
''')
j=int(input("Enter(1-34):"))
if j==1:
    print("#Pattern 1(Simple triangle)")
    rows=int(input("Enter a no:"))
    for num in range(rows+1):
        for i in range(num):
            print(num,end=" ")
        print()
elif j==2:
    print("#Pattern 2(Inverted Pyramid of numbers)")
    rows=int(input("Enter a no:"))
    b=0
    for i in range(rows,0,-1):
        b+=1
        for j in range(1,i+1):
            print(b,end=" ")
        print()
elif j==3:
    print("#Pattern 3(Half pyramid)")
    rows=int(input("Enter a no:"))
    for num in range(1,rows+1):
        for i in range(1,num+1):
            print(i,end=" ")
        print()
elif j==4:
    print("#Pattern 4(Inverted pyramid of descending order)")
    rows=int(input("Enter a no:"))
    for i in range(rows,0,-1):
        num=i
        for j in range(0,i):
            print(num,end=" ")
        print()
elif j==5:
    print("#Pattern 5(Inverted Pyramid of same digit)")
    rows=int(input("Enter a no:"))
    num=rows
    for i in range(rows,0,-1):
        for j in range(0,i):
            print(num,end=" ")
        print()
elif j==6:
    print("#Pattern 6(reverse pyramid of no)")
    rows=int(input("Enter a no:"))
    for i in range(1,rows):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
elif j==7:
    print("#Pattern 7(Inverted half pyramid)")
    rows=int(input("Enter a no:"))
    for i in range(rows, 0, -1):
        for j in range(0, i + 1):
            print(j, end=" ")
        print()
elif j==8:
    print("#Pattern 8(Pyramid of natural no)")
    c=1
    rows=int(input("Enter a no:"))
    stop=int(input("Enter where you want to stop:"))
    for i in range(rows):
        for j in range(1,stop):
            print(c,end=" ")
            c+=1
        print()
elif j==9:
    print("#Pattern 9(Unique Pyramid Pattern of Digits)")
    rows=int(input("Enter a no:"))
    for i in range(1,rows+1):
        for j in range(1,i-1):
            print(j,end=" ")
        for k in range(i-1,0,-1):
            print(k,end=" ")
        print()
elif j==10:
    print("#Pattern 10(Connected Inverted Pyramid Pattern of Numbers)")
    rows=int(input("Enter a no:"))
    for i in range(0,rows):
        for j in range(rows-1,i,-1):
            print(j,end=" ")
        for k in range(i):
            print(" ",end=" ")
        for l in range(i+1,rows):
            print(l,end=" ")
        print()
elif j==11:
    print("#Pattern 11(Even Number Pyramid Pattern)")
    rows=int(input("Enter a no:"))
    last=2*rows
    for i in range(1,rows+1):
        even=last
        for j in range(i):
            print(even,end=" ")
            even-=2
        print()
elif j==12:
    print("#Pattern 12(Pyramid of Horizontal Tables)")
    rows=int(input("Enter a no:"))
    for i in range(0,rows):
        for j in range(0,i+1):
            print(i*j,end=" ")
        print()
elif j==13:
    print("#Pattern 13(Pyramid Pattern of Alternate Numbers)")
    rows=int(input("Enter a no:"))
    i=1
    while i<=rows:
        j=1
        while j<=i:
            print((i*2-1),end=" ")
            j=j+1
        i=i+1
        print()
elif j==14:
    print("#Pattern 14( Mirrored Pyramid (Right-angled Triangle) Pattern of Numbers)")
    rows=int(input("Enter a no:"))
    for i in range(1,rows):
        num=1
        for j in range(rows,0,-1):
            if j>i:
                print(" ",end=" ")
            else:
                print(num,end=" ")
                num+=1
        print()
elif j==15:
    print("#Pattern 15(Equilateral Triangle with Stars (Asterisk Symbol))")
    size=int(input("Enter a no:"))
    m=(2*size)-2
    for i in range(0,size):
        for j in range(0,m):
            print(end=" ")
        m=m-1
        for k in range(0,i+1):
                print("*",end=" ")
        print()
elif j==16:
    print("#Pattern 16(Downward Triangle Pattern of Stars)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    for i in range(rows,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for l in range(0,i+1):
            print("*",end=" ")
        print()
elif j==17:
    print("#Pattern 17(Pyramid Pattern of Stars)")
    rows=int(input("Enter a no:"))
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
elif j==18:
    print("#Pattern 18(Right Start Pattern Program)")
    rows=int(input("Enter a no:"))
    for i in range(0,rows):
        for j in range(0,i+1):
            print("*", end=" ")
        print()
    for m in range(rows,0,-1):
        for l in range(0,m-1):
            print("*",end=" ")
        print()
elif j==19:
    print("#Pattern 19(Left Start Pattern Program)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    for i in range(0,rows-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for l in range(0,i+1):
            print("*",end=" ")
        print()
    g=-1
    for m in range(rows-1,-1,-1):
        for h in range(g,-1,-1):
            print(end=" ")
        g=g+2
        for n in range(0,m+1):
            print("*",end=" ")
        print()
elif j==20:
    print("#Pattern 20(Hourglass Pattern Program)")
    rows=int(input("Enter a no:"))
    k=rows-2
    for i in range(rows,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for l in range(0,i+1):
            print("*",end=" ")
        print()
    m=2*rows-2
    for a in range(0,rows+1):
        for b in range(0,m):
            print(end=" ")
        m=m-1
        for c in range(0,a+1):
            print("*",end=" ")
        print()
elif j==21:
    print("#Pattern 21(Left Half-Pyramid Pattern Program)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    for i in range(0,rows):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for l in range(0,i+1):
            print("*",end=" ")
        print()
elif j==22:
    print("#Pattern 22(Downward Half-Pyramid Pattern Program)")
    rows=int(input("Enter a no:"))
    for i in range(rows,-1,-1):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
elif j==23:
    print("#Pattern 23(Diamond Shaped Pattern Program1)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    for i in range(0,rows):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for l in range(0,i+1):
            print("*",end=" ")
        print()
    m=rows-2
    for a in range(rows,-1,-1):
        for b in range(m,0,-1):
            print(end=" ")
        m=m+1
        for c in range(0,a+1):
            print("*",end=" ")
        print()
elif j==24:
    print("#Pattern 24(Diamond Star Pattern Program2)")
    for i in range(5):
        for j in range(5):
            if i+j==2 or i-j==2 or i+j==6 or j-i==2:
                print("*",end=" ")
            else:
                print(end=" ")
        print()
elif j==25:
    print("#Pattern 25(1,212)")
    rows=int(input("Enter a no:"))
    s=rows*2-1
    for i in range(1,rows+1):
        for j in range(0,s):
            print(end=" ")
        for l in range(i,0,-1):
            print(end=" ")
        for m in range(2,i+1):
            print(j,end=" ")
        s=s-2
        print()
elif j==26:
    print("#Pattern 26(Half-Pyramid Pattern With Numbers)")
    rows=int(input("Enter a no:"))
    for i in range(1,rows):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
elif j==27:
    print("#Pattern 27(Diamond Pattern With Numbers)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    x=0
    for i in range(0,rows):
        x+=1
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for l in range(0,i+1):
            print(x,end=" ")
        print()
    m=rows-2
    n=rows+2
    for a in range(rows,-1,-1):
        n-=1
        for b in range(m,0,-1):
            print(end=" ")
        m=m+1
        for c in range(0,a+1):
            print(n,end=" ")
        print()
elif j==28:
    print("#Pattern 28(Descending Order Pattern Program)")
    rows=int(input("Enter a no:"))
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
elif j==29:
    print("#Pattern 29(Binary Numbers Pattern Program)")
    rows=int(input("Enter a no:"))
    k=2*rows-2
    for i in range(0,rows):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for l in range(0,i+1):
            print("10",end=" ")
        print()
elif j==30:
    print("#Pattern 30(Right Alphabetical Triangle)")
    n=int(input("Enter a no:"))
    x = 65
    for i in range(0, n):
        ch = chr(x)
        x += 1
        for j in range(0, i + 1):
            print(ch, end=" ")
        print()
elif j==31:
    print("#Pattern 31(Square)")
    rows=int(input("Enter rows:"))
    for i in range(0,rows+1):
        for j in range(0,rows+1):
            print("*",end=" ")
        print()
elif j==32:
    print("#Pattern 32(Rectangle)")
    rows=int(input("Enter rows:"))
    for i in range(0,rows+1):
        for j in range(0,rows-1):
            print("*",end=" ")
        print()
elif j==33:
    print("#Pattern 33(Right alphabet)")
    rows=int(input("Enter a no:"))
    for i in range (65,rows):
        for j in range(65,i+1):
            print(chr(j),end=" ")
        print()
elif j==34:
    print("#Pattern 34(Hollow straight triangle)")
    row=int(input("Enter row:"))
    for i in range(row):
        for j in range(row-i):
            print(" ",end=" ")
        for l in range(2*i+1):
            if l==0 or l==2*i or i==row-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("Invalid choose from 1 to 34")
    
print("Stop Execution : ",end="")
print(time.ctime())
