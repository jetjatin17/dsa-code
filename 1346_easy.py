# Check If N and Its Double Exist

arr = [10,2,5,3]
l = len(arr)
result = False
for i in range (0,l):
    for j in range (0,l):
        if (i==j):
            continue
        if (arr[i] == arr[j]*2):
            result = True
        
print(result)