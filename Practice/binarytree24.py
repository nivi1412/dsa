#binarytree24.py
#Add One Row to Tree

from binarytree1 import build_binarytree,print_binarytree

class BT:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

def Addval(root,val,depth):
	if depth==1:
		root_node=BT(val)
		root_node.left=root
		return root
	else:
		

		

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
val=int(input("enter the value to be added:"))
depth=int(input("enter the depth at which value to be added:"))

root=Addval(root,val,depth)
print_binarytree(root)