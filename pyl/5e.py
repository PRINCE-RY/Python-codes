mat1=[[1,2],[2,3],[3,4]]
trans=[[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range (len(mat1[0])):
        trans[j][i]=mat1[i][j]
for k in trans:
    print(k)
