#binarytree4.py
#inorder travelsal, preorder traversal and postorder traversal

from binarytree_lib import build_binarytree, print_binarytree

def inorder_traversal(root):
	if root.left != None:
		inorder_traversal(root.left)
	if root != None:
		print(root.data)
	if root.right != None:
		inorder_traversal(root.right)
def preorder_traversal(root):
	if root != None:
		print(root.data)
	if root.left != None:
		preorder_traversal(root.left)
	if root.right != None:
		preorder_traversal(root.right)
def postorder_traversal(root):
	if root.left!=None:
		postorder_traversal(root.left)
	if root.right!=None:
		postorder_traversal(root.right)
	if root != None:
		print(root.data)

inp=input("enter the elements of tree seperated by space")
inp=inp.split()

root=build_binarytree(inp)
print("inorder_traversal:")
inorder_traversal(root)
print("preorder traversal:")
preorder_traversal(root)
print("postorder_traversal")
postorder_traversal(root)