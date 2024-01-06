'''
gender=input("enter the gender=")
gender1=gender.lower()
if gender1=="male":
    print("the gender is male")
elif gender1=="female":
    print("the gender is female")
else:
    print("invalid input")


num1=int(input("enter the first="))
num2=int(input("enter the second="))
num3=int(input("enter the third="))
if num1>num2 and num1>num3:
         print(num1,"is greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")


for i in range(1,11):
    if i==6:
        pass
    else:
        print(i)
       
    
         
num=0
for i in range(10):
    
    if num==8:
        break
    print("the num has value=")
    print(i)
    num += 1
    

num=int(input("enter the number for factorial="))
fact=1
if num<0:
    print("factorial does'nt exist")
elif num==0 or num==1 :
    print("factorial is 1")
else:
    for i in range(1,num+1):
        fact=i*fact
    print("the factorial is",fact)



num=int(input("enter the number for binory conversion="))
bi=2        
rem1=num%bi
que1=num//bi
rem2=que1%bi
que2=que1//bi
rem3=que2%bi
que3=que2//bi
rem4=que3%bi
print(rem4,rem3,rem2,rem1)

c_password="computer"
password=input("enter the password=")
lpassword=password.lower()
attempt=1
while attempt<4:
    attempt += 1
    if lpassword==c_password:
        print("unlock")
        break
    if lpassword != c_password and attempt<4:
        password=input("enter the password=")
        
        
    if lpassword != c_password  and attempt==3:
        print("attempts are over")
        break
        

num=int(input("enter the term for fibonacci series="))
f=0
s=1
sum=f+s
count=0
while count<num:
    print(s,end=" ")
    count += 1
    f=s
    s=sum
    sum=f+s
print()


num=int(input("enter the for checking for armstrong no="))

temp=num
sum=0
while num>0:
    remender=num%10
    sum += remender**3
    temp=temp//10
if sum==num:
    print("the given number is armstrong")
else:
    print("the given number is not armstorg")


for i in range(100,1000):
    digit1=i%10
    digit2=(i//10)%10
    digit3=i//100
    if i==(digit3**3+digit2**3+digit1**3):
        print(i)



def armstrong(number):
    digit=len(str(number))
    sum=0
    temp=number
    while number>0:
        remender=number%10
        sum += remender**digit
        temp=temp//10
    if sum==number:
        print("the given number is armstrong")
    else:
         print("the given number is not armstorg")
number=int(input("enter the numbner for armstornge="))
print(armstrong(number))




def rfibo(i):
    if i<=1:
        return i
    else:
        return(rfibo(i-1)+rfibo(i-2))
userno=int(input("enter the for fibonacci seriesa="))
if userno <= 0:
    print("invalid input")
else:
    print("fibonacci series exist")
    for i in range(0,userno):
        print(rfibo(i))



def rfact(x):
    if x==1:
        return(x)
    else:
        return(x*rfact(x-1))
num=int(input("enter the no. for the factorial="))
if num<0:
    print("factorial doesn't exist")
elif num==1 or num==0 :
    print("factorial is 1")
else:
    print(rfact(num))


element=[6,3,1,7]
interm=0
for i in range(0,len(element)):
    for j in range(i+1,len(element)):
        if element[i]>element[j]:
            interm=element[i]
            element[i]=element[j]
            element[j]=interm
print()
print("the correct order of the list is=",element)


x=int(input("how many lines you want to make *triangle="))
for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")    
        





def tringle(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")
x=int(input("how many lines you want to make *triangle="))
tringle(x)

num=int(input("enter the number="))
for i in range(2,num):
    if num%i==0:
        print(num,"the given no. is not a prime")
        break
    else :
        print(num,"the is a prime no.")
        break
'''    


start=int(input("enter the starting point="))
end=int(input("enter the ending point="))
print("the prime series between",start,"and",end)
for i in range(start,end+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count += 1
            break
    if count==0:
        print(i,end=" ")
        
            
    
























            



































    




































       

        


        



























    
