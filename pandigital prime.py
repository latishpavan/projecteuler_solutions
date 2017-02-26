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

def check(n) :
    a=list(str(n))
    a=list(map(int,a))
    for i in range(1,8) :
        if i not in a:
            return 0
    return 1

a=prime(10**7)
b=[]
for i in a:
    if check(i)==1 :
        b.append(i)
print(b[-1])
