#BT_Deletenodes.py

from build_binarytree import build_binarytree,print_binarytree
import ast

def findpaths(root,to_delete,my_list)->list: #return list of roots
	if root==None:
		return None
	if int(root.data) not in to_delete:
		my_list.append(root)
	else: 
		if root.left!=None:
			my_list.append(root.left)
		if root.right!=None:
			my_list.append(root.right)
		root=None
	if root!=None:
		findpaths(root.left,to_delete,my_list)
		findpaths(root.right,to_delete,my_list)

arr=input("enter the nodes seperated by spaces: ")
arr=list(arr.split())
to_delete=input("enter to_delete array: ")
to_delete=ast.literal_eval(to_delete)
to_delete=set(to_delete)
my_list=[]

root=build_binarytree(arr)
findpaths(root,to_delete,my_list)
for i in my_list:
	print_binarytree(i)
	print("------")


