def check(n):
    sum=0
    for c in n:
        c=int(c)
        sum+=pow(c,3)
    print(sum)
    if(sum==int(n)):
        return 1
    return 0
a=input()
# b=int(inp/ut())
# print("entered number ")
print(check(a))
