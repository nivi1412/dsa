#binarytree1.py
#construct binarytree from Arr and print them

class Binarytree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def build_binarytree(Arr):
	my_list=[]
	for node in Arr:
		if node=="null":
			my_list.append(None)
		else:
			my_list.append(Binarytree(node))

	for i in range(len(my_list)):
		if my_list[i]==None:
			continue
		if (2*i+1)<len(Arr) and my_list[2*i+1]!=None:
			my_list[i].left=my_list[2*i+1]
		if (2*i+2)<len(Arr) and Arr[2*i+2]!=None:
			my_list[i].right=my_list[2*i+2]
	return my_list[0]

def print_binarytree(root):
	if root==None:
		return
	print("node:",root.data)
	if root.left!=None:
		print("left:",root.left.data)
	if root.right!=None:
		print("right:",root.right.data)

	print_binarytree(root.left)
	print_binarytree(root.right)

#Arr=input("enter the elements of array sep by spaces:")
#Arr=Arr.split()

#root=build_binarytree(Arr)
#print_binarytree(root)