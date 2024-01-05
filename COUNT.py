n = int(input())
a,b = 1,1
l = []
m = (10**9) + 7
for i in range(n):
    r = a%m+b%m
    a = b
    b = r
    l.append(b)    
print(sum(l))
print((r*r)%m)
