#binarytree4.py
#check if binary tress is symmetrcal at its root
#symmetrical:mirror to its root

from binarytree1 import build_binarytree

def is_symmetrical(left,right):
	if left!=None and right !=None:
		if left.data==right.data:
			return (is_symmetrical(left.left,right.right) and is_symmetrical(left.right,right.left))
		else:
			return False
	elif left==None and right==None:
		return True
	else:
		return False



Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
print(is_symmetrical(root.left,root.right))