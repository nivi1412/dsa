
from binarytree1 import build_binarytree,print_binarytree

class BT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def insertintoBT(root,val):
	if root==None:
		node=BT(val)
		return node
	if root.data<val:
		right=insertintoBT(root.right,val)
		root.right=right
	else:
		left=insertintoBT(root.left,val)
		root.left=left
	return root

Arr=input("enter elements of binarytree")
Arr=Arr.split()
val=input("enter the value to be inserted:")
root=build_binarytree(Arr)
insertintoBT(root,val)
print_binarytree(root)