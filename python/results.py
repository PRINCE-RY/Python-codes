sub1=int(input("enter the mark 1:")) 
sub2=int(input("enter the mark 2:")) 
sport=int(input("enter the value:"))
extras1=int(input("enter the res 1:")) 
extras2=int(input("enter the res 2:")) 
extras3=int(input("enter the res 3:"))
sub=(sub1 + sub2)/2 
exam=sub*0.5 
sports=sport*0.2 
curicular=(extras1+extras2+extras3)/3 
activities=curicular*0.3
all=(exam+sports+activities) 
print("overall results:",all)
