#max_product_subarray.py
import ast
import math

nums=input("enter the array:")
nums=ast.literal_eval(nums)

minproduct=nums[0]
maxproduct=nums[0]
result=-math.inf

for i in range(1,len(nums)):
	if nums[i]<0:
		minproduct,maxproduct=maxproduct,minproduct
	minproduct=min(minproduct*nums[i],nums[i])
	maxproduct=max(maxproduct*nums[i],nums[i])

	result=max(maxproduct,result)
print(result)
