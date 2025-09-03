# BT_BTfrompreandinorderlist.py
import ast
from build_binarytree import print_binarytree
class tree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def construct_BT(preorder,inorder):
	if not preorder or not inorder:
		return None
	root=tree(preorder[0])
	index=inorder.index(preorder[0])
	inorder_left=inorder[:index]
	inorder_right=inorder[index+1:]
	preorder_left=preorder[1:len(inorder_left)+1]
	preorder_right=preorder[len(inorder_left)+1:]

	root.left=construct_BT(preorder_left,inorder_left)
	root.right=construct_BT(preorder_right,inorder_right)

	return root

preorder=input("enter the po list: ")
preorder=ast.literal_eval(preorder)
inorder=input("enter the io list: ")
inorder=ast.literal_eval(inorder)

root=construct_BT(preorder,inorder)

print_binarytree(root)