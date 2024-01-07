def String(n,k):
    p = n[:k]
    q = n[k:]
    return p[::-1] + q
n = input() # abcdefg
k = int(input())
l = len(n)
a = n[:2*k]
b = n[2*k:]
print(String(a,k) + String(b,k))
print(l)

# 100 - length
# 20 - step size
# 40,40
# 
