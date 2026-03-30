def calc(st1):
    n = m = 0
    for i in st1:
        if i.isupper():
            n += 1
        if i.islower():
            m += 1
    print("no of upper:", n)
    print("no of lower:", m)

st1 = input("enter the string: ")
calc(st1)

