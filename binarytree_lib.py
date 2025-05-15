#binarytree_lib.py

class binarytree():
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right


def build_binarytree(nodes):
	binarytrees=[]

	for node in nodes:
		if node == "null":
			binarytrees.append(None)
		else:
			binarytrees.append(binarytree(node))

	for i in range(len(binarytrees)):
		if binarytrees[i] is None:
			continue
		if (2*i+1) < len(binarytrees) and (binarytrees[2*i+1] != None):
			binarytrees[i].left = binarytrees[2*i+1]
		if (2*i+2) < len(binarytrees) and (binarytrees[2*i+2] != None):	
			binarytrees[i].right = binarytrees[2*i+2]

	return binarytrees[0]

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
	

