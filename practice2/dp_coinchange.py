# dp_coinchange.py
import math
import ast

coins=input("enter the coins array: ")
amount=int(input("enter the amount: "))
coins=ast.literal_eval(coins)

dp=[math.inf]*(amount+1)

dp[0]=0

for i in range(1,amount+1):
	for c in coins:
		if c <=i:
			dp[i]=min(dp[i],1+dp[i-c])

for i in range(len(dp)):
	if dp[i]==math.inf:
		dp[i]=-1

print(dp[-1])
