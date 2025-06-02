#uniquebinarysearchtrees II.py

# Learnings:
# 1. list of lists should be returned
# 2. syntax of left list right list division
# 3. final list initize outside for loop


def generate_binarytrees(my_list):
	tree_list=[]
	if len(my_list)==0:
		return [["null"]]
	if len(my_list)==1:
		tree_list.append([my_list[0]])
		return tree_list
	else:
		final_list=[]
		for i in range(len(my_list)):
			root=my_list[i]
			left_subtree=my_list[:i]
			right_subtree=my_list[i+1:]
			left=generate_binarytrees(left_subtree)
			right=generate_binarytrees(right_subtree)
			for i in left:
				for j in right:
					local=[]
					local.append(root)
					for ele in i:
						local.append(ele)
					for ele in j:
						local.append(ele)
					final_list.append(local)
		return final_list


#make list of input range
inp=int(input("enter number of nodes of binary tree"))
my_list=[]

for i in range(inp):
	my_list.append(i+1)

print(generate_binarytrees(my_list))

