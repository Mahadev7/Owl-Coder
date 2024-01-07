def String(n,k):
    p = n[:k]
    q = n[k:]
    return p[::-1] + q
n = input() # abcdefg 
k = int(input()) # 
l = len(n)
a = n[:2*k]
b = n[2*k:]
if len(b)<2*k:
    print(String(a,k) + String(b,k))
else:
    b = n[2*k:-1*k]
    c = n[-1*k:]
    print(String(a,k) + String(b,k)+ String(c,k))

