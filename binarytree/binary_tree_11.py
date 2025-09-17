#binarytree11.py
#Given root of binary tree return all roo to leaf paths

from binarytree_lib import build_binarytree

# def root_leaf_print(root,lists):
# 	print(lists)
# 	if root.left!=None:
# 		lists.append(root.left.data)
# 		print("l:",root.left.data)
# 		root_leaf_print(root.left,lists)
# 	if root.right!=None:
# 		lists.append(root.right.data)
# 		print("r:",root.right.data)
# 		root_leaf_print(root.right,lists)
# 	if root.left == None and root.right == None:
# 		return lists

def binary_tree_paths(root):
	if root.left == None and root.right == None:
		leaf_list = [str(root.data)]
		return leaf_list
	lists = []
	if root.left != None:
		left_lists = binary_tree_paths(root.left)
		for l in left_lists:
			lists.append(l)
	if root.right != None:
		right_lists = binary_tree_paths(root.right)
		for l in right_lists:
			lists.append(l)
	for i in range(len(lists)):
		lists[i] = str(root.data) + "->" + lists[i]
	return lists

inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
# lists=[]
# print(root_leaf_print(root,lists))
lists = binary_tree_paths(root)
print(lists)