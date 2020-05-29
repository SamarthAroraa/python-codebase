def checkdiv(numbers):
	divlist=[]
	for n in numbers:
		if(int(n)%13==0):
			divlist.append(n)
	print(divlist)
numbers= input("Enter numbers:").split()
checkdiv(numbers)