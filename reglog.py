details={}
user=[]
j=1
while(True):
    x=int(input("enter your choice:"))
    if(x):
        i=0
        while(i<5):
            data=input("enter the values:")
            user.append(data)
            i=i+1
            details[j]=user
        j=j+1
        user=[]
        print(details)
    else:
        while(True):
            email=input("enter the value of email:")
            pas=input("enter the value of pass:")
            i=1
            if(email in details[i] and pas in details[i]):
                print(True)
                i=+1
                break
            print(False)
        
 
        
         