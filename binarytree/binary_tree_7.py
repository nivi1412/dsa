#binarytree7.py
#invertedtree
#swap at each node, left and right

from binarytree_lib import build_binarytree, print_binarytree


def invert_tree_simple(root):
	if root == None:
		return root
	local = root.left
	root.left = root.right
	root.right = local
	invert_tree_simple(root.left)
	invert_tree_simple(root.right)

# def invert_tree(root):
# 	if root.left!=None and root.right!=None:
# 		local=root.left
# 		root.left=root.right
# 		root.right=local
# 		invert_tree(root.left)
# 		invert_tree(root.right)
# 	elif root.left!=None and root.right == None:
# 		root.right=root.left
# 		root.left=None
# 		invert_tree(root.right)
# 	elif root.left==None and root.right!=None:
# 		root.left=root.right
# 		root.right=None
# 		invert_tree(root.left)
# 	else:
# 		return


inp=input("enter the nodes of bin tree:")
inp=inp.split()

root=build_binarytree(inp)
invert_tree(root)
# def print_invtree(root):
# 	if root == None:
# 		return
# 	print(root.data)
# 	if root.left !=None:
# 		print_invtree(root.left)
# 	if root.right !=None:
# 		print_invtree(root.right)
# print_invtree(root)

print_binarytree(root)