n = [1,1,1,2,3,3,3]
c  = 0
ans = 0
l = []
for i in range(32):
    c=0
    for j in range(len(n)): 
        if n[j] & (1<<i):
            c += 1
    if c%3 != 0:
        ans |= 1<<i
print(ans)
