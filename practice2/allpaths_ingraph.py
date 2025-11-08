#allpaths_ingraph.py

import ast

def allpaths(graph):
	local_list=[]
	my_list=[]

	def DFS(node):
		nonlocal local_list
		nonlocal my_list

		local_list.append(node)
		finished_nodes.add(node)

		next_node=graph.get(node,[])
		if not next_node:
			my_list.append(local_list.copy())

		else:
			for v in next_node:
				if v in local_list:
					continue
				else:
					DFS(v)
		local_list.pop()
	
	DFS(next(iter(graph)))
	return my_list

edges=input("enter the graph: ")
edges=ast.literal_eval(edges)
graph={}
for i in range(len(edges)):
	graph[i]=edges[i]
print(graph)

print(allpaths(graph))