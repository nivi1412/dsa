#populatenxtrightpointer.py
from collections import deque

class PBT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.next=None

def build_binarytree(inp):
	Arr=[]
	for i in inp:
		if i=='null':
			Arr.append(None)
		else:
			Arr.append(PBT(i))
	for i in range(len(Arr)):
		if Arr[i]==None:
			continue
		if (2*i+1)<len(Arr) and Arr[2*i+1]!=None:
			Arr[i].left=Arr[2*i+1]
		if (2*i+2)<len(Arr) and Arr[2*i+2]!=None:
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def levelorder(root):
	q=deque()
	prev_root=root
	pre_level=0
	q.append([root,0])
	while q:
		root,level=q.popleft()
		if pre_level==level and pre_level>0:
			prev_root.next=root

		pre_level=level
		prev_root=root
		if root.left:
			q.append([root.left,level+1])
		if root.right:
			q.append([root.right,level+1])

def print_nxtrightpointer(root,result):
	if root==None:
		return
	result.append(root.data)
	if root.next==None:
		result.append("#")

		
	print_nxtrightpointer(root.left,result)
	print_nxtrightpointer(root.right,result)




inp=input("enter the nodes of tree seperated by spaces").split()
root=build_binarytree(inp)
levelorder(root)
result=[]
print_nxtrightpointer(root,result)
print(result)
