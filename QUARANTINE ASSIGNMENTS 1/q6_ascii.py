def convert(c):
    if (len(c)!=1):
        print("Entered value is not a character.")
        return;
    print("ascii value of",c, ":", ord(c))
    print("character value of", c, ":", chr(ord(c)))
    return;
c= input("Enter a character value:")
convert(c)
