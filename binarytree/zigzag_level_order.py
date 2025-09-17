#zigzag_levelorder.py

from binarytree_practice1 import build_binarytree,print_binarytree
from collections import deque

q=deque()
result=[]
def zigzag_levelorder(root):
	q.append([root,0])
	while q:
		root,level=q.popleft()
		print(root.data,level)
		result.append([root.data,level])
		if root.left!=None:
			q.append([root.left,level+1])
		if root.right!=None:
			q.append([root.right,level+1])
	return result

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
result=zigzag_levelorder(root)
final_list=[]
local=[]
prev=0
for i in result:
	if prev==i[1]:
		local.append(i[0])
	else:
		final_list.append(local)
		local=[]
		local.append(i[0])
	prev=i[1]
final_list.append(local)
print(final_list)
for i in range(len(final_list)):
	if i%2!=0:
		final_list[i].reverse()
print(final_list)
