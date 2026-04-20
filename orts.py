s = input() 
lower="" 
upper = "" 
even = "" 
odd="" 
for i in s: 
    if i.islower(): 
        lower+=i
    elif i.isupper():
        upper+=i
    elif int(i)%2==0:
        even+=i
    else:
        odd+=i

print("".join((sorted(lower)+sorted(upper)+sorted(odd)+sorted(even))))
