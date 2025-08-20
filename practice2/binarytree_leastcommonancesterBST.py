#binarytree_leastcommonancesterBST.py

import ast
from build_binarytree import build_binarytree,print_binarytree

def LCA_BST(root,p,q):
	if int(root.data)==p or int(root.data)==q:
		return root
	if p<int(root.data) and q<int(root.data):
		return LCA_BST(root.left,p,q)
	elif p>int(root.data) and q>int(root.data):
		return LCA_BST(root.right,p,q)
	else:
		return root

tree=input("enter the nodes of the tree: ")
tree=ast.literal_eval(tree)
p=int(input("enter the 1st node: "))
q=int(input("enter the 2nd node: "))

root=build_binarytree(tree)

print(LCA_BST(root,p,q).data)