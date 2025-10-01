#graph_allpaths.py
#[[1,3],[3,4],[3,5],[5,6]]

import ast

def findallpaths(node,graph):
	my_list=[]
	local_list=[]
	finished_nodes=set()
	def DFS(node):
		nonlocal my_list
		nonlocal local_list

		local_list.append(node)
		finished_nodes.add(node)
		next_node=graph.get(node,[])
		# print("nextnode:",next_node)
		# print("local_list:",local_list)
		if not next_node:
			my_list.append(local_list)
			# print("my_list",my_list)
		else:
			for v in next_node:
				print("v:",v)
				if v in finished_nodes:
					continue
				else:
					DFS(v)
		local_list.pop()
	DFS(node)
	return my_list

inp=input("enter the inp values: ")
inp=ast.literal_eval(inp)
graph={}

for i in range(len(inp)):
	if i not in graph:
		graph[i]=[]
		# visited[i]=False
	graph[i]=inp[i]
print(graph)

for node in graph:
	print(findallpaths(node,graph))









