def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("Enter 1st number input: "))
b=int(input("Enter 2nd input:"))
print("GCD:", gcd(a,b))
