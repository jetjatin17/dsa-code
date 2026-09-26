# make it such that the sequence of the numbers in the list remains the same for the pivot reference.
# like if for nums below 10 the order is 9,5,3 and above 10 is 12,14. order is not ascending
# or descending, it just follows the numbers sequence in the list before the pivot.


nums = [9,12,5,10,14,3,10]
pivot = 10
low = []
high = []
l = len(nums)
for i in range (0,l):
    if (nums[i]<pivot):
        low.append(nums[i])
    elif (nums[i]>pivot):
        high.append(nums[i])
    else :
        high.insert(0,nums[i])
new = low + high
nums = new
for i in range (0,l):
    print(nums[i]) 