list1 = [10, 25, 5, 30]
list2 = [5, 40, 15, 60]
print(list1)
print(list2)
if len(list1) == 0 and len(list2)== 0:
    print("List 1 is empty")
    print("List 2 is empty")
else:
    print("List 1 is not empty")
    print("List 2 is not empty")
com = False
for x in list1:
    for y in list2:
        if x == y:
            com = True
print("Lists have common member",com)
val = 5
temp1 = []
for item in list1:
    if item != val:
        temp1.append(item)
list1 = temp1
temp2 = []
for item in list2:
    if item != val:
        temp2.append(item)
list2 = temp2
print("Lists after removing ",val, "L1: " ,list1," L2: ",list2)
list3 = []
for i in range(len(list1)):
    a = list1[i]
    b = list2[i]
    if (a + b) <= 40:
        list3.append(a)
	list3.append(b)
print("List 3 (Sums <= 40):",list3)

