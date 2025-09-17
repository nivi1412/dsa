#maxdepth_p.py

from binarytree_practice1 import build_binarytree,print_binarytree, binarytree

def max_depth(root: binarytree) -> int:
	if root!=None:
		return 1+max(max_depth(root.left),max_depth(root.right))
	return 0

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print(max_depth(root))
