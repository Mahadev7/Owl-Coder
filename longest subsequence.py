def sequence(nums):
    nums = sorted(nums)
    n = len(nums)
    l = []
    l.append(nums[0])
    for  i in range(1,n):
        if nums[i] > l [-1]:
            l.append(nums[i])
        else:
            lo = 0
            h = len(l)-1
            while lo<h:
                m = (lo+h)//2
                if l[m] < nums[i]:
                    lo = m+1
                else:
                    h = m
            l[lo] = nums[i]
    return len(l)
nums = [0,1,0,3,2,3]
print(sequence(nums))
