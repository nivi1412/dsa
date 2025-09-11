#DP_Besttimetibuysell.py
import ast

prices=input("enter the array: ")
prices=ast.literal_eval(prices)

dp=[[0 for _ in range(len(prices))],[0 for _ in range(len(prices))]]

#min buy
dp[0][0]=prices[0]
#max_sell
dp[1][0]=0

for i in range(1,len(prices)):
	if prices[i]<dp[0][i-1]:
		dp[0][i]=prices[i]
	else:
		dp[0][i]=dp[0][i-1]

	if prices[i]-dp[0][i-1]>dp[1][i-1]:
		dp[1][i]=prices[i]-dp[0][i-1]
	else:
		dp[1][i]=dp[1][i-1]

print(dp)
print(dp[1][len(prices)-1])

