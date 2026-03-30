n=int(input("Enter the n:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
def sums():
    k=0
    for i in d:
        k=k+(i*i)
    print(k)
sums()
