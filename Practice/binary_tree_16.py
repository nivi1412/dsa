#binarytree16.py
#print reverse list of level order traversal
# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]

from binarytree1 import build_binarytree,print_binarytree
from collections import deque

def levelordertraversal(root):
	q=deque()
	level=0
	q.append([root,level])
	prev_level=0
	result=[]
	local=[]
	while q:
		node,level=q.popleft()
		if level==prev_level:
			local.append(node.data)
		else:
			result.append(local)
			local=[]
			local.append(node.data)
		prev_level=level
		if node.left:
			q.append([node.left,level+1])
		if node.right:
			q.append([node.right,level+1])
	result.append(local)
	return result


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
my_list=levelordertraversal(root)
result=[]
for i in range(len(my_list)-1,-1,-1):
	result.append(my_list[i])
print(result)