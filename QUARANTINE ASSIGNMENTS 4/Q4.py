set1 = set()
set2 = set()
set3 = set()
list1 = input("Enter space separated numbers for the first set:").split()
list2 = input("Enter space separated numbers for the second set:").split()
set1.update(list1)
set2.update(list2)
# for x in set1:
#     set3.add(x)

# for y in set2:
#     set3.add(y)
set3 = set1 | set2
print(set3)
