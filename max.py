from itertools import product 

def get_final_result(values, m):
    final_res = 0
    for vals in product(*values):
        temp = 0
        for val in vals:
            temp += val ** 2
        temp = temp % m

        if temp > final_res:
            final_res = temp
    return final_res

k, m = input().split()
n_list = []

for i in range(int(k)):
    n = list(map(int, input().split()))
    n_list.append(n[1:])

result = get_final_result(n_list, int(m))
print(result)
