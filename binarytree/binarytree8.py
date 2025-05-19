#binarytree8.py
#balanced binary search tree

class bal_BST():
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

def balanced_BST(inp):
	if len(inp)==0:
		return None
	mid=len(inp)//2
	root=bal_BST(inp[mid])
	root.left=balanced_BST(inp[:mid])
	root.right=balanced_BST(inp[mid+1:])
	return root
	
def print_bal_BST(root):
	if root == None:
		return
	print("node:",root.data)
	if root.left:
		print(f"left -> ",root.left.data)
	if root.right:
		print(f"right -> ",root.right.data)
	print_bal_BST(root.left)
	print_bal_BST(root.right)

inp=input("enter the sorted array seperated by spaces")
inp=inp.split()
mid=len(inp)//2
root=balanced_BST(inp)
print_bal_BST(root)