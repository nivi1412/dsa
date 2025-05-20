#binarytree14.py

from binarytree_lib import build_binarytree

def min_difference(root):
	if root.left!=None:
		min_difference(root.left)
		# diff=abs(left-root.data)
		# if diff < diff_prev :
		# 	diff_prev=diff
	if root !=None:
		print (root.data)
	if root.right !=None:
		min_difference(root.right,diff_prev)


inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
#diff_prev=abs(root.data-root.left.data)
min_difference(root)