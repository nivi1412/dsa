#build_binarytree.py
import ast

class nodes:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def build_binarytree(tree):
	Arr=[]
	for node in tree:
		if node=="null":
			Arr.append(None)
		else:
			Arr.append(nodes(node))
	for i in range(len(Arr)):
		if Arr[i]==None:
			continue
		if 2*i+1 < len(Arr) and Arr[(2*i+1)]!=None:
			Arr[i].left=Arr[2*i+1]
		if 2*i+2 < len(Arr) and Arr[(2*i+2)]!=None:
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def print_binarytree(root):
	if root==None:
		return
	print(root.data)
	if root.left!=None:
		print("left:",root.left.data)
	if root.right!=None:
		print("right",root.right.data)
	print_binarytree(root.left)
	print_binarytree(root.right)
