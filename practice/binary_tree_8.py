#binarytree8.py
#check if the tree is BST 

from binarytree1 import build_binarytree

# def inorder_traversal(root,my_list):
# 	if root.left!=None:
# 		inorder_traversal(root.left,my_list)
# 	if root!=None:
# 		my_list.append(root.data)
# 	if root.right!=None:
# 		inorder_traversal(root.right,my_list)

def is_BST(root,left_lim,right_lim):
	if root==None:
		return True
	else:
		if not(left_lim<int(root.data)<right_lim):
			return False
		left=is_BST(root.left,left_lim,int(root.data))
		right=is_BST(root.right,int(root.data),right_lim)
		return left and right

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
left_lim=0
right_lim=10**5
print(is_BST(root,left_lim,right_lim))
# is_Bst=True

# my_list=[]
# inorder_traversal(root,my_list)
# Next=0
# for i in my_list:
# 	if int(i)>Next:
# 		Next=int(i)
# 	else:
# 		print("not a Bst")
# 		is_Bst=False
# 		break
# if is_Bst:
# 	print("its a BST")