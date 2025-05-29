#root2leafpath.py
from binarytree_practice1 import build_binarytree,print_binarytree

def root2leafpaths(root):
	if root.left==None and root.right==None:
		leaf_list=[str(root.data)]
		return leaf_list
	lists=[]
	if root.left!=None:
		left_list=root2leafpaths(root.left)
		for i in left_list:
			lists.append(i)
	if root.right!=None:
		right_list=root2leafpaths(root.right)
		for i in right_list:
			lists.append(i)
	for i in range(len(lists)):
		lists[i]=str(root.data)+"->"+lists[i]
	return lists

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print(root2leafpaths(root))
