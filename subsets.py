n = int(input())
x = list(map(int,input().split()))
l = []
for i in range(n):
    for j in range(i+1,n+1):
        l.append(x[i:j])
print(l)
