#complete_binarytree.py
from binarytree_practice1 import build_binarytree,print_binarytree

def count_nodes(root,count):
	if root!=None:
		count[0]+=1
		count_nodes(root.left,count)
		count_nodes(root.right,count)
	return count[0]

inp=input("enter the nodes of tree seperated by spaces:")
inp=inp.split()
root=build_binarytree(inp)
print(count_nodes(root,[0]))