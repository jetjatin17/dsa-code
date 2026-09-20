
def reverse(x):
    min = -2**31
    max = (2**31)-1
    temp = x
    num = 0
    sign = -1 if x<0 else 1
    x*=sign
    while (x!=0):
        digit = x%10
        num = (num*10) + digit
        x = x//10
    num *= sign
    if (num > max or num < min):
        return 0
    return num
n = int (input ("enter the number : "))
result = reverse(n)
print(f"\n{result}")