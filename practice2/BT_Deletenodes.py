#BT_Deletenodes.py

from build_binarytree import build_binarytree,print_binarytree
import ast

def findpaths(root,to_delete,my_list)->list: #return list of roots
	if root==None:
		return None
	root.left=findpaths(root.left,to_delete,my_list)
	root.right=findpaths(root.right,to_delete,my_list)
	print("data:",root.data,my_list)
	if int(root.data) in to_delete:
		if root.left:
			my_list.append(root.left)
		if root.right:
			my_list.append(root.right)
		return None
	return root


arr=input("enter the nodes seperated by spaces: ")
arr=list(arr.split())
to_delete=input("enter to_delete array: ")
to_delete=ast.literal_eval(to_delete)
to_delete=set(to_delete)
my_list=[]

root=build_binarytree(arr)
root=findpaths(root,to_delete,my_list)
if root:
	my_list.append(root)

for i in my_list:
	print_binarytree(i)
