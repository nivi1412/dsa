#binarytree29.py
#814. Binary Tree Pruning
#Given the root of a binary tree, return the same tree where every subtree (of the given tree) containing a 0 has been removed.

# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]

from binarytree1 import build_binarytree,print_binarytree
def pruning(root):
	if root!=None:
		node,left=pruning(root.left)
		node,right=pruning(root.right)

		print(left,right,root.data)
		if left==False and right ==False and root.data==1:
			root.left=None 
			root.right=None
			return root,True
		elif left==False and right==False and root.data==0:
			root.data=None
			root.left=None 
			root.right=None
			return root,True
		elif left==True and right==True and (root.data==1 or root.data==0):
			return root,True
		elif left==False and right==True and (root.data==1 or root.data==0):
			root.left=None
			return root,True
		elif left==True and right ==False and (root.data==0 or root.dat==1):
			root.right=None
			return root,True
	else:
		return None,False

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
root,flag=pruning(root)
print_binarytree(root)