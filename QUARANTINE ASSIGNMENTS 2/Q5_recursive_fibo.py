def fibo(n):
    if(n==1 or n==2):
        return 1
    return fibo(n-1)+fibo(n-2)
n=int(input("Which term of the fibonacci series do you wish to calculate?: "))
if(n<1):
    print("The index must be a natural number")
else:
    print(fibo(n))
