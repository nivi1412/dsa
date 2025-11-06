# houserobber.py
import ast

nums=input("enter the nums array: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]

dp[0]=nums[0]
dp[1]=max(nums[0],nums[1])

for i in range(2,len(nums)):
	dp[i]=max(dp[i-2]+nums[i],dp[i-1])

print(dp)

print(dp[-1])