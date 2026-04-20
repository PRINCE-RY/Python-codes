class MyClass:
    count=0
    def __init__(self):
        MyClass.count+=1

o1=MyClass()
o2=MyClass()
o3=MyClass()
print("Number of instances created:", MyClass.count)
