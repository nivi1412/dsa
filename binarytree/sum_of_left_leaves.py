#sumofleftleaves.py

from binarytree_practice1 import build_binarytree,print_binarytree
def sumofleftleaves(root,is_bool):
	if root.left==None and root.right==None:
		if is_bool:
			return int(root.data)
		else: return 0
	if root.left!=None:
		val_l=sumofleftleaves(root.left,True)
		print(val_l)
	if root.right!=None:
		val_r=sumofleftleaves(root.right,False)
		print(val_r)
	return val_l+val_r

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print(sumofleftleaves(root,True))