#binarytree14.py

from binarytree_lib import build_binarytree
# prev_root=10**5
# prev_diff=10**5

# def min_difference(root):
# 	global prev_diff,prev_root
# 	if root.left!=None:
# 		min_difference(root.left)
# 	if root !=None:
# 		curr_diff=abs(prev_root-int(root.data))
# 		prev_diff=min(curr_diff,prev_diff)
# 		prev_root=int(root.data)

# 	if root.right !=None:
# 		min_difference(root.right)

# 	return prev_diff

def __min_difference(root, my_dict):

	if root.left!=None:
		__min_difference(root.left, my_dict)
	if root !=None:
		curr_diff=abs(my_dict["prev_node"]-int(root.data))
		my_dict["prev_diff"]=min(my_dict["prev_diff"],curr_diff)
		my_dict["prev_node"]=int(root.data)

	if root.right !=None:
		__min_difference(root.right,my_dict)

	return my_dict["prev_diff"]

def min_difference(root):
	my_dict={}
	my_dict["prev_node"]=10**5
	my_dict["prev_diff"]=10**5
	return(__min_difference(root,my_dict))


inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
print("minimum difference:",min_difference(root))