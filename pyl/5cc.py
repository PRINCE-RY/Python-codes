def check_empty(list_a, list_b):
    print("List 1 is {'empty' if not list_a else 'not empty'}")
    print(f"List 2 is {'empty' if not list_b else 'not empty'}")
def have_common_member(list_a, list_b):
    return not set(list_a).isdisjoint(set(list_b))
def remove_element(target_list, element):
    while element in target_list:
        target_list.remove(element)
    return target_list
l1 = [10, 25, 5, 30]
l2 = [5, 40, 15, 60]
check_empty(l1, l2)
has_common = have_common_member(l1, l2)
print(f"Do the lists have common members? {has_common}")
val_to_remove = 5
l1 = remove_element(l1, val_to_remove)
l2 = remove_element(l2, val_to_remove)
print(f"Lists after removing {val_to_remove}: L1: {l1}, L2: {l2}")
list3 = []
for a, b in zip(l1, l2):
    if (a + b) <= 40:
        list3.append(a + b)
print(f"List 3 (Sums <= 40): {list3}")
