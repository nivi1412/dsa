#Validatebinarytree.py
from binarytree_practice1 import build_binarytree,print_binarytree

def validatebinarytree(root,left_lim,right_lim):
	if root ==None:
		return True
	else:
		if not (left_lim<int(root.data)<right_lim):
			return False
		left=validatebinarytree(root.left,left_lim,int(root.data))
		right=validatebinarytree(root.right,int(root.data),right_lim)
		return (left and right)

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
right_lim=10000
left_lim=0
print(validatebinarytree(root,left_lim,right_lim))