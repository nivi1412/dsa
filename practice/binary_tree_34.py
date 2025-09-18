#binarytree34.py
#degree of the binarytree

from binarytree1 import build_binarytree,print_binarytree

def degreeofbinarytree(root):
	my_dict={}
	def count_connections(root,parent=None):
		nonlocal my_dict
		if root == None:
			return None
		connection_count=0
		local=[]
		if parent:
			local.append(parent.data)
		if root.left:
			local.append(root.left.data)
		if root.right:
			local.append(root.right.data)
		my_dict[root.data]=local

		count_connections(root.left,root)
		count_connections(root.right,root)
	count_connections(root,parent=None)
	return my_dict

def DFS(my_dict,visited,start):
	if not visited[start]:
		visited[start]=True
		depths=[]
		for values in my_dict[start]:
			depths.append(DFS(my_dict,visited,values))
			print(start,values,depths)
		return 1+max(depths)
	else:
		return -1


Arr=input("enter elements of binarytree")
Arr=Arr.split()
start=input("enter the start node:")
root=build_binarytree(Arr)
my_dict=degreeofbinarytree(root)
print(my_dict)
visited={}
for key in my_dict:
	visited[key]=False
print(DFS(my_dict,visited,start))





