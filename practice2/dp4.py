#dp4.py
import ast
import math

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]
max_sum=-math.inf
dp[0]=nums[0]

for i in range(1,len(nums)):
	dp[i]=max(dp[i-1]+nums[i],nums[i])

print(max(dp))