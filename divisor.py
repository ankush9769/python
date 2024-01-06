#count the divisors between two numbers
a,b,k=input("enter three number=").split()
a=int(a)
b=int(b)
k=int(k)
count=0
for i in range(a,b+1):
    if i%k==0:
        count=count+1
else:
    print(count)

