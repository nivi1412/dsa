#binarytree5.py
#check if the 2 Binary trees are same

from binarytree1 import build_binarytree

def check_Sametree(p,q):
	if p!=None and q!=None:
		if p.data==q.data:
			left=check_Sametree(p.left,q.left)
			right=check_Sametree(p.right,q.right)
			return (left and right)
		else: return False
	elif p==None and q==None:
		return True
	else:
		return False

Arr1=input("enter elements of binarytree")
Arr1=Arr1.split()
Arr2=input("enter elements of binarytree")
Arr2=Arr2.split()

p=build_binarytree(Arr1)
q=build_binarytree(Arr2)

print(check_Sametree(p,q))
