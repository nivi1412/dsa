#traversal_practice.py
# from binarytree_practice1 import build_binarytree,print_binarytree
# inp=input("enter the nodes of tree seperated by spaces")
# inp=inp.split()
# root=build_binarytree(inp)




from binarytree_practice1 import build_binarytree,print_binarytree

def inordertraversal(root):
	if root!=None:
		print(root.data)
	if root.left !=None:
		inordertraversal(root.left)
	if root.right!=None:
		inordertraversal(root.right)

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
inordertraversal(root)
#print_binarytree(root)