#DP_LIS.py
import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]

dp[0]=1

for i in range(1,len(nums)):
	dp[i]=1+dp[i-1] if nums[i]>nums[i-1] else dp[i-1]

print(dp[-1])