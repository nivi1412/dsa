#sumroottoleftnums.py
from binarytree_practice1 import build_binarytree,print_binarytree

def sumroottotreenums(root):
	if root.left==None and root.right==None:
		return [[root.data]]
	lists=[]
	if root.left!=None:
		left=sumroottotreenums(root.left)
		for i in left:
			lists.append(i)
	if root.right !=None:
		right=sumroottotreenums(root.right)
		for i in right:
			lists.append(i)
	for i in lists:
		i.insert(0,root.data)
	return lists


inp=input("enter the nodes of tree seperated by spaces").split()
root=build_binarytree(inp)
result=sumroottotreenums(root)
summ=0
roottonum=''

for path in result:
	for val in path:
		roottonum=roottonum+val
	summ=summ+int(roottonum)
	roottonum=''
print(summ) 