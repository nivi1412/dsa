#DP1_Jumpgame1.py
import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)
max_index_reached=False
max_index=nums[0]
i = 0

while i <= max_index:
	index=nums[i]+i
	max_index=max(index,max_index)
	print("index:",index)
	if index>=len(nums)-1:
		max_index_reached=True
		break
	i+=1
print(max_index_reached)
		
