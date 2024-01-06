'''
#find prime no. till give n number
num=int(input("enter the number for finding prime="))
for num in range(1,num+1):
   if num>1:
        for x in range(2,num):
            if (num%x==0):
             break
        else:
           print(num)
'''



#check weather the given number is prime or not
num=int(input("enter the number="))
for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("prime")
        
   



    
