
def initprimes(num,primes):
    num=int (num)
    for i in range(3,1+int(num/2)):
        i=int(i)
        if num%i==0:
            primes.append(i)

t=int(input())
k=int(0)
while(k<t):
    primes=[]
    in1=input().split()
    n=int(in1[0])
    l=int(in1[1])
    encrypt=input().split()
    first= int(encrypt[0])
    initprimes(first,primes)
    if int(encrypt[1])%int(primes[0])==0:
        div=int(encrypt[1]/primes[0])

    elif (int(encrypt[1])%int(primes[1])==0):
        div=int(int(encrypt[1])/int(primes[1])
    # ~ else:
        # ~ div= int(-1)

    primes.append(div)
    for i in range(2,n):
        zipkey=int(primes[i])
        ziplock=int(encrypt[i])
        primes.append(int(ziplock/zipkey))

    print(primes.sorted())
    primes.clear()
    k+=1
