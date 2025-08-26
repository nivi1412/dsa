# DP_jumpahead.py
import ast

nums=input("enter the array:")
nums=ast.literal_eval(nums)

dp=[10000 for _ in range(len(nums))]
dp[0]=0

for i in range(len(nums)):
	for k in range(1,nums[i]+1):
		print("i,k:",i,k)
		if i+k < len(nums):
			dp[i+k]=min(dp[i+k],1+dp[i])

print(dp[-1])
