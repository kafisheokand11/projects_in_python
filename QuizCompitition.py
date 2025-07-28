print("welcome to the quiz compitition")

dict=[
    {"q":"what is the capital of india:","option":["1.delhi","2.mumbai","3.pune","4.patna"],"answer":"1"}
      ,{"q":"what plenet is called red plaenet:","option":["1.murcury","2.mars","3.jupiter","4.venus"],"answer":"2"}
       ,{"q":"who PM of India","option":["1.narender modi","2.manohar lal khatter","3.jwaher lal","4.kafi sheokand"],"answer":"1"}
       ]

score=0

for i,q in enumerate(dict,start=1):
    print(f"Q{i}:{q['q']}")
    for option in q["option"]:
        print(option)
        
    user_ans=input("enter your answer (1/2/3/4):")
    
    if(user_ans==q["answer"]):
        print("correct! \n")
        score+=1
    else:
        print("wrong answer")

print(score)