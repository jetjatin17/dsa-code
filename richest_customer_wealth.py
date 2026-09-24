accounts = [[2,8,7],[7,1,3],[1,9,5]]
l = len(accounts)
largest = 0
for i in range (0,l):
    n = len(accounts[i])
    sum = 0
    for j in range (0,n):
        sum = sum + accounts[i][j]
    if (sum>=largest):
        largest = sum
print(largest)