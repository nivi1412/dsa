#minabsdiff.py
from binarytree_practice1 import build_binarytree,print_binarytree

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
min_diff=[]
if root !=None and root.right !=None:
	min_diff.append(abs(int(root.data)-int(root.right.data)))
if root !=None and root.left !=None:
	min_diff.append(abs(int(root.data)-int(root.left.data)))
