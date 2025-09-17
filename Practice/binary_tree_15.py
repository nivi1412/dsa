#binarytree15.py
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal
# of the same tree, construct and return the binary tree.

from binarytree1 import build_binarytree,print_binarytree

class BT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.righ=None

def constructBT(Arr1,Arr2):
	inorder_right=[]
	inorder_left=[]
	postorder_right=[]
	postorder_left=[]
	if not(len(Arr1)) or not(len(Arr2)):
		return None
	root=BT(Arr1[-1])
	for i in range(len(Arr2)):
		if Arr2[i]==root.data:
			inorder_left=Arr2[:i]
			inorder_right=Arr2[i+1:]
			postorder_left=Arr1[:i]
			postorder_right=Arr1[i:i+len(inorder_right)]
		#print(postorder_left,postorder_right,inorder_right,inorder_left)
		root.left=constructBT(postorder_left,inorder_left)
		root.right=constructBT(postorder_right,inorder_right)
	return root


Arr1=input("enter the postorder:")
Arr1=list(map(int,Arr1.split()))
Arr2=input("enter the inorder:")
Arr2=list(map(int,Arr2.split()))
root=constructBT(Arr1,Arr2)

print_binarytree(root)
