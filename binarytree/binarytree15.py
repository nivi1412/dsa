#binarytree15.py
#diameter of the binarytree: its depth of each node 

from binarytree_lib import build_binarytree

def find_depth(root,my_dict):
	if root==None:
		return 0
	if root.data in my_dict:
		return my_dict[root.data]
	my_dict[root.data]=1+max(find_depth(root.left,my_dict),find_depth(root.right,my_dict))
	return my_dict[root.data]

def __inorder_traversal(root,prev_dia,my_dict):
		if root.left != None:
			__inorder_traversal(root.left,prev_dia,my_dict)
		if root!=None:
			dl = find_depth(root.left, my_dict)
			dr = find_depth(root.right, my_dict)
			if dl+dr > prev_dia[0]:
				prev_dia[0]=dl+dr

		if root.right != None:
			__inorder_traversal(root.right,prev_dia,my_dict)
		return prev_dia

def inorder_traversal(root):
	my_dict={}
	find_depth(root,my_dict)
	print(my_dict)
	return __inorder_traversal(root,[0],my_dict)

inp=input("enter the nodes of the binary tree seprated by spaces:")
inp=inp.split()
root=build_binarytree(inp)
print("max diameter of Node:",root.data,"is :",inorder_traversal(root))

