#binarytree20.py
#flatternning the binarytree into linkedlist

from binarytree1 import build_binarytree,print_binarytree

class BT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def preordertraversal(root,result1):
	if root!=None:
		result1.append(root.data)
	if root.left!=None:
		preordertraversal(root.left,result1)
	if root.right!=None:
		preordertraversal(root.right,result1)

def flattenning(result,length):
	if length==0:
		return None
	root=BT(result[length-1])
	root.left=None
	root.right=flattenning(result,length-1)
	return root


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
result1=[]
result=[]
preordertraversal(root,result1)
for i in range(len(result1)-1,-1,-1):
	result.append(result1[i])
print(result)
root=flattenning(result,len(result))

print_binarytree(root)