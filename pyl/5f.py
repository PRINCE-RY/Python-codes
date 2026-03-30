listr=[1,2,3,4,5,6,7,8,9,10]
listk=[]
a=int(input("enter the value 1:"))
b=int(input("enter the value 2:"))
print(listr[a:b])
for i in listr[:]:
    if (i%2!=0):
        listr.remove(i)
        listk.append(i) 
listr.extend(listk) 
print(listr) 
