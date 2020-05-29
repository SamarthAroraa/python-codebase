filepath="/Users/samartharora/Documents/Coding/python/QUARANTINE ASSIGNMENTS 3/source.txt"
counter=int(0)
write_obj=open("/Users/samartharora/Documents/Coding/python/QUARANTINE ASSIGNMENTS 3/newfile.txt",'x')
with open(filepath,'r') as file_object:
    for line in file_object:
        counter+=1
        if(counter%2==0):
            continue
        write_obj.write(line)

write_obj.close()
