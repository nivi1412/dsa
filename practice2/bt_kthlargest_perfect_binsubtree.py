#kthlargest_perfect_binsubtree.py
from build_binarytree import build_binarytree,print_binarytree
import heapq

def perfect_binsubtree(root,heap)->int:
	if root.left==None and root.right==None:
		return 1
	elif (root.left!=None and root.right ==None) or (root.left==None and root.right!=None) :
		return None
	else:
		left=perfect_binsubtree(root.left,heap)
		right=perfect_binsubtree(root.right,heap)
		if left:
			heapq.heappush(heap,-1*left)
		if right:
			heapq.heappush(heap,-1*right)
		if (left==right and left!=None and right !=None):
			return 1+left+right
		else:
			None

inp=input("enter the array of tree nodes: ")
inp=list(inp.split())
k=int(input("enter the value of k: "))
root=build_binarytree(inp)
heap=[]
top_level = perfect_binsubtree(root,heap)
if top_level:
	heapq.heappush(heap, -1 * top_level)
print(heap)
for i in range(k):
	if i==k-1:
		print(-1*heapq.heappop(heap))