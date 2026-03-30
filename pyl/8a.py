set1 = set(map(int, input("Enter integers separated by commas: ").split(',')))
print(len(set1))
def iter(x):
   for i in set1:
      print(i)
   if x in set1:
      print("The value exists")
   else:
      print("The value does not exists")
m=int(input("Enter the value to be checked:"))
iter(m)


