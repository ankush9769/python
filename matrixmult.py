
'''i1=no. of rows in first matrix
j1=no. of column in first matrix
i2=no. of rows in second matrix
j2=no. of column in second matrix
'''
i1=int(input("enter the no. of rows in first matrix="))
j1=int(input("enter the no. of columns in first matrix="))
i2=int(input("enter the no. of rows in second matrix="))
j2=int(input("enter the no. of columns in second matrix="))
x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]
y=[
    [1,2,3,4],
    [5,6,7,8],
    [9,8,7,6]
  ]

result=[
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
       ]  
for i in range(i1):
    for j in range(j2):
        for k in range(i2):
            result[i][j] += x[i][k] * y[k][j]
for x in result:
    print(x)            
                       
