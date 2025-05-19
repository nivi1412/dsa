#binarytree1.py
#[find depth of binary tree]

from binarytree_lib import build_binarytree,print_binarytree

def get_depth(root):
	if root is None:
		return 0
	return 1+(max(get_depth(root.left),get_depth(root.right)))

inp=input("enter the nodes of bin tree:")
inp=inp.split()

root=build_binarytree(inp)
print_binarytree(root)
print("depth of tree:",get_depth(root))