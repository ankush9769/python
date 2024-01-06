def rfact(x):
    if x==1:
        return x
    else:
        return(rfact(x-1)*x)
num=int(input("enter the no. for factorial="))
if num<0:
    print("invalid input")
elif num==0 or num==1:
    print("the factorial is 1")
else:
    print("the factorial is")
    print(rfact(num))

    
              
