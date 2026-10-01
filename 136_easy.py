nums = [4,1,2,1,2]
l = len(nums)
nums.sort()
for i in range (0,l-1,2):
    if (nums[i] != nums[i+1]):
        print(nums[i])
        print("done")
else:
    print(nums[l-1])