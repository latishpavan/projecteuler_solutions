import math 
def prime(n):
    lst = range(0, n + 1)
    lst[1] = 0
    thres = int(math.sqrt(n)) + 1
    for i in xrange(2, thres):
        if lst[i] == 0:
            continue
        for j in xrange(i * 2, len(lst), i):
            if lst[j] != 0:
                lst[j] = 0
    return [i for i in lst if i != 0]

def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def no_of_primes(a,b):
    f=lambda n : n**2+(a*n)+b
    n=1
    p=1
    while 1:
        if f(n)<2:
            return p
        if isprime(f(n))==0:
            return p
        p+=1
        n+=1
        
a=prime(1000)
fin=0
for i in a:
    for j in range(-999,1000,2):
        k=no_of_primes(j,i)
        if k>fin:
            fin=k
            q,w=i,j
print(q*w)
        
