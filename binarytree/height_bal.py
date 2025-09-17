#heightbal.py
from binarytree_practice1 import build_binarytree,print_binarytree

def heightbal(root):
	if root !=None:
		print(root.data)
		max_depth=maxdepth(root)
		min_depth=mindepth(root)
		print(max_depth,min_depth)
		if max_depth-min_depth >1:
			return False
		return True
	return True


def maxdepth(root):
	if root!=None:
		return 1+max(maxdepth(root.left),maxdepth(root.right))
	return 0
def mindepth(root):
	if root!=None:
		return 1+min(mindepth(root.left),mindepth(root.right))
	return 0


inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print(heightbal(root))