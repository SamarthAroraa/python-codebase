filename='/Users/samartharora/Documents/Coding/python/QUARANTINE ASSIGNMENTS 2/names.txt'
with open(filename,'r') as ob:
    data=ob.readlines()
data2=""

for word in data:
    # name=
    data2+=(word.lstrip("123 4567890.").rstrip()+'\n')
with open(filename,'w') as ob:
    ob.write(data2)
    print(data2)
