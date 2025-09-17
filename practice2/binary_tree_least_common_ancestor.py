#binarytree_leastcommonancester.py

import ast
from build_binarytree import build_binarytree,print_binarytree

def LCA(root,p,q):
	if root == None:
		return -1
	if int(root.data)==p or int(root.data)==q:
		return root
	left=LCA(root.left,p,q)
	right=LCA(root.right,p,q)

	if left!=-1 and right !=-1:
		return root
	else:
		if left==-1:
			return right
		if right ==-1:
			return left

tree=input("enter the nodes of the tree: ")
tree=ast.literal_eval(tree)
p=int(input("enter the 1st node: "))
q=int(input("enter the 2nd node: "))

root=build_binarytree(tree)

print(LCA(root,p,q).data)
