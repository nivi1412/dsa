#ArraytoBST.py
#from binarytree_practice1 import build_binarytree,print_binarytree

class BST():
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right
def build_Bst(inp):
	if len(inp) == 0:
		return None
	na=len(inp)
	print(na)
	print(inp)
	mid=na//2
	root=BST(inp[mid])
	root.left=build_Bst(inp[:mid])
	root.right=build_Bst(inp[mid+1:])
	return root
def print_binarytree(root):
	if root==None:
		return 
	print("node:",root.data)
	if root.left!=None:
		print("left:",root.left.data)
	if root.right!=None:
		print("right:",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)


	


inp=input("enter the sorted array seperated by spaces")
inp=list(map(int,inp.split()))
print_binarytree(build_Bst(inp))