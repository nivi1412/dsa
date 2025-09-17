#levelordertraversal.py
from binarytree_practice1 import build_binarytree,print_binarytree
from collections import deque

def levelordertraversal(root):
	q=deque()
	result=[]
	prev_level=0
	q.append([root,0])
	while q:
		data,level=q.popleft()
		result.append([data.data,level])
		if data.left!=None:
			q.append([data.left,level+1])
		if data.right!=None:
			q.append([data.right,level+1])
	return result



inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)

result=levelordertraversal(root)
final_list=[]
local=[]
prev=0
for i in result:
	print(i)
	print(prev,i[1])
	if prev==i[1]:
		local.append(i[0])
	else:
		final_list.append(local)
		local=[]
		local.append(i[0])
	prev=i[1]
final_list.append(local)
print(final_list)


