#sortedlist_BST.py
# Convert Sorted List to Binary Search Tree
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

class Binarysearchtree():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def sortedlist_BST(inp):
	if len(inp)==0:
		return
	nl=len(inp)//2
	root=Binarysearchtree(inp[nl])
	root.left=sortedlist_BST(inp[:nl])
	root.right=sortedlist_BST(inp[nl+1:])

	return root

def print_binarytree(root):
	if root!=None:
		print("Node:",root.data)
		if root.left!=None:
			print("left",root.left.data)
		if root.right!=None:
			print("right",root.right.data)

		print_binarytree(root.left)
		print_binarytree(root.right)
	else:
		return


inp=input("enter the nodes of tree seperated by spaces").split()
root=sortedlist_BST(inp)
print_binarytree(root)

