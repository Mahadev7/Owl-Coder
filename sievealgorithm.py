n = int(input())
x = [1] * n
x[0] = x[1] = 0
for i in range(2,n):
    if x[i] == 1:
        for j in range(i*i,n,i):
            x[j] = 0
print(x)
