d={1:'T',2:'A',3:'M',4:'I',5:'L'}
def get_value(item):
    return item[1]
sorted_asc = dict(sorted(d.items(), key=get_value))
print("Step 1 (A-Z):", sorted_asc)
user_key = int(input("Enter a number: "))
user_val = input("Enter a letter: ")
d[user_key] = user_val
final_dict = dict(sorted(d.items(), key=get_value, reverse=True))
print("Step 2 (Z-A):", final_dict)

