#binarytree5.py
#mindepth of binarytree

from binarytree_lib import build_binarytree

def min_depth(root):
	if root == None:
		return 0
	return(1+min(min_depth(root.left),min_depth(root.right)))



inp= input("enter nodes of the binary tree seperated by spaces")
inp=inp.split()

root=build_binarytree(inp)
print(min_depth(root))