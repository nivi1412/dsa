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
		if (2*i+1)<len(Arr) and Arr[2*i+1]!=None:
			Arr[i].left=Arr[2*i+1]
		if (2*i+2)<len(Arr) and Arr[2*i+2]!=None:
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def print_binarytree(froot):
	if froot == None:
		return
	print("Node:",froot.data)
	if froot.left:
		print("left val",froot.left.data)
	if froot.right:
		print("right val",froot.right.data)
	print_binarytree(froot.left)
	print_binarytree(froot.right)

def preorder(root,Arr):
	if root!=None:
		Arr.append(int(root.data))
	if root.left!=None:
		preorder(root.left,Arr)
	if root.right!=None:
		preorder(root.right,Arr)

def flattening(Arr_local):
	for i in range(0,len(Arr_local)-1,+1):
		Arr_local[i].right=Arr_local[i+1]
	return Arr_local[0]


inp=input("enter the nodes of tree seperated by spaces").split()
root=build_binarytree(inp)
Arr=[]
preorder(root,Arr)
print(Arr)
Arr_local=[]
for node in Arr:
	Arr_local.append(BST(node))
froot=flattening(Arr_local)
print_binarytree(froot)




