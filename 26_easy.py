nums = [0,0,1,1,1,2,2,3,3,4]

l = len(nums)
j = 1
for i in range (1,l):
    if nums[i]>nums[j-1]:
        nums[j] = nums[i]
        j+=1
for i in range (0,j):
    print(nums[i])