
start=int(input("enter the starting range="))
end=int(input("enter the ending range="))
print("the prime series is")
for i in range(start,end+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count += 1
            break
    if count==0:
        print(i)
    

