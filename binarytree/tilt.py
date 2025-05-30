#tilt.py

from binarytree_practice1 import build_binarytree,print_binarytree

def sum_nodes(root,my_dict):
	if root==None:
		return 0
	if root in my_dict:
		return my_dict[root]

	my_dict[root]=sum_nodes(root.left,my_dict)+sum_nodes(root.right,my_dict)+int(root.data)
	return my_dict[root]

def tilt(root,my_dict):
	if root!=None:
		root.data=abs(sum_nodes(root.left,my_dict)-sum_nodes(root.right,my_dict))
		print(root.data)
	else:
		return 0
	tilt(root.left,my_dict)
	tilt(root.right,my_dict)

def tilttree_sum(root):
	if root==None:
		return 0
	return int(root.data)+tilttree_sum(root.left)+tilttree_sum(root.right)

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_dict={}
tilt(root,my_dict)
print_binarytree(root)
print("sum of nodes of tilted tree:", tilttree_sum(root))