nums = [437,315,322,431,686,264,442]
l = len(nums)
output = 0
for i in range (0,l):
    n = nums[i]
    temp = n
    digit = 0
    while (n!=0):
        n=n//10
        digit+=1
    print(f"{temp} = {digit}")
    if (digit%2==0):
        output+=1
print(output)