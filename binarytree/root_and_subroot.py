#rootandsubroot.py
from binarytree_practice1 import build_binarytree,print_binarytree

def rootandsubroot(root,sroot):
	if root!=None and sroot!=None:
		if root.data==sroot.data:
			return rootandsubroot(root.left,sroot.left) and rootandsubroot(root.right,sroot.right)
		return False
	if root==None and sroot==None:
		return True
	return False


def inordertraversal(root,sroot):
	if root == None :
		return False
	if sroot == None:
		return True
	if rootandsubroot(root,sroot):
		return True
	return inordertraversal(root.left,sroot) or inordertraversal(root.right,sroot)



	# print("traversal:",root.data,sroot.data)
	# if root !=None and sroot !=None:
	# 	if not rootandsubroot(root,sroot):
	# 		if root.left!=None:
	# 			inordertraversal(root.left,sroot)
	# 		if root.right!=None:
	# 			inordertraversal(root.right,sroot)
	# 		return False
	# 	return True
	# if root==None and sroot==None:
	# 	return True
	# return False

inp=input("enter the nodes of tree seperated by spaces:")
inp1=input("enter the nodes of subroot:")
inp=inp.split()
inp1=inp1.split()
root=build_binarytree(inp)
sroot=build_binarytree(inp1)
print(inordertraversal(root,sroot))
