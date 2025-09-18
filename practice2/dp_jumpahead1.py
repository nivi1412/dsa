#DP_jumpahead1.py
#[3,0,10,0,0,0,0]
# [3,0,0,0,0,0,0,0] here unnecessory we will check for all the 0's should optimize

import ast

nums=input("enter the list: ")
nums=ast.literal_eval(nums)
last_index_reached=False
max_index=0

for i in range(len(nums)-1):
	if i >max_index:
		break
	index=i+nums[i]
	print(index)
	max_index=max(max_index,index)
	if max_index>=len(nums)-1:
		last_index_reached=True
		break
print(last_index_reached)



