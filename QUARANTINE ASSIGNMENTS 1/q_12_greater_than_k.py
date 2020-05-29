string= input("Enter space separated text")
k=int(input("Enter k:"))
words=[]
string= string.split()
for word in string:
    if(len(word)>k):
        words.append(word)
print("List of words:", words)
