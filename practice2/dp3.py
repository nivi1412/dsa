# dp3.py
import math
import ast
nums=input("enter the nums array: ")
nums=ast.literal_eval(nums)

dp=[math.inf for _ in range(len(nums))]
dp[0]=0
for i in range(len(nums)):
	for j in range(1,nums[i]+1):
		if (i+j)<len(nums):
			dp[i+j]=min(dp[i+j],1+dp[i]) 

print(dp)