#jumpgame_revise.py
import ast
import math

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

dp=[math.inf for _ in range(len(nums))]
dp[0]=0

for i in range(len(nums)):
	for j in range(1,nums[i]+1):
		if i+j<len(nums):
			dp[i+j]=min(dp[i+j],1+dp[i])

print(dp[-1])