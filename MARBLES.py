filepath = "/Users/samartharora/Documents/Coding/python/textfile.txt"
filepath2 = "/Users/samartharora/Documents/Coding/python/textfile2.txt"

final_list = []
list2 = []
with open(filepath, 'r') as obj:
    final_list = obj.readlines()
print(final_list)
with open(filepath2, 'w+') as obj:
    for line in final_list:
        string = " \" " + line.rstrip() + "\", \n"
        print(string)
        obj.write(string)
