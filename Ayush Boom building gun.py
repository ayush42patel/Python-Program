import time
print("Start Execution : ",end="")
print(time.ctime())
import random
n=int(input('Enter no of rounds:'))
options=['b','bu','g']
rounds=1

comp_win=0
user_win=0

while rounds<=n:
    print(f"Round:{rounds}\nBoamb -'b'\nBuilding -'bu'\nGun -'g'")
    try:
        p=input("Choose your option:")
    except EOFError as e:
        print(e)

    if (p!='b' and p!='bu' and p!='g'):
        print("Invalid output")
        continue

    c=random.choice(options)

    if c=='b':
        if p=='bu':
            comp_win+=1
        elif p=='g':
            user_win+=1
    elif c=='bu':
        if p=='b':
            user_win+=1
        elif p=='g':
            comp_win+=1
    elif c=='g':
        if p=='bu':
            user_win+=1
        elif p=='b':
            comp_win+=1

    if user_win > comp_win:
        print(f"You won round {rounds}\n")
    elif comp_win > user_win:
        print(f"Computer won round {rounds}\n")
    else:
        print("Draw!!\n")

    rounds+=1

if user_win > comp_win:
    print("Congratulations!! You Won")
elif comp_win > user_win:
    print("You lose!!")
else:
    print("Match Draw!!")
print(user_win,"/",comp_win)
print("Stop Execution : ",end="")
print(time.ctime())
