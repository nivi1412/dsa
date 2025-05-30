#minabsdiff.py
from binarytree_practice1 import build_binarytree,print_binarytree

def minabsdiff(root,my_dict):
	
	if root!=None:
		print(root.data,my_dict["prev_node"])
		diff=abs(int(root.data)-int(my_dict["prev_node"]))
		my_dict["prev_diff"]=min(diff,my_dict["prev_diff"])
		my_dict["prev_node"]=root.data
	if root.left!=None:
		minabsdiff(root.left,my_dict)
	if root.right!=None:
		minabsdiff(root.right,my_dict)

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_dict={}
my_dict["prev_node"]=10**5
my_dict["prev_diff"]=10**5
minabsdiff(root,my_dict)
print("min diff",my_dict["prev_diff"])