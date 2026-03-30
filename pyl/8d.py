s1=set(map(int,input("Enter the values for set 1:").split(",")))
s2=set(map(int,input("Enter the values for set 2:").split(",")))
print(s1)
print(s2)
if s2.issubset(s1):
   print(True)
else:
   print(False)
#s2.issubset(s1)
