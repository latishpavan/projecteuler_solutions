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

a=prime(1000000)
b=dict.fromkeys(a)
n=len(a)
fin=0
for i in range(n):
    count=a[i]
    k=1
    for j in range(i+1,n):
        count+=a[j]
        k+=1
        if b.has_key(count):
            if k>fin:
                fin=k
                ans=count
                print(ans)

       
