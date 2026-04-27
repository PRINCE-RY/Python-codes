x=int(input("enter thye value for calc:"))
if x==1:
   print("calc with sides")
   a=int(input("enter the side 1:"))
   b=int(input("enter the side 2:"))
   c=int(input("enter the side 3:"))
   s=(a+b+c)/2
   area_tri=(s*(s-a)*(s-b)*(s-c))**0.5
   print("Area of triangle with sides: ",area_tri)
elif x==0:
   print("calc with b and h")
   b=int(input("enter the base:"))
   h=int(input("enter the height:"))
   area=0.5*b*h
   print("Area of tri with b and h: ",area)
else:
   print("Invalid option")
