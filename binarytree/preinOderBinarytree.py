#preinOderBinarytree.py
#construct binarytree from preorder and inorder arrays

#logic: preorder of first element is root
#find the root in inorder and divide inorder based on it
#same way divide preorder array based on index
#call recursive on updated array


from binarytree_practice1 import build_binarytree,print_binarytree
class binarytree:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def construct_tree(preorder,inorder):
	if not preorder or not inorder:
		return
	root=binarytree(preorder[0])
	for i in range(len(inorder)):
		if inorder[i]==root.data:
			index=i

	left_inorder=inorder[:index]
	right_inorder=inorder[index+1:]
	left_preorder=preorder[1:len(left_inorder)+1]
	right_preorder=preorder[len(left_inorder)+1:]

	root.left=construct_tree(left_preorder,left_inorder)
	root.right=construct_tree(right_preorder,right_inorder)

	return root




preorder=input("enter the array elements sepe by spaces").split()
inorder=input("enter the array elements sepe by spaces").split()
root=construct_tree(preorder,inorder)
print_binarytree(root)

#first element of preorder is main root

