#binarytree_levelordertraversal.py

import ast
from collections import deque
from build_binarytree import build_binarytree,print_binarytree

tree=input("enter the nodes of the tree: ")
tree=ast.literal_eval(tree)

root=build_binarytree(tree)
print_binarytree(root)

q=deque()
q.append([root,0])

while q:
	node,level=q.popleft()
	print(node.data)
	if node.left!=None:
		q.append([node.left,level+1])
	if node.right!=None:
		q.append([node.right,level+1])

