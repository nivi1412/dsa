# BT_Recover_BST.py

# dont assign root to prev in root.left or root.right functions
# make a global function and create all the global variables
# call the function with only node as parameter
# make count as a number instead of bool , as we are managing 3 possible states (either 0,1,2 or 3,2,1)
# make sure while checking states for one node enter only one state(keep elif for line 29)
# prev_root.data>root.data then there is error in order not other way
# prev root should be None not the original root during first function call

from build_binarytree import build_binarytree,print_binarytree

def BT_Recover_BST(root):
	count=3
	first=None
	sec=None
	prev_root=None

	def inorder_traversal(root):
		nonlocal count,first,sec,prev_root
		if root.left!=None:
			print("left:",root.data,count)
			inorder_traversal(root.left)
		if root!=None:
			if prev_root is not None and count==3:
				print("root:",prev_root.data,root.data,count)
				if prev_root.data>root.data:
					first=prev_root
					sec=root
					count-=1
			elif prev_root is not None and count==2:
				print("root:",prev_root.data,root.data,count)
				if prev_root.data>root.data:
					sec=root
					count-=1
					print(first.data,sec.data)
					first.data,sec.data=sec.data,first.data
					print("1.hello")
			prev_root=root
		if root.right!=None:
			print("right:",root.data,count)
			inorder_traversal(root.right)

	inorder_traversal(root)
	if count==2:
		print("hello")
		first.data,sec.data=sec.data,first.data



inp=input("enter the nodes seperated by spaces:")
inp=list(inp.split())
root=build_binarytree(inp)
BT_Recover_BST(root)
print("after:")
print_binarytree(root)
