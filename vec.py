class vehicle:
   def __init__(self):
      self.c=''
      self.m=''
      self.p=0
      self.y=0
   def getdetails(self):
      self.c=input("enter company:")
      self.m=input("enter modal:")
      self.p=int(input("enter price:"))
      self.y=int(input("enter year:"))
   def display(self):
      print("******details******")
      print(f"COMPANY:{self.c}\nMODAL:{self.m}\nPrice:{self.p}\nYEAR:{self.y}")
x=vehicle()
y=vehicle()
x.getdetails()
y.getdetails()
x.display()
y.display()
