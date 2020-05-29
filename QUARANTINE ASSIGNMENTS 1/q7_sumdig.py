def sumdigits(n):
    sum=int(0)
    for i in n:
        i=int(i)
        sum+=i
    return sum;

n=input("Enter positive number:")
print("sum of digits of" ,n, " is ", sumdigits(n))
