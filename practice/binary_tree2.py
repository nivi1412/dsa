#binarytree2.py
#traversal

from binarytree1 import build_binarytree

def preorder_traversal(root):
	if root!=None:
		print(root.data)
	if root.left!=None:
		preorder_traversal(root.left)
	if root.right!=None:
		preorder_traversal(root.right)

def inorder_traversal(root):
	if root.left!=None:
		preorder_traversal(root.left)
	if root!=None:
		print(root.data)
	if root.right!=None:
		preorder_traversal(root.right)

def postorder_traversal(root):
	if root.left!=None:
		preorder_traversal(root.left)
	if root.right!=None:
		preorder_traversal(root.right)
	if root!=None:
		print(root.data)




Arr=input("enter elements of binarytree")
Arr=Arr.split()

root=build_binarytree(Arr)

preorder_traversal(root)
inorder_traversal(root)
postorder_traversal(root)