#binarysearch25.py
#701. Insert into a Binary Search Tree

from binarytree1 import build_binarytree,print_binarytree

class BST():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def buildBST(my_list,length):
	if length==0:
		return None
	root=BST(my_list[length//2])
	left_list=my_list[:length//2]
	right_list=my_list[length//2+1:]

	root.left=buildBST(left_list,len(left_list))
	root.right=buildBST(right_list,len(right_list))

	return root

def preorder(root,my_list):
	if root.left!=None:
		preorder(root.left,my_list)
	if root!=None:
		my_list.append(root.data)
	if root.right!=None:
		preorder(root.right,my_list)




Arr=input("enter elements of binarytree")
Arr=Arr.split()
val=input("enter the value to be inserted:")
root=build_binarytree(Arr)
my_list=[]
preorder(root,my_list)
for i in range(len(my_list)):
	if my_list[i]>val:
		my_list.insert(i,val)
		break
print(my_list)
root=buildBST(my_list,len(my_list))
print_binarytree(root)