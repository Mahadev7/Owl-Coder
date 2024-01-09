def fun1(a1):
    x1 = a1[0]
    y1 = a1[1]
    return x1

def fun2(a):
    x2 = a[0]
    y2 = a[1]
    return y2

def fun3(b):
    x3 = b[0]
    y3 = b[1]
    return y3

def fun11(a):
    x2 = a[0]
    y2 = a[1]
    return x2

def fun33(a):
    x1 = a[0]
    y1 = a[1]
    return y1

def fun122(s):
    x3 = s[0]
    y3 = s[1]
    return x3

def fun21(a):
    x2 = a[0]
    y2 = a[1]
    return y2

p = [[1,1],[2,3],[3,2]]

a = fun1(p[0])
b = fun2(p[1])
c = fun3(p[2])

a1 = fun11(p[1])
c1 = fun33(p[0])

a2 = fun122(p[2])
b2 = fun21(p[1])


r  = abs( (a*(b - c)) +  (a1 * ( c - c1 )) + (a2 * ( c1 - b2 )))
re = r **0.5
if re > 0:
    print('True')
else:
    print('False')
