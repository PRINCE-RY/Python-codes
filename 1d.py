p=int(input("enter the principle amount:"))
n=int(input("enter the compound freq:"))
r=float(input("enter the interest:"))
t=int(input("enter the no.of years:"))
print("Simple Interest calc")
si=(p*t*r)/100
print("Simple Interest:",si)
print("Compound Interest calc")
r=r/100
total_amount = p * (pow((1 + r /n), (n * t)))
ci = total_amount - p
print("Compound Interest:",ci)
