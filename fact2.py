def fun(n):
    if n == 1 or n == 0:
        return 1
    return n * fun(n-1)
n = int(input())
print(fun(n))
 # 5 * fun(4)
 # 4 * fun(3)
 # 3 * fun(2)
 # 2 * fun(1)
 # 1 * fun(0)
print(2**.05)
c = (1/2)*(2)
print(c)
