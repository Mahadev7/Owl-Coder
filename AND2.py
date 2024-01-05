def AND(a,l,r):
    s = 1
    for i in range(l,r+1):
        s &= a[i]
    return s
    
a = [7,1,5,2,3,9]
for i in range(int(input())):
    l,r = map(int,input().split())
    p = AND(a,l,r)
    print(p)
