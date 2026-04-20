class Person:
    def __init__(self, name, age, weight, height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height*0.3048 # convert feet to meters

    def get_bmi_result(self):
        bmi=self.weight/(self.height ** 2)
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy"
        else:
            return "Obese"

name = input("Enter name: ")
age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (feet): "))
p = Person(name, age, weight, height)
print("BMI Result:", p.get_bmi_result())
