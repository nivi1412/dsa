# dp_maxproductsubarray.py
import ast

nums=input("enter the nums array:")
nums=ast.literal_eval(nums)

min_num=[0 for _ in range(len(nums))]
max_num=[0 for _ in range(len(nums))]

min_num[0]=nums[0]
max_num[0]=nums[0]


for i in range(1,len(nums)):
	min_num[i]=min(nums[i],min_num[i-1]*nums[i],max_num[i-1]*nums[i])
	max_num[i]=max(nums[i],max_num[i-1]*nums[i],min_num[i-1]*nums[i])

print(max(max_num))