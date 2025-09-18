# DP1_Maximum_Subarray.py

import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

max_sum=-10000
cur_sum=0

j=1
dp=[0 for _ in range(len(nums))]
dp[0]=nums[0]

while(j<len(nums)):
	cur_sum=max(nums[j],nums[j]+dp[j-1])
	dp[j]=cur_sum
	max_sum=dp[j] if dp[j]>max_sum else max_sum
	j+=1
cur_sum=0
print(max_sum)