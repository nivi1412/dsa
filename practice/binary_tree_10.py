#binarytree10.py
#level order traversal

from collections import deque
from binarytree1 import build_binarytree
# Arr=input("enter elements of binarytree")
# Arr=Arr.split()

# root=build_binarytree(Arr)

def levelordertraversal(root):
	q=deque()
	position=0
	returnlist=[]
	if root:
		q.append([root,position])
	while q:
		node,position=q.popleft()
		returnlist.append(node.data)
		print(node.data)
		if node.left:
			q.append([node.left,position+1])
		if node.right:
			q.append([node.right,position+1])



Arr=input("enter elements of binarytree")
Arr=Arr.split()

root=build_binarytree(Arr)
levelordertraversal(root)
