n=int(input("number of records to be entered:"))
parts=[]
for i in range(n):
    dict={}
    name=input("Name:")
    price=input("Price:")
    dict["Name"]= name
    dict["Price"]= price
    parts.append(dict)
print("Entered parts:")
for i in range(len(parts)):
    for j in parts[i].keys():
        print(i+1,")",j," : ", parts[i][j])
    print("")
