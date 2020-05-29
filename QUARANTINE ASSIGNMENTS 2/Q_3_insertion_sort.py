def insertion(list):
    for m in range(1,len(list)):
        el=list[m]
        i=m-1
        while(i>=0 and el<list[i]):
            list[i+1]=list[i]
            i-=1
        i+=1
        list[i]=el
    return list

list=input("Enter integers to be sorted(space-separated)")
list= list.split()
for m in range(len(list)):
    list[m]=int(list[m])
print("sorted list is", insertion(list))
