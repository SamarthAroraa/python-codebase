filepath="/Users/samartharora/Documents/Coding/python/QUARANTINE ASSIGNMENTS 3/source.txt"
with open(filepath,'r') as file_object:
    data= file_object.readlines()
# datarev=""
datarev=""
# words = s.split(' ')
# string =[]
# for word in words:
#     string.insert(0, word)
#
for line in data:
    words=line.split()
    string=""
    for word in words:
        string=word+" "+string
    datarev+=string+'\n'

with open(filepath,'w') as file_object:
    file_object.writelines(datarev)
