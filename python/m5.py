a=int(input("Enter the initial amount:"))
b=int(input("enter the amount spent:"))
balance=a-b
while (balance!=0):
   c=balance//500
   d=c%500
   e=d//200
   f=e%200
   g=f//100
   h=g%100
   i=h//50
   j=i%50
   k=j//20
   l=k%20
   m=l//10
   n=m%10
   break
print("the amount to be returned :",c,d,e,f,g,h,i,j,k,l,m,n)

