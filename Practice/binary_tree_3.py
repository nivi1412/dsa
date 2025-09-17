#binarytree3.py
#find the depth of the tree

from binarytree1 import build_binarytree

def depth_binarytree(root):
	if root==None:
		return 0
	return 1+(max(depth_binarytree(root.left),depth_binarytree(root.right)))

Arr=input("enter elements of binarytree")
Arr=Arr.split()

root=build_binarytree(Arr)

print(depth_binarytree(root))