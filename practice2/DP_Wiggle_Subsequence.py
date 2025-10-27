# DP_Wiggle_Subsequence.py

import ast

nums=input("enter the list of numbers: ")
nums=ast.literal_eval(nums)

up=[1 for _ in range(len(nums))]
down=[1 for _ in range(len(nums)) ]

for i in range(1,len(nums)):
	for j in range(i):
		if nums[i]>nums[j]:
			up[i]=max(up[i], 1+down[j])
		if nums[i]<nums[j]:
			down[i]=max(down[i], 1+up[j])


print(max(up[-1],down[-1]))