#binarytree21.py

from binarytree_lib import build_binarytree,print_binarytree

def search(root,val):
	if root!=None:
		print("search val:",root.data,val)
		if int(root.data)==val:
			return True
		else:
			return search(root.left,val) or search(root.right,val)
	return False

def inorder_traversal(org_root,root,k):
	if root!=None:
		val=k-int(root.data)
		print(root.data,val)
		if val != int(root.data):
			return search(org_root,val)
		return inorder_traversal(org_root,root.left,k) or inorder_traversal(org_root,root.right,k)
	else:
		return  False

inp1=input("enter the nodes of the binary tree seprated by spaces:")
inp1=inp1.split()
k=int(input("enter the required sum value:"))
root=build_binarytree(inp1)
arr=[]
org_root=root
print(inorder_traversal(org_root,root,k))
