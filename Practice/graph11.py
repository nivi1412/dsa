#graph11.py

import ast

class tree():
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def build_tree(root,node_list):
	for i in range(len(node_list)):
		if node[i]!=root:
			root.left=node[i]
			if i+1<len(node_list):
				root.right=node[i+1]
	


n=int(input("enter number of nodes:"))
edges=input("enter the prerequisites array:")
edges=ast.literal_eval(edges)

graph={}
node_list=[]
new_node_list=[]

for edge in edges:
	# print(edge[0],edge[1])
	if edge[0] not in graph:
		graph[edge[0]]=[]
	if edge[1] not in graph:
		graph[edge[1]]=[]
	graph[edge[0]].append(edge[1])

for keys,values in graph.items():
	node_list.append(tree(keys))

for i in range(len(node_list)):
	new_node_list=node_list[:i]+node_list[i+1:]
	build_tree(node,new_node_list)

