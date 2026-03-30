s1=input("Enter the string:")
occ={}

for i in s1:
   if i in occ:
      occ[i]+=1
   else:
      occ[i]=1


occ1={}
for i in sorted(occ, key=occ.get, reverse=True):
    occ1[i]=occ[i]
print(occ1)
   
