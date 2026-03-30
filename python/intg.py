listr=[0,1,2,3,4,5,6,7,8,9,10]
i=0
even=[]
odd=[]
for i in listr:
   if i%2==0:
      even.append(i)
   else:
      odd.append(i)
print(even)
print(odd)
