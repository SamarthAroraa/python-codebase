items = {}


def search(itemname):
    itemname = itemname.lower()
    if(itemname in items.keys()):
        print("Name : ", itemname)
        print("Price : ", items[itemname])
    else:
        print("Item not found!")
    return


n = int(input("Number of items to store:"))
for i in range(n):
    name = input("Name : ")
    price = input("Price: ")
    items[name.lower()] = price
itemname = input("Enter name of item to be searched : ")
search(itemname)
