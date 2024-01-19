a = int(input())
b = int(input())
r = 1
while b:
    if b & 1:
        b = b-1
        r *= a
    else:
        b //= 2
        a *= a
print(r)
