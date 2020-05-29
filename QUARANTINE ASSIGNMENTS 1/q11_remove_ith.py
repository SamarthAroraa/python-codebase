string = input( "Enter the string :" )
print("Enter index of character to be deleted(0-",len(string)-1,"): ")
i=int(input())
ans= string[:i]+string[i+1:]
print("Result:", ans)
