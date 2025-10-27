#jump_game.py

import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

dp=[0 for _ in range(len(nums))]

for i in range(len(nums)):
	if nums[i]>0:
		dp[i]=max(dp[i],i+nums[i])








