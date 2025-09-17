#binarytree3.py
#check if binary tress is symmetrcal at its root

from binarytree_lib import build_binarytree, print_binarytree

def check_symmetry(left,right):
	if left != None and right != None:
		if left.data==right.data:
			return (check_symmetry(left.left,right.right) and check_symmetry(left.right,right.left))
		else:
			return False
	if left != None and right == None:
		return False
	if left == None and right != None:
		return False
	if left== None and right == None:
		return True

inp=input("enter the tree values seperated by spaces:")
inp=inp.split()

root=build_binarytree(inp)
print(check_symmetry(root.left,root.right))

