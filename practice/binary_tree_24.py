#binarytree24.py
#Add One Row to Tree
#in DFS no need to return anything as we are doing inplace value modification

from binarytree1 import build_binarytree,print_binarytree

class BT:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None

def Addval(root,val,depth):
	if depth==1:
		val=BT(val)
		val.left=root
		return val
	else:
		current_depth=1
		def DFS(root,current_depth):
			if root==None:
				return 
			nonlocal depth
			nonlocal val
			if current_depth!=depth-1:
				DFS(root.left,current_depth+1)
				DFS(root.right,current_depth+1)

			else:
				empty1=root.left
				empty2=root.right
				val_left=BT(val)
				val_right=BT(val)
				root.left=val_left
				root.right=val_right
				val_left.left=empty1
				val_right.right=empty2
		DFS(root,current_depth)
		return root

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
val=int(input("enter the value to be added:"))
depth=int(input("enter the depth at which value to be added:"))
root=Addval(root,val,depth)
print("hi:",root)
print_binarytree(root)



