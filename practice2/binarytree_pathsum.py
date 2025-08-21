#binarytree_printpaths.py

from build_binarytree import build_binarytree,print_binarytree

def pathsum(root):
	lists=[]
	if root.left==None and root.right==None:
		return [[root.data]]
	if root.left!=None:
		left=pathsum(root.left)
		for i in left:
			print("i:",i)
			i.insert(0,root.data)
			lists.append(i)
	if root.right !=None:
		right=pathsum(root.right)
		for j in right:
			print("j:",j)
			j.insert(0,root.data)
			lists.append(j)
	return lists

tree=input("enter the nodes of the tree: ")
tree=list(tree.split())

root=build_binarytree(tree)
print(pathsum(root))