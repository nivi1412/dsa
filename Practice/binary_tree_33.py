#binarytree33.py
#binarytree32.py tried the same
#Count Good Nodes in Binary Tree
#do DFS find the value to be inserted is > the max value so far

from binarytree1 import build_binarytree,print_binarytree

def Count_GoodNodes(root):
	node_list=[]
	def DFS(root,Max=root.data):
		nonlocal node_list
		if root==None:
			return
		if root.data>=Max:
			Max=root.data
			node_list.append(root.data)
		DFS(root.left,Max)
		DFS(root.right,Max)

	DFS(root)
	return node_list

Arr=input("enter elements of binarytree")
Arr=Arr.split()
root=build_binarytree(Arr)
print(Count_GoodNodes(root))