# maxsubarray_revise.py
# dp[i] is max sum of the subarray ending with i

import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]
dp[0]=nums[0]

for i in range(1,len(nums)):
	dp[i]=max(nums[i],nums[i]+dp[i-1])

print(max(dp))