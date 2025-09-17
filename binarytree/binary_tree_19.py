#binarytree19.py

from binarytree_lib import build_binarytree,print_binarytree

def merge_binarytree(root1,root2):
	if root1!=None and root2!=None:
		print(root1.data,root2.data)
		root1.data=int(root1.data)+int(root2.data)
		root1.left=merge_binarytree(root1.left,root2.left)
		root1.right=merge_binarytree(root1.right,root2.right)
	if root1==None and root2!=None:
		print(root2.data)
		root1=root2
	return root1



inp1=input("enter the nodes of the 1st binary tree seprated by spaces:")
inp1=inp1.split()
inp2=input("enter the nodes of the 2nd binary tree seprated by spaces")
inp2=inp2.split()

root1=build_binarytree(inp1)
root2=build_binarytree(inp2)
# merge_binarytree(root1,root2)
print_binarytree(merge_binarytree(root1,root2))