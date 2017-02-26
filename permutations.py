import time

def main():
    pass

def first(s):
    global n
    for i in range(n-1,0,-1):
        if int(s[i-1])<int(s[i]):
            return i-1
    return -1

def second(s,i):
    global n
    a=[]
    k=int(s[i])
    for j in range(i+1,n):
        if int(s[j])>k:
            a.append(s[j])
    return s.index(min(a))

def sort_it(p):
    p=sorted(p)
    p=''.join(p)
    return p

def check(s):
    primes=[2,3,5,7,11,13,17]
    for i in range(1,7):
        if int(s[i:i+3])%primes[i-1]!=0:
            return 0
    return 1

def get(s):
    global a
    a=[s]

s=time.time()
if __name__=="__main__":
    main()
a=[]
n=4
count=1
tot=0
while True:
    p=a[-1]
    k=first(p)
    l=second(p,k)
    p=list(p)
    p[k],p[l]=p[l],p[k]
    p=''.join(p)
    p=p[0:k+1]+sort_it(p[k+1:])
    a.append(p)
    count+=1
    if count==23:
        break
print(a)
print(time.time()-s)
