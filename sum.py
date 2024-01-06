'''
#keep on adding till the stoping conditional is not met
num=int(input("keep entering the number="))
addition=0
while num != 0 :
     addition += num
     num=int(input("keeo entering the number="))
print("the sum is =",addition)
'''



#plot the graph
x=[1,2,3,4,5]
y=[12,17,18,10,9]
plt.histogram(x,y)
plt.show()
