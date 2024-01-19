import math
def powerset(arr,n):
    m = []
    p = (int) (math.pow(2,n))
    for i in range(0,p):
        l = []
        for j in range(0,n):
            if (i & (1<<j)):
                l.append(arr[j])
        m.append(l)
    return m
n = int(input())
a = list(map(int,input().split()))
print(powerset(a,n))
