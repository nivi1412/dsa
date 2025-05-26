#samtree_p.py
from binarytree_practice1 import build_binarytree,print_binarytree

def sametree(root1,root2):
	if root1!=None and root2!=None:
		print(root1.data,root2.data)
		if root1.data==root2.data:
			return (sametree(root1.left,root2.left) and sametree(root1.right,root2.right))
		else:
			return False
	elif root1==None and root2==None:
		return True
	else:
		return False

inp=input("enter the nodes of tree1 seperated by spaces")
inp1=input("enter the nodes of tree2 seperated by spaces")
inp=inp.split()
inp1=inp1.split()
root1=build_binarytree(inp)
root2=build_binarytree(inp1)
print(sametree(root1,root2))