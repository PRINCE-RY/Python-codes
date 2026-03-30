list1 = input("enter the colours: ")
result = list1.split(",")
print("The length of colours list: ", len(result))
list2 = input("enter the values: ")
result1 = list2.split(",")
result2 = []
for i in result1:
    result2.append(int(i))
print("the max element: ", max(result2))
print("the min element: ", min(result2))
sum1 = 0
for i in result2:
    sum1 = sum1 + i
print("sum of elements: ", sum1)
