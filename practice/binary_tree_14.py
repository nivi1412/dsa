#binarytree14.py
#check if the binarytree is heightbalanced BT

from binarytree1 import build_binarytree,print_binarytree

def check_HBBT(root):
	if root is None:
		return (0,True)
	left,left_bal= check_HBBT(root.left)
	right,right_bal=check_HBBT(root.right)
	
	curr_height=1+max(left,right)
	is_balanced=abs(left-right)<=1 and left_bal and right_bal

	return curr_height,is_balanced

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)

curr_height,is_balanced=check_HBBT(root)
print(curr_height,is_balanced)