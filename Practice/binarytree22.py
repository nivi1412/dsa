#binarytree22.py
#rahuls problem
from binarytree1 import build_binarytree,print_binarytree

def find_evenodeepathcount(root):
	if root.left==None and root.right==None:
		return 0,1

	elif root.left==None and root.right!=None:
		right_odd,right_even=find_evenodeepathcount(root.right)

		root_even=right_odd
		root_odd=right_even
		print(root.data,root_odd,root_even)

		return root_odd,root_even

	elif root.left!=None and root.right==None:
		left_odd,left_even=find_evenodeepathcount(root.left)

		root_even=left_odd
		root_odd=left_even
		print(root.data,root_odd,root_even)

		return root_odd,root_even


	else:
		left_odd,left_even=find_evenodeepathcount(root.left)
		right_odd,right_even=find_evenodeepathcount(root.right)

		root_even=left_odd+right_odd
		root_odd=left_even+right_even
		print(root.data,root_odd,root_even)

		return root_odd,root_even

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
print("oddpath count,evenpath count:",find_evenodeepathcount(root))