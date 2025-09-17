#binarytree11.py
#zigzaglevelordertraversal

#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
#(i.e., from left to right, then right to left for the next level and alternate between).

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

from collections import deque
from binarytree1 import build_binarytree

def levelordertraversal(root):
	q=deque()
	level=0
	prev_level=0
	result=[]
	local=[]
	q.append([root,level])
	while q:
		node,level=q.popleft()
		if level==prev_level:
			local.append(node.data)
		else:
			#local.append(node.data)
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
result=levelordertraversal(root)
finalresult=[]
for i in range(len(result)):
	if i%2!=0:
		local=[]
		for j in range(len(result[i])-1,-1,-1):
			local.append((result[i])[j])
		finalresult.append(local)
	else:
		finalresult.append(result[i])
print(finalresult)







