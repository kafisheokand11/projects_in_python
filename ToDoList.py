tasks=[]

print("To Do List app")


while(True):
    choice=int(input("enter the choice :"))
    if choice==1:
        print("add the taks in tasks")
        task=input("enter the taks:")
        tasks.append(task)
    
    elif(choice==2):
        print("view the task",tasks)
        
        if not tasks :
            print("no tasks found")
            
        else:
            idx=1
            for i in tasks:
                print(i,idx)
                idx+=1
        
    elif(choice==3):
        print("select removed tasks")
        idx=1
        for i in tasks:
            print(i,idx)
            idx+=1
        
        if tasks:   
            num=int(input("choose a number value:"))
        
            if 1<=num<=len(tasks):
                removed=tasks.pop(num-1)
                
                print(f"tasks '{removed}' removed")
            
            else:
                print("number is out of range")
        
        else:
            print("no taks found")

    elif choice==4:
        print("goodbye")
    
    else:
        print("invalid choice")
    
    print(type(tasks))