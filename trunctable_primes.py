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

def right(s):
    s=str(s)
    n=len(s)
    for i in range(1,n):
        if a.has_key(int(s[i:])):
            continue
        else:
            return 0
    return 1

def left(s):
    s=str(s)
    n=len(s)
    for i in range(n-1,0,-1):
        if a.has_key(int(s[:i])):
            continue
        else:
            return 0
    return 1
    
a=prime(1000000)
count=0
a=dict.fromkeys(a)
for i in a:
    if right(i)==1 and left(i)==1:
        count+=i

print(count-17)
       
