#binarytree32.py
#Count Good Nodes in Binary Tree

from binarytree1 import build_binarytree,print_binarytree

def __Count_GoodNodes(root,root_value):
	result=[]
	if root==None:
		return []
	if root.left==None and root.right==None:
		return [[root.data]]
	left=__Count_GoodNodes(root.left,root_value)
	right=__Count_GoodNodes(root.right,root_value)

	for i in left:
		print("i:",i)
		if int(root.data)>=root_value and int(root.data)<=int(i[0]):
			i.insert(0,root.data)
		else:
			if len(i)==1 and int(root.data)>=int(i[0]):
				i.pop()
				i.insert(0,root.data)
		result.append(i)
	for j in right:
		print("j:",j)
		if int(root.data)>=root_value and int(root.data)<int(j[0]):
			j.insert(0,root.data)
		else:
			if len(j)==1 and int(root.data)>=int(j[0]):
				j.pop()
				j.insert(0,root.data)
		result.append(j)

	return result

def Count_GoodNodes(root):
	root_value=int(root.data)
	return __Count_GoodNodes(root,root_value)


Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
GoodNode_paths=Count_GoodNodes(root)

for i in GoodNode_paths:
	




