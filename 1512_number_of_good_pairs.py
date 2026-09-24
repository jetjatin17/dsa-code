nums = [1,2,3]
l = len(nums)
pair = 0
for i in range (0,l):
    for j in range (i,l):
        if (j==i):
            continue
        if (nums[j] == nums[i]):
            pair+=1
print(pair)