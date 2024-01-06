def rfibo(x):
    if x<=1:
        return x
    else:
        return(rfibo(x-1)+rfibo(x-2))
userno=int(input("enter the no for fibonacci series="))
if userno<=0:
    print("invalid input")
else:
    print("fibonacci series")
for i in range(0,userno):
    print(rfibo(i),end=" ")



    
