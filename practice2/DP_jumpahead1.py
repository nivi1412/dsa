#DP_jumpahead1.py
#[3,0,10,0,0,0,0]
import ast

nums=input("enter the list: ")
nums=ast.literal_eval(nums)
last_index_reached=False
max_steps=0

for i in range(len(nums)-1):
	index=i+nums[i]
	print(index)
	max_index=max(0,index)
	if max_index>=len(nums)-1:
		last_index_reached=True
		break
print(last_index_reached)



