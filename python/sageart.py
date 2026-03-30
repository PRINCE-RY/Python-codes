sq={x**2 for x in range(1,10)}
cu={x**3 for x in range (1,10)}
print(sq)
print(cu)
sq.update(cu)
print(sq)
n=int(input("enter the number to be remove:"))
if n in sq:
   sq.remove(n)
   print(sq)
else:
   print("element not found")
print(sq.pop())
print(cu.pop())
print(sq.clear())
