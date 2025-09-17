#targetsum.py
from binarytree_practice1 import build_binarytree,print_binarytree

def targetsum(root,target):
	if root!=None:
		print("data:",root.data,target)
		target=target-int(root.data)
		if target==0:
			return True
		return (targetsum(root.left,target) or targetsum(root.right,target))
	return False

inp=input("enter the nodes of tree seperated by spaces:")
target=int(input("enter the targetsum:"))
inp=inp.split()
root=build_binarytree(inp)

print(targetsum(root,target))
