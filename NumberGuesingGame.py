import random as rd

print("Welcome to number gussing game:")

while(True):
    k=int(input("guess a number:"))
    num=rd.randint(1,100)
    print("the random number is :",num)
 
    if(num==k):
        print("Congratulation you are win")
        break
        
    elif(abs(k-num)<5):
        print("you are very close , try again")
    
    else:
        print("you are too far , loosing this game")
        break