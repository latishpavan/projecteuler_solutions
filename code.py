
def min_diff(a,n):
    a.sort()
    fin=a[1]-a[0]
    for i in range(n-1):
        temp=a[i+1]-a[i]
        if temp<fin :
            fin=temp
    return fin+1,a[-1]+a[-2]-1

n,l,r=input().split(' ')
n,l,r=int(n),int(l),int(r)
v=[int(i) for i in input().split(' ')]
a,b=min_diff(v,n)
if l<=a and r>=b:
    print((b-a)+1)
if l>a and r>=b:
    print(b-l+1)
if l<=a and r<b:
    print(r-a+1)
if l>a and r<b:
    print(r-l+1)
