#dp_coin_change.py
import ast
import math

coins=input("enter the coins array")
coins=ast.literal_eval(coins)
amount=int(input("enter the amount value: "))

# dp=[100000 for _ in range(amount)]
dp = [math.inf] * (amount + 1)

dp[0]=0

for i in range(1,amount+1):
	for c in coins:
		if c<=i:
			print(i,i-c)
			dp[i]=min(dp[i],1+dp[i-c])
			print(dp)
	dp[i]=1+dp[i]
for i in range(len(dp)):
	if dp[i]==math.inf:
		dp[i]=-1


print(dp)