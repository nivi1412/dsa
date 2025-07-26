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
			connection_count+=1
			local.append(parent.data)
		if root.left:
			connection_count+=1
			local.append(root.left.data)
		if root.right:
			connection_count+=1
			local.append(root.right.data)
		local.append(connection_count)
		my_dict[root.data]=local

		count_connections(root.left,root)
		count_connections(root.right,root)
	count_connections(root,parent=None)
	return my_dict

Arr=input("enter elements of binarytree")
Arr=Arr.split()
start=int(input("enter the start node:"))
root=build_binarytree(Arr)
my_dict=degreeofbinarytree(root)
minute_count=0
for key,value in my_dict.items():
	if key==start:
		minute_count=minute_count+int(value[-1])