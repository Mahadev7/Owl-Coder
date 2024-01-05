a = [7,1,5,2,9]
n = len(a)
m = []
for i in range(n):
    m.append([0] * 32)
    for j in range(32,-1,-1):
        if a[i] & (1<<j): # set 
            m[i][31-j] = 1
        else:
            m[i][31-j] = 0
for i in range(1,n):
    for j in range(31,-1,-1):
        m[i][31-j] += m[i-1][31-j]
print(m,end = ' ')
l,r = 0,2
re = 0
for i in range(31,-1,-1):
    if (r-l+1) == m[r][31-i]:
        re += 2 ** i
print(re)
