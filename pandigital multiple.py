def pandigit(a,b) :
    s=list(str(a))
    s+=list(str(b))
    k=''.join(s)
    s=list(map(int,s))
    for i in range(1,10) :
        if i not in s :
            return 0
    return int(k)

fin=0
for i in range(9000,10000) :
    temp=pandigit(i,i*2)
    if temp :
        if temp>fin :
            fin=temp
print(fin)
    
