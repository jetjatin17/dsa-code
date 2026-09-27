prices = [1,2,2]
money = int(input("enter the money : "))

l = len(prices)
prices.sort()
if ((prices[0]+prices[1])<=money):
    money = money - prices[0] - prices[1]

print(money)