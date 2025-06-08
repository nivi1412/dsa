#flatteningtree.py
# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

from binarytree_practice1 import build_binarytree,print_binarytree

class BST():
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

def build_binarytree(inp):
	Arr=[]
	for i in range(len(inp)):
		if inp[i] =='null':
			Arr.append(None)
		else:
			Arr.append(BST(inp[i]))
	for i in range(len(Arr)):
		if Arr[i]==None:
			continue
		if (2*i+1)<len(Arr) :
			Arr[i].left=Arr[2*i+1]
		if (2*i+2)<len(Arr) :
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def print_binarytree(root):
	if root == None:
		return
	print("Node:",root.data)
	if root.left:
		print("left val",root.left.data)
	if root.right:
		print("right val",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)

#def flattening(root,Arr):
	# if root!=None:
	# 	Arr.append(root.data)
	# if root.left!=None:
	# 	flattening(root.left,Arr)
	# if root.right!=None:
	# 	flattening(root.right,Arr)
	# Arr2=[]
	# for i in range(len(Arr)):



inp=input("enter the nodes of tree seperated by spaces").split()
root=build_binarytree(inp)
print_binarytree(root)
Arr=[]
#froot=flattening(root,Arr)




