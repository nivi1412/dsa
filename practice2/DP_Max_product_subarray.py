#DP_Max_product_subarray.py
import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)

max_num=[0 for _ in range(len(nums))]
min_num=[0 for _ in range(len(nums))]

max_num[0]=nums[0]
min_num[0]=nums[0]

for i in range(1,len(nums)):
	max_num[i]=max(nums[i],max_num[i-1]*nums[i],min_num[i-1]*nums[i])
	min_num[i]=min(nums[i],min_num[i-1]*nums[i],max_num[i-1]*nums[i])

	print(max_num[i],min_num[i])

print(max(max_num))