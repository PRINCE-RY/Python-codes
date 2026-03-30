l1=map(int,input("enter the elements:").split(","))
print("removing duplicate elements")
l2=set(l1)
print(l2)
def add_val(x):
   l2.add(x)
   print(l2)
def remove_val(y):
   l2.remove(y)
   print(l2)
x=int(input("enter the value to be added:"))
y=int(input("enter the value to be removed:"))
add_val(x)
remove_val(y)
