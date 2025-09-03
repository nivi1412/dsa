#DP_House_robber.py

import ast

nums=input("enter the list of homes: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]

dp[0]=nums[0]
dp[1]=max(nums[0],nums[1])

for i in range(2,len(nums)):
	dp[i]=max(dp[i-1],dp[i-2]+nums[i])

print(dp[-1])