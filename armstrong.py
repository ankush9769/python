arm=int(input("enter the no.for checking the armstrong no="))
digit=len(str(arm))
sum=0
n=arm
while(arm>0):
    remender=arm%10
    sum +=remender**digit
    arm=arm//10
if sum==n:
    print("armstong number")
else:
    print("not armstrong number")
    
              
