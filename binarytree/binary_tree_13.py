#binarytree13.py
#find mode of the binary tree
from binarytree_lib import build_binarytree

def __mode_binarytree(root,my_dict):
	if root.data != None:
		if root.data not in my_dict:
			my_dict[root.data]=1
		else:
			my_dict[root.data]+=1

	if root.left != None:
		mode_binarytree(root.left,my_dict)
	if root.right != None:
		mode_binarytree(root.right,my_dict)

def mode_binarytree(root):
	my_dict={}
	__mode_binarytree(root,my_dict)
	return max(my_dict,key=my_dict.get)

inp=input("enter the nodes of the binary tree seprated by spaces")
inp=inp.split()
root=build_binarytree(inp)
mode=mode_binarytree(root)
print("mode of the tree:", mode)


