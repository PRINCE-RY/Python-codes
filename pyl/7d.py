d1={1:'y',2:'o',3:'g'}
d2={4:'e',5:'s',6:'h'}
print(d1)
print(d2)
#d3=d1d2
#print("Using or operator")
#print(d3)
d4=d1.copy()
d4.update(d2)
print("using update option")
print(d4)
d5=dict()
for i in range(1,4):
    d5[i]=d1[i]
for i in range(4,7):
    d5[i]=d2[i]
print("using for loop")
print(d5)
d6={**d1,**d2}
print("using dictionary unpacking method")
print(d6)
