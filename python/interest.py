def si(p,n,age):
   if(age>50):
      print("the customer is senior citizen")
      simpleinterest=(P*n*0.12)/100
      print("the simple interest is ",simpleinterest)
   else:
      print("the customer is not a senoir citizen")
      simpleinterest=(P*n*0.1)/100
      print("the simple interest is ",simpleinterest)
      return p,n

age=int(input("enter the age:"))
P=float(input("enter the principle amount:"))
n=int(input("enter the no.of years"))
si(P,n,age)
