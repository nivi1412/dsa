#binarytree9.py
#print all the nodes in a complete binary tree in O(n)
from binarytree_lib import build_binarytree

def node_count(root):
	if root == None:
		return 0
	return 1+(node_count(root.left)+node_count(root.right))


inp=input("enter the array of elements")
inp=inp.split()

count=0
root=build_binarytree(inp)
print(node_count(root))