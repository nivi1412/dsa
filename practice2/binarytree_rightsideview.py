#binarytree_rightsideview.py
def dfs(root,my_list):
	if root==None:
		return None
	else:
		my_list.append(root.data)
		if root.right != None:
			dfs(root.right,my_list)
	return root

from build_binarytree import build_binarytree,print_binarytree

tree=input("enter the nodes of the tree: ")
tree=list(tree.split())

root=build_binarytree(tree)
my_list=[]
# my_list.append(root.data)
dfs(root,my_list)

print(my_list)