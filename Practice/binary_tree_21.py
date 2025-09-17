#binarytree21.py
# 116. Populating Next Right Pointers in Each Node

from binarytree1 import print_binarytree
from collections import deque

class node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None 
		self.next=None

def build_binarytree(Arr):
	my_list=[]
	for i in range(len(Arr)):
		if Arr[i]=="null":
			my_list.append(None)
		else:
			my_list.append(node(Arr[i]))

	for i in range(len(my_list)):
		if my_list[i]==None:
			continue
		if (2*i+1<len(my_list) and my_list[2*i+1]!=None):
			my_list[i].left=my_list[2*i+1]
		if (2*i+2<len(my_list) and my_list[2*i+2]!=None):
			my_list[i].right=my_list[2*i+2]

	return my_list[0]

def levelordertraversal(root):
	q=deque()
	level=0
	prev_level=0
	prev_node=root
	q.append([root,level])
	while q:
		node,level=q.popleft()
		if level==prev_level and level>0:
			prev_node.next=node

		prev_node=node
		prev_level=level
		if node.left:
			q.append([node.left,level+1])
		if node.right:
			q.append([node.right,level+1])

def printnextrightpointer(root,result):
	if root!=None:
		result.append(root.data)
		if root.next==None:
			result.append("#")
	if root.left!=None:
		printnextrightpointer(root.left,result)
	if root.right!=None:
		printnextrightpointer(root.right,result)


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
print_binarytree(root)
levelordertraversal(root)
result=[]
printnextrightpointer(root,result)
print(result)

