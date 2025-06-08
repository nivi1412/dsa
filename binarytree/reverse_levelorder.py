#reverse_levelorder.py
#to reverse u can directly "if result is deque data structure(appendleft)" no need to create one more list 
#if result is list data structure we use result.insert(0,local) specify at what index u want to insert


from binarytree_practice1 import build_binarytree,print_binarytree
from collections import deque


def levelorder(root):
	q=deque()
	q.append([root,0])
	prelevel=0
	result=[]
	local=[]
	while q:
		root,level=q.popleft()
		if prelevel!=level:
			result.insert(0,local)
			local=[]
			local.append(root.data)
		else:
			local.append(root.data)
		prelevel=level
		if root.left!=None:
			q.append([root.left,level+1])
		if root.right!=None:
			q.append([root.right,level+1])
	result.insert(0,local)
	return result


inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
if inp != None:
	root=build_binarytree(inp)
	result=levelorder(root)
	print(result)
else:
	print("[]")

