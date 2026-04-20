import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
output_string=""
for i in range(0,m):
    for j in range(0,n):
        output_string += matrix[j][i]

pattern = r"(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])"
print(re.sub(pattern," ",output_string))
