#binarytree16.py
#find tilt of the binary tree

from binarytree_lib import build_binarytree,print_binarytree

def find_sum(root,my_dict):
	if root ==None:
		return 0
	if root.data in my_dict:
		return my_dict[root]
	left_sum=find_sum(root.left,my_dict)
	right_sum=find_sum(root.right,my_dict)
	my_dict[root]= left_sum+right_sum+int(root.data)
	return my_dict[root]

def find_tilt(root,my_dict):
	if root==None:
		return
	root.data = abs(int(find_sum(root.left, my_dict)) - int(find_sum(root.right, my_dict)))
	find_tilt(root.left,my_dict)
	find_tilt(root.right,my_dict)

def sum_nodes(root,summ):
	if root == None:
		return 0
	return summ+root.data+sum_nodes(root.left,summ)+sum_nodes(root.right,summ)


inp=input("enter the nodes of the binary tree seprated by spaces:")
inp=inp.split()
root=build_binarytree(inp)
my_dict={}
# find_sum(root,my_dict)
print(my_dict)
find_tilt(root,my_dict)
print_binarytree(root)
print("sum of nodes ins tilt is :",sum_nodes(root,summ=0))