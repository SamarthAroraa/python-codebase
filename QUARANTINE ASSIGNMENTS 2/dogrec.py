n=int(input("Number of records:"))
list={}
for i in range(n):
    name=input("name: ").lower()
    info=[]
    breed=input("breed: ")
    age=input("age: ")
    info.append(breed)
    info.append(age)
    list[name]=info
search=input("Enter name of pet to be searched").lower()
breed=list[name][0]
age=list[name][-1]
print("name:",search)
print("breed:",breed)
print("age",age)
