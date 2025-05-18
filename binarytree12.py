#binarytree12.py
#find sum of leftleaf nodes

from binarytree_lib import build_binarytree

def __sum_leftleaves(root, is_left: bool):
	if root.left==None and root.right==None:
		if is_left:
			return int(root.data)
		else:
			return 0
	if root.left!=None:
		val_l=__sum_leftleaves(root.left, True)
		print("l:",val_l)
	if root.right !=None:
		val_r=__sum_leftleaves(root.right, False)
		print("r:",val_r)
	return val_l+val_r

def sum_of_left_leaves(root):
	return __sum_leftleaves(root, False)

def __sum_rightleaves(root,is_right):
	if root.left == None and root.right == None:
		if is_right:
			return int(root.data)
		else:
			return 0
	if root.left!=None :
		val_l=__sum_rightleaves(root.left,False)
	if root.right!=None:
		val_r=__sum_rightleaves(root.right,True)
	return val_r+val_l

def sum_rightleaves(root):
	return __sum_rightleaves(root,False)

inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print(sum_of_left_leaves(root))
print(sum_rightleaves(root))