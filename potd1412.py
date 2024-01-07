grid =[[0,1,1],[1,0,1],[0,0,1]]
p,q,x,y = [],[],[],[]
for i  in grid:
    a = i.count(1)
    p.append(a)
g = list(zip(*grid))
for i in g:
    b = i.count(1)
    q.append(b)
print(p) #3 [3,3]
print(q) # 2 [2,2,2]
for i  in grid:
    a1 = i.count(0)
    x.append(a1)
g = list(zip(*grid))
for i in g:
    b1 = i.count(0)
    y.append(b1)
print(x,y)
for i in range(len(x)):
    for j in range(len(y)):
        grid[i][j] =  p[i] + q[j] - x[i] - y[j]
print(grid)
