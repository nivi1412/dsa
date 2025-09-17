#prepostorderBinarytree.py
from binarytree_practice1 import print_binarytree
class binarytree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
def construct_tree(postorder,inorder):
	if not (postorder or inorder) :
		return
	root=binarytree(postorder[len(postorder)-1])
	# for i in range(len(inorder)):
	# 	if inorder[i]==root.data:
	# 		index=i

	index=inorder.index(root.data)
	
	inorder_left=inorder[:index]
	inorder_right=inorder[index+1:]
	postorder_left=postorder[:len(inorder_left)]
	postorder_right=postorder[len(inorder_left):len(postorder)-1]


	root.left=construct_tree(postorder_left,inorder_left)
	root.right=construct_tree(postorder_right,inorder_right)


	return root


postorder=input("enter the postorder elements sepe by spaces").split()
inorder=input("enter the inorder elements sepe by spaces").split()
root=construct_tree(postorder,inorder)
print_binarytree(root)