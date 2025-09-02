# BT_Validate_Binary_Tree.py
from build_binarytree import build_binarytree,print_binarytree

def validata_BST(root,prev_root,is_left)->bool:
	left=True
	right=True
	if root==None:
		return True
	print("root,prevroot,isleft",root.data,prev_root,is_left)

	if prev_root:
		if is_left and root.data > prev_root:
			return False
		if not is_left and root.data < prev_root:
			return False

	left=validata_BST(root.left,root.data,True)
	right=validata_BST(root.right,root.data,False)

	return left and right


inp=input("enter the nodes seperated by spaces:")
inp=list(inp.split())
root=build_binarytree(inp)
print(validata_BST(root,prev_root=None,is_left=None))
