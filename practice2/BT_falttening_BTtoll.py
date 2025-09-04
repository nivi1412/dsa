#BT_falttening_BTtoLL.py

from build_binarytree import build_binarytree, print_binarytree

class BT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def preordertraversal(root,Arr):
	if root!=None:
		Arr.append(BT(root.data))
	if root.left!=None:
		preordertraversal(root.left,Arr)
	if root.right!=None:
		preordertraversal(root.right,Arr)

def print_binarytree(root):
	if root==None:
		return
	print(root.data)
	if root.left!=None:
		print("left:",root.left.data)
	else:
		print("left: null")
	if root.right!=None:
		print("right",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)


tree=input("enter the tree nodes sep by spaces:")
tree=list(tree.split())
root=build_binarytree(tree)
Arr=[]
preordertraversal(root,Arr)

for i in range(len(Arr)-1):
	Arr[i].right=Arr[i+1]

print_binarytree(Arr[0])