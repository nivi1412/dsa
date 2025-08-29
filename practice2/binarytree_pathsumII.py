#binarytree_pathsumII.py

from build_binarytree import build_binarytree,print_binarytree
def pathsum(root,psum)->list:
	if root==None:
		return []
	psum=psum-int(root.data)
	if root.left==None and root.right==None and psum==0:
		return [[root.data]]
	left=pathsum(root.left,psum)
	right=pathsum(root.right,psum)
	finallist=[]
	for i in left:
		i.insert(0,root.data)
		finallist.append(i)
	for j in right:
		j.insert(0,root.data)
		finallist.append(j)
	return finallist


tree=input("enter the nodes of the tree: ")
tree=list(tree.split())
psum=int(input("enter the sum: "))
root=build_binarytree(tree)
print(pathsum(root,psum))