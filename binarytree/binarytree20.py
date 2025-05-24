#binarytree20.py

from binarytree_lib import build_binarytree,print_binarytree
from collections import deque

def breadth_first_search(root):
	q=deque()
	q.append([root,0])

	prev_level=0
	count=0
	sum_ele=0
	avg=[]

	while q:
		ele,level=q.popleft()

		if prev_level==level:
			sum_ele+=int(ele.data)
			print(sum_ele)
			count+=1
		else:
			avg.append(sum_ele/count)
			count=1
			sum_ele=int(ele.data)

		if ele.left!=None:
			q.append([ele.left,level+1])
		if ele.right!=None:
			q.append([ele.right,level+1])

		prev_level=level

	avg.append(sum_ele/count)
	return avg


inp1=input("enter the nodes of the 1st binary tree seprated by spaces:")
inp1=inp1.split()
root=build_binarytree(inp1)

print(breadth_first_search(root))