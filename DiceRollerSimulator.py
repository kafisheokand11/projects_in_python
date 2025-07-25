import random as rd
dice_faces = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘"
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘"
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘"
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘"
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘"
    ),
    6: (
        "┌───────┐",
        "│ ●   ● │",
        "│ ●   ● │",
        "│ ●   ● │",
        "└───────┘"
    )
}
print("welcome to the dice roller simulator")
cnt1=0
cnt2=0
while(True):
    
    input("press enter the dice..")
    # genrate the random integer by player one
    dice1=rd.randint(1,6)
    print(f"the rolled dice,{dice1}")
    cnt1+=dice1
    
    # genrate the random integer by player two
    dice2=rd.randint(1,6)
    print(f"the rolled dice,{dice2}")
    cnt2+=dice2
    
    # show the dice faces side by side
    for line1 , line2 in zip(dice_faces[dice1],dice_faces[dice2]):
        print(line1+" "+line2)
    
    again=input("ropll again ?(y/n):")
    
    if(again!='y'):
        print("thanks for playing good bye")
        break
    
# decided who is the winner
if(cnt1>cnt2):
    print("player 1 is win")
else:
    print("player 2 is win")
        


