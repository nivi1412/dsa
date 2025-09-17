#binarytree17.py
#convert sortedarray into BST
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

from binarytree1 import build_binarytree,print_binarytree

class BT():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def converttoBST(Arr):
	length=len(Arr)
	if length==0:
		return None
	root=BT(Arr[length//2])
	left=Arr[:length//2]
	right=Arr[length//2+1:]
	root.left=converttoBST(left)
	root.right=converttoBST(right)

	return root


Arr=input("enter the sorted array to be converted to binary search tree")
Arr=list(map(int,Arr.split()))

root=converttoBST(Arr)
print_binarytree(root)
