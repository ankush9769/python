
list1=[5,6,3,7,2]
interm=0
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            interm=list1[i]
            list1[i]=list1[j]
            list1[j]=interm
            print()
print("the asending order is of given list1",list1)




