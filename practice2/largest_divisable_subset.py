#largest_divisable_subset.py
import ast

nums=input("enter the array: ")
nums=ast.literal_eval(nums)
Ans=[[nums[0]]]
divisable=False
local_list=[]

nums.sort()
for i in range(1,len(nums)):
	j=i-1
	divisable=False
	local_list=[]
	while(j>=0):
		if nums[i]%nums[j]==0:
			local=Ans[j].copy()
			local.append(nums[i]) 
			local_list.append(local)
			divisable=True
		j-=1
	length=max(len(llist) for llist in local_list)
	if not divisable:
		Ans.append([nums[i]])
	for llist in local_list:
		if len(llist)==length:
			Ans.append(llist)

max_len=max(len(sub) for sub in Ans)
for lists in Ans:
	if len(lists)==max_len:
		print(lists)
		break



