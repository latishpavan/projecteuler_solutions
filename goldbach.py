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

def check(a,n) :
    p=0
    for i in a :
        if i<n :
            k=math.sqrt((n-i)/2)
            if k>0 and int(k)/k==1 :
                p=1
    if p==0 :
        return n
    return 0

a=prime(10**5)
for i in range(4,10**5):
    if i not in a:
        if check(a,i) and i%2!=0:
            print(i)
            break
