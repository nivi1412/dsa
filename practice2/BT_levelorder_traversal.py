# BT_levelorder_traversal.py

from build_binarytree import build_binarytree,print_binarytree
import deque


inp=input("enter the nodes seperated by spaces:")
inp=list(inp.split())
root=build_binarytree(inp)
q=deque()
prev_level=0
q.append([root,0])
my_list=[]
local=[]

while q:
	root,level=q.popleft()
	if level==prev_level:
		local.append(root.data)
		if root.left!=None:
			q.append([root.left,level+1])
		if root.right!=None:
			q.append([root.right,level+1])


