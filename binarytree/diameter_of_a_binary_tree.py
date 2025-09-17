#diameterofabinarytree.py

from binarytree_practice1 import build_binarytree,print_binarytree

def height_subtree(root,my_dict):
	if root==None:
		return 0
	if root.data in my_dict:
		return my_dict[root.data]
	my_dict[root.data]=1+max(height_subtree(root.left,my_dict),height_subtree(root.right,my_dict))
	return my_dict[root.data]

def diameterofBT(root,prev_dia,my_dict):
	if root.left!=None:
		diameterofBT(root.left,prev_dia,my_dict)
	if root!=None:
		left=height_subtree(root.left,my_dict)
		right=height_subtree(root.right,my_dict)
		dia=left+right
		if prev_dia[0]<dia:
			prev_dia[0]=dia
	if root.right!=None:
		diameterofBT(root.right,prev_dia,my_dict)

	return prev_dia[0]


inp=input("enter the nodes of tree seperated by spaces")
inp=inp.split()
root=build_binarytree(inp)
my_dict={}
print(diameterofBT(root,[0],my_dict))
print(my_dict)