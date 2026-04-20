import numpy as np

N = int(input()) 

A = [list(map(float,input().split())) 

for _ in range(N)]

A = np.array(A)

Det = np.linalg.det(A)

print(round(Det,2))
