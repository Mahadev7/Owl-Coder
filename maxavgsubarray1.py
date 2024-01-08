def Good(x,k):
    p =  sum(x)/k
    r = '%.5f'%p
    return r
arr = [5]
k = int(input())
n = len(arr)
l = []
for i in range(n-k+1):
    pi = Good(arr[i:i+k],k)
    l.append(pi)
ma = max(l)
print(ma)
