#binarytree18.py
from binarytree_lib import build_binarytree,print_binarytree

def is_equal(root,subroot):
	# a=True
	# b=True
	# c=True

	if root!=None and subroot!=None:
		a = is_equal(root.left,subroot.left)
		b = is_equal(root.right,subroot.right)
		print(root.data,subroot.data)
		c = root.data == subroot.data
		# if root.data != subroot.data:
		# 	return False
		# else:
		# 	c= True
		return a and b and c
		# if a and b and c: return True
		# else: return False
	elif root == None and root == None:
		return True
	else:
		return False
	
def subroot_check(root,subroot):
	# if root == None and subroot == None:
	# 	return True
	# elif root == None and subroot != None :
	# 	return False
	if root == None:
		return subroot == None
	return is_equal(root, subroot) or subroot_check(root.left, subroot) or subroot_check(root.right, subroot)
	# elif is_equal(root,subroot):
	# 	return True
	# elif subroot_check(root.left,subroot):
	# 	return True
	# elif subroot_check(root.right,subroot):
	# 	return True
	# else:
	# 	return False





inp=input("enter the nodes of the binary tree seprated by spaces:")
inp=inp.split()
subtree=input("enter the nodes of subtree to be comapared seperated by spaces")
subtree=subtree.split()
root=build_binarytree(inp)
subroot=build_binarytree(subtree)
print(subroot_check(root,subroot))











