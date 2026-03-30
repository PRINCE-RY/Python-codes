st1=input("enter the string:")
n=len(st1)
st2="ing"
st3="ly"
if(st1[-3:]=="ing"):
   print(st1+st3)
elif(n<3):
   print(st1)
else:
   print(st1+st2)
