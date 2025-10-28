#jump_game.py

import ast
import math

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

max_index=0

i=0

while(i<len(nums)):
	if i>max_index:
		print(False)
		break
	max_index=max(max_index,i+nums[i])
	i+=1

if max_index>=len(nums)-1:
	print(True)

	






