#breadthfirstsearch.py
from collections import deque
from binarytree_lib import build_binarytree,print_binarytree

def BFS(root):
	q=deque()
	q.append([root,0])

	pre_level=0
	count=0
	summ=0
	avg_list=[]

	while q:
		ele,level=q.popleft()
		if pre_level!=level:
			print("sum,count:",summ,count)
			avg_list.append(summ/count)
			pre_level=level
			count=1
			summ=int(ele.data)
		else:
			print("element",ele.data)
			summ=summ+int(ele.data)
			count+=1

		if ele.left!=None:
			q.append([ele.left,level+1])
		if ele.right!=None:
			q.append([ele.right,level+1])

	avg_list.append(summ / count)	
	return avg_list

inp1=input("enter the nodes of the 1st binary tree seprated by spaces:")
inp1=inp1.split()

root=build_binarytree(inp1)
print(BFS(root))