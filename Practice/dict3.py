#dict3.py
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

class BinaryTree():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def Build_BinaryTree(inp):
	Arr=[]
	for i in inp:
		if i =='null':
			Arr.append(None)
		else:
			Arr.append(BinaryTree(i))
	for i in range(len(Arr)):
		if Arr[i]==None:
			continue
		if 2*i+1 < len(Arr) and Arr[2*i+1]!=None:
			Arr[i].left=Arr[2*i+1]
		if 2*i+2 < len(Arr) and Arr[2*i+2]!=None:
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def Print_BinaryTree(root):
	if root==None:
		return
	print("Node:",root.data)
	if root.left!=None:
		print("left:",root.left.data)
	if root.right!=None:
		print("right:",root.right.data)
	Print_BinaryTree(root.left)
	Print_BinaryTree(root.right)

def Depth_BinaryTree(root):
	if root==None:
		return 0
	return 1+max(Depth_BinaryTree(root.left),Depth_BinaryTree(root.right))


inp=input("enter nodes of tree sep by spaces")
inp=inp.split()
root=Build_BinaryTree(inp)
Print_BinaryTree(root)
print(Depth_BinaryTree(root))


