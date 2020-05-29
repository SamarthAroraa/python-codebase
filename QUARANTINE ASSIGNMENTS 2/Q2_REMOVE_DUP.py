def remove_dupl(list1):
    list2=[]
    for m in list1:
        if(list2.count(m)==0):
            list2.append(m)
    return list2

list=input("Enter space separated list elements")
list = list.split()
list=remove_dupl(list)
print("After removing duplictes the list(set) is:", list)
