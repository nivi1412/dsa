#binarytree6.py
#find if tree is balanced: tree is balanced if the max depth - min depth of the binary trees is atmost 1

from binarytree_lib import build_binarytree,print_binarytree

def maxdepth(root):
	if root == None:
		return 0
	return 1+(max(maxdepth(root.left),maxdepth(root.right)))
def mindepth(root):
	if root == None:
		return 0
	return 1+(min(mindepth(root.left),mindepth(root.right)))

def balanced_binarytree(root):
	mxdepth=maxdepth(root)
	mndepth=mindepth(root)

	if (mxdepth-mndepth)>1:
		return False
	else:
		return True


inp=input("enter the elements of tree seperated by space")
inp=inp.split()

root=build_binarytree(inp)
print_binarytree(root)
print(balanced_binarytree(root))