def lcm(a,b):
    lcm = max(a,b)
    while(lcm%a!=0 or lcm%b!=0):
        lcm+=1
    return lcm

a= int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("LCM of entered numbers is ", lcm(a,b))
