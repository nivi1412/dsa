#BT_rightsideview.py
from build_binarytree import build_binarytree
from collections import deque

tree=input("enter the tree nodes: ")
tree=tree.split()

root=build_binarytree(tree)
my_list=[]

q=deque()
#level order traversal
q.append([root,1])
prev_level=1
prev_node=root.data

while q:
	node,level=q.popleft()
	if level!=prev_level:
		my_list.append(prev_node)
	if node.left!=None:
		q.append([node.left,level+1])
	if node.right!=None:
		q.append([node.right,level+1])
	prev_node=node.data
	prev_level=level

my_list.append(prev_node)
print(my_list)