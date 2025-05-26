#binarytree_practice1.py
#practie_binarytree construction

class binarytree():
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

def build_binarytree(inp):
	Arr=[]
	for i in range(len(inp)):
		if inp[i]== 'null':
			Arr.append(None)
		else:
			Arr.append(binarytree(inp[i]))

	for i in range(len(Arr)):
		if Arr[i]==None:
			continue
		if (2*i+1)<len(Arr) and Arr[2*i+1]!=None:
			Arr[i].left=Arr[2*i+1]
		if (2*i+2)<len(Arr) and Arr[2*i+2]!=None:
			Arr[i].right=Arr[2*i+2]
	return Arr[0]

def print_binarytree(root):
	if root == None:
		return
	print("Node:",root.data)
	if root.left:
		print("left val",root.left.data)
	if root.right:
		print("right val",root.right.data)

		print
	print_binarytree(root.left)
	print_binarytree(root.right)

# inp=input("enter the nodes of binary tree seperated by spaces")
# inp=inp.split()
# root=build_binarytree(inp)
# print_binarytree(root)
