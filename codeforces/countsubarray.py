#countsubarray.py

import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)
k=int(input("enter the sum: "))
m=int(input("enter the max element: "))
count=0

prefix_array=[0]
for i in range(len(nums)):
	prefix_array.append(prefix_array[-1]+nums[i])

print(prefix_array)

for i in range(len(prefix_array)):
	if (prefix_array[i]-k in prefix_array):
		index=prefix_array.index(prefix_array[i]-k)
		print(nums[index:i])
		if i > index and max(nums[index:i])==m:
			count+=1
print(count)
			
