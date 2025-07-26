#binarytree31.py
#Flip Equivalent Binary Trees

from binarytree1 import build_binarytree,print_binarytree

def are_flipequivalent(root1,root2):

	if root1==None and root2==None:
		return True
	if root1==None and root2!=None:
		return False
	if root1!=None and root2==None:
		return False
	print("data:",root1.data,root2.data)
	if root1.data==root2.data:
		left_left=are_flipequivalent(root1.left,root2.left)
		right_right=are_flipequivalent(root1.right,root2.right)
		print("ll:,rr:",left_left,right_right)
		if left_left ==False and right_right==False:
			left_right=are_flipequivalent(root1.left,root2.right)
			right_left=are_flipequivalent(root1.right,root2.left)
			print("lr:,rl:",left_right,right_left)
			return (left_right and right_left)
		else:
			return (left_left and right_right)
	else:
		return False

Arr1=input("enter elements of binarytree")
Arr1=Arr1.split()
Arr2=input("enter elements of binarytree")
Arr2=Arr2.split()
root1=build_binarytree(Arr1)
root2=build_binarytree(Arr2)

print(are_flipequivalent(root1,root2))


