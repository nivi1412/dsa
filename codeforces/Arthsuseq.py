#Arthsuseq.py

import ast

arr=input("enter array: ")
arr=ast.literal_eval(arr)
k=int(input("enter the difference:"))

arr=list(set(arr))
arr.sort()
print("array input:",arr)
my_dict={}

for ele in arr:
	my_dict[ele]=False

final_list=[]
local=[arr[0]]
i=0
while (i<len(arr) and my_dict[arr[i]]==False):
	my_dict[arr[i]]=True
	if local[-1]+k in arr and my_dict[local[-1]+k]==False:
		my_dict[local[-1]+k]=True
		local.append(local[-1]+k)
	else:
		final_list.append(local)
		local=[arr[i]]
	i+=1
print(final_list)

# 	j=0
# 	while(j<len(arr)):
# 		if local[-1]+k in arr and my_dict[local[-1]+k]==False:
# 			my_dict[local[-1]+k]=True
# 			local.append(local[-1]+k)
# 			j+=1
# 		else:
# 			break
# 	final_list.append(local)
# 	i+=1
# 	local=[]
# print(final_list)