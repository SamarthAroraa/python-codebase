def fibo(n):
    if(n <= 2):
        return 1
    return fibo(n-1)+fibo(n-2)


n = int(input("which term of the series do you want?"))
print(fibo(n))
