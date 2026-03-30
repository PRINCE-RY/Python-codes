a=int(input("enter the rows:"))
b=int(input("enter the col:"))
for i in range(a):
   for j in range(b):
      print('*' 
	    if(i==0 or i==a-1 or j==0 or j==b-1) 
	    else ' ',end=' ')
   print()
