def palindrome(s):
    n=len(s)
    for i in range(int(n/2)):
        if s[i]!=s[n-i-1]:
            return 0
    return 1

count=0
for i in range(1,1000001):
    b=bin(i)
    if palindrome(str(i))==1 and palindrome(b[2:]):
        count+=i
print(count)
