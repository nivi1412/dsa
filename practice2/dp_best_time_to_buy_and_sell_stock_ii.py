#DP_BestTimetoBuyandSellStockII.py

import ast

prices=input("enter the prices array: ")
prices=ast.literal_eval(prices)

dp=[0 for _ in range(len(prices))]

dp[1]=prices[1]-prices[0]

for i in range(1,len(prices)):
	print(dp)
	dp[i]=max(dp[i-1],dp[i-1]+(prices[i]-prices[i-1]),(prices[i]-prices[i-1]))

print(dp[-1])

# max_profit=0

# for i in range(1,len(prices)):
# 	if prices[i]>prices[i-1]:
# 		max_profit+= prices[i]-prices[i-1]
# print(max_profit)