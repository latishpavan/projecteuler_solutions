def lychrel(n):
	for i in range(50):
		n+=int(str(n)[::-1])
		if n==int(str(n)[::-1]):
			return 0
	return 1

count=0
for i in range(10001):
	if lychrel(i):
		count+=1
print(count)