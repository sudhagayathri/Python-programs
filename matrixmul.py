a =[[1,2,3],
    [4,5,6],
    [7,8,9]]
b=[[6,5,3],
   [4,3,6],
   [2,1,5]]

result = [[0,0,0],
       [0,0,0],
       [0,0,0]]
# a 3*3 b 3*2 so result 3*2
for i in range(len(a)):
    for k in range(len(b[0])):
        for j in range(len(b)):
            result[i][k]+= a[i][j]*b[j][k]