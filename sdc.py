a={}
def calculate(n):
    dup=str(n)
    while True:
        tot=0
        for i in dup:
             tot+=int(i)**2
        if tot==89 or str(tot) in a:
            a[n]=1
            return 1
        if tot==1:
            return 0
        dup=str(tot)

count=0
for i in range(1,10000000):
    if calculate(i):
        count+=1
print(count)
