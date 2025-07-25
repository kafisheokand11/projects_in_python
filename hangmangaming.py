import random
 
l1=["orange","grapes","fig","mango","banana","jaat"]
word= random.choice(l1)
# print(word)
guess=['_']*len(word)

 
 
for i in range(len(word)):
    letter=input("enter the value of l:")
    if letter in word:
        for i ,char in enumerate(word):
            if char==letter:
                guess[i]=letter
    else:
        break
char_list=list(word)
flag=False
for i in range (len(word)):
    if(guess[i]!=char_list[i]):
        print("we loose",word)
        flag=True
        break
if not flag:
    print("we won",word)  
         
print(guess)              


