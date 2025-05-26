#symmetric_p.py

from binarytree_practice1 import build_binarytree,print_binarytree

def symmetric(left,right):
	if left !=None and right!=None:
		if left.data == right.data:
			return symmetric(left.left,right.right) and symmetric(left.right,right.left)
		return False
	elif left==None and right ==None:
		return True
	return False


inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
if root.left!=None and root.right!=None:
	print(symmetric(root.left,root.right))
elif root.left ==None and root.right ==None:
	print(True)
else:
	print(False)