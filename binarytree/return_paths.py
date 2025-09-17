#returnpaths.py
#print all the  paths of the binarytree
from binarytree_practice1 import build_binarytree,print_binarytree

def returnpaths(root):
	if root==None:
		return []
	if root.left==None and root.right==None:
		return[[root.data]]
	left=returnpaths(root.left)
	right=returnpaths(root.right)
	
	result=[]

	for i in left:
		i.insert(0,root.data)
		result.append(i)
	for j in right:
		j.insert(0,root.data)
		result.append(j)
	return result

inp=input("enter the nodes of tree seperated by spaces").split()
root=build_binarytree(inp)
print(returnpaths(root))