#binarytree12.py
#construct binary tree from preorder,inorder traversal

from binarytree1 import build_binarytree,print_binarytree


class BT:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def constructBT(preorder,inorder):
	inorder_left=[]
	inorder_right=[]
	preorder_left=[]
	preorder_right=[]

	if not(preorder) or not(inorder):
		return None
	root=BT(preorder[0])
	for i in range(len(inorder)):
		if inorder[i]==root.data:
			inorder_left=inorder[:i]
			inorder_right=inorder[i+1:]
			preorder_left=preorder[1:len(inorder_left)+1]
			preorder_right=preorder[len(inorder_left)+1:]
		
		root.left=constructBT(preorder_left,inorder_left)
		root.right=constructBT(preorder_right,inorder_right)
	return root

Arr1=input("enter the preorder:")
Arr1=list(map(int,Arr1.split()))
Arr2=input("enter the inorder:")
Arr2=list(map(int,Arr2.split()))
root=constructBT(Arr1,Arr2)

print_binarytree(root)