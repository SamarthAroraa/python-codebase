def duplicate():
    list1=input("Enter space separated inegers for list 1:")
    list1= list1.split()
    list2=input("Enter space separated inegers for list 2:")
    list2= list2.split()

    for m in list1:
        if(list2.count(m)>0):
            return True;
    return False;

if(duplicate()):
    print("Duplicates exist")
else:
    print("Duplicates do no exist")
