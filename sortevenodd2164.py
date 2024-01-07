nums = [4,1,2,3]
a,b,ev,od = [],[],[],[]
for i in range(len(nums)):
    if i%2 == 0:
        ev.append(i)
        a.append(nums[i])
    else:
        od.append(i)
        b.append(nums[i])
a.sort()
b.sort(reverse = True)
print(ev)
print(od)
l = []
for i in range(len(a)):
    nums[ev[i]] = a[i] # nums[0] = 2,nums[1] = 4 
for j in range(len(b)):
    nums[od[j]] = b[j] # nums[1] = 3 # nums[3] = 1
print(nums)