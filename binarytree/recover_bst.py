#recoverBST.py
from binarytree_practice1 import build_binarytree,print_binarytree

class BST():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None


def recoverBST(my_list,isadjacent):
	if isadjacent:
		prev=0
		for i in range(1,len(my_list),+1):
			if my_list[prev]>my_list[i]:
				my_list[prev],my_list[i]=my_list[i],my_list[prev]
				return
			prev=i
	else:
		prev=my_list[0]
		count=0
		for i in range(1,len(my_list),+1):
			curr=my_list[i]
			if prev >curr and count==0:
				swap1=i-1
				count=1
			elif prev > curr and count==1:
				swap2=i
				my_list[swap1],my_list[swap2]=my_list[swap2],my_list[swap1]
				return
			prev=my_list[i]


def isadjacentfun(my_list):
	prev=my_list[0]
	count=0
	for i in my_list:
		if prev > i:
			count+=1

		prev=i
	if count==1:
		isadjacent=True
	else: isadjacent=False
	return isadjacent

def inordertraversal(root,my_list):
	if root.left!=None:
		inordertraversal(root.left,my_list)
	if root!=None:
		my_list.append(int(root.data))
	if root.right!=None:
		inordertraversal(root.right,my_list)

def construct_BST(result):
	nl=len(result):
	mid=(nl//2)
	root=BST(mid)
	root.left=construct_BST([:mid])



inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_list=[]
inordertraversal(root,my_list)
print(my_list)
isadjacent=isadjacentfun(my_list)
print(isadjacent)
recoverBST(my_list,isadjacent)
print(my_list)
result=[]
j=0
for i in range(len(inp)):
	if inp[i] == 'null':
		result.append('null')
	else:
		result.append(my_list[j])
		j+=1

