#nested for loop


#1)
serial_no=[1,2,3]
WHwords=["what","when","why"]
for i in serial_no:
    print(i)
    for j in WHwords:
        print(j)


#2)using single for loop to access each list
list1=[["ankush","rishabh","rohit"],["mayura","shreeya","sneha"]]
for i in list1:
    print(i,end=" ")




#3)using nested for loop access each individual element from list with in the list
list1=[["ankush","rishabh","rohit"],["mayura","shreeya","sneha"]]
for i in list1:
    for j in i:
        print(j)



#4)multiply with place values [10*s,100*s]to the given lists
x=[[1,2],[3,4]]
print(x)
m=1
for i in range(0,2):
    m*=10
    for j in range(0,2):
        x[i][j]*=m
print(x)




#5)print the piramid by using natural no.

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()      




#6)skip ovals to print from the sentence'python logic for kids'
x="python logic for kids"
for p in x:
    if p=="a" or p=="e" or p=="i" or p=="o" or p=="u":
        continue
    else:
        print(p,end=" ")




#7)print the *pattern using nested for loops

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()   
for p in range(6,0,-1):
    for q in range(p):
        print("*",end=" ")
    print()   




#8)print * given pattern
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()




#9)print * odd number pattern
for i in range(1,10):
    if i%2==0:
        continue
    else:
        for j in range(1,i+1):
            print("*",end="")
        print()   




#10)print your name in 3rows and columns
name=input("enter your name=")
for i in range(1,4):
    for j in range(1,4):
        print(name,end=" ")
    print()    
        

















































        
