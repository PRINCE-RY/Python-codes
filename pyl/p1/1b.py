a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))
m=(-b)/2*a
n=(b*b)-(4*a*c)
if n>0:
   print("Roots are real and distinct")
   r1=m+((n**0.5)/2*a)
   r2=m-((n**0.5)/2*a)
   print(r1,"and",r2)
elif n==0:
   print("Roots are real and equal")
   r1=m
   r2=m
   print(r1,"and",r2)
else:
   print("Roots are complex conjucate")
   n=((-n)**0.5)/(2*a)
   print("r1=",m,"+j",n)
   print("r2=",m,"-j",n)
