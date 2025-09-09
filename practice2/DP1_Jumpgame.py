#DP1_Jumpgame.py
import ast

nums=input("enter the array:")
nums=ast.literal_eval(nums)

dp=[10000 for _ in range(len(nums))]
dp[0]=0

# for i in range(len(nums)):
# 	for j in range(1,dp[i]+1):
# 		dp[j]=min(dp[j],1+dp[i])
