def Fact(n):
    f = [1]
    for i in range(2,n+1):
        c = 0
        for j in range(len(f)):
            p = f[j] * i + c
            f[j] = p % 10
            c = p//10
        while c:
            f.append(c%10)
            c //= 10
    p = int(''.join(map(str,f[::-1])))
    return p
n = int(input())
print(Fact((n)))
