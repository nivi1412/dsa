#DP1_Jumpgame.py
import ast

nums=input("enter the array:")
nums=ast.literal_eval(nums)

dp=[100000 for _ in range(len(nums))]
dp[0]=0

for i in range(len(nums)-1):
	for j in range(1,nums[i]+1):
		if (i+j)<len(nums):
			dp[i+j]=min(dp[i+j],1+dp[i])

print(dp[-1])