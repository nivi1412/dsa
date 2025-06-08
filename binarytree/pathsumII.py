#pathsumII.py
from binarytree_practice1 import build_binarytree,print_binarytree


# def pathsumII(root,target_sum):
# 	if root.left == None and root.right ==None and target_sum==0:
# 		leaf_list=[root.data]
# 		return leaf_list
# 	result=[]
# 	if root.left!=None:
# 		left=pathsumII(root.left,target_sum)
# 		for i in left:
# 			result.append(i)
# 	if root.right !=None:
# 		right=pathsumII(root.right,target_sum)
# 		for i in right:
# 			result.append(i)
# 	for i in range(len(result)):
# 		result[i]=root.data+result[i]
# 	return result

def pathsumII(root, target_sum):
	if root==None: 
		return []
	target_sum=target_sum-int(root.data)
	print("data",root.data)
	if root.left==None and root.right ==None and target_sum==0:
		print(root.data)
		return [[root.data]]
	
	left=pathsumII(root.left,target_sum)
	right=pathsumII(root.right,target_sum)


	local=[]
	for i in left:
		i.insert(0,root.data)
		local.append(i)
	for i in right:
		i.insert(0,root.data)
		local.append(i)


	return local

inp=input("enter the nodes of tree seperated by spaces").split()
target_sum=int(input("enter the target sum:"))
root=build_binarytree(inp)

print(pathsumII(root,target_sum))
