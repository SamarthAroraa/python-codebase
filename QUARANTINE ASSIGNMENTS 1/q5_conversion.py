def convert(n):
    # binary
    binary=""
    temp=int(n)
    while(temp):
        binary=str(temp%2)+binary
        temp=int(temp/2)
    temp=int(n)
    print("Binary:",binary)
    oct=""
    while(temp):
        oct=str(temp%8)+oct
        temp=int(temp/8)
    temp=int(n)
    hex=""
    alpha=['A','B','C','D','E','F']
    while(temp):
        rem= temp%16
        if(rem>9):
            hex= str(alpha[rem-10])+hex
        else:
            hex= str(temp%16)+hex
        temp=int(temp/16)
    print("Octal:",oct)
    print("Hexadecimal",hex)

n=int(input())
convert(n)
