inp= input("Enter integers(space separated)")
inp= inp.split()
freq={}
duplicates=[]
for m in inp:
    if(m not in freq.keys()):
        freq[m]=1
    else:
        # freq[m]+=1
        duplicates.append(m)
print("Duplicate integers are",duplicates)
