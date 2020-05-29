
def selection(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        temp=list[i]
        list[i]=list[min_index]
        list[min_index]=temp
    return list

list=input("Enter space separated integers to be sorted")
list=list.split()
for m in range(len(list)):
    list[m]=int(list[m])
print ("Sorted array",selection(list))
