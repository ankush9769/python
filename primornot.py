x=int(input("enter the number for prime="))
for i in range(2,x):
    if x%i==0:
        print(x,"is not a prime no.")
        break
    else:
        print(x,"is a prime no.")
        break
