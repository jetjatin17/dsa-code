arr = [3,4,5,2,1]

l = len(arr)
high = l-1
low = 0
while (high != low):
    mid = (high + low)//2
    if (arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
        print(mid)
        break
    if (arr[mid-1]<arr[mid]<arr[mid+1]):
        low = mid
        continue
    high = mid
            