#invert_binarytree.py
from binarytree_practice1 import build_binarytree,print_binarytree

def invert_binarytree(root):
	if root.left!=None and root.right!=None:
		print(root.left.data,root.right.data)
		local=root.left
		root.left=root.right
		root.right=local
		invert_binarytree(root.left)
		return invert_binarytree(root.right)
	elif root.left!=None and root.right==None:
		print(root.left.data)
		root.right=root.left
		root.left=None
		return invert_binarytree(root.right)
	elif root.left==None and root.right!=None:
		print(root.right.data)
		root.left=root.right
		root.right=None
		return invert_binarytree(root.left)
	else: return 

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
invert_binarytree(root)
print_binarytree(root)