nums = [1,3,5,6]
target = int(input("enter the target value = "))
l = len(nums)
for i in range (0,l):
    if (target <= nums[i]):
        print(i)
        break
else:
    print(l)