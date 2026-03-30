d1 = {1:'T', 2:'A', 3:'M', 4:'I', 5:'L'}
d2 = {6:'N', 7:'A', 8:'D', 9:'U'}
d1.update(d2)
print("Merged Dictionary:", d1)

def check(a):
    if a in d1:
        print("Key exists! and the Value is: ",d1[a])
    else:
        print("Key does not exist.")
m = int(input("Enter the key to search (1-9): "))
check(m)

