import time
print("Start Execution : ",end="")
print(time.ctime())
import random
print("Stone-Paper-Scissors")
n=int(input('Enter no of rounds:'))
options=['s','p','sc']
rounds=1

comp_win=0
user_win=0

while rounds<=n:
    print(f"Round:{rounds}\nStone- 's'\nPaper- 'p'\nScissors- 'sc'")
    try:
        p=input("Choose your option:")
    except EOFError as e:
        print(e)

    if p!='s' and p!='p' and p!='sc':
        print("Invalid output")
        continue

    c=random.choice(options)

    if c=='s':
        if p=='p':
            user_win+=1
        elif p=='sc':
            comp_win+=1
    elif c=='p':
        if p=='s':
            comp_win+=1
        elif p=='sc':
            user_win+=1
    elif c=='sc':
        if p=='s':
            user_win+=1
        elif p=='p':
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
