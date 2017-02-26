import math as m

def isprime(n):
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def check(s,primes):
    for i in range(1,len(a)):
        diff=abs(int(a[i])-int(a[0]))
        if diff+a[0] not in primes:
            return 0
    return 1

a=[]
for i in range(1000,10000):
    if isprime(i):
        a.append(i)
for i in a:
    if check(str(i),a):
        print(i)
