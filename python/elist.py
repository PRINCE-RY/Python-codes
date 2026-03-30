listo=[1,2,3,4,5,6,7,8,9,10]
for i in listo:
   even=i%2
   if even==0:
      listo.remove(i)
print("the list ater update: ",listo)      
