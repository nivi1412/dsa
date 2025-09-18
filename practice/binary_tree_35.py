#binarytree35.py
#reverse the no values at odd level

from binarytree1 import build_binarytree,print_binarytree

def reverse_nodevalues(root,level=1):
	if root==None:
		return

	if level%2!=0:
		if root.left!=None and root.right!=None:
			root.left.data,root.right.data=root.right.data,root.left.data
		if root.left!=None and root.right==None:
			root.right.data=root.left.data
			root.left.data=None
		if root.right!=None and root.left==None:
			root.left.data=root.right.data
			root.right.data=None

	reverse_nodevalues(root.left,level+1)
	reverse_nodevalues(root.right,level+1)
	return root


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
new_root=reverse_nodevalues(root)
print_binarytree(new_root)