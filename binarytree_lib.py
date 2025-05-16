#binarytree_lib.py

#this will create adress location for data,adress of leftpointer pointing None and adress of right pointer pointing None
class binarytree():
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

#nodes is the input list of numbers we are giving [1 2 3 4 5 6 7]
#inside this we are creating Nodes from the input list and stores list of adrress for each node stored in binarytrees
def build_binarytree(nodes):
	binarytrees=[]

	for node in nodes:
		if node == "null":
			binarytrees.append(None)
		else:
			binarytrees.append(binarytree(node)) # converting integer to binary tree node, where node value is data value,left is noe right is none
												 # now binarytrees[] consists of list of adress if each node 

#once binarytrees have adresses of list of nodes, we need to link each nodes left and right , so remove the existing None from left anf right we are 
#linking adress for each node, to make a tree and return the top node whcih is root 
#from root we can get the childrean 
	for i in range(len(binarytrees)):
		if binarytrees[i] is None:
			continue
		if (2*i+1) < len(binarytrees) and (binarytrees[2*i+1] != None):
			binarytrees[i].left = binarytrees[2*i+1]
		if (2*i+2) < len(binarytrees) and (binarytrees[2*i+2] != None):	
			binarytrees[i].right = binarytrees[2*i+2]

	return binarytrees[0]
	
#root is the top node, since root is linked to the left and right data values we can print entire tree from the root itself
def print_binarytree(root):
	if root is None:
		return
	print(f"node: {root.data}")
	if root.left:
		print(f" Left -> {root.left.data}")
	if root.right:
		print(f" Right -> {root.right.data}")
	print_binarytree(root.left)
	print_binarytree(root.right)
	

