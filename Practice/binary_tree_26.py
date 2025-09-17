#binarytree26.py
#814. Binary Tree Pruning
#Given the root of a binary tree, return the same tree where every subtree (of the given tree) containing a 0 has been removed.

# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]

from binarytree1 import build_binarytree,print_binarytree

def pruning(root):
	if root==None:
		return False
	else:
		left_true=pruning(root.left)
		right_true=pruning(root.right)

		print(root.data,left_true,right_true)

		if left_true==False and right_true==True:
			root.left=None

		elif left_true==True and right_true==False:
			root.right=None

		elif left_true==False and right_true==False:
			root.left=None
			root.right=None

		print(int(root.data)==1)
		print(int(root.data)==0 and (left_true or right_true))

		return int(root.data)==1 or (int(root.data)==0 and (left_true or right_true))

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
true=pruning(root)
print_binarytree(root)