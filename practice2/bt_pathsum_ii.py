#BT_PathsumII.py
from build_binarytree import build_binarytree, print_binarytree

def pathsum(root,target_sum):
	if root==None:
		return []
	target_sum=target_sum-int(root.data)
	if root.left==None and root.right==None and target_sum==0:
		return [[root.data]]
	left=pathsum(root.left,target_sum)
	right=pathsum(root.right,target_sum)
	finallist=[]
	for l in left:
		l.insert(0,root.data)
		finallist.append(l)
	for r in right:
		r.insert(0,root.data)
		finallist.append(r)
	return finallist

tree=input("enter the tree nodes sep by spaces:")
tree=list(tree.split())
root=build_binarytree(tree)
target_sum=int(input("enter the target sum: "))

print(pathsum(root,target_sum))




