#mode_BT.py

from binarytree_practice1 import build_binarytree,print_binarytree

def mode_BT(root,my_dict):
	if root!=None:
		if root.data not in my_dict:
			my_dict[root.data]=1
		else:
			my_dict[root.data]+=1
		if root.left !=None:
			mode_BT(root.left,my_dict)
		if root.right !=None:
			mode_BT(root.right,my_dict)
	max_local=my_dict[root.data]
	key_local=root.data
	print(my_dict)
	for key,value in my_dict.items():
		if max_local<my_dict[key]:
			max_local=my_dict[key]
			key_local=key

	return key_local

inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_dict={}
print(mode_BT(root,my_dict))