# BT_sum_root_toleaf.py

from build_binarytree import build_binarytree,print_binarytree

def sum_Root_to_Leaf(root):
	if root==None:
		return []
	if root.left==None and root.right ==None:
		return [[root.data]]
	left=sum_Root_to_Leaf(root.left)
	right=sum_Root_to_Leaf(root.right)
	finallist=[]
	for i in left:
		i[0]=root.data+i[0]
		finallist.append(i)
	for j in right:
		j[0]=root.data+j[0]
		finallist.append(j)
	return finallist

inp=input("enter the nodes sep by spaces: ")
inp=list(inp.split())
root=build_binarytree(inp)

finallist=sum_Root_to_Leaf(root)
my_sum=0
for i in finallist:
	my_sum=my_sum+int(i[0])
print(my_sum)