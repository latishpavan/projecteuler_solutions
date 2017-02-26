import math,time
def divisors(n):
    k=1
    for i  in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            k+=i
            if int(n/i)!=i:
                k+=int(n/i)
    if k>n:
        return n
    return 0
s=time.time()
a=[]
b={}
l=0
p=0
for i in range(1,28124):
    l+=i
    if divisors(i)==i:
        a.append(i)
for i in range(len(a)):
    for j in range(i,len(a)):
        k=a[i]+a[j]
        if k>28123:
            break
        else:
            if k not in b:
                b[k]=1
                p+=k
print(l-p)
print(time.time()-s)
