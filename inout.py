import numpy as np

A = np.array([int(x) for x in input().split()])
B = np.array([int(x) for x in input().split()])

def inner_prod(A,B):
    result = np.inner(A,B)
    return result
    
def outer_prod(A,B):
    result = np.outer(A,B)   
    return result

print(inner_prod(A,B))
print(outer_prod(A,B))
