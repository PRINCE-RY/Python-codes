value=input("Enter the 4-digit binary numbers: ")
bilist=value.split(',')
result=[]
for i in bilist:
    decval=int(i, 2)
    if (decval%5==0):
        result.append(i)
print(",".join(result))
