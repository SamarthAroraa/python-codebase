n= int(input("Number of records:"))
records=[]

stream= open("recordfile.txt","w")
# if()
for m in range(n):
    student={}
    student['name']= input("Name:")
    student['roll']=input("Roll no:")
    student['DOB']=input("Date of Birth")
    records.append(student)
    stream.write("Name: "+student['name']+'\n')
    stream.write("Roll number:"+student['roll']+'\n')
    stream.write("Date of Birth:"+student['DOB']+'\n')
