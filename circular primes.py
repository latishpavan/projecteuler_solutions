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
def check(a) :
    s=list(str(a))
    s=list(map(int,s))
    for i in s:
        if i%2==0 :
            return 0
    return 1
def circular(a,n) :
    s=list(str(n))
    temp=tuple(s)
    k=len(s)
    while k :
        s[0]=temp[-1]
        for i in range(0,len(s)-1):
            s[i+1]=temp[i]
        temp=tuple(s)
        t=int(''.join(s))
        if t not in a :
            return 0
        k-=1
    return 1

a=prime(10**6)
t=0
b=[]
for i in a:
    if check(i) :
        b.append(i)
for i in b:
    if circular(b,i) :
        t+=1
        print(i)
print(t)
