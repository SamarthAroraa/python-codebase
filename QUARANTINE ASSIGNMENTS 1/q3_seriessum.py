def series_sum(n):
    numerator= float(1)
    denominator=float(2)
    sum=float(0)
    while(numerator<=n):
        sum+=float(numerator/denominator)
        numerator+=1
        denominator+=1
    return sum
n=int(input("(1/2 + 2/3 + 3/4 +.....n/(n+1) )Sum upto n. Enter n: "))
print("series sum:", series_sum(n))
