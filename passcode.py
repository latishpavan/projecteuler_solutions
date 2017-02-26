import operator
with open("p79.txt") as f:
    lines=f.read().splitlines()

a={}
k=1
for i in lines:
    for j in i:
        if j not in a:
             a[j]=k
             k+=1

while True:
    change=0
    for i in lines:
        if a[i[0]]>a[i[1]]:
            a[i[0]],a[i[1]]=a[i[1]],a[i[0]]
            change+=1
        if a[i[0]]>a[i[2]]:
            a[i[0]],a[i[2]]=a[i[2]],a[i[0]]
            change+=1
        if a[i[1]]>a[i[2]]:
            a[i[1]],a[i[2]]=a[i[2]],a[i[1]]
            change+=1
    if change==0:
        break

a=sorted(a.items(),key=operator.itemgetter(1))
num=''
for i in a:
    num+=i[0]
print(num)
