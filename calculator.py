num1=float(input("enter the value of num1:"))
num2=float(input("enter the value of num2:"))

operation=input("choose the any one operation-(+,-,*,/):")

if(operation=='+'):
    result=num1+num2
elif(operation=='-'):
    result=num1-num2
elif(operation=='*'):
    result=num1*num2
elif(operation=='/'):
    if(num2==0):
        result="error!"
    else:
        result=num1/num2
else:
    result="Invalid operation"

print("result:",result)
    