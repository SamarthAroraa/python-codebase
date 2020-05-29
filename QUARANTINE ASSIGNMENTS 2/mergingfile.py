import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
path1=input("Enter complete file name pf first file: ")
path1= os.path.join(THIS_FOLDER, path1)

path2=input("Enter complete file name pf second file: ")
path2= os.path.join(THIS_FOLDER, path2)

f1=open(path1,"r")
f2=open(path2,"r")
f3=open("merged_file.txt","w")
f3.write(f1.read())
f3.write(f2.read())
