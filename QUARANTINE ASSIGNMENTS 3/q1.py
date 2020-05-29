filepath="/Users/samartharora/Documents/Coding/python/QUARANTINE ASSIGNMENTS 3/source.txt"
w1= input("Enter word to be replaced")
w2= input("Enter replacement")

with open(filepath,'r') as file_object:
    data= file_object.read()
data=data.replace(w1,w2)
with open(filepath,'w') as file_object:
    file_object.write(data)
