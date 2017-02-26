def check(a,b,c) :
    s=list(str(a))
    s+=list(str(b))
    s+=list(str(c))
    s=list(map(int,s))
    t=0
    if len(s)==9 :
        for i in range(1,10) :
            if i in s:
                t+=1
    if t==9 :
        return 1
    return 0
a=[]
for i in range(1,9999) :
    for j in range(1,1000) :
        k=i*j
        if check(i,j,k) and k not in a:
            a.append(k)
print(a)
print(sum(a))
            
